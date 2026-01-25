"""
Custom Chart Schemas
Custom Chart Data Validation

Note: The ChartType enum is defined here and imported from the model to avoid duplication.
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum
from uuid import UUID


class ChartType(str, Enum):
    """
    Available chart types.

    This enum is the source of truth and is also imported from the SQLAlchemy model.
    """
    LINE = "line"
    BAR = "bar"
    PIE = "pie"
    AREA = "area"


class CustomChartBase(BaseModel):
    """Basic custom chart scheme"""
    name: str = Field(..., min_length=1, max_length=100, description="Nome del grafico")
    chart_type: ChartType = Field(..., description="Tipo di grafico")
    config: Dict[str, Any] = Field(..., description="Configurazione grafico (JSON)")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filtri applicati (JSON)")


class CustomChartCreate(CustomChartBase):
    """Custom chart creation scheme"""
    pass


class CustomChartUpdate(BaseModel):
    """Custom chart update scheme"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    chart_type: Optional[ChartType] = None
    config: Optional[Dict[str, Any]] = None
    filters: Optional[Dict[str, Any]] = None


class CustomChartResponse(CustomChartBase):
    """Custom chart response scheme"""
    id: UUID = Field(..., description="Chart unique identifier")
    user_id: UUID = Field(..., description="Owner user ID")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    class Config:
        from_attributes = True