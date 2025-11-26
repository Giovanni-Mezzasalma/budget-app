"""
CRUD operations package.
"""

from app.crud.user import (
    get_user_by_email,
    get_user_by_id,
    create_user,
    authenticate_user,
    update_user,
    delete_user,
    deactivate_user,
)

from app.crud.account import (
    get_accounts,
    get_account,
    get_account_by_id,
    create_account,
    update_account,
    delete_account,
    deactivate_account,
    update_account_balance,
    get_total_balance,
    get_accounts_summary,
)

from app.crud.category import (
    get_categories,
    get_categories_tree,
    get_category,
    get_category_by_id,
    create_category,
    update_category,
    delete_category,
    deactivate_category,
    seed_default_categories,
    get_category_statistics,
)

from app.crud.transaction import (
    get_transactions,
    get_transaction,
    get_transaction_by_id,
    create_transaction,
    update_transaction,
    delete_transaction,
    get_transaction_summary,
    get_transactions_by_category,
    get_monthly_totals,
)

from app.crud.transfer import (
    get_transfers,
    get_transfer,
    get_transfer_by_id,
    create_transfer,
    update_transfer,
    delete_transfer,
    get_transfers_by_type,
    get_loans_summary,
    get_transfer_statistics,
)

from app.crud.custom_chart import (
    get_custom_charts,
    get_custom_chart,
    create_custom_chart,
    update_custom_chart,
    delete_custom_chart,
)

from app.crud.analytics import (
    calculate_summary,
    calculate_monthly_trend,
    calculate_totals_by_category,
    calculate_totals_by_account,
    calculate_daily_breakdown,
    calculate_year_comparison,
)

__all__ = [
    # User CRUD
    "get_user_by_email",
    "get_user_by_id",
    "create_user",
    "authenticate_user",
    "update_user",
    "delete_user",
    "deactivate_user",
    # Account CRUD
    "get_accounts",
    "get_account",
    "get_account_by_id",
    "create_account",
    "update_account",
    "delete_account",
    "deactivate_account",
    "update_account_balance",
    "get_total_balance",
    "get_accounts_summary",
    # Category CRUD
    "get_categories",
    "get_categories_tree",
    "get_category",
    "get_category_by_id",
    "create_category",
    "update_category",
    "delete_category",
    "deactivate_category",
    "seed_default_categories",
    "get_category_statistics",
    # Transaction CRUD
    "get_transactions",
    "get_transaction",
    "get_transaction_by_id",
    "create_transaction",
    "update_transaction",
    "delete_transaction",
    "get_transaction_summary",
    "get_transactions_by_category",
    "get_monthly_totals",
    # Transfer CRUD
    "get_transfers",
    "get_transfer",
    "get_transfer_by_id",
    "create_transfer",
    "update_transfer",
    "delete_transfer",
    "get_transfers_by_type",
    "get_loans_summary",
    "get_transfer_statistics",
    # Custom Chart CRUD
    "get_custom_charts",
    "get_custom_chart",
    "create_custom_chart",
    "update_custom_chart",
    "delete_custom_chart",
    # Analytics
    "calculate_summary",
    "calculate_monthly_trend",
    "calculate_totals_by_category",
    "calculate_totals_by_account",
    "calculate_daily_breakdown",
    "calculate_year_comparison",
]