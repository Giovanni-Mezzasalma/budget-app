"""
Custom Chart CRUD Operations
Database operations per Custom Chart model
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
    Lista tutti i grafici personalizzati dell'utente.
    
    Args:
        db: Database session
        user_id: ID utente proprietario
        skip: Offset per paginazione
        limit: Numero massimo risultati
    
    Returns:
        Lista di CustomChart objects
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
    Recupera singolo grafico verificando ownership.
    
    Args:
        db: Database session
        chart_id: ID grafico da recuperare
        user_id: ID utente (per verifica ownership)
    
    Returns:
        CustomChart object se trovato e appartiene all'utente, None altrimenti
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
    Crea nuovo grafico personalizzato.
    
    Args:
        db: Database session
        chart: Dati grafico da CustomChartCreate schema
        user_id: ID utente proprietario
    
    Returns:
        CustomChart object creato
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
    Aggiorna grafico esistente.
    
    Args:
        db: Database session
        chart_id: ID grafico da aggiornare
        chart_update: Dati da aggiornare
        user_id: ID utente (per verifica ownership)
    
    Returns:
        CustomChart aggiornato se trovato, None altrimenti
    """
    db_chart = get_custom_chart(db, chart_id, user_id)
    
    if not db_chart:
        return None
    
    # Aggiorna solo i campi forniti (exclude_unset=True)
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
    Elimina grafico personalizzato.
    
    Args:
        db: Database session
        chart_id: ID grafico da eliminare
        user_id: ID utente (per verifica ownership)
    
    Returns:
        True se eliminato, False se non trovato
    """
    db_chart = get_custom_chart(db, chart_id, user_id)
    
    if not db_chart:
        return False
    
    db.delete(db_chart)
    db.commit()
    
    return True