"""
ItalianHoliday CRUD Operations.

Manages the pre-populated table of national Italian holidays.
Fixed holidays are inserted once; mobile holidays (Easter/Pasquetta)
are calculated per year on demand via ensure_holidays_exist().
"""
from datetime import date
from typing import List, Optional, Union
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.italian_holiday import ItalianHoliday, FIXED_ITALIAN_HOLIDAYS
from app.utils.easter import calculate_easter_monday


# ── Read ──────────────────────────────────────────────────────────────────────

def get_by_date(db: Session, d: date) -> Optional[ItalianHoliday]:
    """Return the holiday record for a given date, or None."""
    return (
        db.query(ItalianHoliday)
        .filter(ItalianHoliday.date == d)
        .first()
    )


def get_by_year(db: Session, year: int) -> List[ItalianHoliday]:
    """Return all holidays for a given year (fixed + mobile), ordered by date."""
    return (
        db.query(ItalianHoliday)
        .filter(
            ItalianHoliday.date >= date(year, 1, 1),
            ItalianHoliday.date <= date(year, 12, 31),
        )
        .order_by(ItalianHoliday.date)
        .all()
    )


# ── Write / seed ──────────────────────────────────────────────────────────────

def _seed_fixed_holidays(db: Session, year: int) -> None:
    """Insert fixed national holidays for a year if not already present."""
    for month, day, name_it, name_en in FIXED_ITALIAN_HOLIDAYS:
        d = date(year, month, day)
        if get_by_date(db, d) is None:
            db.add(ItalianHoliday(
                date=d,
                name=name_it,
                name_en=name_en,
                is_fixed=True,
                is_national=True,
            ))


def _seed_easter(db: Session, year: int) -> None:
    """Insert Easter Monday (Pasquetta) for a year if not already present."""
    pasquetta = calculate_easter_monday(year)
    if get_by_date(db, pasquetta) is None:
        db.add(ItalianHoliday(
            date=pasquetta,
            name="Lunedì dell'Angelo (Pasquetta)",
            name_en="Easter Monday",
            is_fixed=False,
            is_national=True,
        ))


def ensure_holidays_exist(db: Session, year: int) -> List[ItalianHoliday]:
    """
    Ensure all holidays for a year exist in the DB, creating them if needed.

    Called lazily by the router: if the year's holidays are not yet seeded
    (e.g. first request for a new year), they are created and committed here.

    Returns the full list of holidays for the year.
    """
    existing = get_by_year(db, year)
    if not existing:
        _seed_fixed_holidays(db, year)
        _seed_easter(db, year)
        db.commit()
        existing = get_by_year(db, year)
    return existing
