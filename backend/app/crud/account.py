"""
Account CRUD Operations
Database operations for Account model with proper balance management.

Balance Strategy:
- initial_balance: Set at creation, NEVER modified
- current_balance: Updated by transactions and transfers
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
    is_active: Optional[bool] = None,
    account_type: Optional[str] = None
) -> List[Account]:
    """
    List all accounts for a user.
    
    Args:
        db: Database session
        user_id: Owner user ID
        skip: Pagination offset
        limit: Maximum results
        is_active: Filter by active/inactive status
        account_type: Filter by account type
    
    Returns:
        List of Account objects
    """
    query = db.query(Account).filter(Account.user_id == user_id)
    
    if is_active is not None:
        query = query.filter(Account.is_active == is_active)
    
    if account_type is not None:
        query = query.filter(Account.type == account_type)
    
    return query.order_by(Account.name).offset(skip).limit(limit).all()


def get_account(
    db: Session, 
    account_id: str, 
    user_id: str
) -> Optional[Account]:
    """
    Get single account verifying ownership.
    
    Args:
        db: Database session
        account_id: Account ID to retrieve
        user_id: User ID (for ownership verification)
    
    Returns:
        Account object if found and belongs to user, None otherwise
    """
    return db.query(Account).filter(
        Account.id == account_id,
        Account.user_id == user_id
    ).first()


def get_account_by_id(db: Session, account_id: str) -> Optional[Account]:
    """
    Get account by ID (without ownership verification).
    Use only internally when ownership already verified.
    """
    return db.query(Account).filter(Account.id == account_id).first()


def create_account(
    db: Session, 
    account: AccountCreate, 
    user_id: str
) -> Account:
    """
    Create new account for user.
    
    initial_balance and current_balance are set to the same value at creation.
    After creation, only current_balance will be modified by transactions/transfers.
    
    Args:
        db: Database session
        account: Account data from AccountCreate schema
        user_id: Owner user ID
    
    Returns:
        Created Account object
    """
    db_account = Account(
        user_id=user_id,
        name=account.name,
        type=account.type,
        currency=account.currency,
        initial_balance=account.initial_balance,
        current_balance=account.initial_balance,  # Start with same value
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
    Update existing account.
    
    Note: initial_balance and current_balance cannot be modified through this function.
    - initial_balance is immutable after creation
    - current_balance is only modified by transactions/transfers
    
    Args:
        db: Database session
        account_id: Account ID to update
        account_update: Data to update
        user_id: User ID (for ownership verification)
    
    Returns:
        Updated account if found, None otherwise
    """
    db_account = get_account(db, account_id, user_id)
    
    if not db_account:
        return None
    
    # Update only provided fields (exclude_unset=True)
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
    Delete account (hard delete).
    
    Args:
        db: Database session
        account_id: Account ID to delete
        user_id: User ID (for ownership verification)
    
    Returns:
        True if deleted, False if not found
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
    Deactivate account (soft delete).
    
    Args:
        db: Database session
        account_id: Account ID to deactivate
        user_id: User ID (for ownership verification)
    
    Returns:
        Deactivated account if found, None otherwise
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
    Update account's current_balance (called by transactions/transfers).
    
    Args:
        db: Database session
        account_id: Account ID
        amount: Amount to add/subtract
        operation: 'add' to add, 'subtract' to subtract
    
    Returns:
        Updated account if found, None otherwise
    
    Note:
        This function does NOT commit - caller must manage the transaction.
        Only current_balance is modified, initial_balance remains unchanged.
    """
    account = db.query(Account).filter(Account.id == account_id).first()
    
    if not account:
        return None
    
    if operation == 'add':
        account.current_balance += amount
    elif operation == 'subtract':
        account.current_balance -= amount
    else:
        raise ValueError(f"Invalid operation: {operation}. Must be 'add' or 'subtract'")
    
    return account


def get_total_balance(db: Session, user_id: str, is_active: Optional[bool] = True) -> Decimal:
    """
    Calculate total current_balance of all accounts for a user.
    
    Args:
        db: Database session
        user_id: User ID
        is_active: Filter by active status (default: only active accounts)
    
    Returns:
        Sum of current_balance of all matching accounts
    """
    accounts = get_accounts(db, user_id, is_active=is_active, limit=1000)
    
    total = Decimal("0.00")
    for account in accounts:
        total += account.current_balance
    
    return total


def get_accounts_summary(db: Session, user_id: str) -> dict:
    """
    Calculate financial summary for user's accounts.
    
    Categories:
    - Liquid assets (checking, savings, cash)
    - Investments (investment)
    - Credits/Loans (loan) - money owed to you
    - Debts (credit_card with negative balance)
    - Other (other)
    
    Returns:
        Dict with totals by category and net worth calculations
    """
    accounts = get_accounts(db, user_id, is_active=True, limit=500)
    
    # Account type categories
    liquid_types = ['checking', 'savings', 'cash']
    investment_types = ['investment']
    loan_types = ['loan']  # Credits to third parties
    debt_types = ['credit_card']
    
    # Calculate totals by category
    total_liquid = Decimal("0.00")
    total_investments = Decimal("0.00")
    total_loans = Decimal("0.00")  # Credits (money owed to you)
    total_debts = Decimal("0.00")  # Debts (money you owe)
    total_other = Decimal("0.00")
    
    # Also track initial balances for comparison
    initial_liquid = Decimal("0.00")
    initial_investments = Decimal("0.00")
    
    accounts_by_type = {
        "liquid": [],
        "investments": [],
        "loans": [],
        "debts": [],
        "other": []
    }
    
    for account in accounts:
        balance = account.current_balance  # Use current_balance, not initial_balance
        
        if account.type in liquid_types:
            total_liquid += balance
            initial_liquid += account.initial_balance
            accounts_by_type["liquid"].append(account)
        elif account.type in investment_types:
            total_investments += balance
            initial_investments += account.initial_balance
            accounts_by_type["investments"].append(account)
        elif account.type in loan_types:
            total_loans += balance
            accounts_by_type["loans"].append(account)
        elif account.type in debt_types:
            # For credit cards, negative balance = debt
            if balance < 0:
                total_debts += abs(balance)
            else:
                total_liquid += balance  # If positive, it's liquidity
            accounts_by_type["debts"].append(account)
        else:
            total_other += balance
            accounts_by_type["other"].append(account)
    
    # Net worth = liquid + investments - debts
    # Loans (credits) are separate as they're "locked" money
    net_worth = total_liquid + total_investments - total_debts
    
    # Total assets including credits
    total_assets = net_worth + total_loans
    
    return {
        "total_liquid": total_liquid,
        "total_investments": total_investments,
        "total_loans": total_loans,  # Credits to third parties
        "total_debts": total_debts,
        "total_other": total_other,
        "net_worth": net_worth,  # Net worth (excluding credits)
        "total_assets": total_assets,  # Total including credits
        "accounts_count": len(accounts),
        "by_category": {
            "liquid": {
                "total": total_liquid,
                "initial": initial_liquid,
                "difference": total_liquid - initial_liquid,
                "count": len(accounts_by_type["liquid"]),
                "types": liquid_types
            },
            "investments": {
                "total": total_investments,
                "initial": initial_investments,
                "difference": total_investments - initial_investments,
                "count": len(accounts_by_type["investments"]),
                "types": investment_types
            },
            "loans": {
                "total": total_loans,
                "count": len(accounts_by_type["loans"]),
                "types": loan_types,
                "description": "Credits to third parties (money owed to you)"
            },
            "debts": {
                "total": total_debts,
                "count": len(accounts_by_type["debts"]),
                "types": debt_types,
                "description": "Debts (money you owe)"
            },
            "other": {
                "total": total_other,
                "count": len(accounts_by_type["other"]),
                "types": ["other"]
            }
        }
    }


def verify_all_balances(db: Session, user_id: str) -> List[dict]:
    """
    Verify balance integrity for all user accounts.
    
    Returns:
        List of accounts with balance discrepancies
    """
    accounts = get_accounts(db, user_id, limit=1000)
    discrepancies = []
    
    for account in accounts:
        is_valid, difference = account.verify_balance_integrity()
        if not is_valid:
            discrepancies.append({
                "account_id": account.id,
                "account_name": account.name,
                "current_balance": float(account.current_balance),
                "calculated_balance": float(account.recalculate_balance()),
                "difference": float(difference)
            })
    
    return discrepancies


def fix_account_balance(db: Session, account_id: str, user_id: str) -> Optional[Account]:
    """
    Recalculate and fix current_balance from transactions/transfers.
    
    Use this to correct any balance discrepancies.
    
    Args:
        db: Database session
        account_id: Account ID to fix
        user_id: User ID (for ownership verification)
    
    Returns:
        Account with corrected balance, None if not found
    """
    account = get_account(db, account_id, user_id)
    
    if not account:
        return None
    
    # Recalculate from transactions and transfers
    correct_balance = account.recalculate_balance()
    account.current_balance = correct_balance
    
    db.commit()
    db.refresh(account)
    
    return account
