"""
CRUD operations for User model.
"""

from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password, verify_password
from typing import Optional
from uuid import UUID
from typing import Optional, Union


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """
    Retrieve a user by email address.
    
    Args:
        db: Database session
        email: User email address
        
    Returns:
        User object if found, None otherwise
    """
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: Union[str, UUID]) -> Optional[User]:
    """
    Retrieve a user by ID.
    
    Args:
        db: Database session
        user_id: User unique identifier
        
    Returns:
        User object if found, None otherwise
    """
    if isinstance(user_id, str):
        user_id = UUID(user_id)
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserCreate) -> User:
    """
    Create a new user with hashed password.
    
    Args:
        db: Database session
        user: UserCreate schema with user data
        
    Returns:
        Created User object
        
    Raises:
        ValueError: If email already exists
    """
    # Check if user already exists
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise ValueError(f"User with email {user.email} already exists")
    
    # Hash the password
    hashed_password = hash_password(user.password)
    
    # Create user instance
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        password_hash=hashed_password,
        is_active=True
    )
    
    # Add to database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    """
    Authenticate a user by email and password.
    
    Args:
        db: Database session
        email: User email address
        password: Plain text password
        
    Returns:
        User object if authentication successful, None otherwise
    """
    # Get user by email
    user = get_user_by_email(db, email)
    
    if not user:
        return None
    
    # Check if user is active
    if not user.is_active:
        return None
    
    # Verify password
    if not verify_password(password, user.password_hash):
        return None
    
    return user


def update_user(db: Session, user_id: Union[str, UUID], **kwargs) -> Optional[User]:
    """
    Update user information.
    
    Args:
        db: Database session
        user_id: User unique identifier
        **kwargs: Fields to update (email, full_name, password)
        
    Returns:
        Updated User object if found, None otherwise
    """
    user = get_user_by_id(db, user_id)
    
    if not user:
        return None
    
    # Update fields if provided
    if "email" in kwargs:
        # Check if new email already exists
        if kwargs["email"] != user.email:
            existing = get_user_by_email(db, kwargs["email"])
            if existing:
                raise ValueError(f"Email {kwargs['email']} already in use")
        user.email = kwargs["email"]
    
    if "full_name" in kwargs:
        user.full_name = kwargs["full_name"]
    
    if "password" in kwargs:
        user.password_hash = hash_password(kwargs["password"])
    
    if "is_active" in kwargs:
        user.is_active = kwargs["is_active"]
    
    db.commit()
    db.refresh(user)
    
    return user


def delete_user(db: Session, user_id: Union[str, UUID]) -> bool:
    """
    Delete a user (hard delete).
    
    Args:
        db: Database session
        user_id: User unique identifier
        
    Returns:
        True if user was deleted, False if not found
    """
    user = get_user_by_id(db, user_id)
    
    if not user:
        return False
    
    db.delete(user)
    db.commit()
    
    return True


def deactivate_user(db: Session, user_id: Union[str, UUID]) -> Optional[User]:
    """
    Deactivate a user (soft delete).
    
    Args:
        db: Database session
        user_id: User unique identifier
        
    Returns:
        Updated User object if found, None otherwise
    """
    return update_user(db, user_id, is_active=False)
