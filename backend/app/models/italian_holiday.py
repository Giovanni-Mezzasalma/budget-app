"""
ItalianHoliday database model.

Pre-populated table with national holidays.
Mobile holidays (Easter/Pasquetta) are calculated and inserted dynamically.
NOTE: Shift domenica→lunedì rimandato a Fase 7.
"""

import uuid as uuid_lib
from datetime import date as date_type

from sqlalchemy import Boolean, Date, Index, String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class ItalianHoliday(Base):
    """
    Italian public holidays (national).

    Fixed holidays are pre-populated at migration time.
    Mobile holidays (Pasqua, Pasquetta) are calculated and inserted dynamically
    per year by the easter utility.

    Attributes:
        date: Holiday date (unique — one record per date)
        name: Holiday name in Italian
        name_en: Holiday name in English
        is_fixed: True if same date every year (e.g. Natale), False for mobile (Pasquetta)
        is_national: True if national holiday
    """

    __tablename__ = "italian_holidays"

    # Primary Key
    id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid_lib.uuid4,
        index=True,
    )

    date: Mapped[date_type] = mapped_column(Date, nullable=False, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    name_en: Mapped[str | None] = mapped_column(String(100), nullable=True)
    is_fixed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    is_national: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    # Indexes
    __table_args__ = (
        Index("ix_italian_holidays_year", "date"),
    )

    def __repr__(self) -> str:
        return f"<ItalianHoliday(date={self.date}, name={self.name})>"


# Fixed Italian national holidays: (month, day, name_it, name_en)
FIXED_ITALIAN_HOLIDAYS = [
    (1,  1,  "Capodanno",                "New Year's Day"),
    (1,  6,  "Epifania",                 "Epiphany"),
    (4,  25, "Festa della Liberazione",  "Liberation Day"),
    (5,  1,  "Festa dei Lavoratori",     "Labour Day"),
    (6,  2,  "Festa della Repubblica",   "Republic Day"),
    (8,  15, "Ferragosto",               "Assumption of Mary"),
    (11, 1,  "Tutti i Santi",            "All Saints' Day"),
    (12, 8,  "Immacolata Concezione",    "Immaculate Conception"),
    (12, 25, "Natale",                   "Christmas Day"),
    (12, 26, "Santo Stefano",            "St. Stephen's Day"),
]
