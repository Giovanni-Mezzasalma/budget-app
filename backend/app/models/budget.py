"""
Budget model for monthly expense tracking and planning.
"""
from datetime import datetime, date
from typing import Optional, TYPE_CHECKING
from decimal import Decimal
from sqlalchemy import String, Boolean, DateTime, Date, Numeric, ForeignKey, Index, text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
import uuid as uuid_lib

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.category import Category


class Budget(Base):
    """Budget model for tracking monthly spending limits."""

    __tablename__ = "budgets"

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
        nullable=False
    )

    category_id: Mapped[Optional[uuid_lib.UUID]] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="SET NULL"),
        nullable=True
    )

    # Budget Information
    amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
        comment="Budget amount for the period"
    )

    period: Mapped[str] = mapped_column(
        String(20),
        default="monthly",
        nullable=False,
        comment="Budget period: 'monthly' for MVP"
    )

    # Dates
    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        comment="Date when this budget becomes active"
    )

    # Status
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        comment="Active budgets are used for current tracking"
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
    user: Mapped["User"] = relationship("User", back_populates="budgets")
    category: Mapped[Optional["Category"]] = relationship("Category")

    # Indexes and Constraints
    __table_args__ = (
        Index('ix_budgets_user_active', 'user_id', 'is_active'),
        Index('ix_budgets_category', 'category_id'),
        Index('ix_budgets_start_date', 'start_date'),
        # Partial unique index: only one active budget per category per user
        # Inactive budgets are excluded, allowing historical records
        Index(
            'uq_budget_user_category_active',
            'user_id', 'category_id',
            unique=True,
            postgresql_where=text('is_active = true')
        ),
    )

    def __repr__(self) -> str:
        return f"<Budget(id={self.id}, amount={self.amount}, period={self.period}, active={self.is_active})>"
