"""
Easter date calculator using the Computus algorithm.
Calculates Easter Sunday and Easter Monday (Pasquetta) for any year.
"""
from datetime import date, timedelta


def calculate_easter_sunday(year: int) -> date:
    """
    Calculate Easter Sunday for a given year using the Anonymous Gregorian algorithm.

    This is the most widely used algorithm for calculating Easter,
    valid for years 1583 and later (Gregorian calendar).

    Args:
        year: The year to calculate Easter for (must be >= 1583)

    Returns:
        date: Easter Sunday date

    Raises:
        ValueError: If year < 1583
    """
    if year < 1583:
        raise ValueError("Easter calculation only valid for years >= 1583 (Gregorian calendar)")

    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1

    return date(year, month, day)


def calculate_easter_monday(year: int) -> date:
    """
    Calculate Easter Monday (Pasquetta) for a given year.

    Easter Monday is the day after Easter Sunday.

    Args:
        year: The year to calculate for

    Returns:
        date: Easter Monday date
    """
    easter_sunday = calculate_easter_sunday(year)
    return easter_sunday + timedelta(days=1)


def get_easter_dates(year: int) -> dict:
    """
    Get both Easter Sunday and Monday for a year.

    Args:
        year: The year to calculate for

    Returns:
        dict with 'sunday' and 'monday' dates
    """
    sunday = calculate_easter_sunday(year)
    return {
        "sunday": sunday,
        "monday": sunday + timedelta(days=1)
    }
