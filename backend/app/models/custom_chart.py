"""
CustomChart Model
Gestisce grafici personalizzati utente
"""
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from ..database import Base
# Import ChartType dallo schema per evitare duplicazione
from ..schemas.custom_chart import ChartType


class CustomChart(Base):
    """Modello CustomChart per grafici salvati"""
    
    __tablename__ = "custom_charts"
    
    # Primary Key    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Foreign Key
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Chart details
    name = Column(String(100), nullable=False)
    chart_type = Column(SQLEnum(ChartType), nullable=False)
    
    # Configuration (JSONB per flessibilità)
    config = Column(JSONB, nullable=False)
    filters = Column(JSONB)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="custom_charts")
    
    def __repr__(self):
        return f"<CustomChart {self.name} ({self.chart_type})>"