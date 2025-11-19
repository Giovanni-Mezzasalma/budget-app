"""
Transaction-related Pydantic schemas for request/response validation.
"""

from datetime import datetime, date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class TransactionBase(BaseModel):
    """Base transaction schema with common fields."""
    account_id: str = Field(..., description="Account ID for this transaction")
    category_id: str = Field(..., description="Category ID for this transaction")
    amount: Decimal = Field(..., gt=0, description="Transaction amount (always positive)")
    type: str = Field(..., description="Transaction type: income or expense")
    date: date = Field(..., description="Transaction date")
    description: Optional[str] = Field(None, max_length=500, description="Transaction description")
    notes: Optional[str] = Field(None, max_length=1000, description="Additional notes")
    is_recurring: bool = Field(default=False, description="Whether this is a recurring transaction")
    recurring_frequency: Optional[str] = Field(None, description="Frequency: daily, weekly, monthly, yearly")
    tags: Optional[list[str]] = Field(default=None, description="Transaction tags for filtering")
    
    @field_validator('type')
    @classmethod
    def validate_transaction_type(cls, v: str) -> str:
        """Validate transaction type."""
        allowed_types = ['income', 'expense']
        if v.lower() not in allowed_types:
            raise ValueError(f'Transaction type must be one of: {", ".join(allowed_types)}')
        return v.lower()
    
    @field_validator('amount')
    @classmethod
    def validate_amount(cls, v: Decimal) -> Decimal:
        """Validate amount has max 2 decimal places and is positive."""
        if v <= 0:
            raise ValueError('Amount must be positive')
        if v.as_tuple().exponent < -2:
            raise ValueError('Amount cannot have more than 2 decimal places')
        return v.quantize(Decimal('0.01'))
    
    @field_validator('recurring_frequency')
    @classmethod
    def validate_recurring_frequency(cls, v: Optional[str], info) -> Optional[str]:
        """Validate recurring frequency if transaction is recurring."""
        # Access is_recurring from the values dictionary
        if info.data.get('is_recurring') and v is None:
            raise ValueError('Recurring frequency is required for recurring transactions')
        
        if v is not None:
            allowed_frequencies = ['daily', 'weekly', 'monthly', 'yearly']
            if v.lower() not in allowed_frequencies:
                raise ValueError(f'Recurring frequency must be one of: {", ".join(allowed_frequencies)}')
            return v.lower()
        return v
    
    @field_validator('description')
    @classmethod
    def validate_description(cls, v: Optional[str]) -> Optional[str]:
        """Clean description if provided."""
        if v is None:
            return v
        return v.strip()
    
    @field_validator('tags')
    @classmethod
    def validate_tags(cls, v: Optional[list[str]]) -> Optional[list[str]]:
        """Validate and clean tags."""
        if v is None:
            return v
        # Remove empty strings and duplicates
        cleaned_tags = list(set(tag.strip().lower() for tag in v if tag.strip()))
        return cleaned_tags if cleaned_tags else None


class TransactionCreate(TransactionBase):
    """Schema for creating a new transaction."""
    pass


class TransactionUpdate(BaseModel):
    """Schema for updating an existing transaction."""
    account_id: Optional[str] = Field(None, description="Account ID")
    category_id: Optional[str] = Field(None, description="Category ID")
    amount: Optional[Decimal] = Field(None, gt=0, description="Transaction amount")
    type: Optional[str] = Field(None, description="Transaction type: income or expense")
    date: Optional[date] = Field(None, description="Transaction date")
    description: Optional[str] = Field(None, max_length=500, description="Transaction description")
    notes: Optional[str] = Field(None, max_length=1000, description="Additional notes")
    is_recurring: Optional[bool] = Field(None, description="Whether this is recurring")
    recurring_frequency: Optional[str] = Field(None, description="Frequency")
    tags: Optional[list[str]] = Field(None, description="Transaction tags")
    
    @field_validator('type')
    @classmethod
    def validate_transaction_type(cls, v: Optional[str]) -> Optional[str]:
        """Validate transaction type if provided."""
        if v is None:
            return v
        allowed_types = ['income', 'expense']
        if v.lower() not in allowed_types:
            raise ValueError(f'Transaction type must be one of: {", ".join(allowed_types)}')
        return v.lower()
    
    @field_validator('amount')
    @classmethod
    def validate_amount(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        """Validate amount if provided."""
        if v is None:
            return v
        if v <= 0:
            raise ValueError('Amount must be positive')
        if v.as_tuple().exponent < -2:
            raise ValueError('Amount cannot have more than 2 decimal places')
        return v.quantize(Decimal('0.01'))
    
    @field_validator('recurring_frequency')
    @classmethod
    def validate_recurring_frequency(cls, v: Optional[str]) -> Optional[str]:
        """Validate recurring frequency if provided."""
        if v is not None:
            allowed_frequencies = ['daily', 'weekly', 'monthly', 'yearly']
            if v.lower() not in allowed_frequencies:
                raise ValueError(f'Recurring frequency must be one of: {", ".join(allowed_frequencies)}')
            return v.lower()
        return v
    
    @field_validator('description')
    @classmethod
    def validate_description(cls, v: Optional[str]) -> Optional[str]:
        """Clean description if provided."""
        if v is None:
            return v
        return v.strip()
    
    @field_validator('tags')
    @classmethod
    def validate_tags(cls, v: Optional[list[str]]) -> Optional[list[str]]:
        """Validate and clean tags if provided."""
        if v is None:
            return v
        cleaned_tags = list(set(tag.strip().lower() for tag in v if tag.strip()))
        return cleaned_tags if cleaned_tags else None


class TransactionResponse(TransactionBase):
    """Schema for transaction response."""
    id: str = Field(..., description="Transaction unique identifier")
    user_id: str = Field(..., description="Owner user ID")
    created_at: datetime = Field(..., description="Transaction creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    
    class Config:
        from_attributes = True


class TransactionWithDetails(TransactionResponse):
    """Schema for transaction response with related details."""
    account_name: Optional[str] = Field(None, description="Account name")
    category_name: Optional[str] = Field(None, description="Category name")
    category_color: Optional[str] = Field(None, description="Category color")
    category_icon: Optional[str] = Field(None, description="Category icon")
