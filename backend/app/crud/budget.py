"""
Budget CRUD Operations
Database operations for Budget model with spending calculations.
"""
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional, Union
from uuid import UUID
from datetime import date, datetime
from decimal import Decimal
from calendar import monthrange

from app.models.budget import Budget
from app.models.transaction import Transaction
from app.models.category import Category
from app.schemas.budget import BudgetCreate, BudgetUpdate


def _to_uuid(value: Union[str, UUID, None]) -> Optional[UUID]:
    """Convert string to UUID if necessary."""
    if value is None:
        return None
    if isinstance(value, str):
        return UUID(value)
    return value


def get_budgets(
    db: Session,
    user_id: Union[str, UUID],
    skip: int = 0,
    limit: int = 100,
    is_active: Optional[bool] = None,
    category_id: Optional[Union[str, UUID]] = None
) -> List[Budget]:
    """
    List user's budgets with optional filters.

    Args:
        db: Database session
        user_id: User ID
        skip: Pagination offset
        limit: Maximum results
        is_active: Filter by active status
        category_id: Filter by category
    """
    user_id = _to_uuid(user_id)
    query = db.query(Budget).filter(Budget.user_id == user_id)

    if is_active is not None:
        query = query.filter(Budget.is_active == is_active)

    if category_id is not None:
        category_id = _to_uuid(category_id)
        query = query.filter(Budget.category_id == category_id)

    return query.order_by(Budget.created_at.desc()).offset(skip).limit(limit).all()


def get_budget(
    db: Session,
    budget_id: Union[str, UUID],
    user_id: Union[str, UUID]
) -> Optional[Budget]:
    """Get single budget by ID, verifying ownership."""
    budget_id = _to_uuid(budget_id)
    user_id = _to_uuid(user_id)

    return db.query(Budget).filter(
        Budget.id == budget_id,
        Budget.user_id == user_id
    ).first()


def create_budget(
    db: Session,
    budget: BudgetCreate,
    user_id: Union[str, UUID]
) -> Budget:
    """
    Create a new budget.

    Validates:
    - Category belongs to user
    - Category is expense type (not income)
    - No other active budget exists for this category
    """
    user_id = _to_uuid(user_id)

    # Verify category exists and belongs to user
    category = db.query(Category).filter(
        Category.id == budget.category_id,
        Category.user_id == user_id
    ).first()

    if not category:
        raise ValueError("Category not found or does not belong to user")

    # Verify category is expense type
    if category.type not in ['expense_necessity', 'expense_extra']:
        raise ValueError("Budgets can only be created for expense categories")

    # Check for existing active budget (constraint will also catch this)
    existing = db.query(Budget).filter(
        Budget.user_id == user_id,
        Budget.category_id == budget.category_id,
        Budget.is_active == True
    ).first()

    if existing:
        raise ValueError("An active budget already exists for this category")

    db_budget = Budget(
        **budget.model_dump(),
        user_id=user_id
    )
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)

    return db_budget


def update_budget(
    db: Session,
    budget_id: Union[str, UUID],
    budget_update: BudgetUpdate,
    user_id: Union[str, UUID]
) -> Optional[Budget]:
    """Update existing budget."""
    db_budget = get_budget(db, budget_id, user_id)

    if not db_budget:
        return None

    update_data = budget_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_budget, field, value)

    db.commit()
    db.refresh(db_budget)

    return db_budget


def delete_budget(
    db: Session,
    budget_id: Union[str, UUID],
    user_id: Union[str, UUID]
) -> bool:
    """Delete a budget."""
    db_budget = get_budget(db, budget_id, user_id)

    if not db_budget:
        return False

    db.delete(db_budget)
    db.commit()

    return True


def calculate_spent_for_month(
    db: Session,
    user_id: Union[str, UUID],
    category_id: Union[str, UUID],
    year: int,
    month: int
) -> Decimal:
    """
    Calculate total spent for a category in a specific month.

    Returns absolute value (positive number).
    """
    user_id = _to_uuid(user_id)
    category_id = _to_uuid(category_id)

    # Get first and last day of month
    start_date = date(year, month, 1)
    last_day = monthrange(year, month)[1]
    end_date = date(year, month, last_day)

    # Query transactions for this category in this month
    # Only expenses: filtro per tipo (le transazioni sono salvate con amount positivo)
    result = db.query(func.sum(Transaction.amount)).filter(
        Transaction.user_id == user_id,
        Transaction.category_id == category_id,
        Transaction.date >= start_date,
        Transaction.date <= end_date,
        Transaction.type.in_(["expense_necessity", "expense_extra"])
    ).scalar()

    if result is None:
        return Decimal('0')

    # Return absolute value (positive)
    return abs(Decimal(str(result)))


def get_budget_status(spent: Decimal, budget_amount: Decimal) -> dict:
    """
    Calculate budget status based on spending percentage.

    Returns:
        dict with status, indicator emoji, and color
    """
    if budget_amount == 0:
        return {
            "status": "invalid",
            "indicator": "❌",
            "color": "gray"
        }

    percentage = (spent / budget_amount) * 100

    if percentage < 70:
        return {"status": "ok", "indicator": "🟢", "color": "green"}
    elif percentage < 90:
        return {"status": "warning", "indicator": "🟡", "color": "yellow"}
    elif percentage < 100:
        return {"status": "danger", "indicator": "🔴", "color": "red"}
    else:
        return {"status": "exceeded", "indicator": "🚨", "color": "darkred"}


def get_budget_with_spending(
    db: Session,
    budget: Budget,
    year: int,
    month: int
) -> dict:
    """
    Get budget with current spending data.

    Returns enriched budget dict with spending info and status.
    """
    # Calculate spent amount
    spent = Decimal('0')
    if budget.category_id:
        spent = calculate_spent_for_month(
            db,
            budget.user_id,
            budget.category_id,
            year,
            month
        )

    # Calculate remaining and percentage
    remaining = budget.amount - spent
    percentage = (spent / budget.amount * 100) if budget.amount > 0 else Decimal('0')

    # Get status
    if budget.category_id is None:
        # Orphaned budget
        status_info = {"status": "orphan", "indicator": "⚠️", "color": "gray"}
    else:
        status_info = get_budget_status(spent, budget.amount)

    # Get category info
    category_info = None
    category_name = "Categoria Eliminata"

    if budget.category:
        category_info = {
            "id": str(budget.category.id),
            "name": budget.category.name,
            "type": budget.category.type,
            "color": budget.category.color
        }
        category_name = budget.category.name

    return {
        "id": str(budget.id),
        "user_id": str(budget.user_id),
        "category_id": str(budget.category_id) if budget.category_id else None,
        "amount": budget.amount,
        "period": budget.period,
        "start_date": budget.start_date,
        "is_active": budget.is_active,
        "created_at": budget.created_at,
        "updated_at": budget.updated_at,
        "category": category_info,
        "category_name": category_name,
        "spent": spent,
        "remaining": remaining,
        "percentage": percentage,
        **status_info
    }


def get_budgets_summary(
    db: Session,
    user_id: Union[str, UUID],
    year: Optional[int] = None,
    month: Optional[int] = None
) -> dict:
    """
    Get summary of all active budgets with spending data.

    Args:
        db: Database session
        user_id: User ID
        year: Target year (default: current year)
        month: Target month (default: current month)

    Returns:
        dict with budgets list and aggregate totals
    """
    user_id = _to_uuid(user_id)

    # Default to current month
    now = datetime.now()
    if year is None:
        year = now.year
    if month is None:
        month = now.month

    # Get all active budgets
    budgets = get_budgets(db, user_id, is_active=True, limit=500)

    # Enrich each budget with spending data
    enriched_budgets = []
    total_budget = Decimal('0')
    total_spent = Decimal('0')

    for budget in budgets:
        budget_data = get_budget_with_spending(db, budget, year, month)
        enriched_budgets.append(budget_data)

        total_budget += budget.amount
        total_spent += budget_data['spent']

    total_remaining = total_budget - total_spent
    overall_percentage = (
        (total_spent / total_budget * 100)
        if total_budget > 0
        else Decimal('0')
    )

    return {
        "month": f"{year}-{month:02d}",
        "budgets": enriched_budgets,
        "totals": {
            "total_budget": total_budget,
            "total_spent": total_spent,
            "total_remaining": total_remaining,
            "overall_percentage": round(overall_percentage, 2)
        }
    }
