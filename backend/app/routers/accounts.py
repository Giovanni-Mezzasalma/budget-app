"""
Accounts Router
User account management with proper balance handling.

Balance Strategy:
- initial_balance: Set at creation, immutable
- current_balance: Updated automatically by transactions/transfers
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
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=100, description="Maximum number of results"),
    is_active: Optional[bool] = Query(None, description="Filter by active/inactive status"),
    type: Optional[str] = Query(None, description="Filter by account type")
):
    """
    List all accounts for the current user.
    
    - **skip**: Pagination offset (default: 0)
    - **limit**: Maximum results (default: 100, max: 100)
    - **is_active**: Filter active (true) or inactive (false) only
    - **type**: Filter by account type (checking, savings, etc.)
    
    **Response includes:**
    - `initial_balance`: Balance set at creation (immutable)
    - `current_balance`: Current balance (updated by transactions/transfers)
    """
    accounts = account_crud.get_accounts(
        db, 
        user_id=str(current_user.id), 
        skip=skip, 
        limit=limit,
        is_active=is_active,
        account_type=type
    )
    return accounts


@router.post("/", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
async def create_account(
    account: AccountCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create a new account.
    
    - **name**: Account name (e.g., "Checking Account", "Savings")
    - **type**: Account type (checking, savings, credit_card, cash, investment, loan, other)
    - **currency**: ISO 4217 currency code (default: EUR)
    - **initial_balance**: Starting balance (default: 0.00) - **set once, never changes**
    - **color**: HEX color for UI (e.g., #3B82F6)
    - **icon**: Icon/emoji for UI
    - **notes**: Additional notes
    
    ⚠️ `initial_balance` is set at creation and cannot be modified afterwards.
    `current_balance` will be automatically initialized to the same value.
    """
    return account_crud.create_account(
        db, 
        account=account, 
        user_id=str(current_user.id)
    )


@router.get("/summary")
async def get_accounts_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get financial summary for the user.
    
    **Categories:**
    - **Liquid** (checking, savings, cash): Available money
    - **Investments** (investment): Invested capital
    - **Credits/Loans** (loan): Money owed to you (loans given)
    - **Debts** (negative credit_card): Money you owe
    
    **Calculations:**
    - **net_worth**: Net worth = Liquid + Investments - Debts
    - **total_assets**: Total assets = net_worth + Credits
    
    Uses `current_balance` for all calculations.
    """
    summary = account_crud.get_accounts_summary(db, user_id=str(current_user.id))
    
    # Convert Decimal to float for JSON
    return {
        "total_liquid": float(summary["total_liquid"]),
        "total_investments": float(summary["total_investments"]),
        "total_loans": float(summary["total_loans"]),
        "total_debts": float(summary["total_debts"]),
        "total_other": float(summary["total_other"]),
        "net_worth": float(summary["net_worth"]),
        "total_assets": float(summary["total_assets"]),
        "accounts_count": summary["accounts_count"],
        "by_category": {
            "liquid": {
                "total": float(summary["by_category"]["liquid"]["total"]),
                "initial": float(summary["by_category"]["liquid"].get("initial", 0)),
                "difference": float(summary["by_category"]["liquid"].get("difference", 0)),
                "count": summary["by_category"]["liquid"]["count"],
                "types": summary["by_category"]["liquid"]["types"],
                "description": "Available liquidity"
            },
            "investments": {
                "total": float(summary["by_category"]["investments"]["total"]),
                "initial": float(summary["by_category"]["investments"].get("initial", 0)),
                "difference": float(summary["by_category"]["investments"].get("difference", 0)),
                "count": summary["by_category"]["investments"]["count"],
                "types": summary["by_category"]["investments"]["types"],
                "description": "Invested capital"
            },
            "loans": {
                "total": float(summary["by_category"]["loans"]["total"]),
                "count": summary["by_category"]["loans"]["count"],
                "types": summary["by_category"]["loans"]["types"],
                "description": "Credits to third parties (money owed to you)"
            },
            "debts": {
                "total": float(summary["by_category"]["debts"]["total"]),
                "count": summary["by_category"]["debts"]["count"],
                "types": summary["by_category"]["debts"]["types"],
                "description": "Debts (money you owe)"
            },
            "other": {
                "total": float(summary["by_category"]["other"]["total"]),
                "count": summary["by_category"]["other"]["count"],
                "types": summary["by_category"]["other"]["types"],
                "description": "Other accounts"
            }
        }
    }


@router.get("/types")
async def get_account_types():
    """
    Get all available account types.
    
    Useful for populating dropdowns in frontend.
    """
    return [
        {"value": "checking", "label": "Checking Account", "category": "liquid"},
        {"value": "savings", "label": "Savings Account", "category": "liquid"},
        {"value": "cash", "label": "Cash", "category": "liquid"},
        {"value": "credit_card", "label": "Credit Card", "category": "debt"},
        {"value": "investment", "label": "Investments", "category": "investment"},
        {"value": "loan", "label": "Loans to Third Parties", "category": "loan"},
        {"value": "other", "label": "Other", "category": "other"},
    ]


@router.get("/verify-balances")
async def verify_account_balances(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Verify balance integrity for all accounts.
    
    Compares `current_balance` with calculated balance from transactions/transfers.
    Returns list of accounts with discrepancies (if any).
    """
    discrepancies = account_crud.verify_all_balances(db, user_id=str(current_user.id))
    
    return {
        "status": "ok" if len(discrepancies) == 0 else "discrepancies_found",
        "discrepancies_count": len(discrepancies),
        "discrepancies": discrepancies
    }


@router.post("/{account_id}/fix-balance", response_model=AccountResponse)
async def fix_account_balance(
    account_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Recalculate and fix account's current_balance from transactions/transfers.
    
    Use this to correct any balance discrepancies.
    """
    account = account_crud.fix_account_balance(
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


@router.get("/{account_id}", response_model=AccountResponse)
async def get_account(
    account_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get details of a single account.
    
    **Response includes:**
    - `initial_balance`: Balance set at creation
    - `current_balance`: Current balance after all transactions/transfers
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
    Update an existing account.
    
    **Updatable fields:** name, type, currency, color, icon, notes, is_active
    
    ⚠️ **Cannot update:** initial_balance, current_balance
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
    Delete an account.
    
    ⚠️ **Warning**: This also deletes all transactions and transfers associated with the account.
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
    Deactivate an account (soft delete).
    
    The account will be hidden from lists but can be reactivated with PUT (is_active=true).
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
