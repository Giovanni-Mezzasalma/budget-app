"""
Transfer database model.
"""

from datetime import datetime, date
from decimal import Decimal
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, DateTime, Date, Numeric, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID as PGUUID
import uuid as uuid_lib

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.account import Account


class Transfer(Base):
    """Transfer model for moving money between accounts."""
    
    __tablename__ = "transfers"
    
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
    
    from_account_id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("accounts.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    
    to_account_id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("accounts.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    
    # Transfer Type
    type: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="generic"
    )  # generic, withdrawal, deposit, savings, investment, loan_given, loan_received
    
    # Transfer Information
    amount: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False
    )
    date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    
    # Exchange Rate (for transfers between different currencies)
    exchange_rate: Mapped[Optional[Decimal]] = mapped_column(
        Numeric(15, 6),
        nullable=True
    )
    
    # Transfer Fee
    fee: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=Decimal("0.00")
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
    user: Mapped["User"] = relationship("User", back_populates="transfers")
    
    from_account: Mapped["Account"] = relationship(
        "Account",
        foreign_keys=[from_account_id],
        back_populates="transfers_from"
    )
    
    to_account: Mapped["Account"] = relationship(
        "Account",
        foreign_keys=[to_account_id],
        back_populates="transfers_to"
    )
    
    # Indexes
    __table_args__ = (
        Index('ix_transfers_user_date', 'user_id', 'date'),
        Index('ix_transfers_from_account', 'from_account_id'),
        Index('ix_transfers_to_account', 'to_account_id'),
        Index('ix_transfers_accounts', 'from_account_id', 'to_account_id'),
        Index('ix_transfers_user_type', 'user_id', 'type'),
    )
    
    def __repr__(self) -> str:
        return f"<Transfer(id={self.id}, type={self.type}, amount={self.amount}, date={self.date})>"
    
    @property
    def converted_amount(self) -> Decimal:
        """
        Calculate the amount received in destination account.
        If exchange_rate is set, multiply amount by rate.
        Otherwise, return the same amount.
        """
        if self.exchange_rate:
            return self.amount * self.exchange_rate
        return self.amount