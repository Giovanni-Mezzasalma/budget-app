"""
Custom Chart CRUD Operations
Database operations for Custom Chart model
"""
from sqlalchemy.orm import Session
from typing import List, Optional, Union
from uuid import UUID

from app.models.custom_chart import CustomChart
from app.schemas.custom_chart import CustomChartCreate, CustomChartUpdate

def _to_uuid(value: Union[str, UUID, None]) -> Optional[UUID]:
    """Convert string to UUID if necessary."""
    if value is None:
        return None
    if isinstance(value, str):
        return UUID(value)
    return value

def get_custom_charts(
    db: Session,
    user_id: Union[str, UUID],
    skip: int = 0,
    limit: int = 100
) -> List[CustomChart]:
    """
    Lists all the user's custom charts.

    Args:
    db: Database session
    user_id: Owner user ID
    skip: Offset for pagination
    limit: Maximum number of results

    Returns:
    List of CustomChart objects
    """
    user_id = _to_uuid(user_id)
    return db.query(CustomChart).filter(
        CustomChart.user_id == user_id
    ).order_by(CustomChart.created_at.desc()).offset(skip).limit(limit).all()


def get_custom_chart(
    db: Session,
    chart_id: Union[str, UUID],
    user_id: Union[str, UUID]
) -> Optional[CustomChart]:
    """
    Retrieves a single chart, verifying ownership.

    Args:
    db: Database session
    chart_id: Chart ID to retrieve
    user_id: User ID (for verifying ownership)

    Returns:
    CustomChart object if found and owned by the user, None otherwise
    """
    chart_id = _to_uuid(chart_id)
    user_id = _to_uuid(user_id) 
    return db.query(CustomChart).filter(
        CustomChart.id == chart_id,
        CustomChart.user_id == user_id
    ).first()


def create_custom_chart(
    db: Session,
    chart: CustomChartCreate,
    user_id: Union[str, UUID]
) -> CustomChart:
    """
    Create a new custom chart.

    Args:
    db: Database session
    chart: Chart data from CustomChartCreate schema
    user_id: Owner user ID

    Returns:
    CustomChart object created
    """
    user_id = _to_uuid(user_id)
    db_chart = CustomChart(
        user_id=user_id,
        name=chart.name,
        chart_type=chart.chart_type,
        config=chart.config,
        filters=chart.filters
    )
    
    db.add(db_chart)
    db.commit()
    db.refresh(db_chart)
    
    return db_chart


def update_custom_chart(
    db: Session,
    chart_id: Union[str, UUID],
    chart_update: CustomChartUpdate,
    user_id: Union[str, UUID]
) -> Optional[CustomChart]:
    """
    Update existing chart.

    Args:
    db: Database session
    chart_id: Chart ID to update
    chart_update: Data to update
    user_id: User ID (for ownership verification)

    Returns:
    CustomChart updated if found, None otherwise
    """
    db_chart = get_custom_chart(db, chart_id, user_id)
    
    if not db_chart:
        return None
    
    # Update only the provided fields (exclude_unset=True)
    update_data = chart_update.model_dump(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(db_chart, field, value)
    
    db.commit()
    db.refresh(db_chart)
    
    return db_chart


def delete_custom_chart(
    db: Session,
    chart_id: Union[str, UUID],
    user_id: Union[str, UUID]
) -> bool:
    """
    Delete custom chart.

    Args:
    db: Database session
    chart_id: Chart ID to delete
    user_id: User ID (for ownership verification)

    Returns:
    True if deleted, False if not found
    """
    db_chart = get_custom_chart(db, chart_id, user_id)
    
    if not db_chart:
        return False
    
    db.delete(db_chart)
    db.commit()
    
    return True