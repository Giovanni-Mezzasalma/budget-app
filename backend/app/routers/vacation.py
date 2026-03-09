"""
Vacation Router
Vacation planning: settings, entries, balance, calendar, holidays, bridge days.

Endpoints:
  GET/PUT  /vacation/settings
  GET/POST /vacation/entries
  PUT/DELETE /vacation/entries/{id}
  POST     /vacation/entries/bulk
  GET      /vacation/balance
  GET      /vacation/calendar/{year}/{month}
  GET      /vacation/holidays/{year}
  GET      /vacation/bridges/{year}
  GET/POST /vacation/user-holidays
  DELETE   /vacation/user-holidays/{id}
"""
from datetime import date, timedelta
from typing import List, Optional
import calendar as cal_module

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.vacation_entry import MANUAL_HOURS_TYPES, VACATION_ENTRY_TYPE_LABELS, VacationEntryType

from app.crud import vacation_settings as vacation_settings_crud
from app.crud import vacation_entry as vacation_entry_crud
from app.crud import italian_holiday as italian_holiday_crud
from app.crud import user_holiday as user_holiday_crud

from app.schemas.vacation import (
    VacationSettingsUpdate,
    VacationSettingsResponse,
    VacationEntryCreate,
    VacationEntryUpdate,
    VacationEntryResponse,
    VacationEntryBulkCreate,
    VacationBalanceResponse,
    CalendarDayResponse,
    CalendarMonthResponse,
    ItalianHolidayResponse,
    BridgeOpportunityResponse,
    UserHolidayCreate,
    UserHolidayResponse,
)
from app.utils.vacation_balance import calculate_balance
from app.utils.bridge_days import (
    find_bridge_opportunities,
    get_italian_weekday,
    is_weekend,
    ITALIAN_MONTHS,
)

router = APIRouter(prefix="/vacation", tags=["Vacation"])


# ── Helpers ───────────────────────────────────────────────────────────────────

def _enrich_entry(entry) -> VacationEntryResponse:
    """Populate computed fields day_name and type_label on a VacationEntryResponse."""
    resp = VacationEntryResponse.model_validate(entry)
    resp.day_name = get_italian_weekday(entry.date)
    resp.type_label = VACATION_ENTRY_TYPE_LABELS.get(entry.entry_type.value)
    return resp


# ── Settings ──────────────────────────────────────────────────────────────────

@router.get("/settings", response_model=VacationSettingsResponse)
async def get_settings(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get vacation settings for the current user, creating defaults on first access."""
    settings = vacation_settings_crud.get_or_create(db, current_user.id)
    return settings


@router.put("/settings", response_model=VacationSettingsResponse)
async def update_settings(
    settings_update: VacationSettingsUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update vacation settings (partial update)."""
    settings = vacation_settings_crud.update(db, current_user.id, settings_update)
    return settings


# ── Entries ───────────────────────────────────────────────────────────────────

@router.get("/entries", response_model=List[VacationEntryResponse])
async def get_entries(
    year: Optional[int] = Query(None, description="Filter by year"),
    month: Optional[int] = Query(None, ge=1, le=12, description="Filter by month (requires year)"),
    entry_type: Optional[VacationEntryType] = Query(None, description="Filter by type"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List vacation entries with optional filters."""
    entries = vacation_entry_crud.get_all(
        db,
        user_id=current_user.id,
        year=year,
        month=month,
        entry_type=entry_type,
    )
    return [_enrich_entry(e) for e in entries]


@router.post("/entries", response_model=VacationEntryResponse, status_code=status.HTTP_201_CREATED)
async def create_entry(
    entry: VacationEntryCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Create a vacation entry.

    Validations:
    - No weekend
    - No national or user custom holiday
    - One entry per date
    - Ferie: hours automatic from settings; ROL/Permesso: hours required (validated by schema)
    """
    # Ensure holidays are seeded for the year
    italian_holiday_crud.ensure_holidays_exist(db, entry.date.year)

    try:
        db_entry = vacation_entry_crud.create(db, current_user.id, entry)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return _enrich_entry(db_entry)


@router.put("/entries/{entry_id}", response_model=VacationEntryResponse)
async def update_entry(
    entry_id: str,
    entry_update: VacationEntryUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update an existing vacation entry (partial update)."""
    db_entry = vacation_entry_crud.update(db, entry_id, current_user.id, entry_update)
    if db_entry is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entry not found")
    return _enrich_entry(db_entry)


@router.delete("/entries/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entry(
    entry_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a vacation entry."""
    deleted = vacation_entry_crud.delete(db, entry_id, current_user.id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entry not found")


# ── Bulk Entries ──────────────────────────────────────────────────────────────

@router.post(
    "/entries/bulk",
    response_model=List[VacationEntryResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create_bulk_entries(
    bulk: VacationEntryBulkCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create multiple entries for a date range (e.g., a full week of vacation)."""
    # FIX: validate hours_per_day BEFORE any processing
    if bulk.entry_type.value in MANUAL_HOURS_TYPES:
        if bulk.hours_per_day is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"hours_per_day è obbligatorio per {bulk.entry_type.value}",
            )
        hours = bulk.hours_per_day
    else:
        settings = vacation_settings_crud.get_or_create(db, current_user.id)
        hours = bulk.hours_per_day if bulk.hours_per_day else settings.work_hours_per_day

    # Build set of all holiday dates (national + user)
    all_holiday_dates = set()
    if bulk.skip_holidays:
        year = bulk.start_date.year
        holidays = italian_holiday_crud.ensure_holidays_exist(db, year)
        for h in holidays:
            all_holiday_dates.add(h.date)
        user_holidays = user_holiday_crud.get_for_year(db, current_user.id, year)
        for uh in user_holidays:
            uh_date = uh.get_date_for_year(year)
            if uh_date:
                all_holiday_dates.add(uh_date)

    # Build valid entries list
    entries_data = []
    current_date = bulk.start_date
    while current_date <= bulk.end_date:
        if bulk.skip_weekends and is_weekend(current_date):
            current_date += timedelta(days=1)
            continue
        if current_date in all_holiday_dates:
            current_date += timedelta(days=1)
            continue
        if vacation_entry_crud.get_by_date(db, current_user.id, current_date):
            current_date += timedelta(days=1)
            continue
        entries_data.append({
            "date": current_date,
            "entry_type": bulk.entry_type,
            "hours": hours,
            "notes": bulk.notes,
        })
        current_date += timedelta(days=1)

    if not entries_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nessuna data valida nel range (tutte saltate o già presenti)",
        )

    entries = vacation_entry_crud.create_bulk(db, current_user.id, entries_data)
    return [_enrich_entry(e) for e in entries]


# ── Balance ───────────────────────────────────────────────────────────────────

@router.get("/balance", response_model=VacationBalanceResponse)
async def get_balance(
    year: Optional[int] = Query(None, description="Year (default: current year)"),
    month: Optional[int] = Query(None, ge=1, le=12, description="Month (default: current month)"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Get vacation balance with breakdown per type (Ferie/ROL/Permessi) and aggregated totals.
    """
    target_year = year or date.today().year
    settings = vacation_settings_crud.get_or_create(db, current_user.id)
    entries = vacation_entry_crud.get_by_year(db, current_user.id, target_year)
    balance = calculate_balance(settings, entries, year=target_year, month=month)
    return balance


# ── Calendar ──────────────────────────────────────────────────────────────────

@router.get("/calendar/{year}/{month}", response_model=CalendarMonthResponse)
async def get_calendar_month(
    year: int,
    month: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get calendar view for a specific month with holidays, bridge opportunities, and entries."""
    if month < 1 or month > 12:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Month must be 1-12"
        )

    # Holidays
    holidays = italian_holiday_crud.ensure_holidays_exist(db, year)
    holidays_by_date = {h.date: h for h in holidays}

    # User custom holidays
    user_holidays = user_holiday_crud.get_for_year(db, current_user.id, year)
    user_holidays_by_date = {}
    for uh in user_holidays:
        uh_date = uh.get_date_for_year(year)
        if uh_date:
            user_holidays_by_date[uh_date] = uh

    # Bridge opportunities
    bridges = find_bridge_opportunities(holidays, year, user_holidays)
    bridge_dates = set()
    for b in bridges:
        if b["bridge_date"]:
            bridge_dates.add(date.fromisoformat(b["bridge_date"]))

    # OTTIMIZZAZIONE: single query for the full year, then filter by month
    all_entries = vacation_entry_crud.get_by_year(db, current_user.id, year)
    month_entries = [e for e in all_entries if e.date.month == month]
    entries_by_date = {e.date: e for e in month_entries}

    # Build calendar days
    _, num_days = cal_module.monthrange(year, month)
    today = date.today()
    days = []
    hours_used_this_month = 0.0

    for day_num in range(1, num_days + 1):
        current_date = date(year, month, day_num)
        entry = entries_by_date.get(current_date)
        total_hours = 0.0
        entry_responses = []

        if entry:
            total_hours = entry.hours
            hours_used_this_month += total_hours
            entry_responses.append(_enrich_entry(entry))

        holiday = holidays_by_date.get(current_date)
        user_holiday = user_holidays_by_date.get(current_date)

        days.append(CalendarDayResponse(
            date=current_date,
            day_number=day_num,
            day_name=get_italian_weekday(current_date),
            is_weekend=is_weekend(current_date),
            is_today=(current_date == today),
            is_holiday=(holiday is not None),
            holiday_name=holiday.name if holiday else None,
            is_user_holiday=(user_holiday is not None),
            user_holiday_name=user_holiday.name if user_holiday else None,
            is_bridge_opportunity=(current_date in bridge_dates),
            entries=entry_responses,
            total_hours=total_hours,
        ))

    # Balance for end-of-month summary
    settings = vacation_settings_crud.get_or_create(db, current_user.id)
    balance = calculate_balance(settings, all_entries, year, month)
    ferie_accrual = settings.ferie_days_per_month * settings.work_hours_per_day
    total_accrual = ferie_accrual + settings.rol_hours_per_month + settings.permessi_hours_per_month

    return CalendarMonthResponse(
        year=year,
        month=month,
        month_name=ITALIAN_MONTHS[month],
        days=days,
        hours_accrued_this_month=round(total_accrual, 1),
        hours_used_this_month=round(hours_used_this_month, 1),
        hours_available_end_of_month=balance["total_hours_available"],
        days_available_end_of_month=balance["total_days_available"],
    )


# ── Holidays ──────────────────────────────────────────────────────────────────

@router.get("/holidays/{year}", response_model=List[ItalianHolidayResponse])
async def get_holidays(
    year: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get all Italian national holidays for a given year (fixed + Easter Monday)."""
    holidays = italian_holiday_crud.ensure_holidays_exist(db, year)
    result = []
    for h in holidays:
        resp = ItalianHolidayResponse.model_validate(h)
        resp.day_name = get_italian_weekday(h.date)
        result.append(resp)
    return result


# ── Bridge Opportunities ──────────────────────────────────────────────────────

@router.get("/bridges/{year}", response_model=List[BridgeOpportunityResponse])
async def get_bridges(
    year: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get bridge day opportunities for a year, sorted by efficiency."""
    holidays = italian_holiday_crud.ensure_holidays_exist(db, year)
    user_holidays = user_holiday_crud.get_for_year(db, current_user.id, year)
    opportunities = find_bridge_opportunities(holidays, year, user_holidays)
    return opportunities


# ── User Holidays ─────────────────────────────────────────────────────────────

@router.get("/user-holidays", response_model=List[UserHolidayResponse])
async def get_user_holidays(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List all custom holidays for the current user."""
    return user_holiday_crud.get_all(db, current_user.id)


@router.post(
    "/user-holidays",
    response_model=UserHolidayResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user_holiday(
    holiday: UserHolidayCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a custom holiday (patron saint, company closure, etc.)."""
    try:
        return user_holiday_crud.create(db, current_user.id, holiday)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Holiday already exists or invalid data",
        )


@router.delete("/user-holidays/{holiday_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_holiday(
    holiday_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a custom holiday."""
    deleted = user_holiday_crud.delete(db, holiday_id, current_user.id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Holiday not found"
        )
