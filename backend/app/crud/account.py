"""
Account CRUD Operations
Database operations per Account model
"""
from sqlalchemy.orm import Session
from typing import List, Optional
from decimal import Decimal
import uuid

from app.models.account import Account
from app.schemas.account import AccountCreate, AccountUpdate


def get_accounts(
    db: Session, 
    user_id: str, 
    skip: int = 0, 
    limit: int = 100,
    is_active: Optional[bool] = None
) -> List[Account]:
    """
    Lista tutti gli account dell'utente.
    
    Args:
        db: Database session
        user_id: ID utente proprietario
        skip: Offset per paginazione
        limit: Numero massimo risultati
        is_active: Filtra per stato attivo/inattivo
    
    Returns:
        Lista di Account objects
    """
    query = db.query(Account).filter(Account.user_id == user_id)
    
    if is_active is not None:
        query = query.filter(Account.is_active == is_active)
    
    return query.offset(skip).limit(limit).all()


def get_account(
    db: Session, 
    account_id: str, 
    user_id: str
) -> Optional[Account]:
    """
    Recupera singolo account verificando ownership.
    
    Args:
        db: Database session
        account_id: ID account da recuperare
        user_id: ID utente (per verifica ownership)
    
    Returns:
        Account object se trovato e appartiene all'utente, None altrimenti
    """
    return db.query(Account).filter(
        Account.id == account_id,
        Account.user_id == user_id
    ).first()


def get_account_by_id(db: Session, account_id: str) -> Optional[Account]:
    """
    Recupera account per ID (senza verifica ownership).
    Usare solo internamente quando ownership già verificata.
    """
    return db.query(Account).filter(Account.id == account_id).first()


def create_account(
    db: Session, 
    account: AccountCreate, 
    user_id: str
) -> Account:
    """
    Crea nuovo account per l'utente.
    
    Args:
        db: Database session
        account: Dati account da AccountCreate schema
        user_id: ID utente proprietario
    
    Returns:
        Account object creato
    """
    db_account = Account(
        user_id=user_id,
        name=account.name,
        type=account.type,
        currency=account.currency,
        initial_balance=account.initial_balance,
        color=account.color,
        icon=account.icon,
        notes=account.notes,
        is_active=True
    )
    
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    
    return db_account


def update_account(
    db: Session,
    account_id: str,
    account_update: AccountUpdate,
    user_id: str
) -> Optional[Account]:
    """
    Aggiorna account esistente.
    
    Args:
        db: Database session
        account_id: ID account da aggiornare
        account_update: Dati da aggiornare
        user_id: ID utente (per verifica ownership)
    
    Returns:
        Account aggiornato se trovato, None altrimenti
    """
    db_account = get_account(db, account_id, user_id)
    
    if not db_account:
        return None
    
    # Aggiorna solo i campi forniti (exclude_unset=True)
    update_data = account_update.model_dump(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(db_account, field, value)
    
    db.commit()
    db.refresh(db_account)
    
    return db_account


def delete_account(
    db: Session, 
    account_id: str, 
    user_id: str
) -> bool:
    """
    Elimina account (hard delete).
    
    Args:
        db: Database session
        account_id: ID account da eliminare
        user_id: ID utente (per verifica ownership)
    
    Returns:
        True se eliminato, False se non trovato
    """
    db_account = get_account(db, account_id, user_id)
    
    if not db_account:
        return False
    
    db.delete(db_account)
    db.commit()
    
    return True


def deactivate_account(
    db: Session, 
    account_id: str, 
    user_id: str
) -> Optional[Account]:
    """
    Disattiva account (soft delete).
    
    Args:
        db: Database session
        account_id: ID account da disattivare
        user_id: ID utente (per verifica ownership)
    
    Returns:
        Account disattivato se trovato, None altrimenti
    """
    db_account = get_account(db, account_id, user_id)
    
    if not db_account:
        return None
    
    db_account.is_active = False
    db.commit()
    db.refresh(db_account)
    
    return db_account


def update_account_balance(
    db: Session,
    account_id: str,
    amount: Decimal,
    operation: str
) -> Optional[Account]:
    """
    Aggiorna balance account (chiamato da transactions/transfers).
    
    Args:
        db: Database session
        account_id: ID account
        amount: Importo da aggiungere/sottrarre
        operation: 'add' per aggiungere, 'subtract' per sottrarre
    
    Returns:
        Account aggiornato se trovato, None altrimenti
    
    Note:
        Questa funzione NON fa commit - il chiamante deve gestire la transazione
    """
    account = db.query(Account).filter(Account.id == account_id).first()
    
    if not account:
        return None
    
    # Calcola nuovo balance basato su initial_balance + transazioni
    # Per ora aggiorniamo direttamente (in futuro si può calcolare dinamicamente)
    if operation == 'add':
        # Per income o transfer in entrata
        pass  # Il balance viene calcolato dalla property current_balance
    elif operation == 'subtract':
        # Per expense o transfer in uscita
        pass  # Il balance viene calcolato dalla property current_balance
    
    return account


def get_total_balance(db: Session, user_id: str) -> Decimal:
    """
    Calcola balance totale di tutti gli account attivi dell'utente.
    
    Args:
        db: Database session
        user_id: ID utente
    
    Returns:
        Somma dei balance di tutti gli account attivi
    """
    accounts = get_accounts(db, user_id, is_active=True)
    
    total = Decimal("0.00")
    for account in accounts:
        total += account.initial_balance  # In futuro: account.current_balance
    
    return total

def get_accounts_summary(db: Session, user_id: str) -> dict:
    """
    Calcola il riepilogo dei conti dell'utente.
    
    Separa:
    - Patrimonio liquido (checking, savings, cash)
    - Investimenti (investment)
    - Crediti/Prestiti (loan) - soldi che ti devono
    - Debiti (credit_card con balance negativo)
    - Altri (other)
    
    Returns:
        Dict con totali per categoria e totale patrimonio netto
    """
    from decimal import Decimal
    
    accounts = get_accounts(db, user_id, is_active=True, limit=500)
    
    # Categorie di account
    liquid_types = ['checking', 'savings', 'cash']
    investment_types = ['investment']
    loan_types = ['loan']  # Crediti verso terzi
    debt_types = ['credit_card']
    
    # Calcola totali per categoria
    total_liquid = Decimal("0.00")
    total_investments = Decimal("0.00")
    total_loans = Decimal("0.00")  # Crediti (soldi che ti devono)
    total_debts = Decimal("0.00")  # Debiti (soldi che devi)
    total_other = Decimal("0.00")
    
    accounts_by_type = {
        "liquid": [],
        "investments": [],
        "loans": [],
        "debts": [],
        "other": []
    }
    
    for account in accounts:
        balance = account.initial_balance
        
        if account.type in liquid_types:
            total_liquid += balance
            accounts_by_type["liquid"].append(account)
        elif account.type in investment_types:
            total_investments += balance
            accounts_by_type["investments"].append(account)
        elif account.type in loan_types:
            total_loans += balance
            accounts_by_type["loans"].append(account)
        elif account.type in debt_types:
            # Per carte di credito, balance negativo = debito
            if balance < 0:
                total_debts += abs(balance)
            else:
                total_liquid += balance  # Se positivo, è liquidità
            accounts_by_type["debts"].append(account)
        else:
            total_other += balance
            accounts_by_type["other"].append(account)
    
    # Patrimonio netto = liquido + investimenti - debiti
    # I prestiti (crediti) sono a parte perché sono soldi "bloccati"
    net_worth = total_liquid + total_investments - total_debts
    
    # Patrimonio totale inclusi crediti
    total_assets = net_worth + total_loans
    
    return {
        "total_liquid": total_liquid,
        "total_investments": total_investments,
        "total_loans": total_loans,  # Crediti verso terzi
        "total_debts": total_debts,
        "total_other": total_other,
        "net_worth": net_worth,  # Patrimonio netto (esclusi crediti)
        "total_assets": total_assets,  # Totale inclusi crediti
        "accounts_count": len(accounts),
        "by_category": {
            "liquid": {
                "total": total_liquid,
                "count": len(accounts_by_type["liquid"]),
                "types": liquid_types
            },
            "investments": {
                "total": total_investments,
                "count": len(accounts_by_type["investments"]),
                "types": investment_types
            },
            "loans": {
                "total": total_loans,
                "count": len(accounts_by_type["loans"]),
                "types": loan_types,
                "description": "Crediti verso terzi (soldi che ti devono)"
            },
            "debts": {
                "total": total_debts,
                "count": len(accounts_by_type["debts"]),
                "types": debt_types,
                "description": "Debiti (soldi che devi)"
            },
            "other": {
                "total": total_other,
                "count": len(accounts_by_type["other"]),
                "types": ["other"]
            }
        }
    }