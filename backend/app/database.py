"""
SQLAlchemy database and session configuration
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Engine SQLAlchemy
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # Check connection before using it
    pool_size=10,  # Number of connections in the pool
    max_overflow=20  # Extra connections if needed
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


# Dependency to get database session
def get_db():
    """
    Dependency that provides database session
    Automatically closes after use
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
