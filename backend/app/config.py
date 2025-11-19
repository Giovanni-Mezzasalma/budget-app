"""
Configurazione applicazione
Gestisce environment variables e settings globali
"""
from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """Settings globali applicazione"""
    
    # Database
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "budget_app_dev"
    DB_USER: str = "budget_user"
    DB_PASSWORD: str
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080  # 7 giorni
    
    # Application
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]
    
    class Config:
        env_file = ".env"
        extra = "allow"
        case_sensitive = True


# Istanza singola settings
settings = Settings()
