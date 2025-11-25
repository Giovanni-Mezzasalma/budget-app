"""
Custom Charts Router
Gestione grafici personalizzati utente
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.custom_chart import CustomChartCreate, CustomChartUpdate, CustomChartResponse
from app.crud import custom_chart as custom_chart_crud
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/custom-charts", tags=["Custom Charts"])


@router.get("/", response_model=List[CustomChartResponse])
async def get_custom_charts(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Numero di record da saltare"),
    limit: int = Query(100, ge=1, le=100, description="Numero massimo di risultati")
):
    """
    Lista tutti i grafici personalizzati dell'utente corrente.
    
    - **skip**: Offset per paginazione (default: 0)
    - **limit**: Numero massimo risultati (default: 100, max: 100)
    """
    charts = custom_chart_crud.get_custom_charts(
        db,
        user_id=str(current_user.id),
        skip=skip,
        limit=limit
    )
    return charts


@router.post("/", response_model=CustomChartResponse, status_code=status.HTTP_201_CREATED)
async def create_custom_chart(
    chart: CustomChartCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Crea un nuovo grafico personalizzato.
    
    - **name**: Nome descrittivo del grafico
    - **chart_type**: Tipo di grafico (line, bar, pie, area)
    - **config**: Configurazione completa del grafico (JSON)
    - **filters**: Filtri applicati al grafico (JSON, opzionale)
    
    Esempio config per grafico a linee:
```json
    {
        "dataKey": "amount",
        "xAxisKey": "date",
        "yAxisKey": "amount",
        "color": "#8884d8"
    }
```
    
    Esempio filters:
```json
    {
        "start_date": "2025-01-01",
        "end_date": "2025-12-31",
        "category_id": "uuid-here"
    }
```
    """
    return custom_chart_crud.create_custom_chart(
        db,
        chart=chart,
        user_id=str(current_user.id)
    )


@router.get("/{chart_id}", response_model=CustomChartResponse)
async def get_custom_chart(
    chart_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Recupera i dettagli di un singolo grafico personalizzato.
    """
    chart = custom_chart_crud.get_custom_chart(
        db,
        chart_id=chart_id,
        user_id=str(current_user.id)
    )
    
    if not chart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Custom chart not found"
        )
    
    return chart


@router.put("/{chart_id}", response_model=CustomChartResponse)
async def update_custom_chart(
    chart_id: str,
    chart_update: CustomChartUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Aggiorna un grafico personalizzato esistente.
    
    Puoi aggiornare solo i campi che vuoi modificare.
    """
    updated_chart = custom_chart_crud.update_custom_chart(
        db,
        chart_id=chart_id,
        chart_update=chart_update,
        user_id=str(current_user.id)
    )
    
    if not updated_chart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Custom chart not found"
        )
    
    return updated_chart


@router.delete("/{chart_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_custom_chart(
    chart_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Elimina un grafico personalizzato.
    """
    success = custom_chart_crud.delete_custom_chart(
        db,
        chart_id=chart_id,
        user_id=str(current_user.id)
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Custom chart not found"
        )
    
    return None