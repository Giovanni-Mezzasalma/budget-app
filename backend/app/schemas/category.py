"""
Category-related Pydantic schemas for request/response validation.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class CategoryBase(BaseModel):
    """Base category schema with common fields."""
    name: str = Field(..., min_length=1, max_length=100, description="Category name")
    type: str = Field(..., description="Category type: income or expense")
    color: Optional[str] = Field(None, max_length=7, description="Hex color code for UI (e.g., #FF5733)")
    icon: Optional[str] = Field(None, max_length=50, description="Icon name for UI")
    parent_id: Optional[str] = Field(None, description="Parent category ID for subcategories")
    
    @field_validator('type')
    @classmethod
    def validate_category_type(cls, v: str) -> str:
        """Validate category type."""
        allowed_types = ['income', 'expense']
        if v.lower() not in allowed_types:
            raise ValueError(f'Category type must be one of: {", ".join(allowed_types)}')
        return v.lower()
    
    @field_validator('color')
    @classmethod
    def validate_color(cls, v: Optional[str]) -> Optional[str]:
        """Validate hex color format."""
        if v is None:
            return v
        v = v.strip()
        if not v.startswith('#') or len(v) != 7:
            raise ValueError('Color must be in hex format (#RRGGBB)')
        try:
            int(v[1:], 16)
        except ValueError:
            raise ValueError('Color must be a valid hex code')
        return v.upper()
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        """Validate and clean category name."""
        v = v.strip()
        if len(v) < 1:
            raise ValueError('Category name cannot be empty')
        return v


class CategoryCreate(CategoryBase):
    """Schema for creating a new category."""
    pass


class CategoryUpdate(BaseModel):
    """Schema for updating an existing category."""
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="Category name")
    type: Optional[str] = Field(None, description="Category type: income or expense")
    color: Optional[str] = Field(None, max_length=7, description="Hex color code")
    icon: Optional[str] = Field(None, max_length=50, description="Icon name")
    parent_id: Optional[str] = Field(None, description="Parent category ID")
    is_active: Optional[bool] = Field(None, description="Category active status")
    
    @field_validator('type')
    @classmethod
    def validate_category_type(cls, v: Optional[str]) -> Optional[str]:
        """Validate category type if provided."""
        if v is None:
            return v
        allowed_types = ['income', 'expense']
        if v.lower() not in allowed_types:
            raise ValueError(f'Category type must be one of: {", ".join(allowed_types)}')
        return v.lower()
    
    @field_validator('color')
    @classmethod
    def validate_color(cls, v: Optional[str]) -> Optional[str]:
        """Validate hex color format if provided."""
        if v is None:
            return v
        v = v.strip()
        if not v.startswith('#') or len(v) != 7:
            raise ValueError('Color must be in hex format (#RRGGBB)')
        try:
            int(v[1:], 16)
        except ValueError:
            raise ValueError('Color must be a valid hex code')
        return v.upper()
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: Optional[str]) -> Optional[str]:
        """Validate and clean category name if provided."""
        if v is None:
            return v
        v = v.strip()
        if len(v) < 1:
            raise ValueError('Category name cannot be empty')
        return v


class CategoryResponse(CategoryBase):
    """Schema for category response."""
    id: str = Field(..., description="Category unique identifier")
    user_id: str = Field(..., description="Owner user ID")
    is_active: bool = Field(default=True, description="Category active status")
    created_at: datetime = Field(..., description="Category creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    
    class Config:
        from_attributes = True
