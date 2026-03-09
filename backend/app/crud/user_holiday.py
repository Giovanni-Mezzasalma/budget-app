"""
UserHoliday CRUD Operations.

Manages user-defined custom holidays (patron saint, company closures, etc.).
Each UserHoliday stores day+month (and optionally year for non-recurring).
The model's get_date_for_year() resolves the actual date per year.
"""
from typing import List, Optional, Union
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.user_holiday import UserHoliday
from app.schemas.vacation import UserHolidayCreate


def _to_uuid(value: Union[str, UUID]) -> UUID:
    if isinstance(value, str):
        return UUID(value)
    return value


# ── Read ──────────────────────────────────────────────────────────────────────

def get(
    db: Session, holiday_id: Union[str, UUID], user_id: Union[str, UUID]
) -> Optional[UserHoliday]:
    """Return a single UserHoliday owned by the user, or None."""
    return (
        db.query(UserHoliday)
        .filter(
            UserHoliday.id == _to_uuid(holiday_id),
            UserHoliday.user_id == _to_uuid(user_id),
        )
        .first()
    )


def get_all(db: Session, user_id: Union[str, UUID]) -> List[UserHoliday]:
    """Return all custom holidays for a user, ordered by month/day."""
    return (
        db.query(UserHoliday)
        .filter(UserHoliday.user_id == _to_uuid(user_id))
        .order_by(UserHoliday.month, UserHoliday.day)
        .all()
    )


def get_for_year(
    db: Session, user_id: Union[str, UUID], year: int
) -> List[UserHoliday]:
    """
    Return all UserHoliday records relevant to a given year.

    Includes:
    - recurring=True entries (apply to every year)
    - recurring=False entries where year matches exactly
    """
    return (
        db.query(UserHoliday)
        .filter(
            UserHoliday.user_id == _to_uuid(user_id),
            (UserHoliday.recurring == True) | (UserHoliday.year == year),
        )
        .order_by(UserHoliday.month, UserHoliday.day)
        .all()
    )


# ── Write ─────────────────────────────────────────────────────────────────────

def create(
    db: Session, user_id: Union[str, UUID], holiday_in: UserHolidayCreate
) -> UserHoliday:
    """Create a new user holiday."""
    user_id = _to_uuid(user_id)
    holiday = UserHoliday(
        user_id=user_id,
        day=holiday_in.day,
        month=holiday_in.month,
        name=holiday_in.name,
        recurring=holiday_in.recurring,
        year=holiday_in.year,
    )
    db.add(holiday)
    db.commit()
    db.refresh(holiday)
    return holiday


def delete(
    db: Session, holiday_id: Union[str, UUID], user_id: Union[str, UUID]
) -> bool:
    """Delete a user holiday. Returns True if deleted, False if not found."""
    holiday = get(db, holiday_id, user_id)
    if holiday is None:
        return False
    db.delete(holiday)
    db.commit()
    return True
