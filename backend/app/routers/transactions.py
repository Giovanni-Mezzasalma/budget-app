"""
Transactions Router
User transaction management (income and expenditure)
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
    List all user transactions with optional filters.

    **Available filters:**
    - **account_id**: Filter by specific account
    - **category_id**: Filter by specific category
    - **type**: Filter by type (income, expense_necessity, expense_extra)
    - **start_date / end_date**: Filter by period
    - **min_amount / max_amount**: Filter by amount range
    - **search**: Search for text in descriptions and notes

    **Sort:** By date descending (newest first)
    """
    # Validate type if provided
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
    Returns a summary of transactions.

    **Response includes:**
    - Total income
    - Total necessary expenses (expense_necessity)
    - Total extra expenses (expense_extra)
    - Total expenses (necessity + extra)
    - Net balance (income - expenses)
    - Number of transactions

    **Example response:**
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
    Returns the summary for a specific month.

    - **year**: Year (e.g., 2025)
    - **month**: Month (1-12)
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
    Create a new transaction.

    **Required fields:**
    - **account_id**: Account ID
    - **category_id**: Category ID
    - **amount**: Amount (always positive)
    - **date**: Transaction date

    **Optional fields:**
    - **description**: Short description
    - **notes**: Additional notes
    - **tags**: List of tags for filtering

    ⚠️ **Note:** The transaction type (income/expense_necessity/expense_extra)
    is automatically determined by the selected category.

    ✅ The account balance is updated automatically.

    **Example:**
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
    # Verify that the account exists and belongs to the user
    account = account_crud.get_account(db, transaction.account_id, str(current_user.id))
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    # Verify that the category exists and belongs to the user
    category = category_crud.get_category(db, transaction.category_id, str(current_user.id))
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    # Make sure the category is active
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
    Retrieves the details of a single transaction.

    Includes information about the associated account and category.
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
    
    # Build response with details
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
    Update an existing transaction.

    You can only update the fields you want to change.

    ⚠️ **Note:** If you change the category, the transaction type will be automatically updated
    to match the new category type.

    ✅ Account balances are automatically recalculated.
    """
    # Verify that the transaction exists
    existing = transaction_crud.get_transaction(db, transaction_id, str(current_user.id))
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    
    # If you are changing accounts, please check that it exists
    if transaction_update.account_id is not None:
        account = account_crud.get_account(db, transaction_update.account_id, str(current_user.id))
        if not account:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Account not found"
            )
    
    # If you are changing categories, check that they exist and are active
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
    Delete a transaction.

    ✅ Your account balance is automatically restored.
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
    Returns transaction totals grouped by category.

    Useful for pie charts or category analysis.

    **Answer:** Dict with category_id as the key and total as the value.
    """
    totals = transaction_crud.get_transactions_by_category(
        db,
        user_id=str(current_user.id),
        start_date=start_date,
        end_date=end_date
    )
    
    # Enrich with category names
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