"""
Pydantic schemas for request/response validation.
"""

from app.schemas.user import (
    UserBase,
    UserCreate,
    UserLogin,
    UserResponse,
    UserUpdate,
    Token,
    TokenData
)

from app.schemas.account import (
    AccountBase,
    AccountCreate,
    AccountUpdate,
    AccountResponse,
    AccountWithStats
)

from app.schemas.category import (
    CategoryBase,
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse
)

from app.schemas.transaction import (
    TransactionBase,
    TransactionCreate,
    TransactionUpdate,
    TransactionResponse,
    TransactionWithDetails
)

from app.schemas.transfer import (
    TransferBase,
    TransferCreate,
    TransferUpdate,
    TransferResponse,
    TransferWithDetails
)

from app.schemas.budget import (
    BudgetCreate,
    BudgetUpdate,
    BudgetResponse,
    BudgetWithStatus,
    BudgetSummaryResponse,
    CategoryInfo,
)

from app.schemas.vacation import (
    VacationSettingsBase,
    VacationSettingsCreate,
    VacationSettingsUpdate,
    VacationSettingsResponse,
    VacationEntryBase,
    VacationEntryCreate,
    VacationEntryUpdate,
    VacationEntryResponse,
    VacationEntryBulkCreate,
    UserHolidayBase,
    UserHolidayCreate,
    UserHolidayResponse,
    ItalianHolidayResponse,
    BreakdownItem,
    VacationBalanceResponse,
    VacationProjectionResponse,
    CalendarDayResponse,
    CalendarMonthResponse,
    BridgeOpportunityResponse,
)

__all__ = [
    # User schemas
    "UserBase",
    "UserCreate",
    "UserLogin",
    "UserResponse",
    "UserUpdate",
    "Token",
    "TokenData",
    
    # Account schemas
    "AccountBase",
    "AccountCreate",
    "AccountUpdate",
    "AccountResponse",
    "AccountWithStats",
    
    # Category schemas
    "CategoryBase",
    "CategoryCreate",
    "CategoryUpdate",
    "CategoryResponse",
    
    # Transaction schemas
    "TransactionBase",
    "TransactionCreate",
    "TransactionUpdate",
    "TransactionResponse",
    "TransactionWithDetails",
    
    # Transfer schemas
    "TransferBase",
    "TransferCreate",
    "TransferUpdate",
    "TransferResponse",
    "TransferWithDetails",

    # Budget schemas
    "BudgetCreate",
    "BudgetUpdate",
    "BudgetResponse",
    "BudgetWithStatus",
    "BudgetSummaryResponse",
    "CategoryInfo",

    # Vacation schemas
    "VacationSettingsBase",
    "VacationSettingsCreate",
    "VacationSettingsUpdate",
    "VacationSettingsResponse",
    "VacationEntryBase",
    "VacationEntryCreate",
    "VacationEntryUpdate",
    "VacationEntryResponse",
    "VacationEntryBulkCreate",
    "UserHolidayBase",
    "UserHolidayCreate",
    "UserHolidayResponse",
    "ItalianHolidayResponse",
    "BreakdownItem",
    "VacationBalanceResponse",
    "VacationProjectionResponse",
    "CalendarDayResponse",
    "CalendarMonthResponse",
    "BridgeOpportunityResponse",
]
