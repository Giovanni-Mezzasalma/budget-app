"""
VacationSettings database model.

ARCHITETTURA:
- Maturazione separata per tipo (Ferie in giorni/mese, ROL/Permessi in ore/mese)
- Tracking start date invece di carryover year
- Saldo iniziale opzionale per gestire ore già maturate prima del tracking
"""

from datetime import date as date_type, datetime
from typing import TYPE_CHECKING
from sqlalchemy import Integer, Float, ForeignKey, Date, DateTime, UniqueConstraint, Index
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
import uuid as uuid_lib

if TYPE_CHECKING:
    from app.models.user import User


class VacationSettings(Base):
    """
    User settings for vacation tracking.

    Attributes:
        user_id: Owner (one per user, enforced by unique constraint)
        work_hours_per_day: Hours in a work day (default 8, user configurable)

        ferie_days_per_month: Days of vacation accrued per month (default 1.83 ≈ 22 days/year)
        rol_hours_per_month: ROL hours accrued per month (default 2.67 ≈ 32 hours/year)
        permessi_hours_per_month: Permission hours accrued per month (default 8.67 ≈ 104 hours/year)

        tracking_start_date: Date from which accrual begins (employment/contract start)

        initial_balance_month: Optional month (1-12) for the initial balance snapshot
        initial_balance_year: Optional year for the initial balance snapshot
        initial_ferie_days: Initial vacation days (stored in days, converted to hours by logic layer)
        initial_rol_hours: Initial ROL hours
        initial_permessi_hours: Initial permission hours
    """

    __tablename__ = "vacation_settings"

    # Primary Key
    id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid_lib.uuid4,
        index=True,
    )

    # Foreign Key (one per user)
    user_id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # Work configuration
    work_hours_per_day: Mapped[float] = mapped_column(Float, nullable=False, default=8.0)

    # Accrual rates — SEPARATE PER TYPE
    ferie_days_per_month: Mapped[float] = mapped_column(
        Float, nullable=False, default=1.83  # ~22 giorni/anno
    )
    rol_hours_per_month: Mapped[float] = mapped_column(
        Float, nullable=False, default=2.67  # ~32 ore/anno
    )
    permessi_hours_per_month: Mapped[float] = mapped_column(
        Float, nullable=False, default=8.67  # ~104 ore/anno
    )

    # Tracking start
    tracking_start_date: Mapped[date_type] = mapped_column(
        Date, nullable=False, default=date_type.today
    )

    # Optional initial balance (for migration from other systems)
    initial_balance_month: Mapped[int | None] = mapped_column(Integer, nullable=True)  # 1-12
    initial_balance_year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    initial_ferie_days: Mapped[float | None] = mapped_column(Float, nullable=True, default=0.0)
    initial_rol_hours: Mapped[float | None] = mapped_column(Float, nullable=True, default=0.0)
    initial_permessi_hours: Mapped[float | None] = mapped_column(Float, nullable=True, default=0.0)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="vacation_settings")

    # Constraints & Indexes
    __table_args__ = (
        UniqueConstraint("user_id", name="uq_vacation_settings_user"),
        Index("ix_vacation_settings_user_id", "user_id"),
    )

    def __repr__(self) -> str:
        return (
            f"<VacationSettings("
            f"user_id={self.user_id}, "
            f"ferie={self.ferie_days_per_month}d/mo, "
            f"rol={self.rol_hours_per_month}h/mo, "
            f"permessi={self.permessi_hours_per_month}h/mo"
            f")>"
        )
