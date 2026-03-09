"""
Vacation balance calculator with separate tracking per type.

NUOVA ARCHITETTURA:
- Maturazione separata: Ferie (giorni/mese), ROL (ore/mese), Permessi (ore/mese)
- Tracking start date invece di carryover year
- Saldo iniziale opzionale (ferie in giorni, ROL/Permessi in ore)
- Calcolo totali aggregati per vista dashboard

Vista riepilogo:
- Ferie:    maturate Xh / usate Yh / disponibili Zh = Zd
- ROL:      maturate Xh / usate Yh / disponibili Zh = Zd
- Permessi: maturate Xh / usate Yh / disponibili Zh = Zd
- TOTALE:   disponibili Xh = Yd (somma di tutto)
"""
from datetime import date
from typing import Dict, List, Any, Optional
import calendar


def calculate_months_between(start_date: date, end_date: date) -> int:
    """
    Calculate the number of complete months between two dates.

    Examples:
        2025-03-01 to 2026-02-05 = 11 months
        2025-03-15 to 2026-02-05 = 10 months (March not complete)
    """
    months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

    # If we haven't reached the same day in the end month, subtract 1
    if end_date.day < start_date.day:
        months -= 1

    return max(0, months)


def calculate_type_balance(
    type_name: str,
    accrual_per_month: float,
    months_worked: int,
    initial_hours: float,
    entries: List[Any],
    work_hours_per_day: float,
    type_label: str
) -> Dict:
    """
    Calculate balance for a single type (Ferie, ROL, or Permessi).

    Args:
        type_name: "ferie", "rol", or "permesso"
        accrual_per_month: Hours accrued per month (already converted to hours)
        months_worked: Number of months worked since tracking started
        initial_hours: Initial balance in hours
        entries: List of VacationEntry objects for this type
        work_hours_per_day: Hours per work day (for conversion to days)
        type_label: Italian label for display

    Returns:
        Dict with hours and days (accrued, used, available)
    """
    # Accrued
    hours_accrued = initial_hours + (accrual_per_month * months_worked)

    # Used
    hours_used = sum(e.hours for e in entries)

    # Available
    hours_available = hours_accrued - hours_used

    # Convert to days
    days_accrued = hours_accrued / work_hours_per_day
    days_used = hours_used / work_hours_per_day
    days_available = hours_available / work_hours_per_day

    return {
        "type": type_name,
        "label": type_label,
        "hours_accrued": round(hours_accrued, 1),
        "hours_used": round(hours_used, 1),
        "hours_available": round(hours_available, 1),
        "days_accrued": round(days_accrued, 1),
        "days_used": round(days_used, 1),
        "days_available": round(days_available, 1)
    }


def calculate_balance(
    settings: Any,
    entries: List[Any],
    year: int,
    month: Optional[int] = None
) -> Dict:
    """
    Calculate vacation balance for a user with SEPARATE TRACKING per type.

    NUOVA LOGICA:
    1. Calcola mesi lavorati da tracking_start_date
    2. Per ogni tipo (Ferie, ROL, Permessi):
       - Maturato = initial_hours + (accrual_per_month × months_worked)
       - Usato = somma ore entries di quel tipo
       - Disponibile = Maturato - Usato
    3. Totali aggregati per dashboard

    Args:
        settings: VacationSettings object
        entries: List of VacationEntry objects
        year: Year to calculate
        month: Optional month (1-12). If None, calculates up to end of year or current month.

    Returns:
        Dict with complete balance information including:
        - breakdown: List per tipo con ore+giorni (maturate, usate, disponibili)
        - total_hours_available: Somma ore disponibili (tutti i tipi)
        - total_days_available: Somma giorni disponibili (tutti i tipi)
        - tracking_start_date: Data inizio tracciamento
        - months_worked: Mesi lavorati da tracking_start_date
    """
    today = date.today()
    current_year = today.year
    current_month = today.month

    # Determine calculation period
    if month:
        target_month = month
    else:
        target_month = 12 if year < current_year else current_month

    # Calculate target date (last day of target month)
    _, last_day = calendar.monthrange(year, target_month)
    target_date = date(year, target_month, last_day)

    # Calculate months worked from tracking start
    months_worked = calculate_months_between(settings.tracking_start_date, target_date)

    # Separate entries by type
    entries_by_type = {
        "ferie": [e for e in entries if e.date.year == year and e.date.month <= target_month and e.entry_type.value == "ferie"],
        "rol": [e for e in entries if e.date.year == year and e.date.month <= target_month and e.entry_type.value == "rol"],
        "permesso": [e for e in entries if e.date.year == year and e.date.month <= target_month and e.entry_type.value == "permesso"],
    }

    # Get work hours per day
    hours_per_day = settings.work_hours_per_day or 8.0

    # === CALCULATE FERIE ===
    # Convert initial_ferie_DAYS to hours
    initial_ferie_hours = (settings.initial_ferie_days or 0.0) * hours_per_day
    # Convert ferie_DAYS_per_month to hours_per_month
    ferie_accrual_per_month = settings.ferie_days_per_month * hours_per_day

    ferie_data = calculate_type_balance(
        type_name="ferie",
        accrual_per_month=ferie_accrual_per_month,
        months_worked=months_worked,
        initial_hours=initial_ferie_hours,
        entries=entries_by_type["ferie"],
        work_hours_per_day=hours_per_day,
        type_label="Ferie"
    )

    # === CALCULATE ROL ===
    rol_data = calculate_type_balance(
        type_name="rol",
        accrual_per_month=settings.rol_hours_per_month,
        months_worked=months_worked,
        initial_hours=settings.initial_rol_hours or 0.0,
        entries=entries_by_type["rol"],
        work_hours_per_day=hours_per_day,
        type_label="ROL"
    )

    # === CALCULATE PERMESSI ===
    permessi_data = calculate_type_balance(
        type_name="permesso",
        accrual_per_month=settings.permessi_hours_per_month,
        months_worked=months_worked,
        initial_hours=settings.initial_permessi_hours or 0.0,
        entries=entries_by_type["permesso"],
        work_hours_per_day=hours_per_day,
        type_label="Permessi"
    )

    # === BUILD BREAKDOWN ===
    breakdown = [ferie_data, rol_data, permessi_data]

    # === AGGREGATE TOTALS ===
    total_hours_accrued = sum(b["hours_accrued"] for b in breakdown)
    total_hours_used = sum(b["hours_used"] for b in breakdown)
    total_hours_available = sum(b["hours_available"] for b in breakdown)
    total_days_available = sum(b["days_available"] for b in breakdown)

    # === PROJECTED END OF YEAR ===
    months_remaining = 12 - target_month if year == current_year else 0
    ferie_projected = ferie_data["hours_available"] + (ferie_accrual_per_month * months_remaining)
    rol_projected = rol_data["hours_available"] + (settings.rol_hours_per_month * months_remaining)
    permessi_projected = permessi_data["hours_available"] + (settings.permessi_hours_per_month * months_remaining)
    hours_projected_eoy = ferie_projected + rol_projected + permessi_projected
    days_projected_eoy = hours_projected_eoy / hours_per_day

    return {
        "year": year,
        "month": target_month,

        # Tracking info
        "tracking_start_date": settings.tracking_start_date,
        "months_worked": months_worked,

        # Totals (aggregated across all types)
        "total_hours_accrued": round(total_hours_accrued, 1),
        "total_hours_used": round(total_hours_used, 1),
        "total_hours_available": round(total_hours_available, 1),
        "total_days_available": round(total_days_available, 1),

        # Projected end of year
        "hours_projected_eoy": round(hours_projected_eoy, 1),
        "days_projected_eoy": round(days_projected_eoy, 1),

        # Breakdown per type
        "breakdown": breakdown,

        # Settings reference
        "settings": {
            "work_hours_per_day": hours_per_day,
            "ferie_days_per_month": settings.ferie_days_per_month,
            "rol_hours_per_month": settings.rol_hours_per_month,
            "permessi_hours_per_month": settings.permessi_hours_per_month
        }
    }


def calculate_monthly_projection(
    settings: Any,
    entries: List[Any],
    year: int,
    num_months: int = 12
) -> List[Dict]:
    """
    Calculate month-by-month projection for a year.

    Shows cumulative accrued, used, and available hours for each month.

    Args:
        settings: VacationSettings object
        entries: List of VacationEntry objects for the year
        year: Year to project
        num_months: Number of months to project (default 12)

    Returns:
        List of monthly projections
    """
    projections = []

    # Group entries by month (all types combined)
    entries_by_month = {}
    for entry in entries:
        if entry.date.year == year:
            m = entry.date.month
            entries_by_month.setdefault(m, 0.0)
            entries_by_month[m] += entry.hours

    # Calculate cumulative balance
    hours_per_day = settings.work_hours_per_day or 8.0

    # Initial balance (convert ferie days to hours)
    initial_ferie_hours = (settings.initial_ferie_days or 0.0) * hours_per_day
    initial_total = initial_ferie_hours + (settings.initial_rol_hours or 0.0) + (settings.initial_permessi_hours or 0.0)

    # Monthly accrual (convert ferie days to hours)
    ferie_accrual_per_month = settings.ferie_days_per_month * hours_per_day
    monthly_accrual = ferie_accrual_per_month + settings.rol_hours_per_month + settings.permessi_hours_per_month

    cumulative_accrued = initial_total
    cumulative_used = 0.0

    for month in range(1, num_months + 1):
        cumulative_accrued += monthly_accrual
        cumulative_used += entries_by_month.get(month, 0.0)
        balance = cumulative_accrued - cumulative_used

        projections.append({
            "month": month,
            "month_name": ITALIAN_MONTHS[month],
            "hours_accrued_cumulative": round(cumulative_accrued, 1),
            "hours_used_cumulative": round(cumulative_used, 1),
            "hours_available": round(balance, 1),
            "days_available": round(balance / hours_per_day, 1)
        })

    return projections


# Month names
ITALIAN_MONTHS = {
    1: "Gennaio", 2: "Febbraio", 3: "Marzo", 4: "Aprile",
    5: "Maggio", 6: "Giugno", 7: "Luglio", 8: "Agosto",
    9: "Settembre", 10: "Ottobre", 11: "Novembre", 12: "Dicembre"
}
