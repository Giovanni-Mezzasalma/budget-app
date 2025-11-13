"""
Test Database Connection
Script per verificare connessione a PostgreSQL
"""
import psycopg2
from dotenv import load_dotenv
import os
import sys

# Carica variabili d'ambiente da .env
load_dotenv()


def test_connection():
    """Test connessione al database PostgreSQL"""
    
    print("🔍 Testing database connection...")
    print(f"Host: {os.getenv('DB_HOST')}")
    print(f"Port: {os.getenv('DB_PORT')}")
    print(f"Database: {os.getenv('DB_NAME')}")
    print(f"User: {os.getenv('DB_USER')}")
    print("-" * 50)
    
    try:
        # Tenta connessione
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        
        # Se arriviamo qui, connessione riuscita
        print("✅ Database connection successful!")
        print(f"✅ Connected to: {os.getenv('DB_NAME')}")
        print(f"✅ PostgreSQL version: ", end="")
        
        # Ottieni versione PostgreSQL
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(db_version[0].split(',')[0])
        
        # Chiudi connessione
        cursor.close()
        conn.close()
        
        print("-" * 50)
        print("🎉 All good! Database is ready to use.")
        return True
        
    except psycopg2.OperationalError as e:
        print("❌ Connection failed!")
        print(f"Error: {e}")
        print("-" * 50)
        print("\n🔧 Troubleshooting:")
        print("1. Check if PostgreSQL is running")
        print("2. Verify credentials in .env file")
        print("3. Ensure database 'budget_app_dev' exists in pgAdmin")
        print("4. Check if user has permissions on the database")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)