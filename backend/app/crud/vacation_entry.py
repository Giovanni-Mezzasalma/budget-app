"""
VacationEntry CRUD Operations.

VALIDAZIONI in create():
- Blocco inserimento weekend
- Blocco inserimento festività nazionali (ItalianHoliday)
- Blocco inserimento festività custom utente (UserHoliday)
- Un solo entry per data (UniqueConstraint DB)

Logica ore:
- Ferie:          automatiche da VacationSettings.work_hours_per_day
- ROL / Permesso: ore manuali obbligatorie (già validate dallo schema)
"""
from datetime import date as date_type
from typing import List, Optional, Union, Dict, Any
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.vacation_entry import VacationEntry, VacationEntryType, MANUAL_HOURS_TYPES
from app.schemas.vacation import VacationEntryCreate, VacationEntryUpdate
from app.utils.bridge_days import is_weekend


def _to_uuid(value: Union[str, UUID]) -> UUID:
    if isinstance(value, str):
        return UUID(value)
    return value


# ── Read ──────────────────────────────────────────────────────────────────────

def get(
    db: Session, entry_id: Union[str, UUID], user_id: Union[str, UUID]
) -> Optional[VacationEntry]:
    """Return a single entry owned by the user, or None."""
    return (
        db.query(VacationEntry)
        .filter(
            VacationEntry.id == _to_uuid(entry_id),
            VacationEntry.user_id == _to_uuid(user_id),
        )
        .first()
    )


def get_by_date(
    db: Session, user_id: Union[str, UUID], d: date_type
) -> Optional[VacationEntry]:
    """Return the entry for a specific date, or None."""
    return (
        db.query(VacationEntry)
        .filter(
            VacationEntry.user_id == _to_uuid(user_id),
            VacationEntry.date == d,
        )
        .first()
    )


def get_by_year(
    db: Session, user_id: Union[str, UUID], year: int
) -> List[VacationEntry]:
    """Return all entries for a year, ordered by date."""
    return (
        db.query(VacationEntry)
        .filter(
            VacationEntry.user_id == _to_uuid(user_id),
            VacationEntry.date >= date_type(year, 1, 1),
            VacationEntry.date <= date_type(year, 12, 31),
        )
        .order_by(VacationEntry.date)
        .all()
    )


def get_all(
    db: Session,
    user_id: Union[str, UUID],
    year: Optional[int] = None,
    month: Optional[int] = None,
    entry_type: Optional[VacationEntryType] = None,
) -> List[VacationEntry]:
    """Return entries with optional filters, ordered by date descending."""
    user_id = _to_uuid(user_id)
    query = db.query(VacationEntry).filter(VacationEntry.user_id == user_id)

    if year is not None:
        query = query.filter(
            VacationEntry.date >= date_type(year, 1, 1),
            VacationEntry.date <= date_type(year, 12, 31),
        )
    if month is not None and year is not None:
        query = query.filter(
            VacationEntry.date >= date_type(year, month, 1),
        )
        import calendar
        _, last_day = calendar.monthrange(year, month)
        query = query.filter(
            VacationEntry.date <= date_type(year, month, last_day),
        )
    if entry_type is not None:
        query = query.filter(VacationEntry.entry_type == entry_type)

    return query.order_by(VacationEntry.date.desc()).all()


# ── Validations ───────────────────────────────────────────────────────────────

def _validate_date(db: Session, user_id: UUID, d: date_type) -> None:
    """
    Raise ValueError if the date is invalid for a vacation entry:
    - Weekend (sabato/domenica)
    - Italian national holiday
    - User custom holiday

    Imports are deferred to avoid circular imports.
    """
    # 1. Weekend
    if is_weekend(d):
        raise ValueError("Non è possibile inserire ferie nel weekend")

    # 2. Italian national holidays
    from app.crud import italian_holiday as italian_holiday_crud
    holiday = italian_holiday_crud.get_by_date(db, d)
    if holiday:
        raise ValueError(f"Non è possibile inserire ferie durante: {holiday.name}")

    # 3. User custom holidays
    from app.crud import user_holiday as user_holiday_crud
    user_holidays = user_holiday_crud.get_for_year(db, user_id, d.year)
    for uh in user_holidays:
        uh_date = uh.get_date_for_year(d.year)
        if uh_date == d:
            raise ValueError(f"Non è possibile inserire ferie durante: {uh.name}")


# ── Write ─────────────────────────────────────────────────────────────────────

def create(
    db: Session, user_id: Union[str, UUID], entry: VacationEntryCreate
) -> VacationEntry:
    """
    Create a new vacation entry.

    Validates:
    - No weekend
    - No national holiday
    - No user custom holiday
    - Unique per date (enforced by DB UniqueConstraint)

    Hours logic:
    - Ferie:          automatic from VacationSettings.work_hours_per_day
    - ROL/Permesso:   manual (already validated by schema)
    """
    user_id = _to_uuid(user_id)

    _validate_date(db, user_id, entry.date)

    # Check duplicate date
    if get_by_date(db, user_id, entry.date):
        raise ValueError(f"Esiste già un entry per la data {entry.date}")

    # Determine hours
    if entry.entry_type.value in MANUAL_HOURS_TYPES:
        hours = entry.hours
    else:
        # Ferie: automatic from settings
        from app.crud import vacation_settings as vacation_settings_crud
        settings = vacation_settings_crud.get_or_create(db, user_id)
        hours = settings.work_hours_per_day

    db_entry = VacationEntry(
        user_id=user_id,
        date=entry.date,
        entry_type=entry.entry_type,
        hours=hours,
        notes=entry.notes,
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def create_bulk(
    db: Session,
    user_id: Union[str, UUID],
    entries_data: List[Dict[str, Any]],
) -> List[VacationEntry]:
    """
    Bulk insert pre-validated entries (weekends/holidays already skipped by caller).

    entries_data: list of dicts with keys: date, entry_type, hours, notes
    Skips entries that already exist for the date (idempotent).
    """
    user_id = _to_uuid(user_id)
    created = []
    for data in entries_data:
        db_entry = VacationEntry(
            user_id=user_id,
            date=data["date"],
            entry_type=data["entry_type"],
            hours=data["hours"],
            notes=data.get("notes"),
        )
        db.add(db_entry)
        created.append(db_entry)

    db.commit()
    for entry in created:
        db.refresh(entry)
    return created


def update(
    db: Session,
    entry_id: Union[str, UUID],
    user_id: Union[str, UUID],
    entry_update: VacationEntryUpdate,
) -> Optional[VacationEntry]:
    """
    Partially update an entry (PATCH semantics).
    Returns None if not found.
    """
    db_entry = get(db, entry_id, user_id)
    if db_entry is None:
        return None

    update_data = entry_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_entry, field, value)

    db.commit()
    db.refresh(db_entry)
    return db_entry


def delete(
    db: Session, entry_id: Union[str, UUID], user_id: Union[str, UUID]
) -> bool:
    """Delete an entry. Returns True if deleted, False if not found."""
    db_entry = get(db, entry_id, user_id)
    if db_entry is None:
        return False
    db.delete(db_entry)
    db.commit()
    return True
