"""
Analytics Router
Statistics and data dashboard for Budget App
"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.crud import analytics as analytics_crud

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/summary")
async def get_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(None, description="Data inizio periodo (YYYY-MM-DD)"),
    end_date: Optional[date] = Query(None, description="Data fine periodo (YYYY-MM-DD)"),
    account_id: Optional[str] = Query(None, description="Filtra per account specifico")
):
    """
    Returns the complete financial summary.

    **Calculated metrics:**
    - Total income
    - Total expense necessity (expense_necessity)
    - Total extra expenses (expense_extra)
    - Total combined expenses
    - Net balance (income - expenses)
    - Total account balance
    - Number of transactions in the period

    **Optional filters:**
    - `start_date`: Start date (default: start of the current month)
    - `end_date`: End date (default: today)
    - `account_id`: Filter by individual account
    """
    return analytics_crud.calculate_summary(
        db=db,
        user_id=str(current_user.id),
        start_date=start_date,
        end_date=end_date,
        account_id=account_id
    )


@router.get("/monthly-trend")
async def get_monthly_trend(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    months: int = Query(12, ge=1, le=24, description="Numero di mesi da analizzare"),
    account_id: Optional[str] = Query(None, description="Filtra per account specifico")
):
    """
    Returns the monthly trend of income and expenses.

    Data returned for each month:
    - Total income
    - Total expense_necessity
    - Total expense_extra
    - Total combined expenses
    - Net balance
    - Number of transactions

    Parameters:
    - `months`: Number of past months to analyze (1-24, default: 12)
    - `account_id`: Filter by individual account
    """
    return analytics_crud.calculate_monthly_trend(
        db=db,
        user_id=str(current_user.id),
        months=months,
        account_id=account_id
    )


@router.get("/by-category")
async def get_totals_by_category(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(None, description="Data inizio periodo"),
    end_date: Optional[date] = Query(None, description="Data fine periodo"),
    transaction_type: Optional[str] = Query(None, description="Filtra per tipo: income, expense_necessity, expense_extra")
):
    """
    Returns totals grouped by category.

    Useful for pie charts and category analysis.

    **Answer:** List sorted by descending total with category details.
    """
    return analytics_crud.calculate_totals_by_category(
        db=db,
        user_id=str(current_user.id),
        start_date=start_date,
        end_date=end_date,
        transaction_type=transaction_type
    )


@router.get("/by-account")
async def get_totals_by_account(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(None, description="Data inizio periodo"),
    end_date: Optional[date] = Query(None, description="Data fine periodo")
):
    """
    Returns totals grouped by account.

    Includes:
    - Current account balance
    - Total income per account
    - Total expenses per account
    - Number of transactions
    """
    return analytics_crud.calculate_totals_by_account(
        db=db,
        user_id=str(current_user.id),
        start_date=start_date,
        end_date=end_date
    )


@router.get("/daily-breakdown")
async def get_daily_breakdown(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(None, description="Data inizio (default: 30 giorni fa)"),
    end_date: Optional[date] = Query(None, description="Data fine (default: oggi)"),
    account_id: Optional[str] = Query(None, description="Filtra per account")
):
    """
    Returns a daily breakdown of transactions.

    Useful for line/area charts with daily granularity.
    """
    return analytics_crud.calculate_daily_breakdown(
        db=db,
        user_id=str(current_user.id),
        start_date=start_date,
        end_date=end_date,
        account_id=account_id
    )


@router.get("/year-comparison")
async def get_year_comparison(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    year1: int = Query(..., description="Primo anno da confrontare"),
    year2: int = Query(..., description="Secondo anno da confrontare")
):
    """
    Compare two years side-by-side.

    Returns monthly totals for both years for easy comparison.
    """
    return analytics_crud.calculate_year_comparison(
        db=db,
        user_id=str(current_user.id),
        year1=year1,
        year2=year2
    )