"""
Budget-related Pydantic schemas for request/response validation.

Budgets track monthly spending limits for expense categories.
"""

from datetime import datetime, date
from typing import Optional
from uuid import UUID
from decimal import Decimal

from pydantic import BaseModel, Field, field_validator


class BudgetBase(BaseModel):
    """Base budget schema with common fields."""
    category_id: UUID = Field(..., description="Category ID this budget applies to")
    amount: Decimal = Field(..., gt=0, description="Budget amount (must be positive)")
    period: str = Field(default="monthly", description="Budget period")
    start_date: date = Field(..., description="Date when budget becomes active")

    @field_validator('period')
    @classmethod
    def validate_period(cls, v: str) -> str:
        """Validate budget period (only monthly for MVP)."""
        if v.lower() != "monthly":
            raise ValueError("Only 'monthly' period is supported in MVP")
        return v.lower()

    @field_validator('amount')
    @classmethod
    def validate_amount(cls, v: Decimal) -> Decimal:
        """Validate amount is positive and reasonable."""
        if v <= 0:
            raise ValueError("Budget amount must be positive")
        if v > Decimal('999999.99'):
            raise ValueError("Budget amount too large")
        return v


class BudgetCreate(BudgetBase):
    """Schema for creating a new budget."""
    pass


class BudgetUpdate(BaseModel):
    """Schema for updating an existing budget."""
    amount: Optional[Decimal] = Field(None, gt=0, description="New budget amount")
    start_date: Optional[date] = Field(None, description="New start date")
    is_active: Optional[bool] = Field(None, description="Active status")

    @field_validator('amount')
    @classmethod
    def validate_amount(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        """Validate amount if provided."""
        if v is not None:
            if v <= 0:
                raise ValueError("Budget amount must be positive")
            if v > Decimal('999999.99'):
                raise ValueError("Budget amount too large")
        return v


class BudgetResponse(BaseModel):
    """Schema for budget response."""
    id: UUID = Field(..., description="Budget unique identifier")
    user_id: UUID = Field(..., description="Owner user ID")
    category_id: Optional[UUID] = Field(None, description="Category ID (null if orphaned)")
    amount: Decimal = Field(..., description="Budget amount")
    period: str = Field(..., description="Budget period")
    start_date: date = Field(..., description="Start date")
    is_active: bool = Field(..., description="Active status")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")

    class Config:
        from_attributes = True


class CategoryInfo(BaseModel):
    """Minimal category info for budget responses."""
    id: UUID
    name: str
    type: str
    color: Optional[str] = None


class BudgetWithStatus(BudgetResponse):
    """Budget response with spending status for current period."""
    category: Optional[CategoryInfo] = Field(None, description="Category details (null if orphaned)")
    category_name: str = Field(..., description="Category name or 'Categoria Eliminata'")
    spent: Decimal = Field(..., description="Amount spent in current period")
    remaining: Decimal = Field(..., description="Amount remaining")
    percentage: Decimal = Field(..., description="Percentage used (0-100+)")
    status: str = Field(..., description="Status: 'ok', 'warning', 'danger', 'exceeded', 'orphan'")
    indicator: str = Field(..., description="Visual indicator emoji")
    color: str = Field(..., description="Color for UI display")


class BudgetSummaryResponse(BaseModel):
    """Summary response with all budgets and totals."""
    month: str = Field(..., description="Current month in YYYY-MM format")
    budgets: list[BudgetWithStatus] = Field(..., description="List of budgets with status")
    totals: dict = Field(..., description="Aggregate totals")

    class Config:
        json_schema_extra = {
            "example": {
                "month": "2025-01",
                "budgets": [
                    {
                        "id": "uuid",
                        "category": {"id": "uuid", "name": "Ristoranti", "type": "expense_extra"},
                        "category_name": "Ristoranti",
                        "amount": 200.00,
                        "spent": 150.50,
                        "remaining": 49.50,
                        "percentage": 75.25,
                        "status": "warning",
                        "indicator": "🟡",
                        "color": "yellow"
                    }
                ],
                "totals": {
                    "total_budget": 500.00,
                    "total_spent": 350.00,
                    "total_remaining": 150.00,
                    "overall_percentage": 70.00
                }
            }
        }
