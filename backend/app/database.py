"""
Configurazione database e sessione SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Engine SQLAlchemy
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # Verifica connessione prima di usarla
    pool_size=10,  # Numero connessioni nel pool
    max_overflow=20  # Connessioni extra se necessario
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class per modelli
Base = declarative_base()


# Dependency per ottenere sessione database
def get_db():
    """
    Dependency che fornisce sessione database
    Si chiude automaticamente dopo uso
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
