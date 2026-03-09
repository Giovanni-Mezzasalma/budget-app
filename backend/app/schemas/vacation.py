"""
Vacation-related Pydantic schemas for request/response validation.

UPDATED: Separate accrual rates, tracking start date, aggregated totals
"""
from datetime import date as date_type, datetime
from typing import Optional, List, Dict, Any
from uuid import UUID
from pydantic import BaseModel, Field, field_validator, model_validator

from app.models.vacation_entry import VacationEntryType, MANUAL_HOURS_TYPES


# ==================== VACATION SETTINGS ====================

class VacationSettingsBase(BaseModel):
    """Base schema for vacation settings with separate accrual rates."""
    work_hours_per_day: float = Field(default=8.0, ge=1, le=24)

    # Accrual rates (separate per type!)
    ferie_days_per_month: float = Field(default=1.83, ge=0, le=10,
        description="Days of vacation accrued per month (default 1.83 = 22 days/year)")
    rol_hours_per_month: float = Field(default=2.67, ge=0, le=200,
        description="ROL hours accrued per month (default 2.67 = 32 hours/year)")
    permessi_hours_per_month: float = Field(default=8.67, ge=0, le=200,
        description="Permission hours accrued per month (default 8.67 = 104 hours/year)")

    # Tracking start
    tracking_start_date: date_type = Field(description="Date when tracking started")

    # Initial balance (optional)
    initial_balance_month: Optional[int] = Field(None, ge=1, le=12)
    initial_balance_year: Optional[int] = Field(None, ge=2000, le=2100)
    initial_ferie_days: float = Field(default=0.0, ge=0, description="Initial vacation DAYS")
    initial_rol_hours: float = Field(default=0.0, ge=0, description="Initial ROL hours")
    initial_permessi_hours: float = Field(default=0.0, ge=0, description="Initial permission hours")

    @field_validator('tracking_start_date')
    @classmethod
    def tracking_start_not_future(cls, v):
        if v > date_type.today():
            raise ValueError('Tracking start date cannot be in the future')
        return v

    @field_validator('initial_balance_year')
    @classmethod
    def initial_balance_before_tracking(cls, v, info):
        if v and 'initial_balance_month' in info.data and 'tracking_start_date' in info.data:
            balance_month = info.data.get('initial_balance_month')
            tracking_start = info.data.get('tracking_start_date')
            if balance_month:
                balance_date = date_type(v, balance_month, 1)
                if balance_date > tracking_start:
                    raise ValueError('Initial balance date must be before or equal to tracking start date')
        return v


class VacationSettingsCreate(VacationSettingsBase):
    """Schema for creating vacation settings."""
    pass


class VacationSettingsUpdate(BaseModel):
    """Schema for updating vacation settings (all fields optional)."""
    work_hours_per_day: Optional[float] = Field(None, ge=1, le=24)
    ferie_days_per_month: Optional[float] = Field(None, ge=0, le=10)
    rol_hours_per_month: Optional[float] = Field(None, ge=0, le=200)
    permessi_hours_per_month: Optional[float] = Field(None, ge=0, le=200)
    tracking_start_date: Optional[date_type] = None
    initial_balance_month: Optional[int] = Field(None, ge=1, le=12)
    initial_balance_year: Optional[int] = Field(None, ge=2000, le=2100)
    initial_ferie_days: Optional[float] = Field(None, ge=0)
    initial_rol_hours: Optional[float] = Field(None, ge=0)
    initial_permessi_hours: Optional[float] = Field(None, ge=0)


class VacationSettingsResponse(VacationSettingsBase):
    """Schema for vacation settings response."""
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ==================== VACATION ENTRY ====================

class VacationEntryBase(BaseModel):
    """Base schema for vacation entry."""
    date: date_type = Field(..., description="Date of the entry")
    entry_type: VacationEntryType = Field(
        default=VacationEntryType.FERIE,
        description="Type: ferie, permesso, rol"
    )
    hours: Optional[float] = Field(
        None,
        gt=0,
        le=24,
        description="Hours (required for ROL/permesso, automatic for ferie)"
    )
    notes: Optional[str] = Field(None, max_length=500)


class VacationEntryCreate(VacationEntryBase):
    """
    Schema for creating vacation entry.

    REGOLE:
    - Ferie: ore automatiche da work_hours_per_day (hours ignorato)
    - ROL/Permesso: hours obbligatorio
    """

    @model_validator(mode='after')
    def validate_hours_for_type(self):
        # For manual types, hours is required.
        # Uses model_validator to handle None default (field_validator skips defaults in Pydantic v2).
        if self.entry_type.value in MANUAL_HOURS_TYPES and self.hours is None:
            raise ValueError(f'Hours is required for {self.entry_type.value}')
        return self


class VacationEntryUpdate(BaseModel):
    """Schema for updating vacation entry (all fields optional)."""
    entry_type: Optional[VacationEntryType] = None
    hours: Optional[float] = Field(None, gt=0, le=24)
    notes: Optional[str] = Field(None, max_length=500)


class VacationEntryResponse(VacationEntryBase):
    """Schema for vacation entry response."""
    id: UUID
    user_id: UUID
    hours: float  # Always present in response
    created_at: datetime
    updated_at: datetime
    day_name: Optional[str] = None
    type_label: Optional[str] = None

    class Config:
        from_attributes = True


class VacationEntryBulkCreate(BaseModel):
    """Schema for creating multiple entries (e.g., a week of vacation)."""
    start_date: date_type
    end_date: date_type
    entry_type: VacationEntryType = VacationEntryType.FERIE
    hours_per_day: Optional[float] = Field(None, gt=0, le=24,
        description="Hours per day (required for ROL/permesso, optional for ferie)")
    skip_weekends: bool = Field(default=True)
    skip_holidays: bool = Field(default=True)
    notes: Optional[str] = Field(None, max_length=500)

    @field_validator('end_date')
    @classmethod
    def end_after_start(cls, v, info):
        if 'start_date' in info.data and v < info.data['start_date']:
            raise ValueError('end_date must be >= start_date')
        return v


# ==================== USER HOLIDAY ====================

class UserHolidayBase(BaseModel):
    """Base schema for user custom holiday."""
    day: int = Field(..., ge=1, le=31)
    month: int = Field(..., ge=1, le=12)
    name: str = Field(..., min_length=1, max_length=100)
    recurring: bool = Field(default=True)
    year: Optional[int] = Field(None, ge=2000, le=2100)


class UserHolidayCreate(UserHolidayBase):
    """Schema for creating user holiday."""

    @model_validator(mode='after')
    def validate_user_holiday(self):
        """Combined validator for year and day/month constraints.
        Uses model_validator to handle None defaults (Pydantic v2 skips
        field_validators for fields that use their default value).
        """
        import calendar

        # year required for non-recurring holidays
        if not self.recurring and self.year is None:
            raise ValueError('year is required for non-recurring holidays')

        # day must be valid for the given month (use leap year 2024 to allow Feb 29)
        max_day = calendar.monthrange(2024, self.month)[1]
        if self.day > max_day:
            raise ValueError(f'Day {self.day} is invalid for month {self.month}')

        return self


class UserHolidayResponse(UserHolidayBase):
    """Schema for user holiday response."""
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ==================== ITALIAN HOLIDAY ====================

class ItalianHolidayResponse(BaseModel):
    """Schema for Italian holiday response."""
    id: UUID
    date: date_type
    name: str
    name_en: Optional[str] = None
    is_fixed: bool
    is_national: bool
    day_name: Optional[str] = None

    class Config:
        from_attributes = True


# ==================== VACATION BALANCE (AGGIORNATO) ====================

class BreakdownItem(BaseModel):
    """Schema for balance breakdown by type WITH available hours."""
    type: str
    label: str
    hours_accrued: float
    hours_used: float
    hours_available: float
    days_accrued: float
    days_used: float
    days_available: float


class VacationBalanceResponse(BaseModel):
    """
    Schema for complete vacation balance with AGGREGATED TOTALS.

    NEW: Shows breakdown per type AND total available across all types
    """
    year: int
    month: int

    # Tracking info
    tracking_start_date: date_type
    months_worked: int

    # AGGREGATED TOTALS (across all types)
    total_hours_accrued: float
    total_hours_used: float
    total_hours_available: float
    total_days_available: float

    # Projected end of year
    hours_projected_eoy: float
    days_projected_eoy: float

    # Breakdown by type (Ferie, ROL, Permessi)
    breakdown: List[BreakdownItem]

    # Settings reference
    settings: Dict[str, float]


class MonthlyProjection(BaseModel):
    """Schema for monthly projection."""
    month: int
    month_name: str
    hours_accrued_cumulative: float
    hours_used_cumulative: float
    hours_available: float
    days_available: float


class VacationProjectionResponse(BaseModel):
    """Schema for full year projection."""
    year: int
    projections: List[MonthlyProjection]


# ==================== CALENDAR ====================

class CalendarDayResponse(BaseModel):
    """Schema for a single day in calendar view."""
    date: date_type
    day_number: int
    day_name: str
    is_weekend: bool
    is_today: bool
    is_holiday: bool
    holiday_name: Optional[str] = None
    is_user_holiday: bool = False
    user_holiday_name: Optional[str] = None
    is_bridge_opportunity: bool = False
    entries: List[VacationEntryResponse] = []
    total_hours: float = 0.0


class CalendarMonthResponse(BaseModel):
    """Schema for monthly calendar view."""
    year: int
    month: int
    month_name: str
    days: List[CalendarDayResponse]
    hours_accrued_this_month: float
    hours_used_this_month: float
    hours_available_end_of_month: float
    days_available_end_of_month: float


# ==================== BRIDGE OPPORTUNITIES ====================

class BridgeOpportunityResponse(BaseModel):
    """Schema for bridge day opportunity."""
    holiday_name: str
    holiday_date: str
    holiday_weekday: str
    bridge_date: Optional[str]
    bridge_weekday: str
    vacation_days_needed: int
    total_days_off: int
    efficiency: float
    description: str
