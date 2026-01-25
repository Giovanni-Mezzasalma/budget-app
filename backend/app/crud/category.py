"""
Category CRUD Operations
Database operations for Category model with hierarchical structure
"""
from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Union
from uuid import UUID

from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate

def _to_uuid(value: Union[str, UUID, None]) -> Optional[UUID]:
    """Convert string to UUID if necessary."""
    if value is None:
        return None
    if isinstance(value, str):
        return UUID(value)
    return value

def get_categories(
    db: Session,
    user_id: Union[str, UUID],
    skip: int = 0,
    limit: int = 100,
    category_type: Optional[str] = None,
    is_active: Optional[bool] = None,
    parent_id: Optional[Union[str, UUID]] = None,
    only_main: bool = False
) -> List[Category]:
    """
    Lists the user's categories.

    Args:
    db: Database session
    user_id: Owner user ID
    skip: Offset for pagination
    limit: Maximum number of results
    category_type: Filter by type (income, expense_necessity, expense_extra)
    is_active: Filter by active/inactive status
    parent_id: Filter by parent category
    only_main: If True, returns only main categories (no parent)
    """
    user_id = _to_uuid(user_id)
    query = db.query(Category).filter(Category.user_id == user_id)
    
    if category_type is not None:
        query = query.filter(Category.type == category_type)
    
    if is_active is not None:
        query = query.filter(Category.is_active == is_active)
    
    if parent_id is not None:
        parent_id = _to_uuid(parent_id)
        query = query.filter(Category.parent_id == parent_id)
    
    if only_main:
        query = query.filter(Category.parent_id.is_(None))
    
    return query.order_by(Category.name).offset(skip).limit(limit).all()


def get_categories_tree(
    db: Session,
    user_id: Union[str, UUID],
    is_active: Optional[bool] = True
) -> Dict[str, List[Category]]:
    """
    Returns categories organized in a tree by type.

    Returns:
    Dict with keys 'income', 'expense_necessity', 'expense_extra'
    Each value is a list of main categories with populated subcategories
    """
    # Prendi tutte le categorie principali (senza parent)
    main_categories = get_categories(
        db, user_id, 
        is_active=is_active, 
        only_main=True,
        limit=500
    )
    
    # Organizza per tipo
    tree = {
        "income": [],
        "expense_necessity": [],
        "expense_extra": []
    }
    
    for cat in main_categories:
        if cat.type in tree:
            tree[cat.type].append(cat)
    
    return tree


def get_category(
    db: Session,
    category_id: Union[str, UUID],
    user_id: Union[str, UUID]
) -> Optional[Category]:
    """
    Retrieve single category by verifying ownership.
    """
    category_id = _to_uuid(category_id)
    user_id = _to_uuid(user_id)
    return db.query(Category).filter(
        Category.id == category_id,
        Category.user_id == user_id
    ).first()


def get_category_by_id(db: Session, category_id: Union[str, UUID]) -> Optional[Category]:
    """
    Retrieve category by ID (without ownership verification).
    """
    category_id = _to_uuid(category_id)
    return db.query(Category).filter(Category.id == category_id).first()


def create_category(
    db: Session,
    category: CategoryCreate,
    user_id: Union[str, UUID]
) -> Category:
    """
    Create new category for user.
    """
    user_id = _to_uuid(user_id)
    parent_id = _to_uuid(category.parent_id) if category.parent_id else None

    db_category = Category(
        user_id=user_id,
        name=category.name,
        type=category.type,
        color=category.color,
        icon=category.icon,
        parent_id=parent_id,
        is_active=True
    )
    
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    
    return db_category


def update_category(
    db: Session,
    category_id: Union[str, UUID],
    category_update: CategoryUpdate,
    user_id: Union[str, UUID]
) -> Optional[Category]:
    """
    Update existing category.
    """
    db_category = get_category(db, category_id, user_id)
    
    if not db_category:
        return None
    
    update_data = category_update.model_dump(exclude_unset=True)
    
    if 'parent_id' in update_data and update_data['parent_id'] is not None:
        update_data['parent_id'] = _to_uuid(update_data['parent_id'])

    for field, value in update_data.items():
        setattr(db_category, field, value)
    
    db.commit()
    db.refresh(db_category)
    
    return db_category


def delete_category(
    db: Session,
    category_id: Union[str, UUID],
    user_id: Union[str, UUID]
) -> bool:
    """
    Delete category (hard delete).
    Delete also all subcategories (cascade).
    """
    db_category = get_category(db, category_id, user_id)
    
    if not db_category:
        return False
    
    db.delete(db_category)
    db.commit()
    
    return True


def deactivate_category(
    db: Session,
    category_id: Union[str, UUID],
    user_id: Union[str, UUID]
) -> Optional[Category]:
    """
    Deactivate category (soft delete).
    """
    db_category = get_category(db, category_id, user_id)
    
    if not db_category:
        return None
    
    db_category.is_active = False
    db.commit()
    db.refresh(db_category)
    
    return db_category


def seed_default_categories(db: Session, user_id: Union[str, UUID]) -> List[Category]:
    """
    Create default categories for a new user.
    Structure based on the Excel file:
    - 3 macro categories (type): Income, Necessary Expenses, Extra Expenses
    - Main categories (parent_id=None)
    - Subcategories (parent_id=category)
    """
    user_id = _to_uuid(user_id)

    created_categories = []
    
    # ========================================================================
    # INCOME
    # ========================================================================
    income_structure = {
        "Reddito": {
            "color": "#10B981",
            "icon": "💰",
            "subcategories": [
                "Reddito Principale",
                "Reddito Secondario"
            ]
        },
        "Affitto": {
            "color": "#3B82F6",
            "icon": "🏠",
            "subcategories": []
        },
        "Vendita": {
            "color": "#8B5CF6",
            "icon": "🏷️",
            "subcategories": []
        },
        "Rimborsi": {
            "color": "#06B6D4",
            "icon": "🔄",
            "subcategories": []
        },
        "Altro Entrate": {
            "color": "#6B7280",
            "icon": "💵",
            "subcategories": []
        }
    }
    
    # ========================================================================
    # NECESSARY EXPENSES
    # ========================================================================
    expense_necessity_structure = {
        "Casa": {
            "color": "#EF4444",
            "icon": "🏠",
            "subcategories": [
                "Mutuo/Affitto",
                "Elettricità",
                "Gas",
                "Acqua",
                "Manutenzione",
                "Tasse",
                "Telefono/Internet",
                "Assicurazione Casa",
                "Spesa/Cibo"
            ]
        },
        "Trasporti": {
            "color": "#F59E0B",
            "icon": "🚗",
            "subcategories": [
                "Rate auto",
                "Assicurazione Auto",
                "Benzina",
                "Manutenzione",
                "Bollo",
                "Pedaggi",
                "Parcheggi",
                "Mezzi pubblici",
                "Multa"
            ]
        },
        "Salute": {
            "color": "#EC4899",
            "icon": "🏥",
            "subcategories": [
                "Medicinali",
                "Polizze",
                "Visite mediche",
                "Sport",
                "Occhiali/Lenti"
            ]
        },
        "Figli": {
            "color": "#8B5CF6",
            "icon": "👶",
            "subcategories": [
                "Scuola",
                "Abbigliamento",
                "Attività extra",
                "Babysitting"
            ]
        },
        "Istruzione": {
            "color": "#3B82F6",
            "icon": "📚",
            "subcategories": [
                "Retta scolastica",
                "Libri scolastici",
                "Formazione"
            ]
        },
        "Altro Necessità": {
            "color": "#6B7280",
            "icon": "📦",
            "subcategories": [
                "Abbigliamento/Calzature",
                "Rate prestito",
                "Rate carta di credito",
                "Una tantum"
            ]
        }
    }
    
    # ========================================================================
    # EXTRA EXPENSES
    # ========================================================================
    expense_extra_structure = {
        "Svago": {
            "color": "#A855F7",
            "icon": "🎭",
            "subcategories": [
                "Ristorazione",
                "Bar",
                "Cinema/Uscite/Eventi",
                "Abbonamenti digitali",
                "Cura personale",
                "Donazioni e Regali",
                "Divertimento",
                "Fumo",
                "Arredamento",
                "Cultura",
                "Viaggi",
                "Shopping"
            ]
        },
        "Animali": {
            "color": "#F97316",
            "icon": "🐾",
            "subcategories": [
                "Cibo",
                "Veterinario"
            ]
        }
    }
    
    # Helper function to create category with subcategories
    def create_category_with_subs(
        name: str, 
        cat_type: str, 
        color: str, 
        icon: str, 
        subcategories: List[str]
    ) -> Category:
        # Create main category
        main_cat = Category(
            user_id=user_id,
            name=name,
            type=cat_type,
            color=color,
            icon=icon,
            parent_id=None,
            is_active=True
        )
        db.add(main_cat)
        db.flush()  # To get the ID
        created_categories.append(main_cat)
        
        # Create subcategories
        for sub_name in subcategories:
            sub_cat = Category(
                user_id=user_id,
                name=sub_name,
                type=cat_type,
                color=color,  # Inherit color from parent
                icon=None,  # Subcategories without icon
                parent_id=main_cat.id,
                is_active=True
            )
            db.add(sub_cat)
            created_categories.append(sub_cat)
        
        return main_cat
    
    # Create all INCOME categories
    for name, data in income_structure.items():
        create_category_with_subs(
            name=name,
            cat_type="income",
            color=data["color"],
            icon=data["icon"],
            subcategories=data["subcategories"]
        )
    
    # Create all EXPENSE_NECESSITY categories
    for name, data in expense_necessity_structure.items():
        create_category_with_subs(
            name=name,
            cat_type="expense_necessity",
            color=data["color"],
            icon=data["icon"],
            subcategories=data["subcategories"]
        )
    
    # Create all EXPENSE_EXTRA categories
    for name, data in expense_extra_structure.items():
        create_category_with_subs(
            name=name,
            cat_type="expense_extra",
            color=data["color"],
            icon=data["icon"],
            subcategories=data["subcategories"]
        )
    
    db.commit()
    
    # Refresh all categories
    for cat in created_categories:
        db.refresh(cat)
    
    return created_categories


def get_category_statistics(
    db: Session,
    user_id: Union[str, UUID]
) -> Dict:
    """
    Returns statistics about the user's categories.
    """
    all_categories = get_categories(db, user_id, limit=500)
    
    stats = {
        "total": len(all_categories),
        "by_type": {
            "income": 0,
            "expense_necessity": 0,
            "expense_extra": 0
        },
        "main_categories": 0,
        "subcategories": 0,
        "active": 0,
        "inactive": 0
    }
    
    for cat in all_categories:
        # Count by type
        if cat.type in stats["by_type"]:
            stats["by_type"][cat.type] += 1
        
        # Count main vs sub
        if cat.parent_id is None:
            stats["main_categories"] += 1
        else:
            stats["subcategories"] += 1
        
        # Count active/inactive
        if cat.is_active:
            stats["active"] += 1
        else:
            stats["inactive"] += 1
    
    return stats