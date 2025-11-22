"""
Account database model.
"""

from datetime import datetime
from decimal import Decimal
from typing import List, TYPE_CHECKING
from sqlalchemy import String, Boolean, DateTime, Numeric, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
import uuid

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.transaction import Transaction
    from app.models.transfer import Transfer


class Account(Base):
    """Account model for managing user financial accounts."""
    
    __tablename__ = "accounts"
    
    # Primary Key
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True
    )
    
    # Foreign Keys
    user_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    
    # Account Information
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    type: Mapped[str] = mapped_column(String(50), nullable=False)  # checking, savings, credit_card, cash, investment, loan, other
    currency: Mapped[str] = mapped_column(String(3), nullable=False, default="EUR")  # ISO 4217
    initial_balance: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=Decimal("0.00")
    )
    
    # UI Customization
    color: Mapped[str] = mapped_column(String(7), nullable=True)  # Hex color
    icon: Mapped[str] = mapped_column(String(50), nullable=True)
    notes: Mapped[str] = mapped_column(String(500), nullable=True)
    
    # Status
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )
    
    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="accounts")
    
    transactions: Mapped[List["Transaction"]] = relationship(
        "Transaction",
        back_populates="account",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    transfers_from: Mapped[List["Transfer"]] = relationship(
        "Transfer",
        foreign_keys="Transfer.from_account_id",
        back_populates="from_account",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    transfers_to: Mapped[List["Transfer"]] = relationship(
        "Transfer",
        foreign_keys="Transfer.to_account_id",
        back_populates="to_account",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    # Indexes
    __table_args__ = (
        Index('ix_accounts_user_active', 'user_id', 'is_active'),
        Index('ix_accounts_user_type', 'user_id', 'type'),
    )
    
    def __repr__(self) -> str:
        return f"<Account(id={self.id}, name={self.name}, type={self.type}, currency={self.currency})>"
    
    @property
    def current_balance(self) -> Decimal:
        """
        Calculate current balance: initial_balance + sum(transactions) + sum(transfers).
        Note: This is a computed property. For better performance in queries,
        consider caching or computing at query time.
        """
        balance = self.initial_balance
        
        # Add income transactions, subtract expense transactions
        for transaction in self.transactions:
            if transaction.type == "income":
                balance += transaction.amount
            else:  # expense
                balance -= transaction.amount
        
        # Add incoming transfers, subtract outgoing transfers
        for transfer in self.transfers_to:
            if transfer.exchange_rate:
                # If exchange rate is set, use converted amount
                balance += transfer.amount * transfer.exchange_rate
            else:
                balance += transfer.amount
        
        for transfer in self.transfers_from:
            balance -= (transfer.amount + transfer.fee)
        
        return balance