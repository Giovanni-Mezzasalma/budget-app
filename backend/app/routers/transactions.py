"""
Transactions Router
Gestione transazioni (entrate e uscite) utente
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from decimal import Decimal
from datetime import date

from app.database import get_db
from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
    TransactionResponse,
    TransactionWithDetails,
    TransactionSummary,
    VALID_TRANSACTION_TYPES
)
from app.crud import transaction as transaction_crud
from app.crud import account as account_crud
from app.crud import category as category_crud
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.get("/", response_model=List[TransactionResponse])
async def get_transactions(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Numero di record da saltare"),
    limit: int = Query(100, ge=1, le=500, description="Numero massimo di risultati"),
    account_id: Optional[str] = Query(None, description="Filtra per account"),
    category_id: Optional[str] = Query(None, description="Filtra per categoria"),
    type: Optional[str] = Query(None, description="Filtra per tipo: income, expense_necessity, expense_extra"),
    start_date: Optional[date] = Query(None, description="Data inizio periodo (YYYY-MM-DD)"),
    end_date: Optional[date] = Query(None, description="Data fine periodo (YYYY-MM-DD)"),
    min_amount: Optional[Decimal] = Query(None, ge=0, description="Importo minimo"),
    max_amount: Optional[Decimal] = Query(None, ge=0, description="Importo massimo"),
    search: Optional[str] = Query(None, description="Cerca in descrizione e note")
):
    """
    Lista tutte le transazioni dell'utente con filtri opzionali.
    
    **Filtri disponibili:**
    - **account_id**: Filtra per specifico account
    - **category_id**: Filtra per specifica categoria
    - **type**: Filtra per tipo (income, expense_necessity, expense_extra)
    - **start_date / end_date**: Filtra per periodo
    - **min_amount / max_amount**: Filtra per range importo
    - **search**: Cerca testo in descrizione e note
    
    **Ordinamento:** Per data decrescente (più recenti prima)
    """
    # Valida il tipo se fornito
    if type is not None and type not in VALID_TRANSACTION_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid type. Must be one of: {', '.join(VALID_TRANSACTION_TYPES)}"
        )
    
    transactions = transaction_crud.get_transactions(
        db,
        user_id=str(current_user.id),
        skip=skip,
        limit=limit,
        account_id=account_id,
        category_id=category_id,
        transaction_type=type,
        start_date=start_date,
        end_date=end_date,
        min_amount=min_amount,
        max_amount=max_amount,
        search=search
    )
    
    return transactions


@router.get("/summary", response_model=TransactionSummary)
async def get_transactions_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(None, description="Data inizio periodo"),
    end_date: Optional[date] = Query(None, description="Data fine periodo"),
    account_id: Optional[str] = Query(None, description="Filtra per account")
):
    """
    Restituisce il riepilogo delle transazioni.
    
    **Risposta include:**
    - Totale entrate (income)
    - Totale spese di necessità (expense_necessity)
    - Totale spese extra (expense_extra)
    - Totale spese (necessity + extra)
    - Saldo netto (entrate - spese)
    - Numero transazioni
    
    **Esempio risposta:**
    ```json
    {
        "total_income": 3500.00,
        "total_expense_necessity": 1800.00,
        "total_expense_extra": 450.00,
        "total_expenses": 2250.00,
        "net": 1250.00,
        "transaction_count": 45
    }
    ```
    """
    summary = transaction_crud.get_transaction_summary(
        db,
        user_id=str(current_user.id),
        start_date=start_date,
        end_date=end_date,
        account_id=account_id
    )
    
    return summary


@router.get("/monthly/{year}/{month}", response_model=TransactionSummary)
async def get_monthly_summary(
    year: int,
    month: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Restituisce il riepilogo per un mese specifico.
    
    - **year**: Anno (es. 2025)
    - **month**: Mese (1-12)
    """
    if month < 1 or month > 12:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Month must be between 1 and 12"
        )
    
    if year < 2000 or year > 2100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Year must be between 2000 and 2100"
        )
    
    summary = transaction_crud.get_monthly_totals(
        db,
        user_id=str(current_user.id),
        year=year,
        month=month
    )
    
    return summary


@router.post("/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
async def create_transaction(
    transaction: TransactionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Crea una nuova transazione.
    
    **Campi richiesti:**
    - **account_id**: ID dell'account
    - **category_id**: ID della categoria
    - **amount**: Importo (sempre positivo)
    - **date**: Data della transazione
    
    **Campi opzionali:**
    - **description**: Descrizione breve
    - **notes**: Note aggiuntive
    - **tags**: Lista di tag per filtraggio
    
    ⚠️ **Nota:** Il tipo della transazione (income/expense_necessity/expense_extra) 
    viene determinato automaticamente dalla categoria selezionata.
    
    ✅ Il balance dell'account viene aggiornato automaticamente.
    
    **Esempio:**
    ```json
    {
        "account_id": "uuid-account",
        "category_id": "uuid-categoria-benzina",
        "amount": 45.50,
        "date": "2025-01-15",
        "description": "Rifornimento benzina"
    }
    ```
    """
    # Verifica che l'account esista e appartenga all'utente
    account = account_crud.get_account(db, transaction.account_id, str(current_user.id))
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    # Verifica che la categoria esista e appartenga all'utente
    category = category_crud.get_category(db, transaction.category_id, str(current_user.id))
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    # Verifica che la categoria sia attiva
    if not category.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot use inactive category"
        )
    
    try:
        db_transaction = transaction_crud.create_transaction(
            db,
            transaction=transaction,
            user_id=str(current_user.id)
        )
        return db_transaction
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/{transaction_id}", response_model=TransactionWithDetails)
async def get_transaction(
    transaction_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Recupera i dettagli di una singola transazione.
    
    Include informazioni su account e categoria associati.
    """
    transaction = transaction_crud.get_transaction(
        db,
        transaction_id=transaction_id,
        user_id=str(current_user.id)
    )
    
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    
    # Costruisci risposta con dettagli
    response = TransactionWithDetails(
        id=transaction.id,
        user_id=transaction.user_id,
        account_id=transaction.account_id,
        category_id=transaction.category_id,
        amount=transaction.amount,
        type=transaction.type,
        date=transaction.date,
        description=transaction.description,
        notes=transaction.notes,
        tags=transaction.tags,
        is_recurring=transaction.is_recurring,
        recurring_frequency=transaction.recurring_frequency,
        created_at=transaction.created_at,
        updated_at=transaction.updated_at,
        account_name=transaction.account.name if transaction.account else None,
        account_color=transaction.account.color if transaction.account else None,
        category_name=transaction.category.name if transaction.category else None,
        category_full_name=transaction.category.full_name if transaction.category else None,
        category_color=transaction.category.color if transaction.category else None,
        category_icon=transaction.category.icon if transaction.category else None
    )
    
    return response


@router.put("/{transaction_id}", response_model=TransactionResponse)
async def update_transaction(
    transaction_id: str,
    transaction_update: TransactionUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Aggiorna una transazione esistente.
    
    Puoi aggiornare solo i campi che vuoi modificare.
    
    ⚠️ **Nota:** Se cambi la categoria, il tipo della transazione verrà aggiornato 
    automaticamente per corrispondere al tipo della nuova categoria.
    
    ✅ I balance degli account vengono ricalcolati automaticamente.
    """
    # Verifica che la transazione esista
    existing = transaction_crud.get_transaction(db, transaction_id, str(current_user.id))
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    
    # Se si sta cambiando account, verifica che esista
    if transaction_update.account_id is not None:
        account = account_crud.get_account(db, transaction_update.account_id, str(current_user.id))
        if not account:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Account not found"
            )
    
    # Se si sta cambiando categoria, verifica che esista e sia attiva
    if transaction_update.category_id is not None:
        category = category_crud.get_category(db, transaction_update.category_id, str(current_user.id))
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found"
            )
        if not category.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot use inactive category"
            )
    
    try:
        updated_transaction = transaction_crud.update_transaction(
            db,
            transaction_id=transaction_id,
            transaction_update=transaction_update,
            user_id=str(current_user.id)
        )
        return updated_transaction
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transaction(
    transaction_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Elimina una transazione.
    
    ✅ Il balance dell'account viene ripristinato automaticamente.
    """
    success = transaction_crud.delete_transaction(
        db,
        transaction_id=transaction_id,
        user_id=str(current_user.id)
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    
    return None


@router.get("/by-category/totals")
async def get_totals_by_category(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(None, description="Data inizio periodo"),
    end_date: Optional[date] = Query(None, description="Data fine periodo")
):
    """
    Restituisce i totali delle transazioni raggruppati per categoria.
    
    Utile per grafici a torta o analisi per categoria.
    
    **Risposta:** Dict con category_id come chiave e totale come valore.
    """
    totals = transaction_crud.get_transactions_by_category(
        db,
        user_id=str(current_user.id),
        start_date=start_date,
        end_date=end_date
    )
    
    # Arricchisci con nomi categorie
    result = []
    for category_id, total in totals.items():
        category = category_crud.get_category(db, category_id, str(current_user.id))
        if category:
            result.append({
                "category_id": category_id,
                "category_name": category.name,
                "category_full_name": category.full_name,
                "category_type": category.type,
                "category_color": category.color,
                "category_icon": category.icon,
                "total": float(total)
            })
    
    # Ordina per totale decrescente
    result.sort(key=lambda x: x["total"], reverse=True)
    
    return result