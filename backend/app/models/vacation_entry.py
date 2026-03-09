"""
VacationEntry database model.

IMPORTANTE: Un solo tipo di assenza per giorno (UniqueConstraint su user_id + date).
- Ferie: ore automatiche da work_hours_per_day (no input manuale)
- ROL/Permessi: ore inserite manualmente dall'utente
- MALATTIA: RIMOSSA (non necessaria per utenti privati)
"""

import enum
import uuid as uuid_lib
from datetime import date as date_type, datetime
from typing import TYPE_CHECKING

from sqlalchemy import Date, DateTime, Enum, Float, ForeignKey, Index, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.user import User


class VacationEntryType(str, enum.Enum):
    """Types of vacation/leave entries."""
    FERIE = "ferie"        # Regular vacation (hours automatic from settings)
    PERMESSO = "permesso"  # Personal leave (hours manual)
    ROL = "rol"            # Riduzione Orario Lavoro (hours manual)


# Italian labels for entry types
VACATION_ENTRY_TYPE_LABELS = {
    "ferie": "Ferie",
    "permesso": "Permesso",
    "rol": "ROL (Riduzione Orario Lavoro)",
}

# Types that require manual hour input
MANUAL_HOURS_TYPES = ["permesso", "rol"]


class VacationEntry(Base):
    """
    Individual vacation or leave entry.

    REGOLE:
    - Un solo tipo per giorno (UniqueConstraint su user_id + date)
    - Ferie: ore = work_hours_per_day da settings (automatico)
    - ROL/Permessi: ore inserite manualmente
    - NO weekend: validazione blocca inserimento
    - NO festività: validazione blocca inserimento (nazionali + custom utente)

    Attributes:
        user_id: Owner of this entry
        date: Date of the entry
        entry_type: Type of leave (ferie, permesso, rol)
        hours: Number of hours (automatic for ferie, manual for others)
        notes: Optional notes
    """

    __tablename__ = "vacation_entries"

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

    # Entry data
    date: Mapped[date_type] = mapped_column(Date, nullable=False, index=True)
    entry_type: Mapped[VacationEntryType] = mapped_column(
        Enum(VacationEntryType, name="vacation_entry_type"),
        nullable=False,
        default=VacationEntryType.FERIE,
    )
    hours: Mapped[float] = mapped_column(Float, nullable=False, default=8.0)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="vacation_entries")

    # Constraints & Indexes — un solo tipo per giorno!
    __table_args__ = (
        UniqueConstraint("user_id", "date", name="uq_vacation_entry_user_date"),
        Index("ix_vacation_entries_user_date", "user_id", "date"),
        Index("ix_vacation_entries_user_type", "user_id", "entry_type"),
    )

    def __repr__(self) -> str:
        return (
            f"<VacationEntry("
            f"date={self.date}, "
            f"type={self.entry_type}, "
            f"hours={self.hours}"
            f")>"
        )
