"""
Transaction-related Pydantic schemas for request/response validation.

Transaction types (derived from the category):
- income: Income
- expense_necessity: Necessity Expenses
- expense_extra: Extra Expenses
"""

from datetime import datetime, date as date_type
from decimal import Decimal
from typing import Optional, List
from pydantic import BaseModel, Field, field_validator
from uuid import UUID

# Valid types for transactions (same as categories)
VALID_TRANSACTION_TYPES = ["income", "expense_necessity", "expense_extra"]


class TransactionBase(BaseModel):
    """Base transaction schema with common fields."""
    account_id: UUID = Field(..., description="Account ID for this transaction")
    category_id: UUID = Field(..., description="Category ID for this transaction")
    amount: Decimal = Field(..., gt=0, description="Transaction amount (always positive)")
    date: date_type = Field(..., description="Transaction date")
    description: Optional[str] = Field(None, max_length=500, description="Transaction description")
    notes: Optional[str] = Field(None, max_length=1000, description="Additional notes")
    tags: Optional[List[str]] = Field(default=None, description="Transaction tags for filtering")
    
    @field_validator('amount')
    @classmethod
    def validate_amount(cls, v: Decimal) -> Decimal:
        """Validate amount has max 2 decimal places and is positive."""
        if v <= 0:
            raise ValueError('Amount must be positive')
        return round(v, 2)
    
    @field_validator('description')
    @classmethod
    def validate_description(cls, v: Optional[str]) -> Optional[str]:
        """Clean description if provided."""
        if v is None:
            return v
        return v.strip()
    
    @field_validator('tags')
    @classmethod
    def validate_tags(cls, v: Optional[List[str]]) -> Optional[List[str]]:
        """Validate and clean tags."""
        if v is None:
            return v
        cleaned_tags = list(set(tag.strip().lower() for tag in v if tag.strip()))
        return cleaned_tags if cleaned_tags else None


class TransactionCreate(TransactionBase):
    """Schema for creating a new transaction."""
    pass


class TransactionUpdate(BaseModel):
    """Schema for updating an existing transaction."""
    account_id: Optional[UUID] = Field(None, description="Account ID")
    category_id: Optional[UUID] = Field(None, description="Category ID")
    amount: Optional[Decimal] = Field(None, gt=0, description="Transaction amount")
    date: Optional[date_type] = Field(None, description="Transaction date")
    description: Optional[str] = Field(None, max_length=500, description="Transaction description")
    notes: Optional[str] = Field(None, max_length=1000, description="Additional notes")
    tags: Optional[List[str]] = Field(None, description="Transaction tags")
    
    @field_validator('amount')
    @classmethod
    def validate_amount(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        """Validate amount if provided."""
        if v is None:
            return v
        if v <= 0:
            raise ValueError('Amount must be positive')
        return round(v, 2)
    
    @field_validator('description')
    @classmethod
    def validate_description(cls, v: Optional[str]) -> Optional[str]:
        """Clean description if provided."""
        if v is None:
            return v
        return v.strip()
    
    @field_validator('tags')
    @classmethod
    def validate_tags(cls, v: Optional[List[str]]) -> Optional[List[str]]:
        """Validate and clean tags if provided."""
        if v is None:
            return v
        cleaned_tags = list(set(tag.strip().lower() for tag in v if tag.strip()))
        return cleaned_tags if cleaned_tags else None


class TransactionResponse(BaseModel):
    """Schema for transaction response."""
    id: UUID = Field(..., description="Transaction unique identifier")
    user_id: UUID = Field(..., description="Owner user ID")
    account_id: UUID = Field(..., description="Account ID")
    category_id: UUID = Field(..., description="Category ID")
    amount: Decimal = Field(..., description="Transaction amount")
    type: str = Field(..., description="Transaction type (from category)")
    date: date_type = Field(..., description="Transaction date")
    description: Optional[str] = Field(None, description="Transaction description")
    notes: Optional[str] = Field(None, description="Additional notes")
    tags: Optional[List[str]] = Field(None, description="Transaction tags")
    is_recurring: bool = Field(default=False, description="Is recurring transaction")
    recurring_frequency: Optional[str] = Field(None, description="Recurring frequency")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    
    class Config:
        from_attributes = True


class TransactionWithDetails(TransactionResponse):
    """Schema for transaction response with related details."""
    account_name: Optional[str] = Field(None, description="Account name")
    account_color: Optional[str] = Field(None, description="Account color")
    category_name: Optional[str] = Field(None, description="Category name")
    category_full_name: Optional[str] = Field(None, description="Full category name (with parent)")
    category_color: Optional[str] = Field(None, description="Category color")
    category_icon: Optional[str] = Field(None, description="Category icon")


class TransactionSummary(BaseModel):
    """Schema for transaction summary/statistics."""
    total_income: Decimal = Field(default=Decimal("0.00"), description="Total income")
    total_expense_necessity: Decimal = Field(default=Decimal("0.00"), description="Total necessity expenses")
    total_expense_extra: Decimal = Field(default=Decimal("0.00"), description="Total extra expenses")
    total_expenses: Decimal = Field(default=Decimal("0.00"), description="Total all expenses")
    net: Decimal = Field(default=Decimal("0.00"), description="Net (income - expenses)")
    transaction_count: int = Field(default=0, description="Number of transactions")


class TransactionFilters(BaseModel):
    """Schema for transaction filter parameters."""
    account_id: Optional[UUID] = None
    category_id: Optional[UUID] = None
    type: Optional[str] = None
    start_date: Optional[date_type] = None
    end_date: Optional[date_type] = None
    min_amount: Optional[Decimal] = None
    max_amount: Optional[Decimal] = None
    tags: Optional[List[str]] = None
    search: Optional[str] = None