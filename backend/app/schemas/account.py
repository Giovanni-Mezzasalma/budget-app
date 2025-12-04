"""
Account-related Pydantic schemas for request/response validation.

Balance Strategy:
- initial_balance: Impostato solo alla creazione, poi immutabile
- current_balance: Aggiornato automaticamente, read-only per l'utente
"""

from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, field_validator


# Valid account types
VALID_ACCOUNT_TYPES = ['checking', 'savings', 'credit_card', 'cash', 'investment', 'loan', 'other']


class AccountBase(BaseModel):
    """Base account schema with common fields."""
    name: str = Field(..., min_length=1, max_length=100, description="Account name")
    type: str = Field(..., description="Account type: checking, savings, credit_card, cash, investment, loan, other")
    currency: str = Field(default="EUR", min_length=3, max_length=3, description="Currency code (ISO 4217)")
    color: Optional[str] = Field(None, max_length=7, description="Hex color code for UI (e.g., #FF5733)")
    icon: Optional[str] = Field(None, max_length=50, description="Icon name for UI")
    notes: Optional[str] = Field(None, max_length=500, description="Additional notes")
    
    @field_validator('type')
    @classmethod
    def validate_account_type(cls, v: str) -> str:
        """Validate account type."""
        if v.lower() not in VALID_ACCOUNT_TYPES:
            raise ValueError(f'Account type must be one of: {", ".join(VALID_ACCOUNT_TYPES)}')
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


class AccountCreate(AccountBase):
    """
    Schema for creating a new account.
    
    initial_balance viene impostato alla creazione e non può essere modificato successivamente.
    current_balance viene inizializzato automaticamente allo stesso valore.
    """
    initial_balance: Decimal = Field(
        default=Decimal("0.00"), 
        description="Initial account balance (set once at creation, immutable)"
    )
    
    @field_validator('initial_balance')
    @classmethod
    def validate_initial_balance(cls, v: Decimal) -> Decimal:
        """Validate initial balance has max 2 decimal places."""
        if v.as_tuple().exponent < -2:
            raise ValueError('Balance cannot have more than 2 decimal places')
        return v.quantize(Decimal('0.01'))


class AccountUpdate(BaseModel):
    """
    Schema for updating an existing account.
    
    Note: initial_balance e current_balance NON sono modificabili direttamente.
    - initial_balance è immutabile dopo la creazione
    - current_balance viene aggiornato solo tramite transazioni/trasferimenti
    """
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
        if v.lower() not in VALID_ACCOUNT_TYPES:
            raise ValueError(f'Account type must be one of: {", ".join(VALID_ACCOUNT_TYPES)}')
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
    """Schema for account response with both balance fields."""
    id: str = Field(..., description="Account unique identifier")
    user_id: str = Field(..., description="Owner user ID")
    initial_balance: Decimal = Field(..., description="Initial balance (set at creation, immutable)")
    current_balance: Decimal = Field(..., description="Current balance (updated by transactions/transfers)")
    is_active: bool = Field(default=True, description="Account active status")
    created_at: datetime = Field(..., description="Account creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    
    class Config:
        from_attributes = True


class AccountWithStats(AccountResponse):
    """Schema for account response with additional statistics."""
    balance_difference: Decimal = Field(..., description="Difference between current and initial balance")
    transaction_count: Optional[int] = Field(None, description="Number of transactions")
    
    @field_validator('balance_difference', mode='before')
    @classmethod
    def calculate_difference(cls, v, info):
        """Calculate balance difference if not provided."""
        if v is not None:
            return v
        data = info.data
        if 'current_balance' in data and 'initial_balance' in data:
            return data['current_balance'] - data['initial_balance']
        return Decimal("0.00")


class AccountSummary(BaseModel):
    """Schema for account summary in lists/dashboards."""
    id: str
    name: str
    type: str
    currency: str
    current_balance: Decimal
    color: Optional[str] = None
    icon: Optional[str] = None
    is_active: bool = True
    
    class Config:
        from_attributes = True
