"""
Custom Chart Schemas
Validazione dati grafici personalizzati

Nota: ChartType enum è definito qui ed importato dal model per evitare duplicazioni.
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum


class ChartType(str, Enum):
    """
    Tipi di grafici disponibili.
    
    Questo enum è la source of truth ed è importato anche dal model SQLAlchemy.
    """
    LINE = "line"
    BAR = "bar"
    PIE = "pie"
    AREA = "area"


class CustomChartBase(BaseModel):
    """Schema base custom chart"""
    name: str = Field(..., min_length=1, max_length=100, description="Nome del grafico")
    chart_type: ChartType = Field(..., description="Tipo di grafico")
    config: Dict[str, Any] = Field(..., description="Configurazione grafico (JSON)")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filtri applicati (JSON)")


class CustomChartCreate(CustomChartBase):
    """Schema creazione custom chart"""
    pass


class CustomChartUpdate(BaseModel):
    """Schema aggiornamento custom chart"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    chart_type: Optional[ChartType] = None
    config: Optional[Dict[str, Any]] = None
    filters: Optional[Dict[str, Any]] = None


class CustomChartResponse(CustomChartBase):
    """Schema risposta custom chart"""
    id: str = Field(..., description="Chart unique identifier")
    user_id: str = Field(..., description="Owner user ID")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    class Config:
        from_attributes = True