"""
Transaction CRUD Operations
Database operations for Transaction model with automatic current_balance updates.

Transaction types (derived from category):
- income: Income
- expense_necessity: Necessity expenses
- expense_extra: Extra/discretionary expenses
"""
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional, Dict, Union
from uuid import UUID
from decimal import Decimal
from datetime import date

from app.models.transaction import Transaction
from app.models.account import Account
from app.models.category import Category
from app.schemas.transaction import TransactionCreate, TransactionUpdate, TransactionSummary

def _to_uuid(value: Union[str, UUID, None]) -> Optional[UUID]:
    """Convert string to UUID if necessary."""
    if value is None:
        return None
    if isinstance(value, str):
        return UUID(value)
    return value

def get_transactions(
    db: Session,
    user_id: Union[str, UUID],
    skip: int = 0,
    limit: int = 100,
    account_id: Optional[Union[str, UUID]] = None,
    category_id: Optional[Union[str, UUID]] = None,
    transaction_type: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    min_amount: Optional[Decimal] = None,
    max_amount: Optional[Decimal] = None,
    tags: Optional[List[str]] = None,
    search: Optional[str] = None
) -> List[Transaction]:
    """
    List user transactions with optional filters.
    
    Args:
        db: Database session
        user_id: Owner user ID
        skip: Pagination offset
        limit: Maximum results
        account_id: Filter by account
        category_id: Filter by category
        transaction_type: Filter by type (income, expense_necessity, expense_extra)
        start_date: Period start date
        end_date: Period end date
        min_amount: Minimum amount
        max_amount: Maximum amount
        tags: Filter by tags
        search: Search in description/notes
    """
    user_id = _to_uuid(user_id)
    query = db.query(Transaction).filter(Transaction.user_id == user_id)
    
    if account_id is not None:
        account_id = _to_uuid(account_id)
        query = query.filter(Transaction.account_id == account_id)
    
    if category_id is not None:
        category_id = _to_uuid(category_id)
        query = query.filter(Transaction.category_id == category_id)
    
    if transaction_type is not None:
        query = query.filter(Transaction.type == transaction_type)
    
    if start_date is not None:
        query = query.filter(Transaction.date >= start_date)
    
    if end_date is not None:
        query = query.filter(Transaction.date <= end_date)
    
    if min_amount is not None:
        query = query.filter(Transaction.amount >= min_amount)
    
    if max_amount is not None:
        query = query.filter(Transaction.amount <= max_amount)
    
    if tags is not None and len(tags) > 0:
        query = query.filter(Transaction.tags.overlap(tags))
    
    if search is not None and search.strip():
        search_term = f"%{search.strip()}%"
        query = query.filter(
            or_(
                Transaction.description.ilike(search_term),
                Transaction.notes.ilike(search_term)
            )
        )
    
    # Order by date descending (most recent first)
    query = query.order_by(Transaction.date.desc(), Transaction.created_at.desc())
    
    return query.offset(skip).limit(limit).all()


def get_transaction(
    db: Session,
    transaction_id: Union[str, UUID],
    user_id: Union[str, UUID]
) -> Optional[Transaction]:
    """Get single transaction verifying ownership."""
    transaction_id = _to_uuid(transaction_id)
    user_id = _to_uuid(user_id)
    return db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.user_id == user_id
    ).first()


def get_transaction_by_id(db: Session, transaction_id: Union[str, UUID]) -> Optional[Transaction]:
    """Get transaction by ID (without ownership verification)."""
    transaction_id = _to_uuid(transaction_id)
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()


def create_transaction(
    db: Session,
    transaction: TransactionCreate,
    user_id: Union[str, UUID]
) -> Transaction:
    """
    Create new transaction and update account's current_balance.
    
    Transaction type is derived from the selected category.
    
    Balance update logic:
    - income: current_balance += amount
    - expense_necessity/expense_extra: current_balance -= amount
    """
    user_id = _to_uuid(user_id)
    account_id = _to_uuid(transaction.account_id)
    category_id = _to_uuid(transaction.category_id)
    # Verify account exists and belongs to user
    account = db.query(Account).filter(
        Account.id == account_id,
        Account.user_id == user_id
    ).first()
    
    if not account:
        raise ValueError("Account not found")
    
    # Verify category exists and belongs to user
    category = db.query(Category).filter(
        Category.id == category_id,
        Category.user_id == user_id
    ).first()
    
    if not category:
        raise ValueError("Category not found")
    
    # Transaction type is derived from category
    transaction_type = category.type
    
    # Create the transaction
    db_transaction = Transaction(
        user_id=user_id,
        account_id=account_id,
        category_id=category_id,
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
    
    # Update account's current_balance (NOT initial_balance)
    _update_account_balance_for_transaction(account, transaction.amount, transaction_type, "add")
    
    db.commit()
    db.refresh(db_transaction)
    
    return db_transaction


def update_transaction(
    db: Session,
    transaction_id: Union[str, UUID],
    transaction_update: TransactionUpdate,
    user_id: Union[str, UUID]
) -> Optional[Transaction]:
    """
    Update existing transaction and recalculate balances if necessary.
    
    If amount, type, or account changes, balances are recalculated.
    """
    db_transaction = get_transaction(db, transaction_id, user_id)
    
    if not db_transaction:
        return None
    
    # Save old values for balance recalculation
    old_amount = db_transaction.amount
    old_type = db_transaction.type
    old_account_id = db_transaction.account_id
    
    # Prepare update data
    update_data = transaction_update.model_dump(exclude_unset=True)
    
    # If category changes, update type as well
    new_type = old_type
    if "category_id" in update_data:
        category_id = _to_uuid(update_data["category_id"])
        category = db.query(Category).filter(
            Category.id == category_id,
            Category.user_id == _to_uuid(user_id)
        ).first()
        
        if not category:
            raise ValueError("Category not found")
        
        new_type = category.type
        update_data["type"] = new_type
        update_data["category_id"] = category_id
    
    # If account changes, verify it exists
    new_account_id = _to_uuid(update_data.get("account_id")) if "account_id" in update_data else old_account_id
    if new_account_id != old_account_id:
        new_account = db.query(Account).filter(
            Account.id == new_account_id,
            Account.user_id == _to_uuid(user_id)
        ).first()
        
        if not new_account:
            raise ValueError("Account not found")
        
        update_data["account_id"] = new_account_id
    
    # Apply updates
    for field, value in update_data.items():
        setattr(db_transaction, field, value)
    
    new_amount = db_transaction.amount
    
    # Recalculate balances if necessary
    if old_account_id != new_account_id or old_amount != new_amount or old_type != new_type:
        # Remove effect from old account
        old_account = db.query(Account).filter(Account.id == old_account_id).first()
        if old_account:
            _update_account_balance_for_transaction(old_account, old_amount, old_type, "remove")
        
        # Add effect to new account
        new_account = db.query(Account).filter(Account.id == new_account_id).first()
        if new_account:
            _update_account_balance_for_transaction(new_account, new_amount, new_type, "add")
    
    db.commit()
    db.refresh(db_transaction)
    
    return db_transaction


def delete_transaction(
    db: Session,
    transaction_id: Union[str, UUID],
    user_id: Union[str, UUID]
) -> bool:
    """
    Delete transaction and restore account's current_balance.
    """
    db_transaction = get_transaction(db, transaction_id, user_id)
    
    if not db_transaction:
        return False
    
    # Restore account's current_balance
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
    user_id: Union[str, UUID],
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    account_id: Optional[Union[str, UUID]] = None
) -> TransactionSummary:
    """Calculate transaction summary for a period."""
    user_id = _to_uuid(user_id)
    query = db.query(Transaction).filter(Transaction.user_id == user_id)
    
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    
    if end_date:
        query = query.filter(Transaction.date <= end_date)
    
    if account_id:
        account_id = _to_uuid(account_id)
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
    user_id: Union[str, UUID],
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
) -> Dict[str, Decimal]:
    """Group transactions by category and calculate totals."""
    user_id = _to_uuid(user_id)
    query = db.query(Transaction).filter(Transaction.user_id == user_id)
    
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    
    if end_date:
        query = query.filter(Transaction.date <= end_date)
    
    transactions = query.all()
    
    by_category: Dict[str, Decimal] = {}
    
    for t in transactions:
        if t.category_id not in by_category:
            by_category[t.category_id] = Decimal("0.00")
        by_category[t.category_id] += t.amount
    
    return by_category


def get_monthly_totals(
    db: Session,
    user_id: Union[str, UUID],
    year: int,
    month: int
) -> TransactionSummary:
    """Calculate totals for a specific month."""
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
    Update account's current_balance based on transaction.
    
    Args:
        account: Account to update
        amount: Transaction amount
        transaction_type: Type (income, expense_necessity, expense_extra)
        operation: "add" for new transaction, "remove" for deletion
    
    Logic:
    - income + add → current_balance increases
    - income + remove → current_balance decreases
    - expense + add → current_balance decreases
    - expense + remove → current_balance increases
    
    Note: Only current_balance is modified, initial_balance remains unchanged.
    """
    is_expense = transaction_type in ["expense_necessity", "expense_extra"]
    
    if operation == "add":
        if is_expense:
            account.current_balance -= amount
        else:  # income
            account.current_balance += amount
    elif operation == "remove":
        if is_expense:
            account.current_balance += amount
        else:  # income
            account.current_balance -= amount
    else:
        raise ValueError(f"Invalid operation: {operation}. Must be 'add' or 'remove'")
