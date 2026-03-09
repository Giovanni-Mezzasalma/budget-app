"""
VacationSettings CRUD Operations.

One VacationSettings record per user (enforced by DB UniqueConstraint).
get_or_create() is the main entry point — safe to call on every request.
"""
from datetime import date
from sqlalchemy.orm import Session
from typing import Optional, Union
from uuid import UUID

from app.models.vacation_settings import VacationSettings
from app.schemas.vacation import VacationSettingsCreate, VacationSettingsUpdate


def _to_uuid(value: Union[str, UUID]) -> UUID:
    if isinstance(value, str):
        return UUID(value)
    return value


# ── Read ──────────────────────────────────────────────────────────────────────

def get(db: Session, user_id: Union[str, UUID]) -> Optional[VacationSettings]:
    """Return the settings row for a user, or None if not yet created."""
    user_id = _to_uuid(user_id)
    return (
        db.query(VacationSettings)
        .filter(VacationSettings.user_id == user_id)
        .first()
    )


def get_or_create(db: Session, user_id: Union[str, UUID]) -> VacationSettings:
    """
    Return existing settings or create defaults on first access.

    Default values follow Italian labour standards:
        ferie_days_per_month   = 1.83  → ~22 giorni/anno
        rol_hours_per_month    = 2.67  → ~32 ore/anno
        permessi_hours_per_month = 8.67 → ~104 ore/anno
        work_hours_per_day     = 8.0
        tracking_start_date    = today
    """
    user_id = _to_uuid(user_id)
    settings = get(db, user_id)
    if settings is None:
        settings = VacationSettings(
            user_id=user_id,
            work_hours_per_day=8.0,
            ferie_days_per_month=1.83,
            rol_hours_per_month=2.67,
            permessi_hours_per_month=8.67,
            tracking_start_date=date.today(),
            initial_ferie_days=0.0,
            initial_rol_hours=0.0,
            initial_permessi_hours=0.0,
        )
        db.add(settings)
        db.commit()
        db.refresh(settings)
    return settings


# ── Write ─────────────────────────────────────────────────────────────────────

def create(
    db: Session, user_id: Union[str, UUID], settings_in: VacationSettingsCreate
) -> VacationSettings:
    """
    Create settings from a VacationSettingsCreate schema.
    Raises IntegrityError if settings already exist for the user.
    Prefer get_or_create() for idempotent access.
    """
    user_id = _to_uuid(user_id)
    settings = VacationSettings(
        user_id=user_id,
        **settings_in.model_dump(),
    )
    db.add(settings)
    db.commit()
    db.refresh(settings)
    return settings


def update(
    db: Session,
    user_id: Union[str, UUID],
    settings_update: VacationSettingsUpdate,
) -> VacationSettings:
    """
    Partially update settings for a user (PATCH semantics).
    Creates default settings first if none exist.

    Only fields explicitly set in the request body are updated.
    """
    settings = get_or_create(db, user_id)
    update_data = settings_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(settings, field, value)
    db.commit()
    db.refresh(settings)
    return settings


def delete(db: Session, user_id: Union[str, UUID]) -> bool:
    """
    Delete settings for a user. Returns True if deleted, False if not found.
    On CASCADE the DB will handle this automatically when the user is deleted.
    """
    settings = get(db, user_id)
    if settings is None:
        return False
    db.delete(settings)
    db.commit()
    return True
