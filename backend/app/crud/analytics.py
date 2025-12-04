"""
Analytics CRUD Operations
Calculations and aggregations for statistics and reports.

Uses current_balance for all balance-related calculations.
"""
from sqlalchemy.orm import Session
from typing import Optional, Dict, List, Any
from datetime import date, timedelta
from decimal import Decimal

from app.models.transaction import Transaction
from app.models.transfer import Transfer
from app.models.account import Account
from app.models.category import Category


def calculate_summary(
    db: Session,
    user_id: str,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    account_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Calculate complete financial summary.
    
    Args:
        db: Database session
        user_id: User ID
        start_date: Period start (default: current month start)
        end_date: Period end (default: today)
        account_id: Filter by specific account
    
    Returns:
        Dict with totals, metrics, and period info
    """
    # Default: current month
    if not start_date:
        today = date.today()
        start_date = date(today.year, today.month, 1)
    if not end_date:
        end_date = date.today()
    
    # Query transactions in period
    query = db.query(Transaction).filter(
        Transaction.user_id == user_id,
        Transaction.date >= start_date,
        Transaction.date <= end_date
    )
    
    if account_id:
        query = query.filter(Transaction.account_id == account_id)
    
    transactions = query.all()
    
    # Calculate totals by type
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
    
    # Calculate total current_balance of accounts
    accounts = db.query(Account).filter(
        Account.user_id == user_id,
        Account.is_active == True
    ).all()
    total_balance = sum(a.current_balance for a in accounts)  # Use current_balance
    total_initial = sum(a.initial_balance for a in accounts)
    
    # Metrics
    days_in_period = (end_date - start_date).days + 1
    avg_daily_expense = total_expenses / days_in_period if days_in_period > 0 else Decimal("0.00")
    savings_rate = ((total_income - total_expenses) / total_income * 100) if total_income > 0 else Decimal("0.00")
    
    return {
        "period": {
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "days": days_in_period
        },
        "totals": {
            "income": float(total_income),
            "expense_necessity": float(total_expense_necessity),
            "expense_extra": float(total_expense_extra),
            "expenses": float(total_expenses),
            "net": float(net)
        },
        "accounts": {
            "total_balance": float(total_balance),  # Current balance
            "total_initial": float(total_initial),  # Initial balance for reference
            "balance_change": float(total_balance - total_initial),
            "count": len(accounts)
        },
        "metrics": {
            "transaction_count": len(transactions),
            "avg_daily_expense": float(round(avg_daily_expense, 2)),
            "savings_rate": float(round(savings_rate, 2))
        }
    }


def calculate_monthly_trend(
    db: Session,
    user_id: str,
    months: int = 12,
    account_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Calculate monthly trend of income and expenses.
    
    Args:
        db: Database session
        user_id: User ID
        months: Number of months to analyze (default: 12)
        account_id: Filter by specific account
    
    Returns:
        Dict with monthly data and period info
    """
    today = date.today()
    start_date = date(today.year, today.month, 1) - timedelta(days=30 * (months - 1))
    start_date = date(start_date.year, start_date.month, 1)
    
    # Query transactions
    query = db.query(Transaction).filter(
        Transaction.user_id == user_id,
        Transaction.date >= start_date
    )
    
    if account_id:
        query = query.filter(Transaction.account_id == account_id)
    
    transactions = query.all()
    
    # Group by month
    monthly_data = {}
    
    for t in transactions:
        month_key = t.date.strftime('%Y-%m')
        
        if month_key not in monthly_data:
            monthly_data[month_key] = {
                "month": month_key,
                "income": Decimal("0.00"),
                "expense_necessity": Decimal("0.00"),
                "expense_extra": Decimal("0.00"),
                "expenses": Decimal("0.00"),
                "net": Decimal("0.00"),
                "transaction_count": 0
            }
        
        if t.type == "income":
            monthly_data[month_key]["income"] += t.amount
        elif t.type == "expense_necessity":
            monthly_data[month_key]["expense_necessity"] += t.amount
            monthly_data[month_key]["expenses"] += t.amount
        elif t.type == "expense_extra":
            monthly_data[month_key]["expense_extra"] += t.amount
            monthly_data[month_key]["expenses"] += t.amount
        
        monthly_data[month_key]["transaction_count"] += 1
    
    # Calculate net and convert to list
    result = []
    for month_key in sorted(monthly_data.keys()):
        data = monthly_data[month_key]
        data["net"] = data["income"] - data["expenses"]
        result.append({
            "month": data["month"],
            "income": float(data["income"]),
            "expense_necessity": float(data["expense_necessity"]),
            "expense_extra": float(data["expense_extra"]),
            "expenses": float(data["expenses"]),
            "net": float(data["net"]),
            "transaction_count": data["transaction_count"]
        })
    
    return {
        "period": {
            "months_analyzed": months,
            "start_month": start_date.strftime('%Y-%m'),
            "end_month": today.strftime('%Y-%m')
        },
        "data": result
    }


def calculate_totals_by_category(
    db: Session,
    user_id: str,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    transaction_type: Optional[str] = None
) -> Dict[str, Any]:
    """
    Calculate totals grouped by category.
    
    Args:
        db: Database session
        user_id: User ID
        start_date: Period start
        end_date: Period end
        transaction_type: Filter by type (income, expense_necessity, expense_extra)
    
    Returns:
        Dict with totals by category and grand total
    """
    # Default: current month
    if not start_date:
        today = date.today()
        start_date = date(today.year, today.month, 1)
    if not end_date:
        end_date = date.today()
    
    # Query transactions
    query = db.query(Transaction).filter(
        Transaction.user_id == user_id,
        Transaction.date >= start_date,
        Transaction.date <= end_date
    )
    
    if transaction_type:
        query = query.filter(Transaction.type == transaction_type)
    
    transactions = query.all()
    
    # Group by category
    category_totals = {}
    
    for t in transactions:
        cat_id = str(t.category_id)
        if cat_id not in category_totals:
            category_totals[cat_id] = {
                "category_id": cat_id,
                "total": Decimal("0.00"),
                "count": 0
            }
        category_totals[cat_id]["total"] += t.amount
        category_totals[cat_id]["count"] += 1
    
    # Enrich with category info
    result = []
    for cat_id, data in category_totals.items():
        category = db.query(Category).filter(
            Category.id == cat_id,
            Category.user_id == user_id
        ).first()
        
        if category:
            result.append({
                "category_id": cat_id,
                "category_name": category.name,
                "category_full_name": category.full_name,
                "category_type": category.type,
                "category_color": category.color,
                "category_icon": category.icon,
                "total": float(data["total"]),
                "transaction_count": data["count"],
                "percentage": 0.0
            })
    
    # Calculate percentages
    grand_total = sum(item["total"] for item in result)
    for item in result:
        item["percentage"] = round((item["total"] / grand_total * 100), 2) if grand_total > 0 else 0.0
    
    # Sort by total descending
    result.sort(key=lambda x: x["total"], reverse=True)
    
    return {
        "period": {
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat()
        },
        "grand_total": float(grand_total),
        "categories": result
    }


def calculate_totals_by_account(
    db: Session,
    user_id: str,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
) -> Dict[str, Any]:
    """
    Calculate totals grouped by account.
    
    Args:
        db: Database session
        user_id: User ID
        start_date: Period start
        end_date: Period end
    
    Returns:
        Dict with totals by account
    """
    # Default: current month
    if not start_date:
        today = date.today()
        start_date = date(today.year, today.month, 1)
    if not end_date:
        end_date = date.today()
    
    # Get all active accounts
    accounts = db.query(Account).filter(
        Account.user_id == user_id,
        Account.is_active == True
    ).all()
    
    result = []
    
    for account in accounts:
        transactions = db.query(Transaction).filter(
            Transaction.user_id == user_id,
            Transaction.account_id == account.id,
            Transaction.date >= start_date,
            Transaction.date <= end_date
        ).all()
        
        income = sum(t.amount for t in transactions if t.type == "income")
        expenses = sum(t.amount for t in transactions if t.type in ["expense_necessity", "expense_extra"])
        
        result.append({
            "account_id": str(account.id),
            "account_name": account.name,
            "account_type": account.type,
            "account_color": account.color,
            "currency": account.currency,
            "initial_balance": float(account.initial_balance),
            "current_balance": float(account.current_balance),  # Use current_balance
            "balance_change": float(account.current_balance - account.initial_balance),
            "period_income": float(income),
            "period_expenses": float(expenses),
            "period_net": float(income - expenses),
            "transaction_count": len(transactions)
        })
    
    result.sort(key=lambda x: x["current_balance"], reverse=True)
    
    return {
        "period": {
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat()
        },
        "accounts": result,
        "totals": {
            "total_initial_balance": sum(a["initial_balance"] for a in result),
            "total_current_balance": sum(a["current_balance"] for a in result),
            "total_balance_change": sum(a["balance_change"] for a in result),
            "total_income": sum(a["period_income"] for a in result),
            "total_expenses": sum(a["period_expenses"] for a in result)
        }
    }


def calculate_daily_breakdown(
    db: Session,
    user_id: str,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    account_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Calculate daily breakdown of transactions.
    
    Args:
        db: Database session
        user_id: User ID
        start_date: Start date (default: 30 days ago)
        end_date: End date (default: today)
        account_id: Filter by account
    
    Returns:
        Dict with daily data
    """
    if not end_date:
        end_date = date.today()
    if not start_date:
        start_date = end_date - timedelta(days=30)
    
    # Query transactions
    query = db.query(Transaction).filter(
        Transaction.user_id == user_id,
        Transaction.date >= start_date,
        Transaction.date <= end_date
    )
    
    if account_id:
        query = query.filter(Transaction.account_id == account_id)
    
    transactions = query.all()
    
    # Initialize all days in range
    daily_data = {}
    current = start_date
    while current <= end_date:
        day_key = current.isoformat()
        daily_data[day_key] = {
            "date": day_key,
            "income": Decimal("0.00"),
            "expense_necessity": Decimal("0.00"),
            "expense_extra": Decimal("0.00"),
            "expenses": Decimal("0.00"),
            "net": Decimal("0.00"),
            "transaction_count": 0
        }
        current += timedelta(days=1)
    
    # Populate with transactions
    for t in transactions:
        day_key = t.date.isoformat()
        if day_key in daily_data:
            if t.type == "income":
                daily_data[day_key]["income"] += t.amount
            elif t.type == "expense_necessity":
                daily_data[day_key]["expense_necessity"] += t.amount
                daily_data[day_key]["expenses"] += t.amount
            elif t.type == "expense_extra":
                daily_data[day_key]["expense_extra"] += t.amount
                daily_data[day_key]["expenses"] += t.amount
            
            daily_data[day_key]["transaction_count"] += 1
    
    # Convert to list
    result = []
    for day_key in sorted(daily_data.keys()):
        data = daily_data[day_key]
        data["net"] = data["income"] - data["expenses"]
        result.append({
            "date": data["date"],
            "income": float(data["income"]),
            "expense_necessity": float(data["expense_necessity"]),
            "expense_extra": float(data["expense_extra"]),
            "expenses": float(data["expenses"]),
            "net": float(data["net"]),
            "transaction_count": data["transaction_count"]
        })
    
    return {
        "period": {
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "days": len(result)
        },
        "data": result
    }


def calculate_year_comparison(
    db: Session,
    user_id: str,
    year1: int,
    year2: int
) -> Dict[str, Any]:
    """
    Compare two years side-by-side.
    
    Args:
        db: Database session
        user_id: User ID
        year1: First year
        year2: Second year
    
    Returns:
        Dict with monthly comparison and yearly totals
    """
    result = {
        "year1": year1,
        "year2": year2,
        "comparison": []
    }
    
    for month in range(1, 13):
        month_data = {
            "month": month,
            "month_name": date(2000, month, 1).strftime('%B')
        }
        
        for year in [year1, year2]:
            month_start = date(year, month, 1)
            if month == 12:
                month_end = date(year + 1, 1, 1) - timedelta(days=1)
            else:
                month_end = date(year, month + 1, 1) - timedelta(days=1)
            
            transactions = db.query(Transaction).filter(
                Transaction.user_id == user_id,
                Transaction.date >= month_start,
                Transaction.date <= month_end
            ).all()
            
            income = sum(t.amount for t in transactions if t.type == "income")
            expenses = sum(t.amount for t in transactions if t.type in ["expense_necessity", "expense_extra"])
            
            year_key = f"year{1 if year == year1 else 2}"
            month_data[f"{year_key}_income"] = float(income)
            month_data[f"{year_key}_expenses"] = float(expenses)
            month_data[f"{year_key}_net"] = float(income - expenses)
        
        result["comparison"].append(month_data)
    
    # Yearly totals
    for year_key, year in [("year1", year1), ("year2", year2)]:
        result[f"{year_key}_totals"] = {
            "income": sum(m[f"{year_key}_income"] for m in result["comparison"]),
            "expenses": sum(m[f"{year_key}_expenses"] for m in result["comparison"]),
            "net": sum(m[f"{year_key}_net"] for m in result["comparison"])
        }
    
    return result
