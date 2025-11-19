"""
Category Model
Gestisce categorie per transazioni
"""
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum
from ..database import Base


class TransactionType(str, enum.Enum):
    """Tipi di transazione"""
    INCOME = "income"
    EXPENSE = "expense"


class Category(Base):
    """Modello Category per categorizzazione transazioni"""
    
    __tablename__ = "categories"
    
    # Primary Key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Foreign Keys
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    parent_category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id", ondelete="SET NULL"))
    
    # Category details
    name = Column(String(100), nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    
    # Customization
    color = Column(String(7))  # HEX color
    icon = Column(String(50))
    
    # System category (non eliminabile/modificabile)
    is_system = Column(Boolean, default=False)
    
    # Timestamp
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="categories")
    parent_category = relationship("Category", remote_side=[id], backref="subcategories")
    transactions = relationship("Transaction", back_populates="category")
    
    def __repr__(self):
        return f"<Category {self.name} ({self.type})>"
