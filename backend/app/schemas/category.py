"""
Category-related Pydantic schemas for request/response validation.

Struttura gerarchica:
- type: macro categoria (income, expense_necessity, expense_extra)
- parent_id: riferimento alla categoria padre (per sottocategorie)
"""

from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, Field, field_validator

# Tipi validi per le macro categorie
VALID_CATEGORY_TYPES = ["income", "expense_necessity", "expense_extra"]

# Labels per i tipi
CATEGORY_TYPE_LABELS = {
    "income": "Entrate",
    "expense_necessity": "Spese di Necessità",
    "expense_extra": "Spese Extra"
}


class CategoryBase(BaseModel):
    """Base category schema with common fields."""
    name: str = Field(..., min_length=1, max_length=100, description="Category name")
    type: str = Field(..., description="Macro category type: income, expense_necessity, or expense_extra")
    color: Optional[str] = Field(None, max_length=7, description="Hex color code for UI (e.g., #FF5733)")
    icon: Optional[str] = Field(None, max_length=50, description="Icon/emoji for UI")
    parent_id: Optional[UUID] = Field(None, description="Parent category ID for subcategories")
    
    @field_validator('type')
    @classmethod
    def validate_category_type(cls, v: str) -> str:
        """Validate category type."""
        if v.lower() not in VALID_CATEGORY_TYPES:
            raise ValueError(f'Category type must be one of: {", ".join(VALID_CATEGORY_TYPES)}')
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
    type: Optional[str] = Field(None, description="Macro category type")
    color: Optional[str] = Field(None, max_length=7, description="Hex color code")
    icon: Optional[str] = Field(None, max_length=50, description="Icon/emoji")
    parent_id: Optional[UUID] = Field(None, description="Parent category ID")
    is_active: Optional[bool] = Field(None, description="Category active status")
    
    @field_validator('type')
    @classmethod
    def validate_category_type(cls, v: Optional[str]) -> Optional[str]:
        """Validate category type if provided."""
        if v is None:
            return v
        if v.lower() not in VALID_CATEGORY_TYPES:
            raise ValueError(f'Category type must be one of: {", ".join(VALID_CATEGORY_TYPES)}')
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


class CategoryResponse(BaseModel):
    """Schema for category response."""
    id: UUID = Field(..., description="Category unique identifier")
    user_id: UUID = Field(..., description="Owner user ID")
    parent_id: Optional[UUID] = Field(None, description="Parent category ID")
    name: str = Field(..., description="Category name")
    type: str = Field(..., description="Macro category type")
    color: Optional[str] = Field(None, description="Hex color code")
    icon: Optional[str] = Field(None, description="Icon/emoji")
    is_active: bool = Field(default=True, description="Category active status")
    created_at: datetime = Field(..., description="Category creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    
    class Config:
        from_attributes = True


class CategoryWithSubcategories(CategoryResponse):
    """Schema for category response with nested subcategories."""
    subcategories: List["CategoryResponse"] = Field(default=[], description="List of subcategories")
    
    class Config:
        from_attributes = True


class CategoryTreeResponse(BaseModel):
    """Schema for hierarchical category tree organized by type."""
    income: List[CategoryWithSubcategories] = Field(default=[], description="Income categories")
    expense_necessity: List[CategoryWithSubcategories] = Field(default=[], description="Necessity expense categories")
    expense_extra: List[CategoryWithSubcategories] = Field(default=[], description="Extra expense categories")


# Rebuild model per risolvere forward reference
CategoryWithSubcategories.model_rebuild()