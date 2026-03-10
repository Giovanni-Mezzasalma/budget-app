"""
Budgets Router
User budget management with monthly spending tracking.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas.budget import (
    BudgetCreate,
    BudgetUpdate,
    BudgetResponse,
    BudgetSummaryResponse
)
from app.crud import budget as budget_crud
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/budgets", tags=["Budgets"])


@router.get("/", response_model=List[BudgetResponse])
async def get_budgets(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=500, description="Maximum results"),
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    category_id: Optional[str] = Query(None, description="Filter by category ID")
):
    """
    List all budgets for the current user.

    - **skip**: Pagination offset (default: 0)
    - **limit**: Maximum results (default: 100, max: 500)
    - **is_active**: Filter active/inactive budgets
    - **category_id**: Filter by specific category
    """
    return budget_crud.get_budgets(
        db,
        user_id=str(current_user.id),
        skip=skip,
        limit=limit,
        is_active=is_active,
        category_id=category_id
    )


@router.get("/summary", response_model=BudgetSummaryResponse)
async def get_budgets_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    year: Optional[int] = Query(None, description="Target year (default: current)"),
    month: Optional[int] = Query(None, ge=1, le=12, description="Target month (default: current)")
):
    """
    Get budget summary with spending data for all active budgets.

    Returns:
    - List of budgets with spent/remaining/percentage/status
    - Aggregate totals across all budgets
    - Status indicators (🟢🟡🔴🚨)

    Default: current month. Use year/month params for historical data.
    """
    return budget_crud.get_budgets_summary(
        db,
        user_id=str(current_user.id),
        year=year,
        month=month
    )


@router.get("/{budget_id}", response_model=BudgetResponse)
async def get_budget(
    budget_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get a specific budget by ID.

    Returns budget details without spending data.
    Use /summary for spending info.
    """
    budget = budget_crud.get_budget(db, budget_id, str(current_user.id))

    if not budget:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Budget not found"
        )

    return budget


@router.post("/", response_model=BudgetResponse, status_code=status.HTTP_201_CREATED)
async def create_budget(
    budget: BudgetCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create a new budget.

    - **category_id**: Must be an expense category (not income)
    - **amount**: Budget amount (must be positive)
    - **period**: "monthly" (only option in MVP)
    - **start_date**: When budget becomes active

    Validation:
    - Category must exist and belong to user
    - Category must be expense type
    - No other active budget for this category
    """
    try:
        return budget_crud.create_budget(
            db,
            budget=budget,
            user_id=str(current_user.id)
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.put("/{budget_id}", response_model=BudgetResponse)
async def update_budget(
    budget_id: str,
    budget_update: BudgetUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Update an existing budget.

    Partial updates allowed - only provide fields you want to change.

    💡 To keep history: set is_active=false, then create a new budget.
    """
    updated = budget_crud.update_budget(
        db,
        budget_id=budget_id,
        budget_update=budget_update,
        user_id=str(current_user.id)
    )

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Budget not found"
        )

    return updated


@router.delete("/{budget_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_budget(
    budget_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Delete a budget permanently.

    💡 Alternative: set is_active=false to keep history.
    """
    success = budget_crud.delete_budget(
        db,
        budget_id=budget_id,
        user_id=str(current_user.id)
    )

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Budget not found"
        )
