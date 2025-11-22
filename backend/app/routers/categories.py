"""
Categories Router
Gestione categorie transazioni utente con struttura gerarchica
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas.category import (
    CategoryCreate, 
    CategoryUpdate, 
    CategoryResponse,
    CategoryWithSubcategories,
    CategoryTreeResponse,
    VALID_CATEGORY_TYPES
)
from app.crud import category as category_crud
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=List[CategoryResponse])
async def get_categories(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Numero di record da saltare"),
    limit: int = Query(100, ge=1, le=500, description="Numero massimo di risultati"),
    type: Optional[str] = Query(None, description="Filtra per tipo: income, expense_necessity, expense_extra"),
    is_active: Optional[bool] = Query(None, description="Filtra per stato attivo/inattivo"),
    parent_id: Optional[str] = Query(None, description="Filtra per categoria padre"),
    only_main: bool = Query(False, description="Se true, restituisce solo categorie principali (senza parent)")
):
    """
    Lista tutte le categorie dell'utente corrente.
    
    - **skip**: Offset per paginazione (default: 0)
    - **limit**: Numero massimo risultati (default: 100, max: 500)
    - **type**: Filtra per macro categoria (income, expense_necessity, expense_extra)
    - **is_active**: Filtra solo attive (true) o inattive (false)
    - **parent_id**: Filtra sottocategorie di una specifica categoria
    - **only_main**: Se true, esclude le sottocategorie
    """
    # Valida il tipo se fornito
    if type is not None and type not in VALID_CATEGORY_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid type. Must be one of: {', '.join(VALID_CATEGORY_TYPES)}"
        )
    
    categories = category_crud.get_categories(
        db,
        user_id=str(current_user.id),
        skip=skip,
        limit=limit,
        category_type=type,
        is_active=is_active,
        parent_id=parent_id,
        only_main=only_main
    )
    return categories


@router.get("/tree", response_model=CategoryTreeResponse)
async def get_categories_tree(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    is_active: Optional[bool] = Query(True, description="Filtra per stato attivo/inattivo")
):
    """
    Restituisce le categorie organizzate ad albero per macro categoria.
    
    Struttura risposta:
    ```json
    {
        "income": [
            {
                "id": "...",
                "name": "Reddito",
                "subcategories": [
                    {"id": "...", "name": "Reddito Principale"},
                    {"id": "...", "name": "Reddito Secondario"}
                ]
            }
        ],
        "expense_necessity": [...],
        "expense_extra": [...]
    }
    ```
    """
    tree = category_crud.get_categories_tree(
        db,
        user_id=str(current_user.id),
        is_active=is_active
    )
    return tree


@router.get("/statistics")
async def get_categories_statistics(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Restituisce statistiche sulle categorie dell'utente.
    
    Risposta include:
    - Totale categorie
    - Conteggio per tipo
    - Categorie principali vs sottocategorie
    - Attive vs inattive
    """
    stats = category_crud.get_category_statistics(
        db,
        user_id=str(current_user.id)
    )
    return stats


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(
    category: CategoryCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Crea una nuova categoria.
    
    - **name**: Nome categoria (es. "Ristoranti", "Bonus")
    - **type**: Macro categoria (income, expense_necessity, expense_extra)
    - **color**: Colore HEX per UI (es. #3B82F6)
    - **icon**: Icona/emoji per UI
    - **parent_id**: ID categoria padre per creare una sottocategoria (opzionale)
    
    Esempio creazione sottocategoria:
    ```json
    {
        "name": "Netflix",
        "type": "expense_extra",
        "parent_id": "uuid-della-categoria-Svago"
    }
    ```
    """
    # Se specificato parent_id, verifica che esista e appartenga all'utente
    if category.parent_id:
        parent = category_crud.get_category(db, category.parent_id, str(current_user.id))
        if not parent:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Parent category not found"
            )
        # Verifica che il tipo sia lo stesso del parent
        if parent.type != category.type:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Category type must match parent category type ({parent.type})"
            )
        # Verifica che il parent non sia già una sottocategoria (max 2 livelli)
        if parent.parent_id is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot create subcategory of a subcategory. Maximum depth is 2 levels."
            )
    
    return category_crud.create_category(
        db,
        category=category,
        user_id=str(current_user.id)
    )


@router.get("/{category_id}", response_model=CategoryWithSubcategories)
async def get_category(
    category_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Recupera dettagli di una singola categoria con le sue sottocategorie.
    """
    category = category_crud.get_category(
        db,
        category_id=category_id,
        user_id=str(current_user.id)
    )
    
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    return category


@router.put("/{category_id}", response_model=CategoryResponse)
async def update_category(
    category_id: str,
    category_update: CategoryUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Aggiorna una categoria esistente.
    
    Puoi aggiornare solo i campi che vuoi modificare.
    
    ⚠️ Se cambi il `type`, tutte le sottocategorie verranno aggiornate di conseguenza.
    """
    # Verifica esistenza categoria
    existing = category_crud.get_category(db, category_id, str(current_user.id))
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    # Se si sta aggiornando parent_id, verifica validità
    if category_update.parent_id is not None:
        # Non può essere se stesso
        if category_update.parent_id == category_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category cannot be its own parent"
            )
        
        parent = category_crud.get_category(db, category_update.parent_id, str(current_user.id))
        if not parent:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Parent category not found"
            )
        
        # Verifica che non si crei un ciclo
        if parent.parent_id == category_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot set parent to a subcategory of this category"
            )
    
    # Se si cambia il tipo, aggiorna anche le sottocategorie
    if category_update.type is not None and category_update.type != existing.type:
        for sub in existing.subcategories:
            sub.type = category_update.type
    
    updated_category = category_crud.update_category(
        db,
        category_id=category_id,
        category_update=category_update,
        user_id=str(current_user.id)
    )
    
    return updated_category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: str,
    force: bool = Query(False, description="Se true, elimina anche se ha transazioni associate"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Elimina una categoria.
    
    ⚠️ **Attenzione**: 
    - Elimina anche tutte le sottocategorie
    - Di default, non puoi eliminare categorie con transazioni associate
    - Usa `force=true` per forzare l'eliminazione (le transazioni rimarranno orfane)
    
    💡 Considera di disattivare la categoria invece di eliminarla.
    """
    # Verifica se la categoria esiste
    category = category_crud.get_category(db, category_id, str(current_user.id))
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    # Verifica se ci sono transazioni associate (incluse sottocategorie)
    has_transactions = len(category.transactions) > 0
    for sub in category.subcategories:
        if len(sub.transactions) > 0:
            has_transactions = True
            break
    
    if has_transactions and not force:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot delete category with existing transactions. Use force=true or deactivate instead."
        )
    
    success = category_crud.delete_category(
        db,
        category_id=category_id,
        user_id=str(current_user.id)
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    return None


@router.post("/{category_id}/deactivate", response_model=CategoryResponse)
async def deactivate_category(
    category_id: str,
    include_subcategories: bool = Query(True, description="Se true, disattiva anche le sottocategorie"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Disattiva una categoria (soft delete).
    
    La categoria non verrà eliminata ma sarà nascosta dalle liste.
    Può essere riattivata con PUT impostando is_active=true.
    
    - **include_subcategories**: Se true (default), disattiva anche tutte le sottocategorie
    """
    category = category_crud.get_category(db, category_id, str(current_user.id))
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    # Disattiva sottocategorie se richiesto
    if include_subcategories:
        for sub in category.subcategories:
            sub.is_active = False
    
    deactivated = category_crud.deactivate_category(
        db,
        category_id=category_id,
        user_id=str(current_user.id)
    )
    
    return deactivated


@router.post("/seed-defaults", response_model=List[CategoryResponse])
async def seed_default_categories(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Crea le categorie predefinite per l'utente.
    
    Struttura basata su:
    - **Entrate**: Reddito, Affitto, Vendita, Rimborsi, Altro
    - **Spese di Necessità**: Casa, Trasporti, Salute, Figli, Istruzione, Altro
    - **Spese Extra**: Svago, Animali
    
    Ogni categoria principale ha le sue sottocategorie.
    
    ⚠️ Funziona solo se l'utente non ha ancora categorie.
    """
    # Verifica se l'utente ha già categorie
    existing = category_crud.get_categories(db, str(current_user.id), limit=1)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already has categories. Delete them first if you want to reset."
        )
    
    categories = category_crud.seed_default_categories(db, str(current_user.id))
    return categories


@router.delete("/all", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_categories(
    confirm: bool = Query(..., description="Conferma eliminazione (deve essere true)"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Elimina TUTTE le categorie dell'utente.
    
    ⚠️ **ATTENZIONE**: Operazione irreversibile!
    
    Utile per resettare e ricreare le categorie di default.
    Richiede `confirm=true` come parametro.
    """
    if not confirm:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You must confirm deletion by setting confirm=true"
        )
    
    # Prendi tutte le categorie dell'utente
    all_categories = category_crud.get_categories(
        db, 
        str(current_user.id), 
        limit=1000
    )
    
    # Verifica se qualche categoria ha transazioni
    for cat in all_categories:
        if len(cat.transactions) > 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Cannot delete all categories: '{cat.name}' has transactions associated. Delete transactions first."
            )
    
    # Elimina tutte (le sottocategorie vengono eliminate automaticamente per cascade)
    for cat in all_categories:
        if cat.parent_id is None:  # Solo categorie principali
            db.delete(cat)
    
    db.commit()
    
    return None