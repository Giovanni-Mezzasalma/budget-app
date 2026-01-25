"""
Script to reset database in development
WARNING: Deletes all data!
"""
from app.database import Base, engine
from app.models import *  # Import all models
import sys


def reset_database():
    """Drop and recreate all tables"""
    print("⚠️  ATTENZIONE: Stai per cancellare TUTTI i dati!")
    confirm = input("Sei sicuro? Scrivi 'RESET' per confermare: ")
    
    if confirm != "RESET":
        print("❌ Operazione annullata")
        return
    
    print("🗑️  Dropping tables...")
    Base.metadata.drop_all(bind=engine)
    
    print("🏗️  Creating tables...")
    Base.metadata.create_all(bind=engine)
    
    print("✅ Database resettato con successo!")


if __name__ == "__main__":
    reset_database()
