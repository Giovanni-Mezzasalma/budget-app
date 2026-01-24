"""
Transfer-related Pydantic schemas for request/response validation.

Tipi di trasferimento:
- generic: Trasferimento generico (giroconto)
- withdrawal: Prelievo (Conto → Contanti)
- deposit: Versamento (Contanti → Conto)
- savings: Risparmio (Corrente → Risparmio)
- investment: Investimento (Corrente → Investimento)
- loan_given: Prestito dato (Corrente → Prestiti a terzi)
- loan_received: Prestito ricevuto (Prestiti a terzi → Corrente)
"""

from datetime import datetime, date as date_type
from decimal import Decimal
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field, field_validator


# Tipi validi per i trasferimenti
VALID_TRANSFER_TYPES = [
    "generic",        # Trasferimento generico / Giroconto
    "withdrawal",     # Prelievo (Conto → Contanti)
    "deposit",        # Versamento (Contanti → Conto)
    "savings",        # Risparmio (Corrente → Risparmio)
    "investment",     # Investimento (Corrente → Investimento)
    "loan_given",     # Prestito dato (Corrente → Prestiti a terzi)
    "loan_received",  # Prestito ricevuto (Prestiti a terzi → Corrente)
]

# Labels italiane per i tipi
TRANSFER_TYPE_LABELS = {
    "generic": "Trasferimento",
    "withdrawal": "Prelievo",
    "deposit": "Versamento",
    "savings": "Risparmio",
    "investment": "Investimento",
    "loan_given": "Prestito dato",
    "loan_received": "Prestito ricevuto",
}

# Descrizioni uso per i tipi
TRANSFER_TYPE_USAGE = {
    "generic": "Giroconto generico",
    "withdrawal": "Conto → Contanti",
    "deposit": "Contanti → Conto",
    "savings": "Corrente → Risparmio",
    "investment": "Corrente → Investimento",
    "loan_given": "Corrente → Prestiti a terzi",
    "loan_received": "Prestiti a terzi → Corrente",
}

# Regole di direzione per tipo di trasferimento
# Definisce quali tipi di account sono validi come origine/destinazione per ogni tipo di transfer
# None significa "qualsiasi tipo di account"
# Regole di direzione per tipo di trasferimento
TRANSFER_TYPE_DIRECTION_RULES = {
    "generic": {
        "from_account_types": None,  # Qualsiasi
        "to_account_types": None,    # Qualsiasi
        "description": "Trasferimento generico tra qualsiasi account"
    },
    "withdrawal": {
        "from_account_types": ["checking", "savings"],  # Da conto bancario
        "to_account_types": ["cash"],                   # A contanti
        "description": "Prelievo da conto a contanti"
    },
    "deposit": {
        "from_account_types": ["cash"],                 # Da contanti
        "to_account_types": ["checking", "savings"],    # A conto bancario
        "description": "Versamento da contanti a conto"
    },
    "savings": {
        "from_account_types": ["checking"],             # Da conto corrente
        "to_account_types": ["savings"],                # A risparmio
        "description": "Accantonamento risparmio"
    },
    "investment": {
        "from_account_types": ["checking", "savings"],  # Da conto
        "to_account_types": ["investment"],             # A investimento
        "description": "Investimento"
    },
    "loan_given": {
        "from_account_types": ["checking", "savings", "cash"],  # Da conto/contanti
        "to_account_types": ["loan"],                           # A prestiti
        "description": "Prestito dato a terzi"
    },
    "loan_received": {
        "from_account_types": ["loan"],                         # Da prestiti
        "to_account_types": ["checking", "savings", "cash"],    # A conto/contanti
        "description": "Restituzione prestito da terzi"
    },
}


class TransferBase(BaseModel):
    """Base transfer schema with common fields."""
    from_account_id: UUID = Field(..., description="Source account ID")
    to_account_id: UUID = Field(..., description="Destination account ID")
    amount: Decimal = Field(..., gt=0, description="Transfer amount (always positive)")
    type: str = Field(default="generic", description="Transfer type: generic, withdrawal, deposit, savings, investment, loan_given, loan_received")
    date: date_type = Field(..., description="Transfer date")
    description: Optional[str] = Field(None, max_length=500, description="Transfer description (es. 'Prestito a Mario')")
    notes: Optional[str] = Field(None, max_length=1000, description="Additional notes")
    exchange_rate: Optional[Decimal] = Field(None, gt=0, description="Exchange rate if different currencies")
    fee: Optional[Decimal] = Field(default=Decimal("0.00"), ge=0, description="Transfer fee")
    
    @field_validator('type')
    @classmethod
    def validate_transfer_type(cls, v: str) -> str:
        """Validate transfer type."""
        if v.lower() not in VALID_TRANSFER_TYPES:
            raise ValueError(f'Transfer type must be one of: {", ".join(VALID_TRANSFER_TYPES)}')
        return v.lower()
    
    @field_validator('amount')
    @classmethod
    def validate_amount(cls, v: Decimal) -> Decimal:
        """Validate amount has max 2 decimal places and is positive."""
        if v <= 0:
            raise ValueError('Amount must be positive')
        return round(v, 2)
    
    @field_validator('exchange_rate')
    @classmethod
    def validate_exchange_rate(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        """Validate exchange rate if provided."""
        if v is None:
            return v
        if v <= 0:
            raise ValueError('Exchange rate must be positive')
        return round(v, 6)
    
    @field_validator('fee')
    @classmethod
    def validate_fee(cls, v: Optional[Decimal]) -> Decimal:
        """Validate fee has max 2 decimal places and is non-negative."""
        if v is None:
            return Decimal("0.00")
        if v < 0:
            raise ValueError('Fee cannot be negative')
        return round(v, 2)
    
    @field_validator('description')
    @classmethod
    def validate_description(cls, v: Optional[str]) -> Optional[str]:
        """Clean description if provided."""
        if v is None:
            return v
        return v.strip()
    
    @field_validator('to_account_id')
    @classmethod
    def validate_different_accounts(cls, v: UUID, info) -> UUID:
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
    from_account_id: Optional[UUID] = Field(None, description="Source account ID")
    to_account_id: Optional[UUID] = Field(None, description="Destination account ID")
    amount: Optional[Decimal] = Field(None, gt=0, description="Transfer amount")
    type: Optional[str] = Field(None, description="Transfer type")
    date: Optional[date_type] = Field(None, description="Transfer date")
    description: Optional[str] = Field(None, max_length=500, description="Transfer description")
    notes: Optional[str] = Field(None, max_length=1000, description="Additional notes")
    exchange_rate: Optional[Decimal] = Field(None, gt=0, description="Exchange rate")
    fee: Optional[Decimal] = Field(None, ge=0, description="Transfer fee")
    
    @field_validator('type')
    @classmethod
    def validate_transfer_type(cls, v: Optional[str]) -> Optional[str]:
        """Validate transfer type if provided."""
        if v is None:
            return v
        if v.lower() not in VALID_TRANSFER_TYPES:
            raise ValueError(f'Transfer type must be one of: {", ".join(VALID_TRANSFER_TYPES)}')
        return v.lower()
    
    @field_validator('amount')
    @classmethod
    def validate_amount(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        """Validate amount if provided."""
        if v is None:
            return v
        if v <= 0:
            raise ValueError('Amount must be positive')
        return round(v, 2)
    
    @field_validator('exchange_rate')
    @classmethod
    def validate_exchange_rate(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        """Validate exchange rate if provided."""
        if v is None:
            return v
        if v <= 0:
            raise ValueError('Exchange rate must be positive')
        return round(v, 6)
    
    @field_validator('fee')
    @classmethod
    def validate_fee(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        """Validate fee if provided."""
        if v is None:
            return v
        if v < 0:
            raise ValueError('Fee cannot be negative')
        return round(v, 2)
    
    @field_validator('description')
    @classmethod
    def validate_description(cls, v: Optional[str]) -> Optional[str]:
        """Clean description if provided."""
        if v is None:
            return v
        return v.strip()
    
    @field_validator('to_account_id')
    @classmethod
    def validate_different_accounts(cls, v: Optional[UUID], info) -> Optional[UUID]:
        """Ensure source and destination accounts are different if both provided."""
        if v is None:
            return v
        from_account = info.data.get('from_account_id')
        if from_account and v == from_account:
            raise ValueError('Source and destination accounts must be different')
        return v


class TransferResponse(BaseModel):
    """Schema for transfer response."""
    id: UUID = Field(..., description="Transfer unique identifier")
    user_id: UUID = Field(..., description="Owner user ID")
    from_account_id: UUID = Field(..., description="Source account ID")
    to_account_id: UUID = Field(..., description="Destination account ID")
    type: str = Field(..., description="Transfer type")
    amount: Decimal = Field(..., description="Transfer amount")
    date: date_type = Field(..., description="Transfer date")
    description: Optional[str] = Field(None, description="Transfer description")
    notes: Optional[str] = Field(None, description="Additional notes")
    exchange_rate: Optional[Decimal] = Field(None, description="Exchange rate")
    fee: Decimal = Field(..., description="Transfer fee")
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
    type_label: Optional[str] = Field(None, description="Italian label for transfer type")
    type_usage: Optional[str] = Field(None, description="Usage description for transfer type")


class TransferTypeInfo(BaseModel):
    """Schema for transfer type information."""
    value: str = Field(..., description="Transfer type value")
    label: str = Field(..., description="Italian label")
    usage: str = Field(..., description="Usage description")