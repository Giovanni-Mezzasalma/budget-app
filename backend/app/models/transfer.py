"""
Transfer Model
Gestisce trasferimenti tra account
"""
from sqlalchemy import Column, String, Numeric, Date, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from ..database import Base


class Transfer(Base):
    """Modello Transfer per movimenti tra account"""
    
    __tablename__ = "transfers"
    
    # Primary Key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Foreign Keys
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    from_account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False)
    to_account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False)
    
    # Transfer details
    amount = Column(Numeric(12, 2), nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String(255))
    
    # Timestamp
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="transfers")
    from_account = relationship(
        "Account",
        foreign_keys=[from_account_id],
        back_populates="transfers_from"
    )
    to_account = relationship(
        "Account",
        foreign_keys=[to_account_id],
        back_populates="transfers_to"
    )
    
    # Constraints
    __table_args__ = (
        CheckConstraint('from_account_id != to_account_id', name='different_accounts'),
        CheckConstraint('amount > 0', name='amount_positive'),
    )
    
    def __repr__(self):
        return f"<Transfer {self.amount} on {self.date}>"
