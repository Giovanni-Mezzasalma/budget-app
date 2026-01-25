"""
CustomChart Model
Manages user custom charts
"""
from sqlalchemy import String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import JSONB, UUID as PGUUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid as uuid_lib

from ..database import Base
# Import ChartType dallo schema per evitare duplicazione
from ..schemas.custom_chart import ChartType


class CustomChart(Base):
    """CustomChart template for saved charts"""
    
    __tablename__ = "custom_charts"
    
    # Primary Key    
    id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid_lib.uuid4
    )
    
    # Foreign Key
    user_id: Mapped[uuid_lib.UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    # Chart details
    name = mapped_column(String(100), nullable=False)
    chart_type = mapped_column(SQLEnum(ChartType), nullable=False)
    
    # Configuration (JSONB for flexibility)
    config = mapped_column(JSONB, nullable=False)
    filters = mapped_column(JSONB)
    
    # Timestamps
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="custom_charts")
    
    def __repr__(self):
        return f"<CustomChart {self.name} ({self.chart_type})>"