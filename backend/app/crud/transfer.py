"""
Transfer CRUD Operations
Database operations per Transfer model con aggiornamento automatico balance accounts
"""
from sqlalchemy.orm import Session
from typing import List, Optional
from decimal import Decimal
from datetime import date

from app.models.transfer import Transfer
from app.models.account import Account
from app.schemas.transfer import (
    TransferCreate, 
    TransferUpdate, 
    VALID_TRANSFER_TYPES,
    TRANSFER_TYPE_DIRECTION_RULES,
    TRANSFER_TYPE_LABELS
)


def validate_transfer_direction(
    transfer_type: str,
    from_account: Account,
    to_account: Account
) -> None:
    """
    Valida che la direzione del trasferimento sia coerente con il tipo.
    
    Raises:
        ValueError: Se la direzione non è valida per il tipo di trasferimento
    """
    rules = TRANSFER_TYPE_DIRECTION_RULES.get(transfer_type)
    
    if not rules:
        return  # Tipo non riconosciuto, lascia passare (sarà gestito altrove)
    
    from_types = rules.get("from_account_types")
    to_types = rules.get("to_account_types")
    
    # Verifica account origine
    if from_types is not None and from_account.type not in from_types:
        allowed = ", ".join(from_types)
        raise ValueError(
            f"Per un trasferimento di tipo '{TRANSFER_TYPE_LABELS.get(transfer_type, transfer_type)}', "
            f"l'account di origine deve essere di tipo: {allowed}. "
            f"Account selezionato: {from_account.name} ({from_account.type})"
        )
    
    # Verifica account destinazione
    if to_types is not None and to_account.type not in to_types:
        allowed = ", ".join(to_types)
        raise ValueError(
            f"Per un trasferimento di tipo '{TRANSFER_TYPE_LABELS.get(transfer_type, transfer_type)}', "
            f"l'account di destinazione deve essere di tipo: {allowed}. "
            f"Account selezionato: {to_account.name} ({to_account.type})"
        )


def get_transfers(
    db: Session,
    user_id: str,
    skip: int = 0,
    limit: int = 100,
    transfer_type: Optional[str] = None,
    from_account_id: Optional[str] = None,
    to_account_id: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
) -> List[Transfer]:
    """
    Lista i trasferimenti dell'utente con filtri opzionali.
    """
    query = db.query(Transfer).filter(Transfer.user_id == user_id)
    
    if transfer_type is not None:
        query = query.filter(Transfer.type == transfer_type)
    
    if from_account_id is not None:
        query = query.filter(Transfer.from_account_id == from_account_id)
    
    if to_account_id is not None:
        query = query.filter(Transfer.to_account_id == to_account_id)
    
    if start_date is not None:
        query = query.filter(Transfer.date >= start_date)
    
    if end_date is not None:
        query = query.filter(Transfer.date <= end_date)
    
    query = query.order_by(Transfer.date.desc(), Transfer.created_at.desc())
    
    return query.offset(skip).limit(limit).all()


def get_transfer(
    db: Session,
    transfer_id: str,
    user_id: str
) -> Optional[Transfer]:
    """
    Recupera singolo trasferimento verificando ownership.
    """
    return db.query(Transfer).filter(
        Transfer.id == transfer_id,
        Transfer.user_id == user_id
    ).first()


def get_transfer_by_id(db: Session, transfer_id: str) -> Optional[Transfer]:
    """
    Recupera trasferimento per ID (senza verifica ownership).
    """
    return db.query(Transfer).filter(Transfer.id == transfer_id).first()


def create_transfer(
    db: Session,
    transfer: TransferCreate,
    user_id: str
) -> Transfer:
    """
    Crea nuovo trasferimento e aggiorna i balance di entrambi gli account.
    
    Raises:
        ValueError: Se account non trovato, direzione non valida, etc.
    """
    # Verifica che l'account origine esista e appartenga all'utente
    from_account = db.query(Account).filter(
        Account.id == transfer.from_account_id,
        Account.user_id == user_id
    ).first()
    
    if not from_account:
        raise ValueError("Source account not found")
    
    # Verifica che l'account destinazione esista e appartenga all'utente
    to_account = db.query(Account).filter(
        Account.id == transfer.to_account_id,
        Account.user_id == user_id
    ).first()
    
    if not to_account:
        raise ValueError("Destination account not found")
    
    # Verifica che gli account siano diversi
    if transfer.from_account_id == transfer.to_account_id:
        raise ValueError("Source and destination accounts must be different")
    
    # Valida la direzione del trasferimento rispetto al tipo
    validate_transfer_direction(transfer.type, from_account, to_account)
    
    # Calcola importo totale da sottrarre (amount + fee)
    fee = transfer.fee if transfer.fee else Decimal("0.00")
    total_deduction = transfer.amount + fee
    
    # Crea il trasferimento
    db_transfer = Transfer(
        user_id=user_id,
        from_account_id=transfer.from_account_id,
        to_account_id=transfer.to_account_id,
        type=transfer.type,
        amount=transfer.amount,
        date=transfer.date,
        description=transfer.description,
        notes=transfer.notes,
        exchange_rate=transfer.exchange_rate,
        fee=fee
    )
    
    db.add(db_transfer)
    
    # Aggiorna i balance degli account
    from_account.initial_balance -= total_deduction
    
    if transfer.exchange_rate:
        converted_amount = transfer.amount * transfer.exchange_rate
        to_account.initial_balance += converted_amount
    else:
        to_account.initial_balance += transfer.amount
    
    db.commit()
    db.refresh(db_transfer)
    
    return db_transfer


def update_transfer(
    db: Session,
    transfer_id: str,
    transfer_update: TransferUpdate,
    user_id: str
) -> Optional[Transfer]:
    """
    Aggiorna trasferimento esistente e ricalcola i balance se necessario.
    """
    db_transfer = get_transfer(db, transfer_id, user_id)
    
    if not db_transfer:
        return None
    
    # Salva valori precedenti per ricalcolo balance
    old_amount = db_transfer.amount
    old_fee = db_transfer.fee
    old_from_account_id = db_transfer.from_account_id
    old_to_account_id = db_transfer.to_account_id
    old_exchange_rate = db_transfer.exchange_rate
    
    # Prepara i dati di aggiornamento
    update_data = transfer_update.model_dump(exclude_unset=True)
    
    # Determina i nuovi valori (o mantieni i vecchi)
    new_from_account_id = update_data.get("from_account_id", old_from_account_id)
    new_to_account_id = update_data.get("to_account_id", old_to_account_id)
    new_type = update_data.get("type", db_transfer.type)
    
    # Verifica nuovi account se specificati
    if new_from_account_id != old_from_account_id:
        new_from_account = db.query(Account).filter(
            Account.id == new_from_account_id,
            Account.user_id == user_id
        ).first()
        if not new_from_account:
            raise ValueError("New source account not found")
    else:
        new_from_account = db.query(Account).filter(Account.id == new_from_account_id).first()
    
    if new_to_account_id != old_to_account_id:
        new_to_account = db.query(Account).filter(
            Account.id == new_to_account_id,
            Account.user_id == user_id
        ).first()
        if not new_to_account:
            raise ValueError("New destination account not found")
    else:
        new_to_account = db.query(Account).filter(Account.id == new_to_account_id).first()
    
    if new_from_account_id == new_to_account_id:
        raise ValueError("Source and destination accounts must be different")
    
    # Valida la direzione se cambiano account o tipo
    if (new_from_account_id != old_from_account_id or 
        new_to_account_id != old_to_account_id or 
        "type" in update_data):
        validate_transfer_direction(new_type, new_from_account, new_to_account)
    
    # Ripristina i balance precedenti
    old_from_account = db.query(Account).filter(Account.id == old_from_account_id).first()
    old_to_account = db.query(Account).filter(Account.id == old_to_account_id).first()
    
    if old_from_account:
        old_from_account.initial_balance += (old_amount + old_fee)
    
    if old_to_account:
        if old_exchange_rate:
            old_to_account.initial_balance -= (old_amount * old_exchange_rate)
        else:
            old_to_account.initial_balance -= old_amount
    
    # Applica gli aggiornamenti
    for field, value in update_data.items():
        setattr(db_transfer, field, value)
    
    # Applica nuovi balance
    new_amount = db_transfer.amount
    new_fee = db_transfer.fee
    new_exchange_rate = db_transfer.exchange_rate
    
    new_from_account = db.query(Account).filter(Account.id == new_from_account_id).first()
    new_to_account = db.query(Account).filter(Account.id == new_to_account_id).first()
    
    if new_from_account:
        new_from_account.initial_balance -= (new_amount + new_fee)
    
    if new_to_account:
        if new_exchange_rate:
            new_to_account.initial_balance += (new_amount * new_exchange_rate)
        else:
            new_to_account.initial_balance += new_amount
    
    db.commit()
    db.refresh(db_transfer)
    
    return db_transfer


def delete_transfer(
    db: Session,
    transfer_id: str,
    user_id: str
) -> bool:
    """
    Elimina trasferimento e ripristina i balance degli account.
    """
    db_transfer = get_transfer(db, transfer_id, user_id)
    
    if not db_transfer:
        return False
    
    from_account = db.query(Account).filter(Account.id == db_transfer.from_account_id).first()
    to_account = db.query(Account).filter(Account.id == db_transfer.to_account_id).first()
    
    if from_account:
        from_account.initial_balance += (db_transfer.amount + db_transfer.fee)
    
    if to_account:
        if db_transfer.exchange_rate:
            to_account.initial_balance -= (db_transfer.amount * db_transfer.exchange_rate)
        else:
            to_account.initial_balance -= db_transfer.amount
    
    db.delete(db_transfer)
    db.commit()
    
    return True


def get_transfers_by_type(
    db: Session,
    user_id: str,
    transfer_type: str,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
) -> List[Transfer]:
    """
    Recupera trasferimenti per tipo specifico.
    """
    return get_transfers(
        db,
        user_id=user_id,
        transfer_type=transfer_type,
        start_date=start_date,
        end_date=end_date,
        limit=1000
    )


def get_loans_summary(
    db: Session,
    user_id: str
) -> dict:
    """
    Calcola riepilogo prestiti (dati e ricevuti).
    """
    loans_given = get_transfers_by_type(db, user_id, "loan_given")
    loans_received = get_transfers_by_type(db, user_id, "loan_received")
    
    total_given = sum(t.amount for t in loans_given)
    total_received = sum(t.amount for t in loans_received)
    
    return {
        "loans_given_count": len(loans_given),
        "loans_given_total": total_given,
        "loans_received_count": len(loans_received),
        "loans_received_total": total_received,
        "net_loans": total_given - total_received,
        "loans_given": loans_given,
        "loans_received": loans_received
    }


def get_transfer_statistics(
    db: Session,
    user_id: str,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
) -> dict:
    """
    Calcola statistiche sui trasferimenti per tipo.
    """
    query = db.query(Transfer).filter(Transfer.user_id == user_id)
    
    if start_date:
        query = query.filter(Transfer.date >= start_date)
    
    if end_date:
        query = query.filter(Transfer.date <= end_date)
    
    transfers = query.all()
    
    by_type = {}
    for t_type in VALID_TRANSFER_TYPES:
        type_transfers = [t for t in transfers if t.type == t_type]
        by_type[t_type] = {
            "count": len(type_transfers),
            "total_amount": sum(t.amount for t in type_transfers),
            "total_fees": sum(t.fee for t in type_transfers)
        }
    
    total_transferred = sum(t.amount for t in transfers)
    total_fees = sum(t.fee for t in transfers)
    
    return {
        "total_transfers": len(transfers),
        "total_amount_transferred": total_transferred,
        "total_fees_paid": total_fees,
        "average_transfer_amount": total_transferred / len(transfers) if transfers else Decimal("0.00"),
        "by_type": by_type
    }
