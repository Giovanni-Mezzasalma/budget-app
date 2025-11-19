"""
Transfer-related Pydantic schemas for request/response validation.
"""

from datetime import datetime, date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class TransferBase(BaseModel):
    """Base transfer schema with common fields."""
    from_account_id: str = Field(..., description="Source account ID")
    to_account_id: str = Field(..., description="Destination account ID")
    amount: Decimal = Field(..., gt=0, description="Transfer amount (always positive)")
    date: date = Field(..., description="Transfer date")
    description: Optional[str] = Field(None, max_length=500, description="Transfer description")
    notes: Optional[str] = Field(None, max_length=1000, description="Additional notes")
    exchange_rate: Optional[Decimal] = Field(None, gt=0, description="Exchange rate if different currencies")
    fee: Optional[Decimal] = Field(default=Decimal("0.00"), ge=0, description="Transfer fee")
    
    @field_validator('amount')
    @classmethod
    def validate_amount(cls, v: Decimal) -> Decimal:
        """Validate amount has max 2 decimal places and is positive."""
        if v <= 0:
            raise ValueError('Amount must be positive')
        if v.as_tuple().exponent < -2:
            raise ValueError('Amount cannot have more than 2 decimal places')
        return v.quantize(Decimal('0.01'))
    
    @field_validator('exchange_rate')
    @classmethod
    def validate_exchange_rate(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        """Validate exchange rate if provided."""
        if v is None:
            return v
        if v <= 0:
            raise ValueError('Exchange rate must be positive')
        if v.as_tuple().exponent < -6:
            raise ValueError('Exchange rate cannot have more than 6 decimal places')
        return v.quantize(Decimal('0.000001'))
    
    @field_validator('fee')
    @classmethod
    def validate_fee(cls, v: Optional[Decimal]) -> Decimal:
        """Validate fee has max 2 decimal places and is non-negative."""
        if v is None:
            v = Decimal("0.00")
        if v < 0:
            raise ValueError('Fee cannot be negative')
        if v.as_tuple().exponent < -2:
            raise ValueError('Fee cannot have more than 2 decimal places')
        return v.quantize(Decimal('0.01'))
    
    @field_validator('description')
    @classmethod
    def validate_description(cls, v: Optional[str]) -> Optional[str]:
        """Clean description if provided."""
        if v is None:
            return v
        return v.strip()
    
    @field_validator('to_account_id')
    @classmethod
    def validate_different_accounts(cls, v: str, info) -> str:
        """Ensure source and destination accounts are different."""
        from_account = info.data.get('from_account_id')
        if from_account and v == from_account:
            raise ValueError('Source and destination accounts must be different')
        return v


class TransferCreate(TransferBase):
    """Schema for creating a new transfer."""
    pass


class TransferUpdate(BaseModel):
    """Schema for updating an existing transfer."""
    from_account_id: Optional[str] = Field(None, description="Source account ID")
    to_account_id: Optional[str] = Field(None, description="Destination account ID")
    amount: Optional[Decimal] = Field(None, gt=0, description="Transfer amount")
    date: Optional[date] = Field(None, description="Transfer date")
    description: Optional[str] = Field(None, max_length=500, description="Transfer description")
    notes: Optional[str] = Field(None, max_length=1000, description="Additional notes")
    exchange_rate: Optional[Decimal] = Field(None, gt=0, description="Exchange rate")
    fee: Optional[Decimal] = Field(None, ge=0, description="Transfer fee")
    
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
    
    @field_validator('exchange_rate')
    @classmethod
    def validate_exchange_rate(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        """Validate exchange rate if provided."""
        if v is None:
            return v
        if v <= 0:
            raise ValueError('Exchange rate must be positive')
        if v.as_tuple().exponent < -6:
            raise ValueError('Exchange rate cannot have more than 6 decimal places')
        return v.quantize(Decimal('0.000001'))
    
    @field_validator('fee')
    @classmethod
    def validate_fee(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        """Validate fee if provided."""
        if v is None:
            return v
        if v < 0:
            raise ValueError('Fee cannot be negative')
        if v.as_tuple().exponent < -2:
            raise ValueError('Fee cannot have more than 2 decimal places')
        return v.quantize(Decimal('0.01'))
    
    @field_validator('description')
    @classmethod
    def validate_description(cls, v: Optional[str]) -> Optional[str]:
        """Clean description if provided."""
        if v is None:
            return v
        return v.strip()
    
    @field_validator('to_account_id')
    @classmethod
    def validate_different_accounts(cls, v: Optional[str], info) -> Optional[str]:
        """Ensure source and destination accounts are different if both provided."""
        if v is None:
            return v
        from_account = info.data.get('from_account_id')
        if from_account and v == from_account:
            raise ValueError('Source and destination accounts must be different')
        return v


class TransferResponse(TransferBase):
    """Schema for transfer response."""
    id: str = Field(..., description="Transfer unique identifier")
    user_id: str = Field(..., description="Owner user ID")
    created_at: datetime = Field(..., description="Transfer creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    
    class Config:
        from_attributes = True


class TransferWithDetails(TransferResponse):
    """Schema for transfer response with account details."""
    from_account_name: Optional[str] = Field(None, description="Source account name")
    from_account_currency: Optional[str] = Field(None, description="Source account currency")
    to_account_name: Optional[str] = Field(None, description="Destination account name")
    to_account_currency: Optional[str] = Field(None, description="Destination account currency")
    converted_amount: Optional[Decimal] = Field(None, description="Amount after exchange rate (if applicable)")
    
    @field_validator('converted_amount')
    @classmethod
    def validate_converted_amount(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        """Ensure converted amount has max 2 decimal places if provided."""
        if v is None:
            return v
        return v.quantize(Decimal('0.01'))
