"""
Accounts Router
Gestione conti bancari/portafogli utente
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas.account import AccountCreate, AccountUpdate, AccountResponse
from app.crud import account as account_crud
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.get("/", response_model=List[AccountResponse])
async def get_accounts(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Numero di record da saltare"),
    limit: int = Query(100, ge=1, le=100, description="Numero massimo di risultati"),
    is_active: Optional[bool] = Query(None, description="Filtra per stato attivo/inattivo")
):
    """
    Lista tutti gli account dell'utente corrente.
    
    - **skip**: Offset per paginazione (default: 0)
    - **limit**: Numero massimo risultati (default: 100, max: 100)
    - **is_active**: Filtra solo attivi (true) o inattivi (false)
    """
    accounts = account_crud.get_accounts(
        db, 
        user_id=str(current_user.id), 
        skip=skip, 
        limit=limit,
        is_active=is_active
    )
    return accounts


@router.post("/", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
async def create_account(
    account: AccountCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Crea un nuovo account.
    
    - **name**: Nome account (es. "Conto Corrente", "Risparmio")
    - **type**: Tipo account (checking, savings, credit_card, cash, investment, other)
    - **currency**: Valuta ISO 4217 (default: EUR)
    - **initial_balance**: Saldo iniziale (default: 0.00)
    - **color**: Colore HEX per UI (es. #3B82F6)
    - **icon**: Icona/emoji per UI
    - **notes**: Note aggiuntive
    """
    return account_crud.create_account(
        db, 
        account=account, 
        user_id=str(current_user.id)
    )


@router.get("/{account_id}", response_model=AccountResponse)
async def get_account(
    account_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Recupera dettagli di un singolo account.
    
    - **account_id**: ID univoco dell'account
    """
    account = account_crud.get_account(
        db, 
        account_id=account_id, 
        user_id=str(current_user.id)
    )
    
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    return account


@router.put("/{account_id}", response_model=AccountResponse)
async def update_account(
    account_id: str,
    account_update: AccountUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Aggiorna un account esistente.
    
    Puoi aggiornare solo i campi che vuoi modificare.
    I campi non inclusi nella richiesta rimarranno invariati.
    
    - **name**: Nuovo nome account
    - **type**: Nuovo tipo account
    - **currency**: Nuova valuta
    - **color**: Nuovo colore
    - **icon**: Nuova icona
    - **notes**: Nuove note
    - **is_active**: Attiva/disattiva account
    """
    updated_account = account_crud.update_account(
        db,
        account_id=account_id,
        account_update=account_update,
        user_id=str(current_user.id)
    )
    
    if not updated_account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    return updated_account


@router.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_account(
    account_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Elimina un account.
    
    ⚠️ **Attenzione**: Questa operazione elimina anche tutte le transazioni 
    e i trasferimenti associati all'account.
    
    - **account_id**: ID univoco dell'account da eliminare
    """
    success = account_crud.delete_account(
        db,
        account_id=account_id,
        user_id=str(current_user.id)
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    return None


@router.post("/{account_id}/deactivate", response_model=AccountResponse)
async def deactivate_account(
    account_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Disattiva un account (soft delete).
    
    L'account non verrà eliminato ma sarà nascosto dalle liste.
    Può essere riattivato con PUT impostando is_active=true.
    
    - **account_id**: ID univoco dell'account da disattivare
    """
    deactivated = account_crud.deactivate_account(
        db,
        account_id=account_id,
        user_id=str(current_user.id)
    )
    
    if not deactivated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    return deactivated
