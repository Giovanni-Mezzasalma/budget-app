"""
Transaction CRUD Operations
Database operations per Transaction model con aggiornamento automatico balance account
"""
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import List, Optional, Dict
from decimal import Decimal
from datetime import date

from app.models.transaction import Transaction
from app.models.account import Account
from app.models.category import Category
from app.schemas.transaction import TransactionCreate, TransactionUpdate, TransactionSummary


def get_transactions(
    db: Session,
    user_id: str,
    skip: int = 0,
    limit: int = 100,
    account_id: Optional[str] = None,
    category_id: Optional[str] = None,
    transaction_type: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    min_amount: Optional[Decimal] = None,
    max_amount: Optional[Decimal] = None,
    tags: Optional[List[str]] = None,
    search: Optional[str] = None
) -> List[Transaction]:
    """
    Lista le transazioni dell'utente con filtri opzionali.
    
    Args:
        db: Database session
        user_id: ID utente proprietario
        skip: Offset per paginazione
        limit: Numero massimo risultati
        account_id: Filtra per account
        category_id: Filtra per categoria
        transaction_type: Filtra per tipo (income, expense_necessity, expense_extra)
        start_date: Data inizio periodo
        end_date: Data fine periodo
        min_amount: Importo minimo
        max_amount: Importo massimo
        tags: Filtra per tags
        search: Cerca in description/notes
    """
    query = db.query(Transaction).filter(Transaction.user_id == user_id)
    
    # Filtro per account
    if account_id is not None:
        query = query.filter(Transaction.account_id == account_id)
    
    # Filtro per categoria
    if category_id is not None:
        query = query.filter(Transaction.category_id == category_id)
    
    # Filtro per tipo
    if transaction_type is not None:
        query = query.filter(Transaction.type == transaction_type)
    
    # Filtro per date
    if start_date is not None:
        query = query.filter(Transaction.date >= start_date)
    
    if end_date is not None:
        query = query.filter(Transaction.date <= end_date)
    
    # Filtro per importo
    if min_amount is not None:
        query = query.filter(Transaction.amount >= min_amount)
    
    if max_amount is not None:
        query = query.filter(Transaction.amount <= max_amount)
    
    # Filtro per tags (almeno uno dei tags specificati)
    if tags is not None and len(tags) > 0:
        query = query.filter(Transaction.tags.overlap(tags))
    
    # Ricerca in description e notes
    if search is not None and search.strip():
        search_term = f"%{search.strip()}%"
        query = query.filter(
            or_(
                Transaction.description.ilike(search_term),
                Transaction.notes.ilike(search_term)
            )
        )
    
    # Ordina per data decrescente (più recenti prima)
    query = query.order_by(Transaction.date.desc(), Transaction.created_at.desc())
    
    return query.offset(skip).limit(limit).all()


def get_transaction(
    db: Session,
    transaction_id: str,
    user_id: str
) -> Optional[Transaction]:
    """
    Recupera singola transazione verificando ownership.
    """
    return db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.user_id == user_id
    ).first()


def get_transaction_by_id(db: Session, transaction_id: str) -> Optional[Transaction]:
    """
    Recupera transazione per ID (senza verifica ownership).
    """
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()


def create_transaction(
    db: Session,
    transaction: TransactionCreate,
    user_id: str
) -> Transaction:
    """
    Crea nuova transazione e aggiorna il balance dell'account.
    
    Il tipo della transazione viene derivato dalla categoria selezionata.
    """
    # Verifica che l'account esista e appartenga all'utente
    account = db.query(Account).filter(
        Account.id == transaction.account_id,
        Account.user_id == user_id
    ).first()
    
    if not account:
        raise ValueError("Account not found")
    
    # Verifica che la categoria esista e appartenga all'utente
    category = db.query(Category).filter(
        Category.id == transaction.category_id,
        Category.user_id == user_id
    ).first()
    
    if not category:
        raise ValueError("Category not found")
    
    # Il tipo della transazione deriva dalla categoria
    transaction_type = category.type
    
    # Crea la transazione
    db_transaction = Transaction(
        user_id=user_id,
        account_id=transaction.account_id,
        category_id=transaction.category_id,
        amount=transaction.amount,
        type=transaction_type,
        date=transaction.date,
        description=transaction.description,
        notes=transaction.notes,
        tags=transaction.tags,
        is_recurring=False,
        recurring_frequency=None
    )
    
    db.add(db_transaction)
    
    # Aggiorna il balance dell'account
    _update_account_balance_for_transaction(account, transaction.amount, transaction_type, "add")
    
    db.commit()
    db.refresh(db_transaction)
    
    return db_transaction


def update_transaction(
    db: Session,
    transaction_id: str,
    transaction_update: TransactionUpdate,
    user_id: str
) -> Optional[Transaction]:
    """
    Aggiorna transazione esistente e ricalcola i balance se necessario.
    """
    db_transaction = get_transaction(db, transaction_id, user_id)
    
    if not db_transaction:
        return None
    
    # Salva valori precedenti per ricalcolo balance
    old_amount = db_transaction.amount
    old_type = db_transaction.type
    old_account_id = db_transaction.account_id
    
    # Prepara i dati di aggiornamento
    update_data = transaction_update.model_dump(exclude_unset=True)
    
    # Se cambia la categoria, aggiorna anche il tipo
    new_type = old_type
    if "category_id" in update_data:
        category = db.query(Category).filter(
            Category.id == update_data["category_id"],
            Category.user_id == user_id
        ).first()
        
        if not category:
            raise ValueError("Category not found")
        
        new_type = category.type
        update_data["type"] = new_type
    
    # Se cambia l'account, verifica che esista
    new_account_id = update_data.get("account_id", old_account_id)
    if new_account_id != old_account_id:
        new_account = db.query(Account).filter(
            Account.id == new_account_id,
            Account.user_id == user_id
        ).first()
        
        if not new_account:
            raise ValueError("Account not found")
    
    # Applica gli aggiornamenti
    for field, value in update_data.items():
        setattr(db_transaction, field, value)
    
    new_amount = db_transaction.amount
    
    # Ricalcola i balance se necessario
    if old_account_id != new_account_id or old_amount != new_amount or old_type != new_type:
        # Rimuovi effetto dal vecchio account
        old_account = db.query(Account).filter(Account.id == old_account_id).first()
        if old_account:
            _update_account_balance_for_transaction(old_account, old_amount, old_type, "remove")
        
        # Aggiungi effetto al nuovo account
        new_account = db.query(Account).filter(Account.id == new_account_id).first()
        if new_account:
            _update_account_balance_for_transaction(new_account, new_amount, new_type, "add")
    
    db.commit()
    db.refresh(db_transaction)
    
    return db_transaction


def delete_transaction(
    db: Session,
    transaction_id: str,
    user_id: str
) -> bool:
    """
    Elimina transazione e ripristina il balance dell'account.
    """
    db_transaction = get_transaction(db, transaction_id, user_id)
    
    if not db_transaction:
        return False
    
    # Ripristina il balance dell'account
    account = db.query(Account).filter(Account.id == db_transaction.account_id).first()
    if account:
        _update_account_balance_for_transaction(
            account, 
            db_transaction.amount, 
            db_transaction.type, 
            "remove"
        )
    
    db.delete(db_transaction)
    db.commit()
    
    return True


def get_transaction_summary(
    db: Session,
    user_id: str,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    account_id: Optional[str] = None
) -> TransactionSummary:
    """
    Calcola il riepilogo delle transazioni per un periodo.
    """
    query = db.query(Transaction).filter(Transaction.user_id == user_id)
    
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    
    if end_date:
        query = query.filter(Transaction.date <= end_date)
    
    if account_id:
        query = query.filter(Transaction.account_id == account_id)
    
    transactions = query.all()
    
    total_income = Decimal("0.00")
    total_expense_necessity = Decimal("0.00")
    total_expense_extra = Decimal("0.00")
    
    for t in transactions:
        if t.type == "income":
            total_income += t.amount
        elif t.type == "expense_necessity":
            total_expense_necessity += t.amount
        elif t.type == "expense_extra":
            total_expense_extra += t.amount
    
    total_expenses = total_expense_necessity + total_expense_extra
    net = total_income - total_expenses
    
    return TransactionSummary(
        total_income=total_income,
        total_expense_necessity=total_expense_necessity,
        total_expense_extra=total_expense_extra,
        total_expenses=total_expenses,
        net=net,
        transaction_count=len(transactions)
    )


def get_transactions_by_category(
    db: Session,
    user_id: str,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
) -> Dict[str, Decimal]:
    """
    Raggruppa le transazioni per categoria e calcola i totali.
    """
    query = db.query(Transaction).filter(Transaction.user_id == user_id)
    
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    
    if end_date:
        query = query.filter(Transaction.date <= end_date)
    
    transactions = query.all()
    
    # Raggruppa per category_id
    by_category: Dict[str, Decimal] = {}
    
    for t in transactions:
        if t.category_id not in by_category:
            by_category[t.category_id] = Decimal("0.00")
        by_category[t.category_id] += t.amount
    
    return by_category


def get_monthly_totals(
    db: Session,
    user_id: str,
    year: int,
    month: int
) -> TransactionSummary:
    """
    Calcola i totali per un mese specifico.
    """
    from calendar import monthrange
    
    start_date = date(year, month, 1)
    _, last_day = monthrange(year, month)
    end_date = date(year, month, last_day)
    
    return get_transaction_summary(db, user_id, start_date, end_date)


def _update_account_balance_for_transaction(
    account: Account,
    amount: Decimal,
    transaction_type: str,
    operation: str
) -> None:
    """
    Aggiorna il balance dell'account in base alla transazione.
    
    Args:
        account: Account da aggiornare
        amount: Importo transazione
        transaction_type: Tipo (income, expense_necessity, expense_extra)
        operation: "add" per nuova transazione, "remove" per eliminazione
    
    Logica:
    - income + add → balance aumenta
    - income + remove → balance diminuisce
    - expense + add → balance diminuisce
    - expense + remove → balance aumenta
    """
    is_expense = transaction_type in ["expense_necessity", "expense_extra"]
    
    if operation == "add":
        if is_expense:
            account.initial_balance -= amount
        else:  # income
            account.initial_balance += amount
    elif operation == "remove":
        if is_expense:
            account.initial_balance += amount
        else:  # income
            account.initial_balance -= amount