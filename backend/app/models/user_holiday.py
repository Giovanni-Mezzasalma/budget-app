"""
UserHoliday database model.

User-defined custom holidays (patron saint, company closures, etc.).
"""

import calendar
import uuid as uuid_lib
from datetime import date as date_type, datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, ForeignKey, Index, Integer, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.user import User


class UserHoliday(Base):
    """
    User-defined custom holidays.

    Use cases:
    - Patron saint day (es. Sant'Ambrogio 7/12 Milano, San Giovanni 24/6 Torino)
    - Company mandatory closures
    - Other personal holidays

    Attributes:
        user_id: Owner of this holiday
        day: Day of month (1-31)
        month: Month (1-12)
        name: Holiday name
        recurring: True = repeats every year; False = one-time only
        year: Only used when recurring=False (specific year)
    """

    __tablename__ = "user_holidays"

    # Primary Key
    id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid_lib.uuid4,
        index=True,
    )

    # Foreign Key
    user_id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # Date components (allows recurring holidays without storing a full date)
    day: Mapped[int] = mapped_column(Integer, nullable=False)    # 1-31
    month: Mapped[int] = mapped_column(Integer, nullable=False)  # 1-12
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    # Recurring = repeats every year (e.g. patron saint)
    # Non-recurring = specific year only
    recurring: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    year: Mapped[int | None] = mapped_column(Integer, nullable=True)  # Only for non-recurring

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="user_holidays")

    # Constraints & Indexes
    __table_args__ = (
        UniqueConstraint("user_id", "day", "month", "year", name="uq_user_holiday"),
        Index("ix_user_holidays_user_month", "user_id", "month"),
    )

    def __repr__(self) -> str:
        return (
            f"<UserHoliday("
            f"name={self.name}, "
            f"{self.day}/{self.month}, "
            f"recurring={self.recurring}"
            f")>"
        )

    def get_date_for_year(self, year: int) -> date_type | None:
        """
        Return the actual date for a specific year.

        Returns None if:
        - Holiday is non-recurring and the year doesn't match
        - Date is invalid (e.g. Feb 30)
        """
        if not self.recurring and self.year and self.year != year:
            return None
        try:
            return date_type(year, self.month, self.day)
        except ValueError:
            return None

    def validate_date(self) -> None:
        """Validate that day is valid for the given month."""
        max_day = calendar.monthrange(2024, self.month)[1]  # Use leap year for max day
        if self.day > max_day:
            raise ValueError(f"Day {self.day} is invalid for month {self.month}")
