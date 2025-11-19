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

__all__ = [
    "get_user_by_email",
    "get_user_by_id",
    "create_user",
    "authenticate_user",
    "update_user",
    "delete_user",
    "deactivate_user",
]
