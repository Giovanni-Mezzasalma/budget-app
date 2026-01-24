"""
Transaction database model.
"""

from datetime import datetime, date
from decimal import Decimal
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, DateTime, Date, Numeric, Boolean, ForeignKey, Index, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID as PGUUID
import uuid as uuid_lib

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.account import Account
    from app.models.category import Category


class Transaction(Base):
    """Transaction model for income and expense tracking."""
    
    __tablename__ = "transactions"
    
    # Primary Key
    id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid_lib.uuid4,
        index=True
    )
    
    # Foreign Keys
    user_id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    
    account_id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("accounts.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    
    category_id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )
        
    # Transaction Information
    amount: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False
    )
    type: Mapped[str] = mapped_column(String(20), nullable=False)  # income, expense_necessity or expense_extra
    date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    
    # Recurring Transaction Settings
    is_recurring: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    recurring_frequency: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)  # daily, weekly, monthly, yearly
    
    # Tags for filtering and organization
    tags: Mapped[Optional[list[str]]] = mapped_column(
        ARRAY(String(50)),
        nullable=True
    )
    
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
    user: Mapped["User"] = relationship("User", back_populates="transactions")
    account: Mapped["Account"] = relationship("Account", back_populates="transactions")
    category: Mapped["Category"] = relationship("Category", back_populates="transactions")
    
    # Indexes
    __table_args__ = (
        Index('ix_transactions_user_date', 'user_id', 'date'),
        Index('ix_transactions_user_type', 'user_id', 'type'),
        Index('ix_transactions_account_date', 'account_id', 'date'),
        Index('ix_transactions_category', 'category_id'),
        Index('ix_transactions_user_recurring', 'user_id', 'is_recurring'),
    )
    
    def __repr__(self) -> str:
        return f"<Transaction(id={self.id}, type={self.type}, amount={self.amount}, date={self.date})>"
    
    @property
    def signed_amount(self) -> Decimal:
        """
        Return signed amount based on transaction type.
        Positive for income, negative for expense.
        """
        return self.amount if self.type == "income" else -self.amount
