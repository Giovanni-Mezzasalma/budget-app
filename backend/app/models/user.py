"""
User database model.
"""

from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import String, Boolean, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
import uuid as uuid_lib

if TYPE_CHECKING:
    from app.models.vacation_settings import VacationSettings
    from app.models.vacation_entry import VacationEntry
    from app.models.user_holiday import UserHoliday
class User(Base):
    """User model for authentication and user management."""
    
    __tablename__ = "users"
    
    # Primary Key
    id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid_lib.uuid4,
        index=True
    )
    
    # User Information
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    
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
    accounts: Mapped[List["Account"]] = relationship(
        "Account",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    categories: Mapped[List["Category"]] = relationship(
        "Category",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    transactions: Mapped[List["Transaction"]] = relationship(
        "Transaction",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    transfers: Mapped[List["Transfer"]] = relationship(
        "Transfer",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    custom_charts: Mapped[List["CustomChart"]] = relationship(
        "CustomChart",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    # Vacation relationships
    vacation_settings: Mapped[Optional["VacationSettings"]] = relationship(
        "VacationSettings",
        back_populates="user",
        uselist=False,  # one-to-one
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    vacation_entries: Mapped[List["VacationEntry"]] = relationship(
        "VacationEntry",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    user_holidays: Mapped[List["UserHoliday"]] = relationship(
        "UserHoliday",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    # Indexes
    __table_args__ = (
        Index('ix_users_email_active', 'email', 'is_active'),
    )
    
    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email}, full_name={self.full_name})>"
