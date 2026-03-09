# This file makes the utils directory a Python package
from app.utils.easter import calculate_easter_sunday, calculate_easter_monday, get_easter_dates
from app.utils.bridge_days import (
    find_bridge_opportunities,
    get_italian_weekday,
    is_weekend,
    ITALIAN_WEEKDAYS,
    ITALIAN_MONTHS
)
from app.utils.vacation_balance import calculate_balance, calculate_monthly_projection
