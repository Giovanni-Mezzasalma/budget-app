"""
Account Model
Gestisce conti bancari/portafogli utente
"""
from sqlalchemy import Column, String, Numeric, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum
from ..database import Base


class AccountType(str, enum.Enum):
    """Tipi di account disponibili"""
    CHECKING = "checking"
    SAVINGS = "savings"
    CREDIT = "credit"
    CASH = "cash"
    INVESTMENT = "investment"


class Account(Base):
    """Modello Account per conti utente"""
    
    __tablename__ = "accounts"
    
    # Primary Key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Foreign Key
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    # Account details
    name = Column(String(100), nullable=False)
    account_type = Column(Enum(AccountType), default=AccountType.CHECKING, nullable=False)
    balance = Column(Numeric(12, 2), default=0.00)
    currency = Column(String(3), default="EUR")
    
    # Customization
    color = Column(String(7))  # HEX color
    icon = Column(String(50))
    
    # Status
    is_active = Column(Boolean, default=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account", cascade="all, delete-orphan")
    transfers_from = relationship(
        "Transfer",
        foreign_keys="Transfer.from_account_id",
        back_populates="from_account",
        cascade="all, delete-orphan"
    )
    transfers_to = relationship(
        "Transfer",
        foreign_keys="Transfer.to_account_id",
        back_populates="to_account",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<Account {self.name} ({self.account_type})>"
