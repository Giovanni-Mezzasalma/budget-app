"""
Bridge days (ponti) calculator for Italian holidays.
Identifies opportunities to maximize days off with minimal vacation days.
"""
from datetime import date, timedelta
from typing import List, Dict, Any, Set


ITALIAN_WEEKDAYS = [
    "Lunedì", "Martedì", "Mercoledì", "Giovedì",
    "Venerdì", "Sabato", "Domenica"
]

ITALIAN_MONTHS = {
    1: "Gennaio", 2: "Febbraio", 3: "Marzo", 4: "Aprile",
    5: "Maggio", 6: "Giugno", 7: "Luglio", 8: "Agosto",
    9: "Settembre", 10: "Ottobre", 11: "Novembre", 12: "Dicembre"
}


def get_italian_weekday(d: date) -> str:
    """Get Italian weekday name."""
    return ITALIAN_WEEKDAYS[d.weekday()]


def is_weekend(d: date) -> bool:
    """Check if date is Saturday (5) or Sunday (6)."""
    return d.weekday() >= 5


def find_bridge_opportunities(
    holidays: List[Any],
    year: int,
    user_holidays: List[Any] = None
) -> List[Dict]:
    """
    Find bridge day opportunities for a given year.

    A "ponte" (bridge) is when a holiday falls on Tuesday or Thursday,
    allowing to take Monday or Friday off to create a 4-day weekend.

    VALIDAZIONE: Verifica che il bridge_date non sia:
    - Un weekend
    - Già una festività (nazionale o utente)

    Args:
        holidays: List of ItalianHoliday objects for the year
        year: Year to analyze
        user_holidays: Optional list of UserHoliday objects

    Returns:
        List of bridge opportunities sorted by efficiency
    """
    opportunities = []

    # Build set of all holiday dates for quick lookup
    holiday_dates: Set[date] = set()
    for holiday in holidays:
        if holiday.date.year == year:
            holiday_dates.add(holiday.date)

    # Add user holidays to the set
    if user_holidays:
        for uh in user_holidays:
            uh_date = uh.get_date_for_year(year)
            if uh_date:
                holiday_dates.add(uh_date)

    for holiday in holidays:
        if holiday.date.year != year:
            continue

        weekday = holiday.date.weekday()

        # Tuesday holiday (weekday=1): Monday is a bridge → 4 days off with 1 day
        if weekday == 1:
            bridge_date = holiday.date - timedelta(days=1)
            # Skip if bridge is weekend or already a holiday
            if not is_weekend(bridge_date) and bridge_date not in holiday_dates:
                opportunities.append({
                    "holiday_name": holiday.name,
                    "holiday_date": holiday.date.isoformat(),
                    "holiday_weekday": "Martedì",
                    "bridge_date": bridge_date.isoformat(),
                    "bridge_weekday": "Lunedì",
                    "vacation_days_needed": 1,
                    "total_days_off": 4,  # Sat + Sun + Mon + Tue
                    "efficiency": 4.0,
                    "description": f"Ponte {holiday.name}: prendi Lunedì {bridge_date.strftime('%d/%m')}"
                })

        # Thursday holiday (weekday=3): Friday is a bridge → 4 days off with 1 day
        elif weekday == 3:
            bridge_date = holiday.date + timedelta(days=1)
            # Skip if bridge is weekend or already a holiday
            if not is_weekend(bridge_date) and bridge_date not in holiday_dates:
                opportunities.append({
                    "holiday_name": holiday.name,
                    "holiday_date": holiday.date.isoformat(),
                    "holiday_weekday": "Giovedì",
                    "bridge_date": bridge_date.isoformat(),
                    "bridge_weekday": "Venerdì",
                    "vacation_days_needed": 1,
                    "total_days_off": 4,  # Thu + Fri + Sat + Sun
                    "efficiency": 4.0,
                    "description": f"Ponte {holiday.name}: prendi Venerdì {bridge_date.strftime('%d/%m')}"
                })

        # Wednesday holiday (weekday=2): can bridge both sides → 5 days off with 2 days
        elif weekday == 2:
            mon = holiday.date - timedelta(days=2)
            tue = holiday.date - timedelta(days=1)
            thu = holiday.date + timedelta(days=1)
            fri = holiday.date + timedelta(days=2)

            # Check which side is available
            mon_tue_available = (
                not is_weekend(mon) and mon not in holiday_dates and
                not is_weekend(tue) and tue not in holiday_dates
            )
            thu_fri_available = (
                not is_weekend(thu) and thu not in holiday_dates and
                not is_weekend(fri) and fri not in holiday_dates
            )

            # Create separate opportunities for each side
            if mon_tue_available:
                opportunities.append({
                    "holiday_name": holiday.name,
                    "holiday_date": holiday.date.isoformat(),
                    "holiday_weekday": "Mercoledì",
                    "bridge_date": mon.isoformat(),
                    "bridge_weekday": "Lunedì + Martedì",
                    "vacation_days_needed": 2,
                    "total_days_off": 5,
                    "efficiency": 2.5,
                    "description": f"Ponte prima di {holiday.name}: prendi Lunedì e Martedì per 5 giorni di riposo"
                })

            if thu_fri_available:
                opportunities.append({
                    "holiday_name": holiday.name,
                    "holiday_date": holiday.date.isoformat(),
                    "holiday_weekday": "Mercoledì",
                    "bridge_date": thu.isoformat(),
                    "bridge_weekday": "Giovedì + Venerdì",
                    "vacation_days_needed": 2,
                    "total_days_off": 5,
                    "efficiency": 2.5,
                    "description": f"Ponte dopo {holiday.name}: prendi Giovedì e Venerdì per 5 giorni di riposo"
                })

    # Sort by efficiency (best opportunities first)
    opportunities.sort(key=lambda x: (-x["efficiency"], x["holiday_date"]))

    return opportunities
