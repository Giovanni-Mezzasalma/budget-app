"""
Categories Router
User transaction category management with hierarchical structure
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas.category import (
    CategoryCreate, 
    CategoryUpdate, 
    CategoryResponse,
    CategoryWithSubcategories,
    CategoryTreeResponse,
    VALID_CATEGORY_TYPES
)
from app.crud import category as category_crud
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=List[CategoryResponse])
async def get_categories(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Numero di record da saltare"),
    limit: int = Query(100, ge=1, le=500, description="Numero massimo di risultati"),
    type: Optional[str] = Query(None, description="Filtra per tipo: income, expense_necessity, expense_extra"),
    is_active: Optional[bool] = Query(None, description="Filtra per stato attivo/inattivo"),
    parent_id: Optional[str] = Query(None, description="Filtra per categoria padre"),
    only_main: bool = Query(False, description="Se true, restituisce solo categorie principali (senza parent)")
):
    """
    Lists all categories for the current user.

    - **skip**: Offset for pagination (default: 0)
    - **limit**: Maximum number of results (default: 100, max: 500)
    - **type**: Filter by macro category (income, expense_necessity, expense_extra)
    - **is_active**: Filter only active (true) or inactive (false)
    - **parent_id**: Filter subcategories of a specific category
    - **only_main**: If true, excludes subcategories
    """
    # Valida il tipo se fornito
    if type is not None and type not in VALID_CATEGORY_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid type. Must be one of: {', '.join(VALID_CATEGORY_TYPES)}"
        )
    
    categories = category_crud.get_categories(
        db,
        user_id=str(current_user.id),
        skip=skip,
        limit=limit,
        category_type=type,
        is_active=is_active,
        parent_id=parent_id,
        only_main=only_main
    )
    return categories


@router.get("/tree", response_model=CategoryTreeResponse)
async def get_categories_tree(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    is_active: Optional[bool] = Query(True, description="Filtra per stato attivo/inattivo")
):
    """
    Returns categories organized in a tree by macro category.    
    
    Response structure:
    ```json
    {
        "income": [
            {
                "id": "...",
                "name": "Reddito",
                "subcategories": [
                    {"id": "...", "name": "Reddito Principale"},
                    {"id": "...", "name": "Reddito Secondario"}
                ]
            }
        ],
        "expense_necessity": [...],
        "expense_extra": [...]
    }
    ```
    """
    tree = category_crud.get_categories_tree(
        db,
        user_id=str(current_user.id),
        is_active=is_active
    )
    return tree


@router.get("/statistics")
async def get_categories_statistics(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Returns statistics on the user's categories.

    Response includes:
    - Category total
    - Count by type
    - Parent categories vs. subcategories
    - Active vs. inactive
    """
    stats = category_crud.get_category_statistics(
        db,
        user_id=str(current_user.id)
    )
    return stats


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(
    category: CategoryCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create a new category.

    - **name**: Category name (e.g., "Restaurants", "Bonus")
    - **type**: Category macro (income, expense_necessity, expense_extra)
    - **color**: HEX color for UI (e.g., #3B82F6)
    - **icon**: Icon/emoji for UI
    - **parent_id**: Parent category ID to create a subcategory (optional)

    Example: Subcategory creation:
    ```json
    {
        "name": "Netflix",
        "type": "expense_extra",
        "parent_id": "uuid-della-categoria-Svago"
    }
    ```
    """
    # If parent_id is specified, check that it exists and belongs to the user
    if category.parent_id:
        parent = category_crud.get_category(db, category.parent_id, str(current_user.id))
        if not parent:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Parent category not found"
            )
        # Check that the type is the same as the parent
        if parent.type != category.type:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Category type must match parent category type ({parent.type})"
            )
        # Check that the parent is not already a subcategory (max 2 levels)
        if parent.parent_id is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot create subcategory of a subcategory. Maximum depth is 2 levels."
            )
    
    return category_crud.create_category(
        db,
        category=category,
        user_id=str(current_user.id)
    )


@router.get("/{category_id}", response_model=CategoryWithSubcategories)
async def get_category(
    category_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Retrieve details of a single category with its subcategories.
    """
    category = category_crud.get_category(
        db,
        category_id=category_id,
        user_id=str(current_user.id)
    )
    
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    return category


@router.put("/{category_id}", response_model=CategoryResponse)
async def update_category(
    category_id: str,
    category_update: CategoryUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Update an existing category.

    You can only update the fields you want to change.

    ⚠️ If you change the "type", all subcategories will be updated accordingly.
    """
    # Check category existence
    existing = category_crud.get_category(db, category_id, str(current_user.id))
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    # If updating parent_id, check validity
    if category_update.parent_id is not None:
        # It can't be himself
        if category_update.parent_id == category_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category cannot be its own parent"
            )
        
        parent = category_crud.get_category(db, category_update.parent_id, str(current_user.id))
        if not parent:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Parent category not found"
            )
        
        # Make sure that no loop is created
        if parent.parent_id == category_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot set parent to a subcategory of this category"
            )
    
    # If you change the type, also update the subcategories
    if category_update.type is not None and category_update.type != existing.type:
        for sub in existing.subcategories:
            sub.type = category_update.type
    
    updated_category = category_crud.update_category(
        db,
        category_id=category_id,
        category_update=category_update,
        user_id=str(current_user.id)
    )
    
    return updated_category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: str,
    force: bool = Query(False, description="Se true, elimina anche se ha transazioni associate"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Delete a category.

    ⚠️ **Warning**:
    - Also deletes all subcategories.
    - By default, you cannot delete categories with associated transactions.
    - Use `force=true` to force the deletion (the transactions will be orphaned).

    💡 Consider deactivating the category instead of deleting it.
    """
    # Check if the category exists
    category = category_crud.get_category(db, category_id, str(current_user.id))
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    # Check if there are associated transactions (including subcategories)
    has_transactions = len(category.transactions) > 0
    for sub in category.subcategories:
        if len(sub.transactions) > 0:
            has_transactions = True
            break
    
    if has_transactions and not force:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot delete category with existing transactions. Use force=true or deactivate instead."
        )
    
    success = category_crud.delete_category(
        db,
        category_id=category_id,
        user_id=str(current_user.id)
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    return None


@router.post("/{category_id}/deactivate", response_model=CategoryResponse)
async def deactivate_category(
    category_id: str,
    include_subcategories: bool = Query(True, description="Se true, disattiva anche le sottocategorie"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Deactivates a category (soft delete).

    The category will not be deleted but will be hidden from the lists.
    It can be reactivated with PUT by setting is_active=true.

    - **include_subcategories**: If true (default), also deactivates all subcategories.
    """
    category = category_crud.get_category(db, category_id, str(current_user.id))
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    # Disable subcategories if required
    if include_subcategories:
        for sub in category.subcategories:
            sub.is_active = False
    
    deactivated = category_crud.deactivate_category(
        db,
        category_id=category_id,
        user_id=str(current_user.id)
    )
    
    return deactivated


@router.post("/seed-defaults", response_model=List[CategoryResponse])
async def seed_default_categories(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create default categories for the user.

    Structure based on:
    - **Income**: Income, Rent, Sales, Reimbursements, Other
    - **Necessary Expenses**: Housing, Transportation, Health, Children, Education, Other
    - **Extra Expenses**: Entertainment, Pets

    Each main category has its own subcategories.

    ⚠️ Only works if the user doesn't have any categories yet.
    """
    # Verifica se l'utente ha già categorie
    existing = category_crud.get_categories(db, str(current_user.id), limit=1)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already has categories. Delete them first if you want to reset."
        )
    
    categories = category_crud.seed_default_categories(db, str(current_user.id))
    return categories


@router.delete("/all", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_categories(
    confirm: bool = Query(..., description="Conferma eliminazione (deve essere true)"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Deletes ALL user categories.

    ⚠️ **WARNING**: This operation is irreversible!

    Useful for resetting and recreating default categories.
    Requires `confirm=true` as a parameter.
    """
    if not confirm:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You must confirm deletion by setting confirm=true"
        )
    
    # Get all user categories
    all_categories = category_crud.get_categories(
        db, 
        str(current_user.id), 
        limit=1000
    )
    
    # Check if any category has transactions
    for cat in all_categories:
        if len(cat.transactions) > 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Cannot delete all categories: '{cat.name}' has transactions associated. Delete transactions first."
            )
    
    # Delete all (subcategories are automatically deleted by cascade)
    for cat in all_categories:
        if cat.parent_id is None:  # Main categories only
            db.delete(cat)
    
    db.commit()
    
    return None