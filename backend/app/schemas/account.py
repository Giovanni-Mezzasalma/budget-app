"""
Account-related Pydantic schemas for request/response validation.
"""

from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class AccountBase(BaseModel):
    """Base account schema with common fields."""
    name: str = Field(..., min_length=1, max_length=100, description="Account name")
    type: str = Field(..., description="Account type: checking, savings, credit_card, cash, investment")
    currency: str = Field(default="EUR", min_length=3, max_length=3, description="Currency code (ISO 4217)")
    initial_balance: Decimal = Field(default=Decimal("0.00"), description="Initial account balance")
    color: Optional[str] = Field(None, max_length=7, description="Hex color code for UI (e.g., #FF5733)")
    icon: Optional[str] = Field(None, max_length=50, description="Icon name for UI")
    notes: Optional[str] = Field(None, max_length=500, description="Additional notes")
    
    @field_validator('type')
    @classmethod
    def validate_account_type(cls, v: str) -> str:
        """Validate account type."""
        allowed_types = ['checking', 'savings', 'credit_card', 'cash', 'investment', 'loan', 'other']
        if v.lower() not in allowed_types:
            raise ValueError(f'Account type must be one of: {", ".join(allowed_types)}')
        return v.lower()
    
    @field_validator('currency')
    @classmethod
    def validate_currency(cls, v: str) -> str:
        """Validate and uppercase currency code."""
        v = v.upper().strip()
        if len(v) != 3:
            raise ValueError('Currency code must be exactly 3 characters (ISO 4217)')
        return v
    
    @field_validator('color')
    @classmethod
    def validate_color(cls, v: Optional[str]) -> Optional[str]:
        """Validate hex color format."""
        if v is None:
            return v
        v = v.strip()
        if not v.startswith('#') or len(v) != 7:
            raise ValueError('Color must be in hex format (#RRGGBB)')
        try:
            int(v[1:], 16)
        except ValueError:
            raise ValueError('Color must be a valid hex code')
        return v.upper()
    
    @field_validator('initial_balance')
    @classmethod
    def validate_initial_balance(cls, v: Decimal) -> Decimal:
        """Validate initial balance has max 2 decimal places."""
        if v.as_tuple().exponent < -2:
            raise ValueError('Balance cannot have more than 2 decimal places')
        return v.quantize(Decimal('0.01'))


class AccountCreate(AccountBase):
    """Schema for creating a new account."""
    pass


class AccountUpdate(BaseModel):
    """Schema for updating an existing account."""
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="Account name")
    type: Optional[str] = Field(None, description="Account type")
    currency: Optional[str] = Field(None, min_length=3, max_length=3, description="Currency code")
    color: Optional[str] = Field(None, max_length=7, description="Hex color code")
    icon: Optional[str] = Field(None, max_length=50, description="Icon name")
    notes: Optional[str] = Field(None, max_length=500, description="Additional notes")
    is_active: Optional[bool] = Field(None, description="Account active status")
    
    @field_validator('type')
    @classmethod
    def validate_account_type(cls, v: Optional[str]) -> Optional[str]:
        """Validate account type if provided."""
        if v is None:
            return v
        allowed_types = ['checking', 'savings', 'credit_card', 'cash', 'investment', 'loan', 'other']
        if v.lower() not in allowed_types:
            raise ValueError(f'Account type must be one of: {", ".join(allowed_types)}')
        return v.lower()
    
    @field_validator('currency')
    @classmethod
    def validate_currency(cls, v: Optional[str]) -> Optional[str]:
        """Validate and uppercase currency code if provided."""
        if v is None:
            return v
        v = v.upper().strip()
        if len(v) != 3:
            raise ValueError('Currency code must be exactly 3 characters (ISO 4217)')
        return v
    
    @field_validator('color')
    @classmethod
    def validate_color(cls, v: Optional[str]) -> Optional[str]:
        """Validate hex color format if provided."""
        if v is None:
            return v
        v = v.strip()
        if not v.startswith('#') or len(v) != 7:
            raise ValueError('Color must be in hex format (#RRGGBB)')
        try:
            int(v[1:], 16)
        except ValueError:
            raise ValueError('Color must be a valid hex code')
        return v.upper()


class AccountResponse(AccountBase):
    """Schema for account response."""
    id: str = Field(..., description="Account unique identifier")
    user_id: str = Field(..., description="Owner user ID")
    is_active: bool = Field(default=True, description="Account active status")
    created_at: datetime = Field(..., description="Account creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    
    class Config:
        from_attributes = True


class AccountWithBalance(AccountResponse):
    """Schema for account response with calculated current balance."""
    current_balance: Decimal = Field(..., description="Current account balance (initial + transactions)")
    
    @field_validator('current_balance')
    @classmethod
    def validate_current_balance(cls, v: Decimal) -> Decimal:
        """Ensure current balance has max 2 decimal places."""
        return v.quantize(Decimal('0.01'))
