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
]
