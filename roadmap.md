# 🗺️ ROADMAP - Budget App Multi-Utente
## Da Prototipo JavaScript a SaaS con PostgreSQL + Python

**Progetto:** Budget Management Web App  
**Autore:** Giovanni Mezzasalma  
**Data Inizio:** Novembre 2025  
**Stack:** Python FastAPI + PostgreSQL + React  
**Setup:** Python 3.12.4 | pgAdmin 4 | GitHub Desktop | Docker Desktop | VS Code

---

## 📋 INDICE

- [FASE 0: Setup Progetto](#fase-0-setup-progetto-1-giorno)
- [FASE 1: Database Foundation](#fase-1-database-foundation-2-3-giorni)
- [FASE 2: Backend API - Autenticazione](#fase-2-backend-api-autenticazione-3-4-giorni)
- [FASE 3: Backend API - Core Features](#fase-3-backend-api-core-features-4-5-giorni)
- [FASE 4: Testing & Debug](#fase-4-testing-debug-2-giorni)
- [FASE 5: Frontend Integration](#fase-5-frontend-integration-5-7-giorni)
- [FASE 6: Deployment](#fase-6-deployment-3-4-giorni)
- [FASE 7: Sviluppi Futuri](#fase-7-sviluppi-futuri)

**Timeline Totale:** 6-8 settimane lavorando part-time (10-15h/settimana)

---

## ✅ LEGENDA SIMBOLI

- 🎯 = Milestone importante
- 🔧 = Azione da compiere
- 📝 = File da creare
- 🧪 = Test da eseguire
- ⚠️ = Attenzione/punto critico
- 💡 = Suggerimento/best practice
- 🐛 = Possibile bug/problema

---

# FASE 0: Setup Progetto (1 giorno)

## 🎯 Obiettivo
Preparare ambiente di sviluppo, repository Git e struttura progetto.

---

### 0.1 - Configurazione Repository GitHub

#### 0.1.1 - Creazione Repository
- [x] Apri **GitHub Desktop**
- [x] File → New Repository
- [x] Nome: `budget-app`
- [x] Description: `Multi-user budget management web application`
- [x] Local Path: scegli cartella sul tuo Mac
- [x] ✅ Initialize with README
- [x] Git Ignore: Python
- [x] License: MIT (o quella che preferisci)
- [x] Click "Create Repository"
- [x] Publish repository su GitHub

#### 0.1.2 - Configurazione Git
- [x] Apri **VS Code**
- [x] File → Open Folder → seleziona `budget-app`
- [x] Verifica che Git sia attivo (icona source control laterale)

---

### 0.2 - Struttura Cartelle Progetto

#### 0.2.1 - Crea struttura base
- [x] In VS Code, crea le seguenti cartelle:

```
budget-app/
├── backend/              ← Python FastAPI
├── frontend/             ← React (migrazione futura)
├── database/             ← SQL scripts e migrations
├── docs/                 ← Documentazione
└── docker/               ← Docker configs
```

#### 0.2.2 - Comandi per creare struttura
- [x] Apri Terminal in VS Code (View → Terminal)
- [x] Esegui:
```bash
mkdir -p backend frontend database docs docker
touch backend/.gitkeep frontend/.gitkeep database/.gitkeep docs/.gitkeep docker/.gitkeep
```

---

### 0.3 - File Configurazione Progetto

#### 0.3.1 - `.gitignore`
- [x] 📝 Crea file `.gitignore` nella root

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
.venv

# Environment variables
.env
.env.local
.env.*.local

# IDEs
.vscode/settings.json
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Database
*.db
*.sqlite
*.sqlite3
pgdata/

# Logs
*.log
logs/

# Build
dist/
build/
*.egg-info/

# Testing
.pytest_cache/
.coverage
htmlcov/

# Docker
docker-compose.override.yml
```

#### 0.3.2 - `README.md`
- [x] 📝 Aggiorna `README.md`

```markdown
# 💰 Budget App SaaS

App web multi-utente per gestione budget personali.

## 🚀 Tech Stack

**Backend:**
- Python 3.12.4
- FastAPI
- PostgreSQL 16
- SQLAlchemy ORM
- Alembic (migrations)
- JWT Authentication

**Frontend:**
- React 18
- Vite
- TailwindCSS
- Recharts

**DevOps:**
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- Render.com (hosting)

## 📦 Setup Locale

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # macOS
pip install -r requirements.txt
```

### Database
Usare pgAdmin 4 per gestione database

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 🛠️ Development

- **Backend API:** http://localhost:8000
- **Frontend:** http://localhost:5173
- **API Docs:** http://localhost:8000/docs

## 📝 Documentazione

Vedi cartella `/docs` per documentazione completa.
```

#### 0.3.3 - Commit iniziale
- [x] In **GitHub Desktop**:
  - [x] Verifica file nella sezione "Changes"
  - [x] Scrivi commit message: `Initial project setup`
  - [x] Click "Commit to main"
  - [x] Push to origin

---

### 0.4 - Setup Python Virtual Environment

#### 0.4.1 - Creazione venv
- [x] Apri Terminal in VS Code
- [x] Naviga in backend:
```bash
cd backend
```
- [x] Crea virtual environment:
```bash
python3 -m venv venv
```
- [x] Attiva venv:
```bash
source venv/bin/activate
```
- [x] Verifica attivazione (dovresti vedere `(venv)` nel prompt)

#### 0.4.2 - File requirements.txt
- [x] 📝 Crea `backend/requirements.txt`

```txt
# Core Framework
fastapi==0.115.0
uvicorn[standard]==0.32.0

# Database
psycopg2-binary==2.9.10
sqlalchemy==2.0.36
alembic==1.14.0

# Authentication & Security
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.20
bcrypt==4.2.1

# Validation
pydantic==2.10.3
pydantic-settings==2.7.0
email-validator==2.2.0

# CORS
python-dotenv==1.0.1

# Testing
pytest==8.3.4
pytest-asyncio==0.24.0
httpx==0.28.1

# Development
black==24.10.0
flake8==7.1.1
mypy==1.13.0
```

#### 0.4.3 - Installa dipendenze
- [x] Con venv attivo, esegui:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
- [ ] Verifica installazione:
```bash
pip list
```
- [x] Dovresti vedere tutte le librerie elencate

#### 0.4.4 - Commit dependencies
- [x] In **GitHub Desktop**:
  - [x] Commit message: `Add Python dependencies`
  - [x] Commit e push

---

### 0.5 - Setup Database PostgreSQL

#### 0.5.1 - Creazione Database tramite pgAdmin 4
- [x] Apri **pgAdmin 4**
- [x] Connetti al server locale (PostgreSQL 16)
- [x] Click destro su "Databases" → Create → Database
- [x] Nome: `budget_app_dev`
- [x] Owner: postgres (o tuo user)
- [x] Click "Save"
- [x] Verifica che database appaia nella lista

#### 0.5.2 - Creazione User dedicato (opzionale ma consigliato)
- [x] In pgAdmin, espandi il database `budget_app_dev`
- [x] Click destro su "Login/Group Roles" → Create → Login/Group Role
- [x] General tab → Name: `budget_user`
- [x] Definition tab → Password: `scegli_password_sicura`
- [x] Privileges tab → ✅ Can login, ✅ Create databases
- [x] Click "Save"

#### 0.5.3 - Configurazione .env
- [x] 📝 Crea `backend/.env`

```env
# Database
DATABASE_URL=postgresql://budget_user:tua_password@localhost:5432/budget_app_dev
DB_HOST=localhost
DB_PORT=5432
DB_NAME=budget_app_dev
DB_USER=budget_user
DB_PASSWORD=tua_password

# Application
DEBUG=True
SECRET_KEY=genera_stringa_random_minimo_32_caratteri
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# CORS
CORS_ORIGINS=["http://localhost:5173","http://localhost:3000"]

# Server
HOST=0.0.0.0
PORT=8000
```

⚠️ **IMPORTANTE:** Non committare mai `.env`! È già in `.gitignore`

#### 0.5.4 - File .env.example
- [x] 📝 Crea `backend/.env.example` (versione template da committare)

```env
# Database
DATABASE_URL=postgresql://username:password@localhost:5432/budget_app_dev
DB_HOST=localhost
DB_PORT=5432
DB_NAME=budget_app_dev
DB_USER=your_username
DB_PASSWORD=your_password

# Application
DEBUG=True
SECRET_KEY=your_secret_key_min_32_chars
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# CORS
CORS_ORIGINS=["http://localhost:5173","http://localhost:3000"]

# Server
HOST=0.0.0.0
PORT=8000
```

#### 0.5.5 - Test connessione database
- [x] 📝 Crea `backend/test_db_connection.py`

```python
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def test_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        print("✅ Connessione database riuscita!")
        conn.close()
    except Exception as e:
        print(f"❌ Errore connessione: {e}")

if __name__ == "__main__":
    test_connection()
```

- [x] Esegui test:
```bash
python test_db_connection.py
```
- [x] Dovresti vedere: `✅ Connessione database riuscita!`

#### 0.5.6 - Commit database setup
- [x] In **GitHub Desktop**:
  - [x] Aggiungi `.env.example` e `test_db_connection.py`
  - [x] Commit: `Add database configuration`
  - [x] Push

---

### 0.6 - Setup Docker (preparazione futura)

#### 0.6.1 - Crea docker-compose.yml
- [x] 📝 Crea `docker/docker-compose.yml`

```yaml

services:
  db:
    image: postgres:16-alpine
    container_name: budget_app_db
    environment:
      POSTGRES_USER: budget_user
      POSTGRES_PASSWORD: budget_password
      POSTGRES_DB: budget_app_dev
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U budget_user"]
      interval: 10s
      timeout: 5s
      retries: 5

  backend:
    build:
      context: ../backend
      dockerfile: Dockerfile
    container_name: budget_app_backend
    environment:
      - DATABASE_URL=postgresql://budget_user:budget_password@db:5432/budget_app_dev
    ports:
      - "8000:8000"
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - ../backend:/app
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

volumes:
  pgdata:
```

#### 0.6.2 - Crea Dockerfile backend
- [x] 📝 Crea `backend/Dockerfile`

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### 0.6.3 - Commit Docker files
- [x] In **GitHub Desktop**:
  - [x] Commit: `Add Docker configuration`
  - [x] Push

💡 **Nota:** Userai Docker più avanti per deployment. Per ora continua con setup locale.

---

### 0.7 - Documentazione Progetto

#### 0.7.1 - Crea struttura docs
- [x] 📝 Crea `docs/ARCHITECTURE.md`
- [x] 📝 Crea `docs/API_SPEC.md`
- [x] 📝 Crea `docs/DEVELOPMENT.md`

```markdown
# 🏗️ Architettura Sistema

## Overview

Budget App è un'applicazione web multi-tenant per gestione budget personali.

## Componenti

### Backend (Python FastAPI)
- **API REST**: endpoint per tutte le operazioni
- **Autenticazione**: JWT tokens
- **ORM**: SQLAlchemy per gestione database
- **Validazione**: Pydantic schemas

### Database (PostgreSQL)
- **Multi-tenancy**: isolamento dati per utente
- **Schema relazionale**: 
  - users
  - accounts
  - categories
  - transactions
  - transfers
  - custom_charts

### Frontend (React)
- **SPA**: Single Page Application
- **State Management**: React Context + Hooks
- **UI Components**: TailwindCSS
- **Charts**: Recharts

## Data Flow

```
User → Frontend → API (FastAPI) → Database (PostgreSQL)
       ↓
     JWT Auth
       ↓
   User-specific data
```

## Security

- Password hashing (bcrypt)
- JWT tokens (7 giorni)
- HTTPS only (production)
- CORS configurato
- SQL injection protection (SQLAlchemy)
- Rate limiting
```

#### 0.7.2 - Crea API specifications
- [x] 📝 Crea `docs/API_SPEC.md`

```markdown
# 📡 API Specifications

Base URL: `http://localhost:8000/api/v1`

## Authentication

### POST /auth/register
Registrazione nuovo utente

### POST /auth/login
Login e ottenimento JWT token

### GET /auth/me
Recupera profilo utente autenticato

## Accounts

### GET /accounts
Lista tutti gli account dell'utente

### POST /accounts
Crea nuovo account

### PUT /accounts/{id}
Modifica account

### DELETE /accounts/{id}
Elimina account

## Transactions

### GET /transactions
Lista transazioni con filtri

### POST /transactions
Crea nuova transazione

### PUT /transactions/{id}
Modifica transazione

### DELETE /transactions/{id}
Elimina transazione

## Categories

### GET /categories
Lista categorie

### POST /categories
Crea categoria

(continua...)
```

#### 0.7.3 - Commit documentazione
- [x] In **GitHub Desktop**:
  - [x] Commit: `Add project documentation`
  - [x] Push

---

## 🎯 CHECKPOINT FASE 0

Prima di continuare, verifica:

- [x] ✅ Repository GitHub creato e configurato
- [x] ✅ Struttura cartelle progetto completa
- [x] ✅ Python venv creato e attivo
- [x] ✅ Dipendenze Python installate
- [x] ✅ Database PostgreSQL creato in pgAdmin
- [x] ✅ File .env configurato (non committato)
- [x] ✅ Test connessione database passato
- [x] ✅ Docker files preparati
- [x] ✅ Documentazione base creata
- [x] ✅ Tutti i commit pushati su GitHub

**Tempo stimato:** 1 giornata  
**Prossimo:** FASE 1 - Database Foundation

---

# FASE 1: Database Foundation (2-3 giorni)

## 🎯 Obiettivo
Creare schema database completo, modelli SQLAlchemy e sistema di migrations.

---

### 1.1 - Schema Database SQL

#### 1.1.1 - Progettazione schema
- [x] 📝 Crea `database/schema_design.md`

```markdown
# 🗄️ Database Schema Design

## Tabelle

### users
- id (PK, UUID)
- email (UNIQUE, NOT NULL)
- password_hash (NOT NULL)
- full_name
- created_at
- updated_at
- is_active
- last_login

### accounts
- id (PK, UUID)
- user_id (FK → users.id)
- name (NOT NULL)
- account_type (ENUM: checking, savings, credit, cash, investment)
- balance (NUMERIC, default 0)
- currency (default 'EUR')
- color (HEX color)
- icon
- is_active
- created_at
- updated_at

### categories
- id (PK, UUID)
- user_id (FK → users.id)
- name (NOT NULL)
- type (ENUM: income, expense)
- parent_category_id (FK → categories.id, self-referential)
- color (HEX)
- icon
- is_system (boolean, per categorie predefinite)
- created_at

### transactions
- id (PK, UUID)
- user_id (FK → users.id)
- account_id (FK → accounts.id)
- category_id (FK → categories.id)
- amount (NUMERIC, NOT NULL)
- type (ENUM: income, expense)
- date (DATE, NOT NULL)
- description
- notes
- tags (ARRAY of strings)
- created_at
- updated_at

### transfers
- id (PK, UUID)
- user_id (FK → users.id)
- from_account_id (FK → accounts.id)
- to_account_id (FK → accounts.id)
- amount (NUMERIC, NOT NULL)
- date (DATE, NOT NULL)
- description
- created_at

### custom_charts
- id (PK, UUID)
- user_id (FK → users.id)
- name (NOT NULL)
- chart_type (ENUM: line, bar, pie, area)
- config (JSONB, configurazione chart)
- filters (JSONB, filtri applicati)
- created_at
- updated_at

## Indici

- users: email (UNIQUE)
- accounts: user_id, is_active
- categories: user_id, type
- transactions: user_id, date, account_id, category_id
- transfers: user_id, date
- custom_charts: user_id

## Constraints

- ON DELETE CASCADE per tutti i FK user_id
- CHECK constraints per amount > 0
- CHECK per date <= TODAY
```

#### 1.1.2 - Script SQL creazione tabelle
- [x] 📝 Crea `database/01_create_schema.sql`

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create ENUM types
CREATE TYPE account_type_enum AS ENUM ('checking', 'savings', 'credit', 'cash', 'investment');
CREATE TYPE transaction_type_enum AS ENUM ('income', 'expense');
CREATE TYPE chart_type_enum AS ENUM ('line', 'bar', 'pie', 'area');

-- Table: users
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);

-- Table: accounts
CREATE TABLE accounts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    account_type account_type_enum NOT NULL DEFAULT 'checking',
    balance NUMERIC(12, 2) DEFAULT 0.00,
    currency VARCHAR(3) DEFAULT 'EUR',
    color VARCHAR(7),
    icon VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT balance_positive CHECK (balance >= 0)
);

-- Table: categories
CREATE TABLE categories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    type transaction_type_enum NOT NULL,
    parent_category_id UUID REFERENCES categories(id) ON DELETE SET NULL,
    color VARCHAR(7),
    icon VARCHAR(50),
    is_system BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table: transactions
CREATE TABLE transactions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    account_id UUID NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    category_id UUID NOT NULL REFERENCES categories(id) ON DELETE RESTRICT,
    amount NUMERIC(12, 2) NOT NULL,
    type transaction_type_enum NOT NULL,
    date DATE NOT NULL,
    description VARCHAR(255),
    notes TEXT,
    tags TEXT[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT amount_positive CHECK (amount > 0)
);

-- Table: transfers
CREATE TABLE transfers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    from_account_id UUID NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    to_account_id UUID NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    amount NUMERIC(12, 2) NOT NULL,
    date DATE NOT NULL,
    description VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT amount_positive CHECK (amount > 0),
    CONSTRAINT different_accounts CHECK (from_account_id != to_account_id)
);

-- Table: custom_charts
CREATE TABLE custom_charts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    chart_type chart_type_enum NOT NULL,
    config JSONB NOT NULL,
    filters JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_accounts_user_id ON accounts(user_id);
CREATE INDEX idx_accounts_is_active ON accounts(is_active);
CREATE INDEX idx_categories_user_id ON categories(user_id);
CREATE INDEX idx_categories_type ON categories(type);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_date ON transactions(date DESC);
CREATE INDEX idx_transactions_account_id ON transactions(account_id);
CREATE INDEX idx_transactions_category_id ON transactions(category_id);
CREATE INDEX idx_transfers_user_id ON transfers(user_id);
CREATE INDEX idx_transfers_date ON transfers(date DESC);
CREATE INDEX idx_custom_charts_user_id ON custom_charts(user_id);

-- Trigger per aggiornare updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_accounts_updated_at BEFORE UPDATE ON accounts
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_transactions_updated_at BEFORE UPDATE ON transactions
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_custom_charts_updated_at BEFORE UPDATE ON custom_charts
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

#### 1.1.3 - Esegui script in pgAdmin
- [x] Apri **pgAdmin 4**
- [x] Seleziona database `budget_app_dev`
- [x] Click destro → Query Tool
- [x] Apri file `database/01_create_schema.sql`
- [x] Click Execute (⚡️ icona)
- [x] Verifica output: tutte le tabelle create con successo
- [x] Refresh "Schemas" → "Tables" per vedere le nuove tabelle

#### 1.1.4 - Verifica schema creato
- [x] In pgAdmin, espandi `budget_app_dev` → `Schemas` → `public` → `Tables`
- [x] Dovresti vedere:
  - [x] users
  - [x] accounts
  - [x] categories
  - [x] transactions
  - [x] transfers
  - [x] custom_charts

#### 1.1.5 - Script categorie predefinite
- [x] 📝 Crea `database/02_seed_default_categories.sql`

```sql
-- Funzione per inserire categorie predefinite per un nuovo utente
CREATE OR REPLACE FUNCTION seed_default_categories(p_user_id UUID)
RETURNS VOID AS $$
BEGIN
    -- Categorie INCOME
    INSERT INTO categories (user_id, name, type, color, icon, is_system) VALUES
    (p_user_id, 'Stipendio', 'income', '#10B981', '💰', TRUE),
    (p_user_id, 'Freelance', 'income', '#3B82F6', '💼', TRUE),
    (p_user_id, 'Investimenti', 'income', '#8B5CF6', '📈', TRUE),
    (p_user_id, 'Altro reddito', 'income', '#6B7280', '💵', TRUE);
    
    -- Categorie EXPENSE
    INSERT INTO categories (user_id, name, type, color, icon, is_system) VALUES
    (p_user_id, 'Casa', 'expense', '#EF4444', '🏠', TRUE),
    (p_user_id, 'Alimentari', 'expense', '#F59E0B', '🛒', TRUE),
    (p_user_id, 'Trasporti', 'expense', '#14B8A6', '🚗', TRUE),
    (p_user_id, 'Salute', 'expense', '#EC4899', '🏥', TRUE),
    (p_user_id, 'Svago', 'expense', '#8B5CF6', '🎭', TRUE),
    (p_user_id, 'Abbigliamento', 'expense', '#06B6D4', '👕', TRUE),
    (p_user_id, 'Educazione', 'expense', '#3B82F6', '📚', TRUE),
    (p_user_id, 'Tecnologia', 'expense', '#6366F1', '💻', TRUE),
    (p_user_id, 'Altro', 'expense', '#6B7280', '📦', TRUE);
END;
$$ LANGUAGE plpgsql;

-- Esempio di utilizzo (commentato, verrà chiamato dall'API):
-- SELECT seed_default_categories('user-uuid-here');
```

#### 1.1.6 - Esegui script seed
- [x] In pgAdmin, apri ed esegui `database/02_seed_default_categories.sql`
- [x] Verifica che la funzione sia stata creata in `Schemas` → `public` → `Functions`

#### 1.1.7 - Commit database scripts
- [x] In **GitHub Desktop**:
  - [x] Commit: `Add database schema and seed functions`
  - [x] Push

---

### 1.2 - Modelli SQLAlchemy

#### 1.2.1 - Database configuration
- [x] 📝 Crea `backend/app/__init__.py` (vuoto)
- [x] 📝 Crea `backend/app/config.py`

```python
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
        case_sensitive = True


# Istanza singola settings
settings = Settings()
```

#### 1.2.2 - Database connection
- [x] 📝 Crea `backend/app/database.py`

```python
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
```

#### 1.2.3 - Base models
- [x] 📝 Crea `backend/app/models/__init__.py`

```python
"""
SQLAlchemy Models
Importa tutti i modelli per Alembic autogenerate
"""
from .user import User
from .account import Account
from .category import Category
from .transaction import Transaction
from .transfer import Transfer
from .custom_chart import CustomChart

__all__ = [
    "User",
    "Account",
    "Category",
    "Transaction",
    "Transfer",
    "CustomChart"
]
```

#### 1.2.4 - User model
- [x] 📝 Crea `backend/app/models/user.py`

```python
"""
User Model
Gestisce dati utente e autenticazione
"""
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from ..database import Base


class User(Base):
    """Modello User per autenticazione e profilo"""
    
    __tablename__ = "users"
    
    # Primary Key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Autenticazione
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    
    # Profilo
    full_name = Column(String(255))
    
    # Status
    is_active = Column(Boolean, default=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True))
    
    # Relationships
    accounts = relationship("Account", back_populates="user", cascade="all, delete-orphan")
    categories = relationship("Category", back_populates="user", cascade="all, delete-orphan")
    transactions = relationship("Transaction", back_populates="user", cascade="all, delete-orphan")
    transfers = relationship("Transfer", back_populates="user", cascade="all, delete-orphan")
    custom_charts = relationship("CustomChart", back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<User {self.email}>"
```

#### 1.2.5 - Account model
- [x] 📝 Crea `backend/app/models/account.py`

```python
"""
Account Model
Gestisce conti bancari/portafogli utente
"""
from sqlalchemy import Column, String, Numeric, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum
from ..database import Base


class AccountType(str, enum.Enum):
    """Tipi di account disponibili"""
    CHECKING = "checking"
    SAVINGS = "savings"
    CREDIT = "credit"
    CASH = "cash"
    INVESTMENT = "investment"


class Account(Base):
    """Modello Account per conti utente"""
    
    __tablename__ = "accounts"
    
    # Primary Key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Foreign Key
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    # Account details
    name = Column(String(100), nullable=False)
    account_type = Column(Enum(AccountType), default=AccountType.CHECKING, nullable=False)
    balance = Column(Numeric(12, 2), default=0.00)
    currency = Column(String(3), default="EUR")
    
    # Customization
    color = Column(String(7))  # HEX color
    icon = Column(String(50))
    
    # Status
    is_active = Column(Boolean, default=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account", cascade="all, delete-orphan")
    transfers_from = relationship(
        "Transfer",
        foreign_keys="Transfer.from_account_id",
        back_populates="from_account",
        cascade="all, delete-orphan"
    )
    transfers_to = relationship(
        "Transfer",
        foreign_keys="Transfer.to_account_id",
        back_populates="to_account",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<Account {self.name} ({self.account_type})>"
```

#### 1.2.6 - Category model
- [x] 📝 Crea `backend/app/models/category.py`

```python
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
```

#### 1.2.7 - Transaction model
- [x] 📝 Crea `backend/app/models/transaction.py`

```python
"""
Transaction Model
Gestisce entrate e uscite
"""
from sqlalchemy import Column, String, Text, Numeric, Date, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from ..database import Base
from .category import TransactionType


class Transaction(Base):
    """Modello Transaction per movimenti finanziari"""
    
    __tablename__ = "transactions"
    
    # Primary Key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Foreign Keys
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id", ondelete="RESTRICT"), nullable=False)
    
    # Transaction details
    amount = Column(Numeric(12, 2), nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String(255))
    notes = Column(Text)
    
    # Tags per ricerca/filtro
    tags = Column(ARRAY(String))
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="transactions")
    account = relationship("Account", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")
    
    def __repr__(self):
        return f"<Transaction {self.type} {self.amount} on {self.date}>"
```

#### 1.2.8 - Transfer model
- [x] 📝 Crea `backend/app/models/transfer.py`

```python
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
```

#### 1.2.9 - CustomChart model
- [x] 📝 Crea `backend/app/models/custom_chart.py`

```python
"""
CustomChart Model
Gestisce grafici personalizzati utente
"""
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum
from ..database import Base


class ChartType(str, enum.Enum):
    """Tipi di grafici disponibili"""
    LINE = "line"
    BAR = "bar"
    PIE = "pie"
    AREA = "area"


class CustomChart(Base):
    """Modello CustomChart per grafici salvati"""
    
    __tablename__ = "custom_charts"
    
    # Primary Key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Foreign Key
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    # Chart details
    name = Column(String(100), nullable=False)
    chart_type = Column(Enum(ChartType), nullable=False)
    
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
```

#### 1.2.10 - Commit models
- [x] In **GitHub Desktop**:
  - [x] Commit: `Add SQLAlchemy models`
  - [x] Push

---

### 1.3 - Alembic Migrations

#### 1.3.1 - Inizializzazione Alembic
- [x] Nel terminal, assicurati che venv sia attivo
- [x] Naviga in `backend/`:
```bash
cd backend
```
- [ ] Inizializza Alembic:
```bash
alembic init alembic
```
- [x] Dovresti vedere cartella `alembic/` creata

#### 1.3.2 - Configurazione Alembic
- [x] 📝 Modifica `backend/alembic.ini`
- [x] Trova la riga `sqlalchemy.url = ...`
- [x] Cambiala in:
```ini
# sqlalchemy.url = driver://user:pass@localhost/dbname
# Commenta la riga sopra, useremo .env invece
```

- [x] 📝 Modifica `backend/alembic/env.py`
- [x] Sostituisci l'intero contenuto con:

```python
"""
Alembic environment configuration
Gestisce migrations database
"""
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import sys
import os

# Aggiungi parent directory al path per import
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import settings e models
from app.config import settings
from app.database import Base
from app.models import *  # Import tutti i modelli

# Alembic Config object
config = context.config

# Sovrascrivi sqlalchemy.url con quello da .env
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata per autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

#### 1.3.3 - Prima migration
- [x] Genera prima migration:
```bash
alembic revision --autogenerate -m "Initial database schema"
```
- [x] Dovresti vedere messaggio tipo: `Generating .../alembic/versions/xxxx_initial_database_schema.py`
- [x] Apri il file migration generato e verifica contenuto

⚠️ **NOTA:** Se hai già creato le tabelle manualmente con SQL (step 1.1.3), Alembic potrebbe non rilevare cambiamenti. In tal caso:
- Opzione A: Droppa tutte le tabelle in pgAdmin e rifa migration
- Opzione B: Continua con migration vuota (Alembic non cambierà nulla ma terrà traccia versione)

#### 1.3.4 - Applica migration
- [x] Esegui migration:
```bash
alembic upgrade head
```
- [x] Verifica in pgAdmin che sia stata creata tabella `alembic_version`

#### 1.3.5 - Script helper per reset database
- [x] 📝 Crea `backend/reset_db.py` (utile in development)

```python
"""
Script per resettare database in development
ATTENZIONE: Cancella tutti i dati!
"""
from app.database import Base, engine
from app.models import *  # Import tutti i modelli
import sys


def reset_database():
    """Droppa e ricrea tutte le tabelle"""
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
```

#### 1.3.6 - Commit migrations
- [x] In **GitHub Desktop**:
  - [x] Commit: `Add Alembic migrations`
  - [x] Push

---

## 🎯 CHECKPOINT FASE 1

Prima di continuare, verifica:

- [x] ✅ Schema database progettato e documentato
- [x] ✅ Tabelle create in PostgreSQL (via SQL o Alembic)
- [x] ✅ Tutti i modelli SQLAlchemy creati e funzionanti
- [x] ✅ Alembic configurato e prima migration applicata
- [x] ✅ Relazioni tra modelli verificate
- [x] ✅ Funzione seed categorie predefinite creata
- [x] ✅ Database.py e config.py funzionanti
- [x] ✅ Tutti i commit pushati su GitHub

**Test rapido:**
```python
# In Python terminal (con venv attivo)
from app.database import engine, Base
from app.models import User, Account

# Questo non dovrebbe dare errori
Base.metadata.tables.keys()
```

**Tempo stimato:** 2-3 giorni  
**Prossimo:** FASE 2 - Backend API - Autenticazione

---

# FASE 2: Backend API - Autenticazione (3-4 giorni)

## 🎯 Obiettivo
Implementare sistema completo di autenticazione con JWT, registrazione, login e protezione endpoints.

---

### 2.1 - Security Utilities

#### 2.1.1 - Password hashing
- [x] 📝 Crea `backend/app/utils/__init__.py` (vuoto)
- [x] 📝 Crea `backend/app/utils/security.py`

```python
"""
Security utilities
Password hashing e JWT token management
"""
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from typing import Optional
from ..config import settings

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Genera hash password con bcrypt
    
    Args:
        password: Password in chiaro
        
    Returns:
        Password hash
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica password contro hash
    
    Args:
        plain_password: Password da verificare
        hashed_password: Hash salvato nel database
        
    Returns:
        True se password corretta
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Crea JWT access token
    
    Args:
        data: Dict con dati da codificare (user_id, email, etc)
        expires_delta: Durata token (default da settings)
        
    Returns:
        JWT token string
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    return encoded_jwt


def verify_token(token: str) -> Optional[dict]:
    """
    Verifica e decodifica JWT token
    
    Args:
        token: JWT token string
        
    Returns:
        Dict con payload o None se invalido
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None
```

#### 2.1.2 - Commit security utils
- [x] In **GitHub Desktop**:
  - [x] Commit: `Add security utilities`
  - [x] Push

---

### 2.2 - Pydantic Schemas

#### 2.2.1 - Base schemas
- [x] 📝 Crea `backend/app/schemas/__init__.py`

```python
"""
Pydantic Schemas
Validazione input/output API
"""
from .user import UserCreate, UserLogin, UserResponse, Token
from .account import AccountCreate, AccountUpdate, AccountResponse
from .category import CategoryCreate, CategoryUpdate, CategoryResponse
from .transaction import TransactionCreate, TransactionUpdate, TransactionResponse
from .transfer import TransferCreate, TransferResponse

__all__ = [
    "UserCreate", "UserLogin", "UserResponse", "Token",
    "AccountCreate", "AccountUpdate", "AccountResponse",
    "CategoryCreate", "CategoryUpdate", "CategoryResponse",
    "TransactionCreate", "TransactionUpdate", "TransactionResponse",
    "TransferCreate", "TransferResponse"
]
```

#### 2.2.2 - User schemas
- [x] 📝 Crea `backend/app/schemas/user.py`

```python
"""
User Schemas
Validazione dati utente
"""
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import datetime
import uuid


class UserBase(BaseModel):
    """Schema base utente"""
    email: EmailStr


class UserCreate(UserBase):
    """Schema creazione utente"""
    password: str = Field(..., min_length=8, description="Password minimo 8 caratteri")
    full_name: Optional[str] = Field(None, max_length=255)
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        """Valida password strength"""
        if len(v) < 8:
            raise ValueError('Password deve essere almeno 8 caratteri')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password deve contenere almeno un numero')
        if not any(char.isupper() for char in v):
            raise ValueError('Password deve contenere almeno una maiuscola')
        return v


class UserLogin(BaseModel):
    """Schema login"""
    email: EmailStr
    password: str


class UserResponse(UserBase):
    """Schema risposta utente"""
    id: uuid.UUID
    full_name: Optional[str]
    is_active: bool
    created_at: datetime
    last_login: Optional[datetime]
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    """Schema JWT token"""
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class TokenData(BaseModel):
    """Schema dati dentro JWT"""
    user_id: Optional[uuid.UUID] = None
    email: Optional[str] = None
```

#### 2.2.3 - Account schemas (base)
- [x] 📝 Crea `backend/app/schemas/account.py`

```python
"""
Account Schemas
Validazione dati account
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal
import uuid
from ..models.account import AccountType


class AccountBase(BaseModel):
    """Schema base account"""
    name: str = Field(..., min_length=1, max_length=100)
    account_type: AccountType
    currency: str = Field(default="EUR", pattern="^[A-Z]{3}$")
    color: Optional[str] = Field(None, pattern="^#[0-9A-Fa-f]{6}$")
    icon: Optional[str] = Field(None, max_length=50)


class AccountCreate(AccountBase):
    """Schema creazione account"""
    balance: Decimal = Field(default=Decimal("0.00"), ge=0)


class AccountUpdate(BaseModel):
    """Schema aggiornamento account"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    color: Optional[str] = Field(None, pattern="^#[0-9A-Fa-f]{6}$")
    icon: Optional[str] = Field(None, max_length=50)
    is_active: Optional[bool] = None


class AccountResponse(AccountBase):
    """Schema risposta account"""
    id: uuid.UUID
    user_id: uuid.UUID
    balance: Decimal
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True
```

#### 2.2.4 - Category e Transaction schemas (base)
- [x] 📝 Crea `backend/app/schemas/category.py`
- [x] 📝 Crea `backend/app/schemas/transaction.py`
- [x] 📝 Crea `backend/app/schemas/transfer.py`

```python
# category.py - Versione minima
from pydantic import BaseModel
import uuid

class CategoryCreate(BaseModel):
    name: str

class CategoryUpdate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: uuid.UUID
    name: str
    
    class Config:
        from_attributes = True

# transaction.py - Versione minima
from pydantic import BaseModel
import uuid
from datetime import date
from decimal import Decimal

class TransactionCreate(BaseModel):
    account_id: uuid.UUID
    amount: Decimal
    date: date

class TransactionUpdate(BaseModel):
    amount: Decimal

class TransactionResponse(BaseModel):
    id: uuid.UUID
    amount: Decimal
    
    class Config:
        from_attributes = True

# transfer.py - Versione minima
from pydantic import BaseModel
import uuid

class TransferCreate(BaseModel):
    from_account_id: uuid.UUID
    to_account_id: uuid.UUID
    amount: float

class TransferResponse(BaseModel):
    id: uuid.UUID
    
    class Config:
        from_attributes = True
```

💡 **Nota:** Schemas completi verranno creati in FASE 3. Questi sono placeholder.

#### 2.2.5 - Commit schemas
- [x] In **GitHub Desktop**:
  - [x] Commit: `Add Pydantic schemas`
  - [x] Push

---

### 2.3 - Authentication Dependencies

#### 2.3.1 - Auth dependencies
- [x] 📝 Crea `backend/app/dependencies.py`

```python
"""
FastAPI Dependencies
Gestisce autenticazione e autorizzazione
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import Optional
import uuid

from .database import get_db
from .utils.security import verify_token
from .models.user import User

# Security scheme per Swagger UI
security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency per ottenere utente autenticato corrente
    Verifica JWT token e restituisce User object
    
    Raises:
        HTTPException 401 se token invalido o utente non trovato
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Verifica token
    token = credentials.credentials
    payload = verify_token(token)
    
    if payload is None:
        raise credentials_exception
    
    # Estrai user_id
    user_id_str: Optional[str] = payload.get("sub")
    if user_id_str is None:
        raise credentials_exception
    
    # Converti a UUID
    try:
        user_id = uuid.UUID(user_id_str)
    except ValueError:
        raise credentials_exception
    
    # Recupera utente da database
    user = db.query(User).filter(User.id == user_id).first()
    
    if user is None:
        raise credentials_exception
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )
    
    return user


async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Dependency per assicurarsi che utente sia attivo
    """
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
```

#### 2.3.2 - Commit dependencies
- [x] In **GitHub Desktop**:
  - [x] Commit: `Add authentication dependencies`
  - [x] Push

---

### 2.4 - Auth Router

#### 2.4.1 - CRUD operations User
- [x] 📝 Crea `backend/app/crud/__init__.py` (vuoto)
- [x] 📝 Crea `backend/app/crud/user.py`

```python
"""
User CRUD Operations
Database operations per User model
"""
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, timezone
import uuid

from ..models.user import User
from ..schemas.user import UserCreate
from ..utils.security import hash_password, verify_password


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Trova utente per email"""
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: uuid.UUID) -> Optional[User]:
    """Trova utente per ID"""
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserCreate) -> User:
    """
    Crea nuovo utente
    
    Args:
        db: Sessione database
        user: Dati utente da UserCreate schema
        
    Returns:
        User object creato
    """
    # Hash password
    hashed_pwd = hash_password(user.password)
    
    # Crea user object
    db_user = User(
        email=user.email,
        password_hash=hashed_pwd,
        full_name=user.full_name
    )
    
    # Salva in database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    """
    Autentica utente verificando email e password
    
    Args:
        db: Sessione database
        email: Email utente
        password: Password in chiaro
        
    Returns:
        User object se autenticato, None altrimenti
    """
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    
    # Aggiorna last_login
    user.last_login = datetime.now(timezone.utc)
    db.commit()
    
    return user
```

#### 2.4.2 - Auth router endpoints
- [x] 📝 Crea `backend/app/routers/__init__.py` (vuoto)
- [x] 📝 Crea `backend/app/routers/auth.py`

```python
"""
Authentication Router
Endpoints per registrazione, login e gestione profilo
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated

from ..database import get_db
from ..schemas.user import UserCreate, UserLogin, UserResponse, Token
from ..crud import user as user_crud
from ..utils.security import create_access_token
from ..dependencies import get_current_user
from ..models.user import User

# Router con prefisso /auth
router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Registrazione nuovo utente
    
    - **email**: Email valida (univoca)
    - **password**: Minimo 8 caratteri, 1 numero, 1 maiuscola
    - **full_name**: Nome completo (opzionale)
    
    Returns JWT token per login automatico
    """
    # Verifica email non già registrata
    existing_user = user_crud.get_user_by_email(db, email=user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Crea utente
    new_user = user_crud.create_user(db, user=user_data)
    
    # TODO: Crea categorie predefinite per nuovo utente
    # from ..crud import category as category_crud
    # category_crud.seed_default_categories(db, user_id=new_user.id)
    
    # Genera JWT token
    access_token = create_access_token(data={"sub": str(new_user.id)})
    
    return Token(
        access_token=access_token,
        user=UserResponse.model_validate(new_user)
    )


@router.post("/login", response_model=Token)
async def login(
    credentials: UserLogin,
    db: Session = Depends(get_db)
):
    """
    Login utente esistente
    
    - **email**: Email registrata
    - **password**: Password corretta
    
    Returns JWT token valido per 7 giorni
    """
    # Autentica utente
    user = user_crud.authenticate_user(db, credentials.email, credentials.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Genera JWT token
    access_token = create_access_token(data={"sub": str(user.id)})
    
    return Token(
        access_token=access_token,
        user=UserResponse.model_validate(user)
    )


@router.get("/me", response_model=UserResponse)
async def get_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    """
    Recupera profilo utente autenticato corrente
    
    Richiede JWT token valido nell'header Authorization
    """
    return UserResponse.model_validate(current_user)


@router.post("/logout")
async def logout():
    """
    Logout (client-side)
    
    Il client deve rimuovere il JWT token salvato localmente.
    Server non mantiene stato delle sessioni.
    """
    return {"message": "Successfully logged out"}
```

#### 2.4.3 - Commit auth router
- [x] In **GitHub Desktop**:
  - [x] Commit: `Add authentication router`
  - [x] Push

---

### 2.5 - Main Application Setup

#### 2.5.1 - FastAPI main app
- [x] 📝 Crea `backend/main.py`

```python
"""
FastAPI Main Application
Entry point dell'API
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import settings
from app.database import engine, Base
from app.routers import auth

# Lifespan context manager per startup/shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gestisce eventi startup e shutdown
    """
    # Startup
    print("🚀 Starting Budget App API...")
    print(f"📊 Database: {settings.DB_NAME}")
    print(f"🔒 JWT expires in: {settings.ACCESS_TOKEN_EXPIRE_MINUTES} minutes")
    
    # Crea tabelle se non esistono (in production usa Alembic)
    if settings.DEBUG:
        print("⚠️  DEBUG MODE: Creating tables if not exist...")
        Base.metadata.create_all(bind=engine)
    
    yield
    
    # Shutdown
    print("👋 Shutting down Budget App API...")

# Inizializza FastAPI app
app = FastAPI(
    title="Budget App API",
    description="API per gestione budget personali multi-utente",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1")

# Health check endpoint
@app.get("/")
async def root():
    """Root endpoint - health check"""
    return {
        "message": "Budget App API is running",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
```

#### 2.5.2 - Run script
- [x] 📝 Crea `backend/run.py` (script helper per avvio)

```python
"""
Run script per development
Avvia server Uvicorn con hot reload
"""
import uvicorn
from app.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
```

#### 2.5.3 - Test avvio server
- [x] Nel terminal (con venv attivo):
```bash
python run.py
```
- [x] Dovresti vedere output tipo:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```
- [x] Apri browser: http://localhost:8000
- [x] Dovresti vedere messaggio JSON
- [x] Apri: http://localhost:8000/docs
- [x] Dovresti vedere Swagger UI con endpoints auth

#### 2.5.4 - Commit main app
- [x] Ferma server (CTRL+C)
- [x] In **GitHub Desktop**:
  - [x] Commit: `Add FastAPI main application`
  - [x] Push

---

### 2.6 - Testing Authentication

#### 2.6.1 - Test con Swagger UI
- [x] Avvia server: `python run.py`
- [x] Apri http://localhost:8000/docs

**Test Registrazione:**
- [x] Expand `POST /api/v1/auth/register`
- [x] Click "Try it out"
- [x] Inserisci dati:
```json
{
  "email": "test@example.com",
  "password": "Test1234",
  "full_name": "Test User"
}
```
- [x] Click "Execute"
- [x] Verifica risposta 201 con JWT token

**Test Login:**
- [x] Expand `POST /api/v1/auth/login`
- [x] Inserisci stessi dati di registrazione
- [x] Verifica risposta 200 con JWT token

**Test Get Profile:**
- [x] Copia il `access_token` dalla risposta login
- [x] Click pulsante "Authorize" in alto
- [x] Incolla token (senza "Bearer")
- [x] Click "Authorize" poi "Close"
- [x] Expand `GET /api/v1/auth/me`
- [x] Click "Try it out" poi "Execute"
- [x] Verifica risposta 200 con dati utente

#### 2.6.2 - Verifica database
- [x] Apri **pgAdmin 4**
- [x] Naviga a `budget_app_dev` → `Schemas` → `public` → `Tables` → `users`
- [x] Click destro → View/Edit Data → All Rows
- [x] Dovresti vedere utente creato con:
  - [x] email corretta
  - [x] password_hash (non password in chiaro!)
  - [x] created_at popolato
  - [x] is_active = true

#### 2.6.3 - Test errori
- [x] In Swagger, prova a registrare stesso email
  - [x] Dovresti ricevere errore 400 "Email already registered"
- [x] Prova login con password sbagliata
  - [x] Dovresti ricevere errore 401 "Incorrect email or password"
- [x] Prova GET /me senza token
  - [x] Click "Authorize" → "Logout"
  - [x] Prova GET /me
  - [x] Dovresti ricevere errore 401

#### 2.6.4 - Test con curl (opzionale)
- [x] Apri nuovo terminal
- [x] Test registrazione:
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email":"curl@test.com","password":"Curl1234","full_name":"Curl Test"}'
```
- [x] Salva il token dalla risposta

- [x] Test profilo con token:
```bash
curl -X GET "http://localhost:8000/api/v1/auth/me" \
  -H "Authorization: Bearer TUO_TOKEN_QUI"
```

#### 2.6.5 - Documentazione test
- [x] 📝 Crea `docs/TESTING.md`

```markdown
# 🧪 Testing Guide

## Manual Testing con Swagger UI

### 1. Avvia server
```bash
cd backend
source venv/bin/activate
python run.py
```

### 2. Apri Swagger UI
http://localhost:8000/docs

### 3. Test Workflow

#### Registrazione
1. POST /api/v1/auth/register
2. Body:
```json
{
  "email": "user@example.com",
  "password": "Password123",
  "full_name": "Test User"
}
```
3. Salva `access_token` dalla risposta

#### Login
1. POST /api/v1/auth/login
2. Stesse credenziali di registrazione
3. Verifica ricezione token

#### Profilo Autenticato
1. Click "Authorize" (🔒 in alto)
2. Inserisci token
3. GET /api/v1/auth/me
4. Verifica dati utente

## Test Errors

- Email duplicata → 400
- Password sbagliata → 401
- Token invalido → 401
- Token scaduto → 401
- Utente inattivo → 403

## Test con cURL

```bash
# Register
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"Test1234"}'

# Login
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"Test1234"}'

# Get Profile (sostituisci TOKEN)
curl -X GET http://localhost:8000/api/v1/auth/me \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## Automated Tests (Fase 4)

Verranno aggiunti test Pytest nella Fase 4.
```

#### 2.6.6 - Commit testing docs
- [x] In **GitHub Desktop**:
  - [x] Commit: `Add testing documentation`
  - [x] Push

---

## 🎯 CHECKPOINT FASE 2

Prima di continuare, verifica:

- [x] ✅ Security utils (hashing, JWT) funzionanti
- [x] ✅ Pydantic schemas User creati e validanti
- [x] ✅ Auth dependencies per protezione endpoints
- [x] ✅ CRUD operations User implementate
- [x] ✅ Router /auth con register, login, me
- [x] ✅ FastAPI main app configurata con CORS
- [x] ✅ Server avvia senza errori
- [x] ✅ Swagger UI accessibile e funzionante
- [x] ✅ Test registrazione passato
- [x] ✅ Test login passato
- [x] ✅ Test profilo autenticato passato
- [x] ✅ Utenti salvati correttamente in database
- [x] ✅ Tutti i commit pushati su GitHub

**Test completo workflow:**
```
1. Registra utente → Ottieni token
2. Login con stesso utente → Ottieni token
3. GET /me con token → Vedi profilo
4. Verifica in pgAdmin che utente esista
```

**Tempo stimato:** 3-4 giorni  
**Prossimo:** FASE 3 - Backend API - Core Features (Accounts, Transactions, etc)

---

# FASE 3: Backend API - Core Features (4-5 giorni)

## 🎯 Obiettivo
Implementare tutti gli endpoints CRUD per Accounts, Categories, Transactions, Transfers e Custom Charts.

---

### 3.1 - Accounts CRUD & Router

#### 3.1.1 - Completare Account schemas
- [x] 📝 Apri `backend/app/schemas/account.py`
- [x] Aggiungi schemas mancanti se necessario
- [x] Assicurati ci siano: `AccountCreate`, `AccountUpdate`, `AccountResponse`

#### 3.1.2 - Account CRUD operations
- [x] 📝 Crea `backend/app/crud/account.py`

```python
"""
Account CRUD Operations
"""
from sqlalchemy.orm import Session
from typing import List, Optional
import uuid
from decimal import Decimal

from ..models.account import Account
from ..schemas.account import AccountCreate, AccountUpdate


def get_accounts(db: Session, user_id: uuid.UUID, skip: int = 0, limit: int = 100) -> List[Account]:
    """Lista tutti gli account dell'utente"""
    return db.query(Account).filter(
        Account.user_id == user_id
    ).offset(skip).limit(limit).all()


def get_account(db: Session, account_id: uuid.UUID, user_id: uuid.UUID) -> Optional[Account]:
    """Recupera singolo account verificando ownership"""
    return db.query(Account).filter(
        Account.id == account_id,
        Account.user_id == user_id
    ).first()


def create_account(db: Session, account: AccountCreate, user_id: uuid.UUID) -> Account:
    """Crea nuovo account"""
    db_account = Account(
        **account.model_dump(),
        user_id=user_id
    )
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def update_account(
    db: Session,
    account_id: uuid.UUID,
    account: AccountUpdate,
    user_id: uuid.UUID
) -> Optional[Account]:
    """Aggiorna account esistente"""
    db_account = get_account(db, account_id, user_id)
    if not db_account:
        return None
    
    update_data = account.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_account, key, value)
    
    db.commit()
    db.refresh(db_account)
    return db_account


def delete_account(db: Session, account_id: uuid.UUID, user_id: uuid.UUID) -> bool:
    """Elimina account"""
    db_account = get_account(db, account_id, user_id)
    if not db_account:
        return False
    
    db.delete(db_account)
    db.commit()
    return True


def update_account_balance(
    db: Session,
    account_id: uuid.UUID,
    amount: Decimal,
    operation: str  # 'add' or 'subtract'
) -> Optional[Account]:
    """
    Aggiorna balance account (usato da transactions/transfers)
    """
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        return None
    
    if operation == 'add':
        account.balance += amount
    elif operation == 'subtract':
        account.balance -= amount
    
    db.commit()
    db.refresh(account)
    return account
```

#### 3.1.3 - Account router
- [x] 📝 Crea `backend/app/routers/accounts.py`

```python
"""
Accounts Router
Gestione conti utente
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Annotated
import uuid

from ..database import get_db
from ..schemas.account import AccountCreate, AccountUpdate, AccountResponse
from ..crud import account as account_crud
from ..dependencies import get_current_user
from ..models.user import User

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.get("/", response_model=List[AccountResponse])
async def get_accounts(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    """Lista tutti gli account dell'utente corrente"""
    accounts = account_crud.get_accounts(db, user_id=current_user.id, skip=skip, limit=limit)
    return accounts


@router.post("/", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
async def create_account(
    account: AccountCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """Crea nuovo account"""
    return account_crud.create_account(db, account=account, user_id=current_user.id)


@router.get("/{account_id}", response_model=AccountResponse)
async def get_account(
    account_id: uuid.UUID,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """Recupera singolo account"""
    account = account_crud.get_account(db, account_id=account_id, user_id=current_user.id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account


@router.put("/{account_id}", response_model=AccountResponse)
async def update_account(
    account_id: uuid.UUID,
    account: AccountUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """Aggiorna account esistente"""
    updated = account_crud.update_account(
        db, account_id=account_id, account=account, user_id=current_user.id
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Account not found")
    return updated


@router.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_account(
    account_id: uuid.UUID,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """Elimina account"""
    success = account_crud.delete_account(db, account_id=account_id, user_id=current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Account not found")
    return None
```

#### 3.1.4 - Registra router in main
- [x] 📝 Apri `backend/main.py`
- [x] Aggiungi import:
```python
from app.routers import auth, accounts
```
- [x] Aggiungi router:
```python
app.include_router(accounts.router, prefix="/api/v1")
```

#### 3.1.5 - Test Accounts
- [x] Avvia server: `python run.py`
- [x] Apri Swagger: http://localhost:8000/docs
- [x] Autorizza con token utente
- [x] Test POST /accounts (crea account)
- [x] Test GET /accounts (lista)
- [x] Test GET /accounts/{id} (dettaglio)
- [x] Test PUT /accounts/{id} (modifica)
- [x] Test DELETE /accounts/{id} (elimina)
- [x] Verifica in pgAdmin che dati siano salvati

#### 3.1.6 - Commit accounts
- [x] In **GitHub Desktop**:
  - [x] Commit: `Add accounts CRUD and router`
  - [x] Push

---

### 3.2 - Categories CRUD & Router

💡 **Nota:** Implementazione molto simile ad Accounts. Segui stesso pattern.

#### 3.2.1 - Completare Category schemas
- [x] 📝 Completa `backend/app/schemas/category.py` con tutti i campi necessari

#### 3.2.2 - Category CRUD
- [x] 📝 Crea `backend/app/crud/category.py`
- [x] Implementa: `get_categories`, `create_category`, `update_category`, `delete_category`
- [x] Aggiungi funzione `seed_default_categories(db, user_id)` che chiama funzione SQL

#### 3.2.3 - Category router
- [x] 📝 Crea `backend/app/routers/categories.py`
- [x] Implementa endpoints GET, POST, PUT, DELETE

#### 3.2.4 - Registra router
- [x] Aggiungi in `main.py`

#### 3.2.5 - Test
- [x] Test tutti gli endpoints in Swagger

#### 3.2.6 - Commit
- [x] Commit: `Add categories CRUD and router`

---

### 3.3 - Transactions CRUD & Router

#### 3.3.1 - Completare Transaction schemas
- [x] 📝 Completa `backend/app/schemas/transaction.py`
- [x] Include tutti i campi: amount, type, date, description, notes, tags

#### 3.3.2 - Transaction CRUD
- [x] 📝 Crea `backend/app/crud/transaction.py`
- [x] Implementa CRUD base
- [x] **IMPORTANTE:** In `create_transaction`, aggiorna anche balance dell'account:
```python
def create_transaction(db, transaction, user_id):
    # Crea transaction
    db_transaction = Transaction(...)
    db.add(db_transaction)
    
    # Aggiorna balance account
    if transaction.type == 'income':
        account_crud.update_account_balance(db, transaction.account_id, transaction.amount, 'add')
    else:  # expense
        account_crud.update_account_balance(db, transaction.account_id, transaction.amount, 'subtract')
    
    db.commit()
    return db_transaction
```

#### 3.3.3 - Transaction router
- [x] 📝 Crea `backend/app/routers/transactions.py`
- [x] Implementa endpoints con query parameters per filtri:
  - `account_id` (opzionale)
  - `category_id` (opzionale)
  - `start_date` (opzionale)
  - `end_date` (opzionale)
  - `type` (income/expense, opzionale)

#### 3.3.4 - Registra e testa
- [x] Registra router in main
- [x] Test creazione transaction
- [x] **Verifica in pgAdmin che balance account si aggiorni automaticamente**
- [x] Test filtri

#### 3.3.5 - Commit
- [X] Commit: `Add transactions CRUD and router`

---

### 3.4 - Transfers CRUD & Router

#### 3.4.1 - Transfer CRUD
- [x] 📝 Crea `backend/app/crud/transfer.py`
- [x] **IMPORTANTE:** In `create_transfer`, aggiorna balance di entrambi gli account:
```python
def create_transfer(db, transfer, user_id):
    # Crea transfer
    db_transfer = Transfer(...)
    db.add(db_transfer)
    
    # Sottrai da account origine
    account_crud.update_account_balance(db, transfer.from_account_id, transfer.amount, 'subtract')
    
    # Aggiungi ad account destinazione
    account_crud.update_account_balance(db, transfer.to_account_id, transfer.amount, 'add')
    
    db.commit()
    return db_transfer
```

#### 3.4.2 - Transfer router
- [x] 📝 Crea `backend/app/routers/transfers.py`

#### 3.4.3 - Test
- [x] Crea 2 account
- [x] Crea transfer tra loro
- [x] Verifica che balance di entrambi si aggiorni

#### 3.4.4 - Commit
- [x] Commit: `Add transfers CRUD and router`

---

### 3.5 - Custom Charts (opzionale per MVP)

💡 **Decisione:** Puoi fare custom charts ora o lasciare per dopo.

- [x] Decidi se implementare ora o rimandare a "Sviluppi Futuri"
- [x] Se implementi ora:
  - [x] CRUD per custom_charts
  - [x] Router
  - [x] Test

---

### 3.6 - Statistics & Analytics Endpoints

#### 3.6.1 - Analytics router
- [x] 📝 Crea `backend/app/routers/analytics.py`

```python
"""
Analytics Router
Statistiche e dashboard data
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Annotated
from datetime import date, datetime
from decimal import Decimal

from ..database import get_db
from ..dependencies import get_current_user
from ..models.user import User
from ..models.transaction import Transaction
from ..models.account import Account

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/summary")
async def get_summary(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
    start_date: date = None,
    end_date: date = None
):
    """
    Ritorna summary dashboard:
    - Total income
    - Total expenses
    - Net balance
    - Account balances
    """
    query = db.query(Transaction).filter(Transaction.user_id == current_user.id)
    
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    if end_date:
        query = query.filter(Transaction.date <= end_date)
    
    transactions = query.all()
    
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expense = sum(t.amount for t in transactions if t.type == 'expense')
    
    accounts = db.query(Account).filter(Account.user_id == current_user.id).all()
    total_balance = sum(a.balance for a in accounts)
    
    return {
        "total_income": float(total_income),
        "total_expense": float(total_expense),
        "net": float(total_income - total_expense),
        "total_balance": float(total_balance),
        "accounts_count": len(accounts)
    }


@router.get("/monthly-trend")
async def get_monthly_trend(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
    months: int = 12
):
    """
    Ritorna trend mensile income/expense ultimi N mesi
    """
    # Query con GROUP BY mese
    results = db.query(
        func.date_trunc('month', Transaction.date).label('month'),
        Transaction.type,
        func.sum(Transaction.amount).label('total')
    ).filter(
        Transaction.user_id == current_user.id
    ).group_by('month', Transaction.type).order_by('month').all()
    
    # Format results
    monthly_data = {}
    for row in results:
        month_str = row.month.strftime('%Y-%m')
        if month_str not in monthly_data:
            monthly_data[month_str] = {'income': 0, 'expense': 0}
        monthly_data[month_str][row.type] = float(row.total)
    
    return monthly_data
```

#### 3.6.2 - Registra analytics router
- [x] Aggiungi in `main.py`

#### 3.6.3 - Test analytics
- [x] Crea alcune transactions
- [x] Test GET /analytics/summary
- [x] Test GET /analytics/monthly-trend

#### 3.6.4 - Commit
- [x] Commit: `Add analytics endpoints`
---

# SEZIONE 3.7 - Code Review & Bug Fixing

---

### 3.7 - Code Review & Bug Fixing

Prima di procedere alla Fase 4 (Testing), è necessario effettuare una revisione completa del codice e correggere le incongruenze identificate.

#### 3.7.1 - Problemi Critici (Bloccanti)

##### A. Mismatch `initial_balance` vs `current_balance`
- [x] **Problema:** Il campo `initial_balance` viene usato come balance corrente e modificato ad ogni transazione/transfer. Questo è semanticamente errato - `initial_balance` dovrebbe essere il saldo iniziale immutabile.
- [x] **File coinvolti:**
  - `app/models/account.py` - ha property `current_balance` mai usata
  - `app/crud/account.py` - modifica `initial_balance` invece di calcolare
  - `app/crud/transaction.py` - modifica `initial_balance`
  - `app/crud/transfer.py` - modifica `initial_balance`
- [x] **Decisione da prendere:**
  - **Opzione A:** Rinominare `initial_balance` in `balance` (più semplice, meno corretto semanticamente)
  - **Opzione B:** Mantenere `initial_balance` immutabile e calcolare `current_balance` dinamicamente (più corretto, richiede refactoring)
  - **Opzione C:** Aggiungere campo `balance` separato che viene aggiornato (compromesso)
- [x] **Azione:** Decidere approccio e implementare

##### B. Mismatch tipi Transazione/Categoria (2 vs 3 tipi)
- [x] **Problema:** Inconsistenza tra documentazione, SQL originale, model e schema
  - SQL originale: `ENUM ('income', 'expense')`
  - Model comment: "income or expense"
  - Schema attuale: `["income", "expense_necessity", "expense_extra"]`
- [x] **File coinvolti:**
  - `app/models/category.py` - commento dice 2 tipi
  - `app/models/transaction.py` - commento dice 2 tipi
  - `app/schemas/category.py` - valida 3 tipi
  - `app/schemas/transaction.py` - valida 3 tipi
  - `app/crud/transaction.py` - usa 3 tipi nella logica
  - `app/crud/analytics.py` - usa 3 tipi
- [x] **Decisione:** I 3 tipi (`income`, `expense_necessity`, `expense_extra`) sono la scelta corretta per il business logic (basato sul file Excel originale)
- [x] **Azione:** Aggiornare commenti nei model per riflettere i 3 tipi

##### C. Path errato in `run.py` e `Dockerfile`
- [x] **Problema:** I file riferiscono `main:app` ma il file è in `app/main.py`
- [x] **File coinvolti:**
  - `backend/Dockerfile` - riga `CMD ["uvicorn", "main:app", ...]`
- [x] **Azione:** Correggere in `app.main:app`

#### 3.7.2 - Problemi Medi (Da correggere prima del deploy)

##### D. Enum `ChartType` duplicato
- [x] **Problema:** Definito sia in `models/custom_chart.py` che in `schemas/custom_chart.py`
- [x] **Rischio:** Potrebbero andare out of sync
- [x] **Azione:** Centralizzare in un unico file (es. `schemas/custom_chart.py`) e importare nel model

##### E. Validazione incompleta in `update_transfer`
- [x] **Problema:** La validazione della direzione transfer potrebbe non coprire tutti i casi edge
- [x] **File:** `app/crud/transfer.py`
- [x] **Azione:** Verificare e completare validazione

##### F. File SQL in `database/` obsoleti
- [x] **Problema:** I file SQL originali sono out of sync con i model attuali
- [x] **File:**
  - `database/01_create_schema.sql`
  - `database/02_seed_default_categories.sql`
- [x] **Azione:** 
  - Opzione A: Rimuovere (Alembic gestisce tutto)
  - Opzione B: Aggiornare e tenere come documentazione
  - Opzione C: Spostare in `database/archive/` con nota

#### 3.7.3 - Problemi Minori / Note

##### G. Migration `c744b8064fb0` vuota
- [x] **Nota:** La migration per `custom_charts` è vuota perché la tabella era già stata creata via SQL manuale
- [x] **Impatto:** Nessuno per il funzionamento attuale
- [x] **Rischio:** Se si fa `alembic downgrade` completo e poi `upgrade`, la tabella potrebbe non essere ricreata
- [x] **Azione:** Documentare, non richiede fix immediato

##### H. UUID come String(36) invece di UUID nativo
- [x] **Nota:** I model usano `String(36)` invece del tipo UUID nativo PostgreSQL
- [x] **Impatto:** Funziona ma perde ottimizzazioni PostgreSQL
- [x] **Azione:** è stata effettuata la modifica da `String(36)` a UIID

##### I. Commenti misti italiano/inglese
- [x] **Nota:** Inconsistenza nella lingua dei commenti e docstring
- [x] **Azione:** Uniformare (suggerimento: inglese per codice, italiano per docs utente)

##### J. CORS_ORIGINS parsing
- [x] **Nota:** `.env.example` usa stringa JSON, `config.py` si aspetta lista
- [x] **Impatto:** Pydantic-settings dovrebbe gestirlo, ma verificare
- [X] **Azione:** Testare parsing da `.env`

#### 3.7.4 - Checklist Correzioni

**Critiche (fare ora):**
- [x] Decidere e implementare strategia balance (A/B/C)
- [x] Aggiornare commenti model per 3 tipi transazione
- [x] Correggere path in `run.py`: `app.main:app`
- [x] Correggere path in `Dockerfile`: `app.main:app`

**Medie (fare prima di Fase 6):**
- [x] Centralizzare `ChartType` enum
- [x] Verificare validazione `update_transfer`
- [x] Gestire file SQL obsoleti

**Minori (nice to have):**
- [x] Uniformare lingua commenti
- [X] Documentare nota su migration vuota
- [x] Testare parsing CORS_ORIGINS

#### 3.7.5 - Test Post-Correzioni

Dopo le correzioni, verificare:
- [x] Server avvia senza errori: `python run.py` (o con path corretto)
- [x] Swagger UI accessibile: http://localhost:8000/docs
- [x] Test creazione transaction → balance aggiornato correttamente
- [x] Test creazione transfer → entrambi i balance aggiornati
- [x] Test analytics/summary → dati corretti
- [x] Nessun errore nei log

#### 3.7.6 - Commit
- [x] Commit: `Code review fixes - Phase 3.7`
- [x] Push

---

## 🎯 CHECKPOINT FASE 3 (AGGIORNATO)

Verifica che tutti questi endpoint funzionino E che le correzioni 3.7 siano applicate:

[... resto del checkpoint esistente ...]

**Aggiunte Fase 3.7:**
- [x] ✅ Path `run.py` e `Dockerfile` corretti
- [x] ✅ Strategia balance definita e implementata
- [x] ✅ Commenti model allineati con schema
- [x] ✅ Test post-correzioni passati

---

## 🎯 CHECKPOINT FASE 3

Verifica che tutti questi endpoints funzionino:

**Authentication:**
- [x] ✅ POST /auth/register
- [x] ✅ POST /auth/login
- [x] ✅ GET /auth/me

**Accounts:**
- [x] ✅ GET /accounts (lista)
- [x] ✅ POST /accounts (crea)
- [x] ✅ GET /accounts/{id} (dettaglio)
- [x] ✅ PUT /accounts/{id} (modifica)
- [x] ✅ DELETE /accounts/{id} (elimina)

**Categories:**
- [x] ✅ GET /categories
- [x] ✅ POST /categories
- [x] ✅ PUT /categories/{id}
- [x] ✅ DELETE /categories/{id}

**Transactions:**
- [x] ✅ GET /transactions (con filtri)
- [x] ✅ POST /transactions (crea + aggiorna balance)
- [x] ✅ PUT /transactions/{id}
- [x] ✅ DELETE /transactions/{id}

**Transfers:**
- [x] ✅ GET /transfers
- [x] ✅ POST /transfers (crea + aggiorna 2 balance)
- [x] ✅ DELETE /transfers/{id}

**Analytics:**
- [x] ✅ GET /analytics/summary
- [x] ✅ GET /analytics/monthly-trend

**Test integrazione completa:**
1. [x] Registra utente
2. [x] Crea 2 account
3. [x] Crea alcune categorie
4. [x] Crea transactions (verifica balance si aggiorna)
5. [x] Crea transfer (verifica entrambi i balance)
6. [x] Chiama /analytics/summary (verifica dati corretti)
7. [x] Tutto funziona end-to-end!

# FASE 3.8: Backend API - Vacation Planning (3-4 giorni)

## 🎯 Obiettivo
Implementare il backend completo per il modulo di gestione ferie per dipendenti, con calendario festività italiane, calcolo automatico Pasqua/Pasquetta, maturazione separata per tipo (Ferie/ROL/Permessi) e proiezione ore residue.

**Target:** Utenti privati (dipendenti)  
**Integrazione Budget:** Livello A - Leggera (widget in dashboard, nessuna automazione)

---

## 📋 Panoramica Funzionalità

### Core Features
- ✅ **Maturazione separata per tipo**: Ferie (giorni/mese), ROL (ore/mese), Permessi (ore/mese)
- ✅ Configurazione ore giornaliere lavorative (default 8h, **configurabile dall'utente**)
- ✅ **Data inizio tracciamento** invece di riporto anno precedente
- ✅ **Saldo iniziale opzionale** per mese specifico (ferie in giorni, ROL/Permessi in ore)
- ✅ Calendario annuale con festività italiane (fisse + mobili)
- ✅ Festività custom utente (patrono, chiusure aziendali)
- ✅ Inserimento ferie/ROL/permessi per giorno (**un solo tipo per giorno**)
- ✅ **Validazione**: blocco inserimento in weekend e festività (nazionali + custom)
- ✅ Ferie: ore automatiche da settings (no input manuale)
- ✅ ROL/Permessi: ore inserite manualmente
- ✅ Calcolo automatico Pasqua e Pasquetta (algoritmo Computus)
- ✅ Proiezione ore residue mese per mese
- ✅ Identificazione automatica "ponti"
- ✅ **Vista riepilogo con totali aggregati**: ore + giorni per tipo + TOTALE disponibile

### Decisioni Architetturali
- **UniqueConstraint**: `(user_id, date)` - un solo tipo di assenza per giorno
- **Festività custom**: tabella separata `UserHoliday` (flessibile per patrono + altre)
- **Maturazione separata**: 3 campi distinti invece di unico `hours_per_month`
- **Tracking start**: `tracking_start_date` (Date) invece di `carryover_year` (Integer)
- **Saldo iniziale**: Ferie in **giorni**, ROL/Permessi in **ore**
- **NO Malattia**: Rimosso completamente (non necessario per utenti privati)
- **Shift domenica→lunedì**: rimandato a Fase 7

---

## 🗄️ 3.8.1 - Database Models

### 3.8.1.1 - Crea model VacationSettings
- [ ] 📝 Crea `backend/app/models/vacation_settings.py`

```python
"""
VacationSettings model - User vacation configuration.

NUOVA ARCHITETTURA:
- Maturazione separata per tipo (Ferie in giorni/mese, ROL/Permessi in ore/mese)
- Tracking start date invece di carryover year
- Saldo iniziale opzionale per mese specifico
"""
from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import date as date_type

from app.database import Base
from app.models.mixins import TimestampMixin


class VacationSettings(Base, TimestampMixin):
    """
    User settings for vacation tracking.
    
    ARCHITETTURA:
    - Maturazione separata per tipo (Ferie, ROL, Permessi)
    - Tracking start: da quando l'utente inizia a maturare
    - Saldo iniziale opzionale per gestire ore già maturate prima del tracking
    
    Attributes:
        user_id: Owner of these settings (one per user)
        work_hours_per_day: Hours in a work day (default 8, user configurable)
        
        ferie_days_per_month: Days of vacation accrued per month (default 1.83 = 22 days/year)
        rol_hours_per_month: ROL hours accrued per month (default 2.67 = 32 hours/year)
        permessi_hours_per_month: Permission hours accrued per month (default 8.67 = 104 hours/year)
        
        tracking_start_date: Date when tracking started (user employment/contract start)
        
        initial_balance_month: Optional month for initial balance (1-12)
        initial_balance_year: Optional year for initial balance
        initial_ferie_days: Initial vacation days (will be converted to hours internally)
        initial_rol_hours: Initial ROL hours
        initial_permessi_hours: Initial permission hours
    """
    __tablename__ = "vacation_settings"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True), 
        ForeignKey("users.id", ondelete="CASCADE"), 
        unique=True,  # One settings per user
        nullable=False, 
        index=True
    )
    
    # Work configuration
    work_hours_per_day = Column(Float, nullable=False, default=8.0)
    
    # Accrual rates (SEPARATE PER TYPE!)
    ferie_days_per_month = Column(Float, nullable=False, default=1.83)     # ~22 days/year
    rol_hours_per_month = Column(Float, nullable=False, default=2.67)      # ~32 hours/year
    permessi_hours_per_month = Column(Float, nullable=False, default=8.67) # ~104 hours/year
    
    # Tracking start (when user started accruing)
    tracking_start_date = Column(Date, nullable=False, default=date_type.today)
    
    # Optional: Initial balance for specific month (for migration from other systems)
    initial_balance_month = Column(Integer, nullable=True)  # 1-12
    initial_balance_year = Column(Integer, nullable=True)
    initial_ferie_days = Column(Float, nullable=True, default=0.0)    # GIORNI (converted to hours internally)
    initial_rol_hours = Column(Float, nullable=True, default=0.0)
    initial_permessi_hours = Column(Float, nullable=True, default=0.0)
    
    # Relationships
    user = relationship("User", back_populates="vacation_settings")
    
    def __repr__(self):
        return (f"<VacationSettings(user_id={self.user_id}, "
                f"ferie={self.ferie_days_per_month}d/m, "
                f"rol={self.rol_hours_per_month}h/m, "
                f"permessi={self.permessi_hours_per_month}h/m)>")
```

### 3.8.1.2 - Crea model VacationEntry
- [ ] 📝 Crea `backend/app/models/vacation_entry.py`

```python
"""
VacationEntry model - Individual vacation/leave entries.

IMPORTANTE: Un solo tipo di assenza per giorno (UniqueConstraint su user_id + date).
- Ferie: ore automatiche da work_hours_per_day (no input manuale)
- ROL/Permessi: ore inserite manualmente dall'utente
- MALATTIA: RIMOSSA (non necessaria per utenti privati)
"""
from sqlalchemy import Column, String, ForeignKey, Float, Date, Text, Enum, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
import enum

from app.database import Base
from app.models.mixins import TimestampMixin


class VacationEntryType(str, enum.Enum):
    """Types of vacation/leave entries."""
    FERIE = "ferie"              # Regular vacation (hours automatic from settings)
    PERMESSO = "permesso"        # Personal leave/permission (hours manual)
    ROL = "rol"                  # Riduzione Orario Lavoro (hours manual)


# Italian labels for entry types
VACATION_ENTRY_TYPE_LABELS = {
    "ferie": "Ferie",
    "permesso": "Permesso",
    "rol": "ROL (Riduzione Orario Lavoro)",
}

# Types that allow manual hour input (not ferie)
MANUAL_HOURS_TYPES = ["permesso", "rol"]


class VacationEntry(Base, TimestampMixin):
    """
    Individual vacation or leave entry.
    
    REGOLE:
    - Un solo tipo per giorno (UniqueConstraint su user_id + date)
    - Ferie: ore = work_hours_per_day da settings (automatico)
    - ROL/Permessi: ore inserite manualmente
    - NO weekend: validazione blocca inserimento
    - NO festività: validazione blocca inserimento (nazionali + custom utente)
    
    Attributes:
        user_id: Owner of this entry
        date: Date of the entry
        entry_type: Type of leave (ferie, permesso, rol)
        hours: Number of hours (automatic for ferie, manual for others)
        notes: Optional notes
    """
    __tablename__ = "vacation_entries"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True), 
        ForeignKey("users.id", ondelete="CASCADE"), 
        nullable=False, 
        index=True
    )
    
    date = Column(Date, nullable=False, index=True)
    entry_type = Column(
        Enum(VacationEntryType, name="vacation_entry_type"),
        nullable=False,
        default=VacationEntryType.FERIE
    )
    hours = Column(Float, nullable=False, default=8.0)
    notes = Column(Text, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="vacation_entries")
    
    # IMPORTANTE: Un solo tipo per giorno!
    __table_args__ = (
        UniqueConstraint('user_id', 'date', name='uq_user_date'),
    )
    
    def __repr__(self):
        return f"<VacationEntry(date={self.date}, type={self.entry_type}, hours={self.hours})>"
```

### 3.8.1.3 - Crea model ItalianHoliday
- [ ] 📝 Crea `backend/app/models/italian_holiday.py`

```python
"""
ItalianHoliday model - Italian public holidays.
Pre-populated table with national holidays.
"""
from sqlalchemy import Column, String, Date, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class ItalianHoliday(Base):
    """
    Italian public holidays (national).
    
    This table is pre-populated with fixed holidays.
    Mobile holidays (Easter Monday) are calculated and inserted dynamically.
    
    NOTE: Shift domenica→lunedì rimandato a Fase 7.
    
    Attributes:
        date: Holiday date
        name: Holiday name in Italian
        name_en: Holiday name in English
        is_fixed: True if same date every year (Dec 25), False for mobile (Pasquetta)
        is_national: True if national holiday
    """
    __tablename__ = "italian_holidays"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = Column(Date, nullable=False, unique=True, index=True)
    name = Column(String(100), nullable=False)
    name_en = Column(String(100), nullable=True)
    is_fixed = Column(Boolean, nullable=False, default=True)
    is_national = Column(Boolean, nullable=False, default=True)
    
    def __repr__(self):
        return f"<ItalianHoliday(date={self.date}, name={self.name})>"


# Fixed Italian National Holidays: (month, day, name_it, name_en)
FIXED_ITALIAN_HOLIDAYS = [
    (1, 1, "Capodanno", "New Year's Day"),
    (1, 6, "Epifania", "Epiphany"),
    (4, 25, "Festa della Liberazione", "Liberation Day"),
    (5, 1, "Festa dei Lavoratori", "Labour Day"),
    (6, 2, "Festa della Repubblica", "Republic Day"),
    (8, 15, "Ferragosto", "Assumption of Mary"),
    (11, 1, "Tutti i Santi", "All Saints' Day"),
    (12, 8, "Immacolata Concezione", "Immaculate Conception"),
    (12, 25, "Natale", "Christmas Day"),
    (12, 26, "Santo Stefano", "St. Stephen's Day"),
]
```

### 3.8.1.4 - Crea model UserHoliday
- [ ] 📝 Crea `backend/app/models/user_holiday.py`

```python
"""
UserHoliday model - User custom holidays (patron saint, company closures, etc.).
"""
from sqlalchemy import Column, String, ForeignKey, Date, Boolean, Integer, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
import calendar

from app.database import Base
from app.models.mixins import TimestampMixin


class UserHoliday(Base, TimestampMixin):
    """
    User-defined custom holidays.
    
    Use cases:
    - Patron saint day (es. Sant'Ambrogio 7/12 Milano, San Giovanni 24/6 Torino)
    - Company mandatory closures
    - Other personal holidays
    
    Attributes:
        user_id: Owner of this holiday
        day: Day of month (1-31)
        month: Month (1-12)
        name: Holiday name
        recurring: If True, repeats every year. If False, one-time only.
        year: Only used if recurring=False (specific year)
    """
    __tablename__ = "user_holidays"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True), 
        ForeignKey("users.id", ondelete="CASCADE"), 
        nullable=False, 
        index=True
    )
    
    # Date components (allows recurring holidays)
    day = Column(Integer, nullable=False)  # 1-31
    month = Column(Integer, nullable=False)  # 1-12
    name = Column(String(100), nullable=False)
    
    # Recurring = repeats every year (like patron saint)
    # Non-recurring = specific year only
    recurring = Column(Boolean, nullable=False, default=True)
    year = Column(Integer, nullable=True)  # Only for non-recurring
    
    # Relationships
    user = relationship("User", back_populates="user_holidays")
    
    # Unique: one holiday per user per day/month (for recurring)
    # or per day/month/year (for non-recurring)
    __table_args__ = (
        UniqueConstraint('user_id', 'day', 'month', 'year', name='uq_user_holiday'),
    )
    
    def __repr__(self):
        return f"<UserHoliday(name={self.name}, {self.day}/{self.month}, recurring={self.recurring})>"
    
    def get_date_for_year(self, year: int):
        """
        Get the actual date for a specific year.
        
        Returns None if:
        - Holiday is non-recurring and year doesn't match
        - Date is invalid (e.g., Feb 30)
        """
        from datetime import date
        
        if not self.recurring and self.year and self.year != year:
            return None
        
        try:
            return date(year, self.month, self.day)
        except ValueError:
            # Invalid date (e.g., Feb 30)
            return None
    
    def validate_date(self):
        """Validate that day is valid for the given month."""
        max_day = calendar.monthrange(2024, self.month)[1]  # Use leap year for validation
        if self.day > max_day:
            raise ValueError(f"Day {self.day} is invalid for month {self.month}")
```

### 3.8.1.5 - Update User Model
- [ ] 📝 Modifica `backend/app/models/user.py` - aggiungi relationships

```python
# Add these lines to the User model relationships section:

# Vacation relationships
vacation_settings = relationship(
    "VacationSettings", 
    back_populates="user", 
    uselist=False,  # One-to-one
    cascade="all, delete-orphan"
)
vacation_entries = relationship(
    "VacationEntry", 
    back_populates="user", 
    cascade="all, delete-orphan"
)
user_holidays = relationship(
    "UserHoliday", 
    back_populates="user", 
    cascade="all, delete-orphan"
)
```

### 3.8.1.6 - Update Models __init__.py
- [ ] 📝 Modifica `backend/app/models/__init__.py`

```python
# Add these imports:
from app.models.vacation_settings import VacationSettings
from app.models.vacation_entry import VacationEntry, VacationEntryType, VACATION_ENTRY_TYPE_LABELS, MANUAL_HOURS_TYPES
from app.models.italian_holiday import ItalianHoliday, FIXED_ITALIAN_HOLIDAYS
from app.models.user_holiday import UserHoliday

# Add to __all__ list:
"VacationSettings",
"VacationEntry",
"VacationEntryType",
"VACATION_ENTRY_TYPE_LABELS",
"MANUAL_HOURS_TYPES",
"ItalianHoliday",
"FIXED_ITALIAN_HOLIDAYS",
"UserHoliday",
```

### 3.8.1.7 - Generate Alembic Migration
- [ ] Esegui: `alembic revision --autogenerate -m "Add vacation module tables with separate accrual rates"`
- [ ] Verifica migration generata
- [ ] **IMPORTANTE:** Se esiste già il modulo, creare migration per:
  - Aggiungere nuove colonne (ferie_days_per_month, rol_hours_per_month, etc.)
  - Migrare dati esistenti (hours_per_month → ferie_days_per_month)
  - Rimuovere vecchie colonne (hours_per_month, carryover_hours, carryover_year)
  - Rimuovere valore enum "malattia"
- [ ] Esegui: `alembic upgrade head`

### 3.8.1.8 - Commit models
- [ ] Commit: `Add vacation module with separate accrual rates (Ferie/ROL/Permessi)`

---

## 🛠️ 3.8.2 - Utility Functions

### 3.8.2.1 - Easter Calculator
- [ ] 📝 Crea `backend/app/utils/easter.py`

```python
"""
Easter date calculator using the Computus algorithm.
Calculates Easter Sunday and Easter Monday (Pasquetta) for any year.
"""
from datetime import date, timedelta


def calculate_easter_sunday(year: int) -> date:
    """
    Calculate Easter Sunday for a given year using the Anonymous Gregorian algorithm.
    
    This is the most widely used algorithm for calculating Easter,
    valid for years 1583 and later (Gregorian calendar).
    
    Args:
        year: The year to calculate Easter for (must be >= 1583)
        
    Returns:
        date: Easter Sunday date
        
    Raises:
        ValueError: If year < 1583
    """
    if year < 1583:
        raise ValueError("Easter calculation only valid for years >= 1583 (Gregorian calendar)")
    
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    
    return date(year, month, day)


def calculate_easter_monday(year: int) -> date:
    """
    Calculate Easter Monday (Pasquetta) for a given year.
    
    Easter Monday is the day after Easter Sunday.
    
    Args:
        year: The year to calculate for
        
    Returns:
        date: Easter Monday date
    """
    easter_sunday = calculate_easter_sunday(year)
    return easter_sunday + timedelta(days=1)


def get_easter_dates(year: int) -> dict:
    """
    Get both Easter Sunday and Monday for a year.
    
    Args:
        year: The year to calculate for
        
    Returns:
        dict with 'sunday' and 'monday' dates
    """
    sunday = calculate_easter_sunday(year)
    return {
        "sunday": sunday,
        "monday": sunday + timedelta(days=1)
    }
```

### 3.8.2.2 - Bridge Days Calculator
- [ ] 📝 Crea `backend/app/utils/bridge_days.py`

```python
"""
Bridge days (ponti) calculator for Italian holidays.
Identifies opportunities to maximize days off with minimal vacation days.
"""
from datetime import date, timedelta
from typing import List, Dict, Any, Set


ITALIAN_WEEKDAYS = [
    "Lunedì", "Martedì", "Mercoledì", "Giovedì", 
    "Venerdì", "Sabato", "Domenica"
]

ITALIAN_MONTHS = {
    1: "Gennaio", 2: "Febbraio", 3: "Marzo", 4: "Aprile",
    5: "Maggio", 6: "Giugno", 7: "Luglio", 8: "Agosto",
    9: "Settembre", 10: "Ottobre", 11: "Novembre", 12: "Dicembre"
}


def get_italian_weekday(d: date) -> str:
    """Get Italian weekday name."""
    return ITALIAN_WEEKDAYS[d.weekday()]


def is_weekend(d: date) -> bool:
    """Check if date is Saturday (5) or Sunday (6)."""
    return d.weekday() >= 5


def find_bridge_opportunities(
    holidays: List[Any], 
    year: int,
    user_holidays: List[Any] = None
) -> List[Dict]:
    """
    Find bridge day opportunities for a given year.
    
    A "ponte" (bridge) is when a holiday falls on Tuesday or Thursday,
    allowing to take Monday or Friday off to create a 4-day weekend.
    
    VALIDAZIONE: Verifica che il bridge_date non sia:
    - Un weekend
    - Già una festività (nazionale o utente)
    
    Args:
        holidays: List of ItalianHoliday objects for the year
        year: Year to analyze
        user_holidays: Optional list of UserHoliday objects
        
    Returns:
        List of bridge opportunities sorted by efficiency
    """
    opportunities = []
    
    # Build set of all holiday dates for quick lookup
    holiday_dates: Set[date] = set()
    for holiday in holidays:
        if holiday.date.year == year:
            holiday_dates.add(holiday.date)
    
    # Add user holidays to the set
    if user_holidays:
        for uh in user_holidays:
            uh_date = uh.get_date_for_year(year)
            if uh_date:
                holiday_dates.add(uh_date)
    
    for holiday in holidays:
        if holiday.date.year != year:
            continue
        
        weekday = holiday.date.weekday()
        
        # Tuesday holiday (weekday=1): Monday is a bridge → 4 days off with 1 day
        if weekday == 1:
            bridge_date = holiday.date - timedelta(days=1)
            # Skip if bridge is weekend or already a holiday
            if not is_weekend(bridge_date) and bridge_date not in holiday_dates:
                opportunities.append({
                    "holiday_name": holiday.name,
                    "holiday_date": holiday.date.isoformat(),
                    "holiday_weekday": "Martedì",
                    "bridge_date": bridge_date.isoformat(),
                    "bridge_weekday": "Lunedì",
                    "vacation_days_needed": 1,
                    "total_days_off": 4,  # Sat + Sun + Mon + Tue
                    "efficiency": 4.0,
                    "description": f"Ponte {holiday.name}: prendi Lunedì {bridge_date.strftime('%d/%m')}"
                })
        
        # Thursday holiday (weekday=3): Friday is a bridge → 4 days off with 1 day
        elif weekday == 3:
            bridge_date = holiday.date + timedelta(days=1)
            # Skip if bridge is weekend or already a holiday
            if not is_weekend(bridge_date) and bridge_date not in holiday_dates:
                opportunities.append({
                    "holiday_name": holiday.name,
                    "holiday_date": holiday.date.isoformat(),
                    "holiday_weekday": "Giovedì",
                    "bridge_date": bridge_date.isoformat(),
                    "bridge_weekday": "Venerdì",
                    "vacation_days_needed": 1,
                    "total_days_off": 4,  # Thu + Fri + Sat + Sun
                    "efficiency": 4.0,
                    "description": f"Ponte {holiday.name}: prendi Venerdì {bridge_date.strftime('%d/%m')}"
                })
        
        # Wednesday holiday (weekday=2): can bridge both sides → 5 days off with 2 days
        elif weekday == 2:
            mon = holiday.date - timedelta(days=2)
            tue = holiday.date - timedelta(days=1)
            thu = holiday.date + timedelta(days=1)
            fri = holiday.date + timedelta(days=2)
            
            # Check which side is available
            mon_tue_available = (
                not is_weekend(mon) and mon not in holiday_dates and
                not is_weekend(tue) and tue not in holiday_dates
            )
            thu_fri_available = (
                not is_weekend(thu) and thu not in holiday_dates and
                not is_weekend(fri) and fri not in holiday_dates
            )
            
            # Create separate opportunities for each side
            if mon_tue_available:
                opportunities.append({
                    "holiday_name": holiday.name,
                    "holiday_date": holiday.date.isoformat(),
                    "holiday_weekday": "Mercoledì",
                    "bridge_date": mon.isoformat(),
                    "bridge_weekday": "Lunedì + Martedì",
                    "vacation_days_needed": 2,
                    "total_days_off": 5,
                    "efficiency": 2.5,
                    "description": f"Ponte prima di {holiday.name}: prendi Lunedì e Martedì per 5 giorni di riposo"
                })
            
            if thu_fri_available:
                opportunities.append({
                    "holiday_name": holiday.name,
                    "holiday_date": holiday.date.isoformat(),
                    "holiday_weekday": "Mercoledì",
                    "bridge_date": thu.isoformat(),
                    "bridge_weekday": "Giovedì + Venerdì",
                    "vacation_days_needed": 2,
                    "total_days_off": 5,
                    "efficiency": 2.5,
                    "description": f"Ponte dopo {holiday.name}: prendi Giovedì e Venerdì per 5 giorni di riposo"
                })
    
    # Sort by efficiency (best opportunities first)
    opportunities.sort(key=lambda x: (-x["efficiency"], x["holiday_date"]))
    
    return opportunities
```

### 3.8.2.3 - Vacation Balance Calculator (RISCRITTA COMPLETAMENTE)
- [ ] 📝 Crea `backend/app/utils/vacation_balance.py`

```python
"""
Vacation balance calculator with separate tracking per type.

NUOVA ARCHITETTURA:
- Maturazione separata: Ferie (giorni/mese), ROL (ore/mese), Permessi (ore/mese)
- Tracking start date invece di carryover year
- Saldo iniziale opzionale (ferie in giorni, ROL/Permessi in ore)
- Calcolo totali aggregati per vista dashboard

Vista riepilogo:
- Ferie:    maturate Xh / usate Yh / disponibili Zh = Zd
- ROL:      maturate Xh / usate Yh / disponibili Zh = Zd
- Permessi: maturate Xh / usate Yh / disponibili Zh = Zd
- TOTALE:   disponibili Xh = Yd (somma di tutto)
"""
from datetime import date
from typing import Dict, List, Any, Optional
import calendar


def calculate_months_between(start_date: date, end_date: date) -> int:
    """
    Calculate the number of complete months between two dates.
    
    Examples:
        2025-03-01 to 2026-02-05 = 11 months
        2025-03-15 to 2026-02-05 = 10 months (March not complete)
    """
    months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    
    # If we haven't reached the same day in the end month, subtract 1
    if end_date.day < start_date.day:
        months -= 1
    
    return max(0, months)


def calculate_type_balance(
    type_name: str,
    accrual_per_month: float,
    months_worked: int,
    initial_hours: float,
    entries: List[Any],
    work_hours_per_day: float,
    type_label: str
) -> Dict:
    """
    Calculate balance for a single type (Ferie, ROL, or Permessi).
    
    Args:
        type_name: "ferie", "rol", or "permesso"
        accrual_per_month: Hours accrued per month (already converted to hours)
        months_worked: Number of months worked since tracking started
        initial_hours: Initial balance in hours
        entries: List of VacationEntry objects for this type
        work_hours_per_day: Hours per work day (for conversion to days)
        type_label: Italian label for display
        
    Returns:
        Dict with hours and days (accrued, used, available)
    """
    # Accrued
    hours_accrued = initial_hours + (accrual_per_month * months_worked)
    
    # Used
    hours_used = sum(e.hours for e in entries)
    
    # Available
    hours_available = hours_accrued - hours_used
    
    # Convert to days
    days_accrued = hours_accrued / work_hours_per_day
    days_used = hours_used / work_hours_per_day
    days_available = hours_available / work_hours_per_day
    
    return {
        "type": type_name,
        "label": type_label,
        "hours_accrued": round(hours_accrued, 1),
        "hours_used": round(hours_used, 1),
        "hours_available": round(hours_available, 1),
        "days_accrued": round(days_accrued, 1),
        "days_used": round(days_used, 1),
        "days_available": round(days_available, 1)
    }


def calculate_balance(
    settings: Any,
    entries: List[Any],
    year: int,
    month: Optional[int] = None
) -> Dict:
    """
    Calculate vacation balance for a user with SEPARATE TRACKING per type.
    
    NUOVA LOGICA:
    1. Calcola mesi lavorati da tracking_start_date
    2. Per ogni tipo (Ferie, ROL, Permessi):
       - Maturato = initial_hours + (accrual_per_month × months_worked)
       - Usato = somma ore entries di quel tipo
       - Disponibile = Maturato - Usato
    3. Totali aggregati per dashboard
    
    Args:
        settings: VacationSettings object
        entries: List of VacationEntry objects
        year: Year to calculate
        month: Optional month (1-12). If None, calculates up to end of year or current month.
        
    Returns:
        Dict with complete balance information including:
        - breakdown: List per tipo con ore+giorni (maturate, usate, disponibili)
        - total_hours_available: Somma ore disponibili (tutti i tipi)
        - total_days_available: Somma giorni disponibili (tutti i tipi)
        - tracking_start_date: Data inizio tracciamento
        - months_worked: Mesi lavorati da tracking_start_date
    """
    today = date.today()
    current_year = today.year
    current_month = today.month
    
    # Determine calculation period
    if month:
        target_month = month
    else:
        target_month = 12 if year < current_year else current_month
    
    # Calculate target date (last day of target month)
    _, last_day = calendar.monthrange(year, target_month)
    target_date = date(year, target_month, last_day)
    
    # Calculate months worked from tracking start
    months_worked = calculate_months_between(settings.tracking_start_date, target_date)
    
    # Separate entries by type
    entries_by_type = {
        "ferie": [e for e in entries if e.date.year == year and e.date.month <= target_month and e.entry_type.value == "ferie"],
        "rol": [e for e in entries if e.date.year == year and e.date.month <= target_month and e.entry_type.value == "rol"],
        "permesso": [e for e in entries if e.date.year == year and e.date.month <= target_month and e.entry_type.value == "permesso"],
    }
    
    # Get work hours per day
    hours_per_day = settings.work_hours_per_day or 8.0
    
    # === CALCULATE FERIE ===
    # Convert initial_ferie_DAYS to hours
    initial_ferie_hours = (settings.initial_ferie_days or 0.0) * hours_per_day
    # Convert ferie_DAYS_per_month to hours_per_month
    ferie_accrual_per_month = settings.ferie_days_per_month * hours_per_day
    
    ferie_data = calculate_type_balance(
        type_name="ferie",
        accrual_per_month=ferie_accrual_per_month,
        months_worked=months_worked,
        initial_hours=initial_ferie_hours,
        entries=entries_by_type["ferie"],
        work_hours_per_day=hours_per_day,
        type_label="Ferie"
    )
    
    # === CALCULATE ROL ===
    rol_data = calculate_type_balance(
        type_name="rol",
        accrual_per_month=settings.rol_hours_per_month,
        months_worked=months_worked,
        initial_hours=settings.initial_rol_hours or 0.0,
        entries=entries_by_type["rol"],
        work_hours_per_day=hours_per_day,
        type_label="ROL"
    )
    
    # === CALCULATE PERMESSI ===
    permessi_data = calculate_type_balance(
        type_name="permesso",
        accrual_per_month=settings.permessi_hours_per_month,
        months_worked=months_worked,
        initial_hours=settings.initial_permessi_hours or 0.0,
        entries=entries_by_type["permesso"],
        work_hours_per_day=hours_per_day,
        type_label="Permessi"
    )
    
    # === BUILD BREAKDOWN ===
    breakdown = [ferie_data, rol_data, permessi_data]
    
    # === AGGREGATE TOTALS ===
    total_hours_accrued = sum(b["hours_accrued"] for b in breakdown)
    total_hours_used = sum(b["hours_used"] for b in breakdown)
    total_hours_available = sum(b["hours_available"] for b in breakdown)
    total_days_available = sum(b["days_available"] for b in breakdown)
    
    # === PROJECTED END OF YEAR ===
    months_remaining = 12 - target_month if year == current_year else 0
    ferie_projected = ferie_data["hours_available"] + (ferie_accrual_per_month * months_remaining)
    rol_projected = rol_data["hours_available"] + (settings.rol_hours_per_month * months_remaining)
    permessi_projected = permessi_data["hours_available"] + (settings.permessi_hours_per_month * months_remaining)
    hours_projected_eoy = ferie_projected + rol_projected + permessi_projected
    days_projected_eoy = hours_projected_eoy / hours_per_day
    
    return {
        "year": year,
        "month": target_month,
        
        # Tracking info
        "tracking_start_date": settings.tracking_start_date,
        "months_worked": months_worked,
        
        # Totals (aggregated across all types)
        "total_hours_accrued": round(total_hours_accrued, 1),
        "total_hours_used": round(total_hours_used, 1),
        "total_hours_available": round(total_hours_available, 1),
        "total_days_available": round(total_days_available, 1),
        
        # Projected end of year
        "hours_projected_eoy": round(hours_projected_eoy, 1),
        "days_projected_eoy": round(days_projected_eoy, 1),
        
        # Breakdown per type
        "breakdown": breakdown,
        
        # Settings reference
        "settings": {
            "work_hours_per_day": hours_per_day,
            "ferie_days_per_month": settings.ferie_days_per_month,
            "rol_hours_per_month": settings.rol_hours_per_month,
            "permessi_hours_per_month": settings.permessi_hours_per_month
        }
    }


def calculate_monthly_projection(
    settings: Any,
    entries: List[Any],
    year: int,
    num_months: int = 12
) -> List[Dict]:
    """
    Calculate month-by-month projection for a year.
    
    Shows cumulative accrued, used, and available hours for each month.
    
    Args:
        settings: VacationSettings object
        entries: List of VacationEntry objects for the year
        year: Year to project
        num_months: Number of months to project (default 12)
        
    Returns:
        List of monthly projections
    """
    projections = []
    
    # Group entries by month (exclude malattia - already removed from enum)
    entries_by_month = {}
    for entry in entries:
        if entry.date.year == year:
            m = entry.date.month
            entries_by_month.setdefault(m, 0.0)
            entries_by_month[m] += entry.hours
    
    # Calculate cumulative balance
    hours_per_day = settings.work_hours_per_day or 8.0
    
    # Initial balance (convert ferie days to hours)
    initial_ferie_hours = (settings.initial_ferie_days or 0.0) * hours_per_day
    initial_total = initial_ferie_hours + (settings.initial_rol_hours or 0.0) + (settings.initial_permessi_hours or 0.0)
    
    # Monthly accrual (convert ferie days to hours)
    ferie_accrual_per_month = settings.ferie_days_per_month * hours_per_day
    monthly_accrual = ferie_accrual_per_month + settings.rol_hours_per_month + settings.permessi_hours_per_month
    
    cumulative_accrued = initial_total
    cumulative_used = 0.0
    
    for month in range(1, num_months + 1):
        cumulative_accrued += monthly_accrual
        cumulative_used += entries_by_month.get(month, 0.0)
        balance = cumulative_accrued - cumulative_used
        
        projections.append({
            "month": month,
            "month_name": ITALIAN_MONTHS[month],
            "hours_accrued_cumulative": round(cumulative_accrued, 1),
            "hours_used_cumulative": round(cumulative_used, 1),
            "hours_available": round(balance, 1),
            "days_available": round(balance / hours_per_day, 1)
        })
    
    return projections


# Month names
ITALIAN_MONTHS = {
    1: "Gennaio", 2: "Febbraio", 3: "Marzo", 4: "Aprile",
    5: "Maggio", 6: "Giugno", 7: "Luglio", 8: "Agosto",
    9: "Settembre", 10: "Ottobre", 11: "Novembre", 12: "Dicembre"
}
```

### 3.8.2.4 - Export utils in __init__
- [ ] 📝 Crea/Modifica `backend/app/utils/__init__.py`

```python
# Add these exports:
from app.utils.easter import calculate_easter_sunday, calculate_easter_monday, get_easter_dates
from app.utils.bridge_days import (
    find_bridge_opportunities, 
    get_italian_weekday, 
    is_weekend, 
    ITALIAN_WEEKDAYS,
    ITALIAN_MONTHS
)
from app.utils.vacation_balance import calculate_balance, calculate_monthly_projection
```

### 3.8.2.5 - Commit utilities
- [ ] Commit: `Add vacation utilities with separate accrual calculation`

---

## 📝 3.8.3 - Pydantic Schemas

Continua nel prossimo messaggio...

## 📝 3.8.3 - Pydantic Schemas (AGGIORNATI)

### 3.8.3.1 - Crea vacation schemas
- [ ] 📝 Crea `backend/app/schemas/vacation.py`

**MODIFICHE PRINCIPALI:**
- VacationSettingsBase: nuovi campi per maturazione separata
- BreakdownItem: aggiungere hours_available, days_available (rimuovere note)
- VacationBalanceResponse: aggiungere totali aggregati, rimuovere carryover
- Rimuovere riferimenti a "malattia"

```python
"""
Vacation-related Pydantic schemas for request/response validation.

UPDATED: Separate accrual rates, tracking start date, aggregated totals
"""
from datetime import date as date_type, datetime
from typing import Optional, List, Dict, Any
from uuid import UUID
from pydantic import BaseModel, Field, field_validator

from app.models.vacation_entry import VacationEntryType, MANUAL_HOURS_TYPES


# ==================== VACATION SETTINGS ====================

class VacationSettingsBase(BaseModel):
    """Base schema for vacation settings with separate accrual rates."""
    work_hours_per_day: float = Field(default=8.0, ge=1, le=24)
    
    # Accrual rates (separate per type!)
    ferie_days_per_month: float = Field(default=1.83, ge=0, le=10, 
        description="Days of vacation accrued per month (default 1.83 = 22 days/year)")
    rol_hours_per_month: float = Field(default=2.67, ge=0, le=200,
        description="ROL hours accrued per month (default 2.67 = 32 hours/year)")
    permessi_hours_per_month: float = Field(default=8.67, ge=0, le=200,
        description="Permission hours accrued per month (default 8.67 = 104 hours/year)")
    
    # Tracking start
    tracking_start_date: date_type = Field(description="Date when tracking started")
    
    # Initial balance (optional)
    initial_balance_month: Optional[int] = Field(None, ge=1, le=12)
    initial_balance_year: Optional[int] = Field(None, ge=2000, le=2100)
    initial_ferie_days: float = Field(default=0.0, ge=0, description="Initial vacation DAYS")
    initial_rol_hours: float = Field(default=0.0, ge=0, description="Initial ROL hours")
    initial_permessi_hours: float = Field(default=0.0, ge=0, description="Initial permission hours")
    
    @field_validator('tracking_start_date')
    @classmethod
    def tracking_start_not_future(cls, v):
        if v > date_type.today():
            raise ValueError('Tracking start date cannot be in the future')
        return v
    
    @field_validator('initial_balance_year')
    @classmethod
    def initial_balance_before_tracking(cls, v, info):
        if v and 'initial_balance_month' in info.data and 'tracking_start_date' in info.data:
            balance_month = info.data.get('initial_balance_month')
            tracking_start = info.data.get('tracking_start_date')
            if balance_month:
                balance_date = date_type(v, balance_month, 1)
                if balance_date > tracking_start:
                    raise ValueError('Initial balance date must be before or equal to tracking start date')
        return v


class VacationSettingsCreate(VacationSettingsBase):
    """Schema for creating vacation settings."""
    pass


class VacationSettingsUpdate(BaseModel):
    """Schema for updating vacation settings (all fields optional)."""
    work_hours_per_day: Optional[float] = Field(None, ge=1, le=24)
    ferie_days_per_month: Optional[float] = Field(None, ge=0, le=10)
    rol_hours_per_month: Optional[float] = Field(None, ge=0, le=200)
    permessi_hours_per_month: Optional[float] = Field(None, ge=0, le=200)
    tracking_start_date: Optional[date_type] = None
    initial_balance_month: Optional[int] = Field(None, ge=1, le=12)
    initial_balance_year: Optional[int] = Field(None, ge=2000, le=2100)
    initial_ferie_days: Optional[float] = Field(None, ge=0)
    initial_rol_hours: Optional[float] = Field(None, ge=0)
    initial_permessi_hours: Optional[float] = Field(None, ge=0)


class VacationSettingsResponse(VacationSettingsBase):
    """Schema for vacation settings response."""
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# ==================== VACATION ENTRY ====================

class VacationEntryBase(BaseModel):
    """Base schema for vacation entry."""
    date: date_type = Field(..., description="Date of the entry")
    entry_type: VacationEntryType = Field(
        default=VacationEntryType.FERIE, 
        description="Type: ferie, permesso, rol"
    )
    hours: Optional[float] = Field(
        None, 
        gt=0, 
        le=24, 
        description="Hours (required for ROL/permesso, automatic for ferie)"
    )
    notes: Optional[str] = Field(None, max_length=500)


class VacationEntryCreate(VacationEntryBase):
    """
    Schema for creating vacation entry.
    
    REGOLE:
    - Ferie: ore automatiche da work_hours_per_day (hours ignorato)
    - ROL/Permesso: hours obbligatorio
    """
    
    @field_validator('hours')
    @classmethod
    def validate_hours_for_type(cls, v, info):
        entry_type = info.data.get('entry_type', VacationEntryType.FERIE)
        
        # For manual types, hours is required
        if entry_type.value in MANUAL_HOURS_TYPES and v is None:
            raise ValueError(f'Hours is required for {entry_type.value}')
        
        return v


class VacationEntryUpdate(BaseModel):
    """Schema for updating vacation entry (all fields optional)."""
    entry_type: Optional[VacationEntryType] = None
    hours: Optional[float] = Field(None, gt=0, le=24)
    notes: Optional[str] = Field(None, max_length=500)


class VacationEntryResponse(VacationEntryBase):
    """Schema for vacation entry response."""
    id: UUID
    user_id: UUID
    hours: float  # Always present in response
    created_at: datetime
    updated_at: datetime
    day_name: Optional[str] = None
    type_label: Optional[str] = None
    
    class Config:
        from_attributes = True


class VacationEntryBulkCreate(BaseModel):
    """Schema for creating multiple entries (e.g., a week of vacation)."""
    start_date: date_type
    end_date: date_type
    entry_type: VacationEntryType = VacationEntryType.FERIE
    hours_per_day: Optional[float] = Field(None, gt=0, le=24,
        description="Hours per day (required for ROL/permesso, optional for ferie)")
    skip_weekends: bool = Field(default=True)
    skip_holidays: bool = Field(default=True)
    notes: Optional[str] = Field(None, max_length=500)
    
    @field_validator('end_date')
    @classmethod
    def end_after_start(cls, v, info):
        if 'start_date' in info.data and v < info.data['start_date']:
            raise ValueError('end_date must be >= start_date')
        return v


# ==================== USER HOLIDAY ====================

class UserHolidayBase(BaseModel):
    """Base schema for user custom holiday."""
    day: int = Field(..., ge=1, le=31)
    month: int = Field(..., ge=1, le=12)
    name: str = Field(..., min_length=1, max_length=100)
    recurring: bool = Field(default=True)
    year: Optional[int] = Field(None, ge=2000, le=2100)


class UserHolidayCreate(UserHolidayBase):
    """Schema for creating user holiday."""
    
    @field_validator('year')
    @classmethod
    def year_required_if_not_recurring(cls, v, info):
        recurring = info.data.get('recurring', True)
        if not recurring and v is None:
            raise ValueError('year is required for non-recurring holidays')
        return v
    
    @field_validator('day')
    @classmethod
    def validate_day_for_month(cls, v, info):
        """Validate that day is valid for the given month."""
        month = info.data.get('month')
        if month:
            import calendar
            max_day = calendar.monthrange(2024, month)[1]  # Use leap year
            if v > max_day:
                raise ValueError(f'Day {v} is invalid for month {month}')
        return v


class UserHolidayResponse(UserHolidayBase):
    """Schema for user holiday response."""
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# ==================== ITALIAN HOLIDAY ====================

class ItalianHolidayResponse(BaseModel):
    """Schema for Italian holiday response."""
    id: UUID
    date: date_type
    name: str
    name_en: Optional[str] = None
    is_fixed: bool
    is_national: bool
    day_name: Optional[str] = None
    
    class Config:
        from_attributes = True


# ==================== VACATION BALANCE (AGGIORNATO) ====================

class BreakdownItem(BaseModel):
    """Schema for balance breakdown by type WITH available hours."""
    type: str
    label: str
    hours_accrued: float
    hours_used: float
    hours_available: float  # NEW!
    days_accrued: float     # NEW!
    days_used: float
    days_available: float   # NEW!


class VacationBalanceResponse(BaseModel):
    """
    Schema for complete vacation balance with AGGREGATED TOTALS.
    
    NEW: Shows breakdown per type AND total available across all types
    """
    year: int
    month: int
    
    # Tracking info
    tracking_start_date: date_type
    months_worked: int
    
    # AGGREGATED TOTALS (across all types)
    total_hours_accrued: float
    total_hours_used: float
    total_hours_available: float
    total_days_available: float
    
    # Projected end of year
    hours_projected_eoy: float
    days_projected_eoy: float
    
    # Breakdown by type (Ferie, ROL, Permessi)
    breakdown: List[BreakdownItem]
    
    # Settings reference
    settings: Dict[str, float]


class MonthlyProjection(BaseModel):
    """Schema for monthly projection."""
    month: int
    month_name: str
    hours_accrued_cumulative: float
    hours_used_cumulative: float
    hours_available: float
    days_available: float


class VacationProjectionResponse(BaseModel):
    """Schema for full year projection."""
    year: int
    projections: List[MonthlyProjection]


# ==================== CALENDAR ====================

class CalendarDayResponse(BaseModel):
    """Schema for a single day in calendar view."""
    date: date_type
    day_number: int
    day_name: str
    is_weekend: bool
    is_today: bool
    is_holiday: bool
    holiday_name: Optional[str] = None
    is_user_holiday: bool = False
    user_holiday_name: Optional[str] = None
    is_bridge_opportunity: bool = False
    entries: List[VacationEntryResponse] = []
    total_hours: float = 0.0


class CalendarMonthResponse(BaseModel):
    """Schema for monthly calendar view."""
    year: int
    month: int
    month_name: str
    days: List[CalendarDayResponse]
    hours_accrued_this_month: float
    hours_used_this_month: float
    hours_available_end_of_month: float
    days_available_end_of_month: float


# ==================== BRIDGE OPPORTUNITIES ====================

class BridgeOpportunityResponse(BaseModel):
    """Schema for bridge day opportunity."""
    holiday_name: str
    holiday_date: str
    holiday_weekday: str
    bridge_date: Optional[str]
    bridge_weekday: str
    vacation_days_needed: int
    total_days_off: int
    efficiency: float
    description: str
```

### 3.8.3.2 - Update Schemas __init__.py
- [ ] 📝 Modifica `backend/app/schemas/__init__.py`

```python
# Add these imports (same as before, schemas are backward compatible):
from app.schemas.vacation import (
    VacationSettingsBase,
    VacationSettingsCreate,
    VacationSettingsUpdate,
    VacationSettingsResponse,
    VacationEntryBase,
    VacationEntryCreate,
    VacationEntryUpdate,
    VacationEntryResponse,
    VacationEntryBulkCreate,
    UserHolidayBase,
    UserHolidayCreate,
    UserHolidayResponse,
    ItalianHolidayResponse,
    BreakdownItem,
    VacationBalanceResponse,
    VacationProjectionResponse,
    CalendarDayResponse,
    CalendarMonthResponse,
    BridgeOpportunityResponse,
)
```

### 3.8.3.3 - Commit schemas
- [ ] Commit: `Update vacation schemas with separate accrual and aggregated totals`

---

## 🔧 3.8.4 - CRUD Operations (AGGIORNAMENTI)

Vedi documento originale per struttura base. **MODIFICHE PRINCIPALI:**

### 3.8.4.2 - Vacation Entry CRUD - AGGIUNGERE VALIDAZIONI

Nel file `backend/app/crud/vacation_entry.py`, funzione `create()`:

```python
def create(db: Session, user_id: UUID, entry: VacationEntryCreate) -> VacationEntry:
    """
    Create a new vacation entry.
    
    NUOVE VALIDAZIONI:
    - Non permette inserimento nei weekend
    - Non permette inserimento nelle festività nazionali
    - Non permette inserimento nelle festività custom utente
    """
    from app.utils.bridge_days import is_weekend
    from app.crud import italian_holiday as italian_holiday_crud
    from app.crud import user_holiday as user_holiday_crud
    
    # Check weekend
    if is_weekend(entry.date):
        raise ValueError("Non è possibile inserire ferie nel weekend")
    
    # Check Italian national holidays
    holiday = italian_holiday_crud.get_by_date(db, entry.date)
    if holiday:
        raise ValueError(f"Non è possibile inserire ferie durante: {holiday.name}")
    
    # Check user custom holidays
    year = entry.date.year
    user_holidays = user_holiday_crud.get_for_year(db, user_id, year)
    for uh in user_holidays:
        uh_date = uh.get_date_for_year(year)
        if uh_date == entry.date:
            raise ValueError(f"Non è possibile inserire ferie durante: {uh.name}")
    
    # Determine hours (rest of logic remains the same)
    if entry.entry_type.value in MANUAL_HOURS_TYPES:
        hours = entry.hours
    else:
        settings = get_settings(db, user_id)
        hours = settings.work_hours_per_day
    
    db_entry = VacationEntry(
        user_id=user_id,
        date=entry.date,
        entry_type=entry.entry_type,
        hours=hours,
        notes=entry.notes
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry
```

**NOTA:** CRUD per settings, italian_holiday, user_holiday rimangono invariati (già corretti nel documento originale)

---

## 🌐 3.8.5 - API Router (AGGIORNAMENTI CRITICI)

Vedi documento originale per struttura base. **MODIFICHE PRINCIPALI:**

### Endpoint `/entries/bulk` - FIX VALIDAZIONE

```python
@router.post("/entries/bulk", response_model=List[VacationEntryResponse], status_code=status.HTTP_201_CREATED)
async def create_bulk_entries(
    bulk: VacationEntryBulkCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create multiple entries for a date range (e.g., a week of vacation)."""
    
    # FIX: Validare hours_per_day PRIMA di qualsiasi elaborazione
    if bulk.entry_type.value in MANUAL_HOURS_TYPES:
        if bulk.hours_per_day is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"hours_per_day è obbligatorio per {bulk.entry_type.value}"
            )
        hours = bulk.hours_per_day
    else:
        # Ferie: usa settings o hours_per_day se specificato
        settings = vacation_settings_crud.get_or_create(db, current_user.id)
        hours = bulk.hours_per_day if bulk.hours_per_day else settings.work_hours_per_day
    
    # Build set di tutte le festività (nazionali + utente)
    all_holiday_dates = set()
    
    if bulk.skip_holidays:
        # Get year from date range
        year = bulk.start_date.year
        
        # Festività nazionali
        holidays = italian_holiday_crud.ensure_holidays_exist(db, year)
        for h in holidays:
            all_holiday_dates.add(h.date)
        
        # Festività utente
        user_holidays = user_holiday_crud.get_for_year(db, current_user.id, year)
        for uh in user_holidays:
            uh_date = uh.get_date_for_year(year)
            if uh_date:
                all_holiday_dates.add(uh_date)
    
    # Create entries
    entries_data = []
    current_date = bulk.start_date
    
    while current_date <= bulk.end_date:
        # Skip weekends
        if bulk.skip_weekends and is_weekend(current_date):
            current_date += timedelta(days=1)
            continue
        
        # Skip holidays (nazionali + utente)
        if current_date in all_holiday_dates:
            current_date += timedelta(days=1)
            continue
        
        # Check if entry already exists
        existing = vacation_entry_crud.get_by_date(db, current_user.id, current_date)
        if existing:
            current_date += timedelta(days=1)
            continue
        
        entries_data.append({
            "date": current_date,
            "entry_type": bulk.entry_type,
            "hours": hours,
            "notes": bulk.notes
        })
        
        current_date += timedelta(days=1)
    
    if not entries_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nessuna data valida nel range (tutte saltate o già presenti)"
        )
    
    # Bulk create
    entries = vacation_entry_crud.create_bulk(db, current_user.id, entries_data)
    
    # Build response
    result = []
    for entry in entries:
        resp = VacationEntryResponse.model_validate(entry)
        resp.day_name = get_italian_weekday(entry.date)
        resp.type_label = VACATION_ENTRY_TYPE_LABELS.get(entry.entry_type.value)
        result.append(resp)
    
    return result
```

### Endpoint `/calendar/{year}/{month}` - OTTIMIZZAZIONE

```python
@router.get("/calendar/{year}/{month}", response_model=CalendarMonthResponse)
async def get_calendar_month(
    year: int,
    month: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get calendar view for a specific month."""
    
    if month < 1 or month > 12:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Month must be 1-12")
    
    # Get holidays
    holidays = italian_holiday_crud.ensure_holidays_exist(db, year)
    holidays_by_date = {h.date: h for h in holidays}
    
    # Get user custom holidays
    user_holidays = user_holiday_crud.get_for_year(db, current_user.id, year)
    user_holidays_by_date = {}
    for uh in user_holidays:
        uh_date = uh.get_date_for_year(year)
        if uh_date:
            user_holidays_by_date[uh_date] = uh
    
    # Get bridge opportunities
    bridges = find_bridge_opportunities(holidays, year, user_holidays)
    bridge_dates = set()
    for b in bridges:
        if b["bridge_date"]:
            bridge_dates.add(date.fromisoformat(b["bridge_date"]))
    
    # OTTIMIZZAZIONE: Una sola query per tutto l'anno
    all_entries = vacation_entry_crud.get_by_year(db, current_user.id, year)
    
    # Filtra per il mese corrente
    month_entries = [e for e in all_entries if e.date.month == month]
    entries_by_date = {e.date: e for e in month_entries}
    
    # Build calendar days
    from calendar import monthrange
    _, num_days = monthrange(year, month)
    today = date.today()
    
    days = []
    hours_used_this_month = 0.0
    
    for day in range(1, num_days + 1):
        current_date = date(year, month, day)
        
        entry = entries_by_date.get(current_date)
        total_hours = 0.0
        entry_responses = []
        
        if entry:
            total_hours = entry.hours
            hours_used_this_month += total_hours
            
            resp = VacationEntryResponse.model_validate(entry)
            resp.day_name = get_italian_weekday(entry.date)
            resp.type_label = VACATION_ENTRY_TYPE_LABELS.get(entry.entry_type.value)
            entry_responses.append(resp)
        
        holiday = holidays_by_date.get(current_date)
        user_holiday = user_holidays_by_date.get(current_date)
        
        days.append(CalendarDayResponse(
            date=current_date,
            day_number=day,
            day_name=get_italian_weekday(current_date),
            is_weekend=is_weekend(current_date),
            is_today=(current_date == today),
            is_holiday=(holiday is not None),
            holiday_name=holiday.name if holiday else None,
            is_user_holiday=(user_holiday is not None),
            user_holiday_name=user_holiday.name if user_holiday else None,
            is_bridge_opportunity=(current_date in bridge_dates),
            entries=entry_responses,
            total_hours=total_hours
        ))
    
    # Get settings for balance calculation (usa all_entries già caricati)
    settings = vacation_settings_crud.get_or_create(db, current_user.id)
    balance = calculate_balance(settings, all_entries, year, month)
    
    # Calculate monthly accrual
    ferie_accrual = settings.ferie_days_per_month * settings.work_hours_per_day
    total_accrual = ferie_accrual + settings.rol_hours_per_month + settings.permessi_hours_per_month
    
    return CalendarMonthResponse(
        year=year,
        month=month,
        month_name=ITALIAN_MONTHS[month],
        days=days,
        hours_accrued_this_month=total_accrual,
        hours_used_this_month=hours_used_this_month,
        hours_available_end_of_month=balance["total_hours_available"],
        days_available_end_of_month=balance["total_days_available"]
    )
```

**NOTA:** Gli altri endpoint rimangono invariati.

---

## 🧪 3.8.6 - Manual Testing

Stesso testing del documento originale, con aggiunta:

- [ ] Test nuovo calcolo balance con breakdown separato
- [ ] Test tracking_start_date e initial balance
- [ ] Test validazione festività in create entry
- [ ] Test bulk create con skip festività

---

## 🎯 CHECKPOINT FASE 3.8

**Database:**
- [ ] ✅ Tabella `vacation_settings` con campi separati (ferie_days_per_month, rol_hours_per_month, permessi_hours_per_month)
- [ ] ✅ Tabella `vacation_entries` (con UniqueConstraint, NO malattia)
- [ ] ✅ Tabella `italian_holidays`
- [ ] ✅ Tabella `user_holidays`

**Models:**
- [ ] ✅ VacationSettings con maturazione separata
- [ ] ✅ VacationEntry senza malattia
- [ ] ✅ UserHoliday con validazione date

**Business Logic:**
- [ ] ✅ Ferie: giorni/mese → ore (conversione automatica)
- [ ] ✅ ROL/Permessi: ore/mese dirette
- [ ] ✅ Balance calculator con totali aggregati
- [ ] ✅ Validazione weekend + festività in create/bulk

**API Endpoints:**
- [ ] ✅ GET/PUT /vacation/settings (nuovi campi)
- [ ] ✅ GET/POST /vacation/entries (con validazione festività)
- [ ] ✅ POST /vacation/entries/bulk (con fix validazione + skip festività)
- [ ] ✅ GET /vacation/balance (con breakdown completo + totali)
- [ ] ✅ GET /vacation/calendar (con ottimizzazione query)

**Tempo stimato:** 3-4 giorni  
**Prossimo:** FASE 4.6 - Testing Vacation Module

---

## 📝 Note Implementazione

### Default Settings Italia (AGGIORNATI)
- **Ferie:** 1.83 giorni/mese = 22 giorni/anno
- **ROL:** 2.67 ore/mese = 32 ore/anno = 4 giorni
- **Permessi:** 8.67 ore/mese = 104 ore/anno = 13 giorni
- **TOTALE:** 39 giorni/anno (312 ore con giornata 8h)
- **Ore giornaliere:** 8h (configurabile dall'utente)

### Tipi Entry (AGGIORNATO - NO MALATTIA)
- **ferie**: Ore automatiche da work_hours_per_day
- **permesso**: Ore manuali
- **rol**: Ore manuali

### Vista Riepilogo (NUOVA)
```
TOTALE DISPONIBILE: 196h = 24.5 giorni

Dettaglio:
- Ferie:    maturate 176h / usate 64h / disponibili 112h = 14.0gg
- ROL:      maturate  32h / usate 12h / disponibili  20h =  2.5gg
- Permessi: maturate 104h / usate 40h / disponibili  64h =  8.0gg
```

### Validazioni (NUOVE)
- ❌ NO inserimento weekend
- ❌ NO inserimento festività nazionali
- ❌ NO inserimento festività custom utente
- ✅ Un solo entry per giorno
- ✅ ROL/Permessi richiedono ore manuali
- ✅ Ferie usano ore automatiche

**Prossimo:** FASE 4 - Testing & Debug

---

# FASE 4: Testing & Debug (2 giorni)

## 🎯 Obiettivo
Implementare test automatici con Pytest e correggere bug trovati.

---

### 4.1 - Setup Pytest

#### 4.1.1 - Test dependencies
- [ ] Verifica che `pytest`, `pytest-asyncio`, `httpx` siano in `requirements.txt`
- [ ] Se mancano, aggiungili e fai `pip install`

#### 4.1.2 - Test configuration
- [ ] 📝 Crea `backend/pytest.ini`

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
asyncio_mode = auto
```

#### 4.1.3 - Test database setup
- [ ] 📝 Crea `backend/tests/__init__.py` (vuoto)
- [ ] 📝 Crea `backend/tests/conftest.py`

```python
"""
Pytest fixtures
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.config import settings
from main import app

# Test database URL
TEST_DATABASE_URL = "postgresql://budget_user:password@localhost:5432/budget_app_test"

# Create test engine
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    """Database session fixture"""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db):
    """Test client fixture"""
    def override_get_db():
        try:
            yield db
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def test_user_data():
    """Test user data"""
    return {
        "email": "test@example.com",
        "password": "TestPass123",
        "full_name": "Test User"
    }
```

⚠️ **IMPORTANTE:** Prima di eseguire i test:
- [ ] Crea database test in pgAdmin: `budget_app_test`
- [ ] Stessi permessi di `budget_app_dev`

#### 4.1.4 - Commit test setup
- [ ] Commit: `Add Pytest configuration`

---

### 4.2 - Test Authentication

#### 4.2.1 - Auth tests
- [ ] 📝 Crea `backend/tests/test_auth.py`

```python
"""
Test Authentication endpoints
"""
import pytest


def test_register_user(client, test_user_data):
    """Test user registration"""
    response = client.post("/api/v1/auth/register", json=test_user_data)
    assert response.status_code == 201
    data = response.json()
    assert "access_token" in data
    assert data["user"]["email"] == test_user_data["email"]


def test_register_duplicate_email(client, test_user_data):
    """Test registration with duplicate email"""
    client.post("/api/v1/auth/register", json=test_user_data)
    response = client.post("/api/v1/auth/register", json=test_user_data)
    assert response.status_code == 400


def test_login_success(client, test_user_data):
    """Test successful login"""
    client.post("/api/v1/auth/register", json=test_user_data)
    
    response = client.post("/api/v1/auth/login", json={
        "email": test_user_data["email"],
        "password": test_user_data["password"]
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


def test_login_wrong_password(client, test_user_data):
    """Test login with wrong password"""
    client.post("/api/v1/auth/register", json=test_user_data)
    
    response = client.post("/api/v1/auth/login", json={
        "email": test_user_data["email"],
        "password": "WrongPassword"
    })
    assert response.status_code == 401


def test_get_me_authenticated(client, test_user_data):
    """Test get profile with valid token"""
    register_response = client.post("/api/v1/auth/register", json=test_user_data)
    token = register_response.json()["access_token"]
    
    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == test_user_data["email"]


def test_get_me_without_token(client):
    """Test get profile without token"""
    response = client.get("/api/v1/auth/me")
    assert response.status_code == 403  # o 401, dipende da implementazione
```

#### 4.2.2 - Run auth tests
- [ ] Nel terminal:
```bash
pytest tests/test_auth.py -v
```
- [ ] Verifica che tutti i test passino
- [ ] Se qualche test fallisce, debugga e correggi

#### 4.2.3 - Commit auth tests
- [ ] Commit: `Add authentication tests`

---

### 4.3 - Test Accounts

#### 4.3.1 - Account tests
- [ ] 📝 Crea `backend/tests/test_accounts.py`
- [ ] Implementa test per:
  - [ ] Create account
  - [ ] List accounts
  - [ ] Get account detail
  - [ ] Update account
  - [ ] Delete account
  - [ ] Access denied (utente A non può vedere account di utente B)

#### 4.3.2 - Run account tests
- [ ] `pytest tests/test_accounts.py -v`

#### 4.3.3 - Commit
- [ ] Commit: `Add account tests`

---

### 4.4 - Test Transactions & Transfers

#### 4.4.1 - Transaction tests
- [ ] 📝 Crea `backend/tests/test_transactions.py`
- [ ] Test creazione transaction
- [ ] **Test che balance account si aggiorni correttamente**
- [ ] Test filtri

#### 4.4.2 - Transfer tests
- [ ] 📝 Crea `backend/tests/test_transfers.py`
- [ ] Test transfer
- [ ] **Test che entrambi i balance si aggiornino**

#### 4.4.3 - Run tests
- [ ] `pytest tests/ -v`

#### 4.4.4 - Commit
- [ ] Commit: `Add transaction and transfer tests`

---

### 4.5 - Coverage Report

#### 4.5.1 - Install coverage
- [ ] `pip install pytest-cov`
- [ ] Aggiungi a `requirements.txt`

#### 4.5.2 - Run with coverage
- [ ] `pytest --cov=app --cov-report=html`
- [ ] Apri `htmlcov/index.html` in browser
- [ ] Verifica coverage (obiettivo: >70%)

#### 4.5.3 - Commit coverage
- [ ] Aggiungi `htmlcov/` a `.gitignore`
- [ ] Commit: `Add test coverage reporting`

---

## 🎯 CHECKPOINT FASE 4

- [ ] ✅ Pytest configurato e funzionante
- [ ] ✅ Test database separato da development
- [ ] ✅ Test authentication completi e passanti
- [ ] ✅ Test accounts completi
- [ ] ✅ Test transactions completi
- [ ] ✅ Test transfers completi
- [ ] ✅ Coverage report generato (>70%)
- [ ] ✅ Tutti i bug trovati corretti
- [ ] ✅ CI/CD ready (test automatici)

**Comando per eseguire tutti i test:**
```bash
pytest tests/ -v --cov=app
```

**Tempo stimato:** 2 giorni

# FASE 4.6: Testing Vacation Module (1-2 giorni)

## 🎯 Obiettivo
Implementare test automatici con Pytest per il modulo Vacation Planning con maturazione separata per tipo.

**AGGIORNAMENTI:**
- Test nuovi campi VacationSettings (ferie_days_per_month, rol_hours_per_month, permessi_hours_per_month)
- Test tracking_start_date e initial balance
- Test validazione weekend + festività
- Test balance con totali aggregati
- Rimozione test malattia

---

## 🧪 4.6.1 - Setup Test Fixtures (AGGIORNATI)

### 4.6.1.1 - Aggiungi fixtures per vacation
- [ ] 📝 Modifica `backend/tests/conftest.py` - aggiungi:

```python
from datetime import date

@pytest.fixture
def vacation_settings_data():
    """Test vacation settings data with separate accrual rates."""
    return {
        "work_hours_per_day": 8.0,
        "ferie_days_per_month": 1.83,
        "rol_hours_per_month": 2.67,
        "permessi_hours_per_month": 8.67,
        "tracking_start_date": "2025-01-01",  # Fixed date for consistent tests
        "initial_ferie_days": 0.0,
        "initial_rol_hours": 0.0,
        "initial_permessi_hours": 0.0
    }


@pytest.fixture
def vacation_settings_with_initial_balance():
    """Test settings with initial balance."""
    return {
        "work_hours_per_day": 8.0,
        "ferie_days_per_month": 1.83,
        "rol_hours_per_month": 2.67,
        "permessi_hours_per_month": 8.67,
        "tracking_start_date": "2026-01-01",
        "initial_balance_month": 12,
        "initial_balance_year": 2025,
        "initial_ferie_days": 10.0,  # 10 days
        "initial_rol_hours": 16.0,
        "initial_permessi_hours": 40.0
    }


@pytest.fixture
def vacation_entry_ferie_data():
    """Test vacation entry data for FERIE (no hours - automatic)."""
    # Use fixed future date for consistent tests
    return {
        "date": "2027-06-15",  # Fixed Wednesday, safe date
        "entry_type": "ferie",
        "notes": "Test vacation day"
    }


@pytest.fixture
def vacation_entry_rol_data():
    """Test vacation entry data for ROL (manual hours required)."""
    return {
        "date": "2027-06-16",  # Fixed Thursday, safe date
        "entry_type": "rol",
        "hours": 4.0,
        "notes": "Test ROL entry"
    }


@pytest.fixture
def user_holiday_data():
    """Test user holiday data (patron saint)."""
    return {
        "day": 7,
        "month": 12,
        "name": "Sant'Ambrogio",
        "recurring": True
    }
```

---

## 🧪 4.6.2 - Test Vacation Settings (AGGIORNATI)

- [ ] 📝 Crea `backend/tests/test_vacation_settings.py`

```python
"""Test Vacation Settings endpoints with separate accrual rates."""
import pytest


class TestVacationSettings:
    
    def test_get_settings_creates_default(self, client, auth_headers):
        """GET creates default settings if none exist."""
        response = client.get("/api/v1/vacation/settings", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert data["ferie_days_per_month"] == 1.83
        assert data["rol_hours_per_month"] == 2.67
        assert data["permessi_hours_per_month"] == 8.67
        assert data["work_hours_per_day"] == 8.0
        assert "tracking_start_date" in data
    
    def test_update_accrual_rates(self, client, auth_headers):
        """Test updating separate accrual rates."""
        client.get("/api/v1/vacation/settings", headers=auth_headers)
        response = client.put(
            "/api/v1/vacation/settings",
            headers=auth_headers,
            json={
                "ferie_days_per_month": 2.0,  # Custom: 24 days/year
                "rol_hours_per_month": 4.0,
                "work_hours_per_day": 7.5
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["ferie_days_per_month"] == 2.0
        assert data["rol_hours_per_month"] == 4.0
        assert data["work_hours_per_day"] == 7.5
    
    def test_initial_balance_validation(self, client, auth_headers):
        """Initial balance date must be before tracking start."""
        response = client.put(
            "/api/v1/vacation/settings",
            headers=auth_headers,
            json={
                "tracking_start_date": "2026-01-01",
                "initial_balance_year": 2026,
                "initial_balance_month": 6,  # After tracking start
                "initial_ferie_days": 10.0
            }
        )
        assert response.status_code == 422
    
    def test_settings_requires_auth(self, client):
        """Settings endpoint requires authentication."""
        response = client.get("/api/v1/vacation/settings")
        assert response.status_code == 401
```

- [ ] Esegui: `pytest tests/test_vacation_settings.py -v`

---

## 🧪 4.6.3 - Test Vacation Entries (AGGIORNATI)

- [ ] 📝 Crea `backend/tests/test_vacation_entries.py`

```python
"""Test Vacation Entries endpoints with weekend/holiday validation."""
import pytest
from datetime import date, timedelta


class TestVacationEntries:
    
    def test_create_ferie_automatic_hours(self, client, auth_headers, vacation_entry_ferie_data):
        """FERIE entry gets automatic hours from settings."""
        client.get("/api/v1/vacation/settings", headers=auth_headers)
        
        response = client.post(
            "/api/v1/vacation/entries",
            headers=auth_headers,
            json=vacation_entry_ferie_data
        )
        assert response.status_code == 201
        data = response.json()
        assert data["entry_type"] == "ferie"
        assert data["hours"] == 8.0  # Automatic from settings
    
    def test_create_rol_requires_hours(self, client, auth_headers):
        """ROL entry requires manual hours."""
        response = client.post(
            "/api/v1/vacation/entries",
            headers=auth_headers,
            json={
                "date": "2027-06-17",
                "entry_type": "rol"
                # Missing hours
            }
        )
        assert response.status_code == 422
    
    def test_create_rol_with_hours(self, client, auth_headers, vacation_entry_rol_data):
        """ROL entry with manual hours succeeds."""
        response = client.post(
            "/api/v1/vacation/entries",
            headers=auth_headers,
            json=vacation_entry_rol_data
        )
        assert response.status_code == 201
        assert response.json()["hours"] == 4.0
    
    def test_weekend_validation(self, client, auth_headers):
        """Cannot create entry on weekend."""
        client.get("/api/v1/vacation/settings", headers=auth_headers)
        
        # June 14, 2027 is Saturday
        response = client.post(
            "/api/v1/vacation/entries",
            headers=auth_headers,
            json={
                "date": "2027-06-14",
                "entry_type": "ferie"
            }
        )
        assert response.status_code == 400
        assert "weekend" in response.json()["detail"].lower()
    
    def test_holiday_validation(self, client, auth_headers):
        """Cannot create entry on national holiday."""
        client.get("/api/v1/vacation/settings", headers=auth_headers)
        
        # January 1 is Capodanno
        response = client.post(
            "/api/v1/vacation/entries",
            headers=auth_headers,
            json={
                "date": "2027-01-01",
                "entry_type": "ferie"
            }
        )
        assert response.status_code == 400
        assert "festività" in response.json()["detail"].lower() or "holiday" in response.json()["detail"].lower()
    
    def test_duplicate_date_fails(self, client, auth_headers, vacation_entry_ferie_data):
        """Only one entry per date allowed."""
        client.get("/api/v1/vacation/settings", headers=auth_headers)
        client.post("/api/v1/vacation/entries", headers=auth_headers, json=vacation_entry_ferie_data)
        
        # Try same date with different type
        duplicate_data = vacation_entry_ferie_data.copy()
        duplicate_data["entry_type"] = "rol"
        duplicate_data["hours"] = 4.0
        response = client.post("/api/v1/vacation/entries", headers=auth_headers, json=duplicate_data)
        assert response.status_code == 400
    
    def test_list_entries(self, client, auth_headers, vacation_entry_ferie_data):
        """Test listing vacation entries."""
        client.get("/api/v1/vacation/settings", headers=auth_headers)
        client.post("/api/v1/vacation/entries", headers=auth_headers, json=vacation_entry_ferie_data)
        response = client.get("/api/v1/vacation/entries", headers=auth_headers)
        assert response.status_code == 200
        assert len(response.json()) >= 1
    
    def test_update_entry(self, client, auth_headers, vacation_entry_rol_data):
        """Test updating entry hours."""
        client.get("/api/v1/vacation/settings", headers=auth_headers)
        create_resp = client.post("/api/v1/vacation/entries", headers=auth_headers, json=vacation_entry_rol_data)
        entry_id = create_resp.json()["id"]
        
        response = client.put(
            f"/api/v1/vacation/entries/{entry_id}",
            headers=auth_headers,
            json={"hours": 6.0}
        )
        assert response.status_code == 200
        assert response.json()["hours"] == 6.0
    
    def test_delete_entry(self, client, auth_headers, vacation_entry_ferie_data):
        """Test deleting entry."""
        client.get("/api/v1/vacation/settings", headers=auth_headers)
        create_resp = client.post("/api/v1/vacation/entries", headers=auth_headers, json=vacation_entry_ferie_data)
        entry_id = create_resp.json()["id"]
        
        response = client.delete(f"/api/v1/vacation/entries/{entry_id}", headers=auth_headers)
        assert response.status_code == 204
```

- [ ] Esegui: `pytest tests/test_vacation_entries.py -v`

---

## 🧪 4.6.4 - Test User Holidays (INVARIATO)

Stesso codice del documento originale.

---

## 🧪 4.6.5 - Test Bulk Entries (AGGIORNATO)

- [ ] 📝 Crea `backend/tests/test_vacation_bulk.py`

```python
"""Test Vacation Bulk Entry creation with holiday skipping."""
import pytest
from datetime import date, timedelta


class TestVacationBulk:
    
    def test_bulk_create_week(self, client, auth_headers):
        """Test bulk creating a week of vacation."""
        client.get("/api/v1/vacation/settings", headers=auth_headers)
        
        # Use safe fixed dates (June 2027)
        bulk_data = {
            "start_date": "2027-06-21",  # Monday
            "end_date": "2027-06-25",    # Friday
            "entry_type": "ferie",
            "skip_weekends": True,
            "skip_holidays": True
        }
        
        response = client.post("/api/v1/vacation/entries/bulk", headers=auth_headers, json=bulk_data)
        assert response.status_code == 201
        data = response.json()
        assert len(data) == 5  # Mon-Fri
    
    def test_bulk_skips_weekends(self, client, auth_headers):
        """Bulk create skips weekends."""
        client.get("/api/v1/vacation/settings", headers=auth_headers)
        
        bulk_data = {
            "start_date": "2027-06-18",  # Friday
            "end_date": "2027-06-21",    # Monday (includes weekend)
            "entry_type": "ferie",
            "skip_weekends": True,
            "skip_holidays": False
        }
        
        response = client.post("/api/v1/vacation/entries/bulk", headers=auth_headers, json=bulk_data)
        data = response.json()
        
        # Should only have Friday and Monday (skip Sat/Sun)
        assert len(data) == 2
        for entry in data:
            entry_date = date.fromisoformat(entry["date"])
            assert entry_date.weekday() < 5  # No weekends
    
    def test_bulk_skips_holidays(self, client, auth_headers):
        """Bulk create skips national holidays."""
        client.get("/api/v1/vacation/settings", headers=auth_headers)
        
        # Include Capodanno (Jan 1) and Epifania (Jan 6) in range
        bulk_data = {
            "start_date": "2027-01-01",  # Friday (Capodanno)
            "end_date": "2027-01-08",    # Friday
            "entry_type": "ferie",
            "skip_weekends": True,
            "skip_holidays": True
        }
        
        response = client.post("/api/v1/vacation/entries/bulk", headers=auth_headers, json=bulk_data)
        data = response.json()
        
        # Should skip: Jan 1 (holiday), Jan 2-3 (weekend), Jan 6 (holiday)
        # Should include: Jan 4, 5, 7, 8 (4 days)
        assert len(data) == 4
    
    def test_bulk_rol_requires_hours(self, client, auth_headers):
        """Bulk ROL requires hours_per_day."""
        bulk_data = {
            "start_date": "2027-06-21",
            "end_date": "2027-06-23",
            "entry_type": "rol",
            "skip_weekends": True
            # Missing hours_per_day
        }
        
        response = client.post("/api/v1/vacation/entries/bulk", headers=auth_headers, json=bulk_data)
        assert response.status_code == 400
        assert "hours_per_day" in response.json()["detail"].lower()
```

- [ ] Esegui: `pytest tests/test_vacation_bulk.py -v`

---

## 🧪 4.6.6 - Test Balance & Calendar (AGGIORNATO)

- [ ] 📝 Crea `backend/tests/test_vacation_balance.py`

```python
"""Test Vacation Balance and Calendar endpoints with aggregated totals."""
import pytest


class TestVacationBalance:
    
    def test_get_balance_structure(self, client, auth_headers):
        """Test balance response structure with aggregated totals."""
        client.get("/api/v1/vacation/settings", headers=auth_headers)
        response = client.get("/api/v1/vacation/balance", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        
        # Check aggregated totals
        assert "total_hours_accrued" in data
        assert "total_hours_used" in data
        assert "total_hours_available" in data
        assert "total_days_available" in data
        
        # Check tracking info
        assert "tracking_start_date" in data
        assert "months_worked" in data
        
        # Check breakdown structure
        assert "breakdown" in data
        breakdown_types = [b["type"] for b in data["breakdown"]]
        assert "ferie" in breakdown_types
        assert "rol" in breakdown_types
        assert "permesso" in breakdown_types
        
        # Check breakdown items have all fields
        for item in data["breakdown"]:
            assert "hours_accrued" in item
            assert "hours_used" in item
            assert "hours_available" in item
            assert "days_available" in item
    
    def test_balance_with_initial_balance(self, client, auth_headers, vacation_settings_with_initial_balance):
        """Test balance calculation with initial balance."""
        # Set settings with initial balance
        client.put("/api/v1/vacation/settings", headers=auth_headers, json=vacation_settings_with_initial_balance)
        
        response = client.get("/api/v1/vacation/balance", headers=auth_headers)
        data = response.json()
        
        # Should include initial balance
        assert data["total_hours_available"] > 0
        
        # Ferie should start with 10 days = 80h
        ferie_item = next(b for b in data["breakdown"] if b["type"] == "ferie")
        assert ferie_item["hours_accrued"] >= 80.0  # At least initial


class TestVacationCalendar:
    
    def test_get_calendar_month(self, client, auth_headers):
        """Test monthly calendar view."""
        response = client.get("/api/v1/vacation/calendar/2027/6", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert data["year"] == 2027
        assert data["month"] == 6
        assert len(data["days"]) == 30  # June has 30 days
    
    def test_calendar_shows_holidays(self, client, auth_headers):
        """Calendar marks national holidays."""
        response = client.get("/api/v1/vacation/calendar/2027/1", headers=auth_headers)
        data = response.json()
        jan1 = next(d for d in data["days"] if d["day_number"] == 1)
        assert jan1["is_holiday"] == True
        assert jan1["holiday_name"] == "Capodanno"
    
    def test_calendar_shows_user_holidays(self, client, auth_headers, user_holiday_data):
        """Calendar marks user custom holidays."""
        # Add patron saint
        client.post("/api/v1/vacation/user-holidays", headers=auth_headers, json=user_holiday_data)
        
        response = client.get("/api/v1/vacation/calendar/2027/12", headers=auth_headers)
        data = response.json()
        dec7 = next(d for d in data["days"] if d["day_number"] == 7)
        assert dec7["is_user_holiday"] == True
        assert dec7["user_holiday_name"] == "Sant'Ambrogio"


class TestVacationHolidays:
    
    def test_get_holidays(self, client, auth_headers):
        """Test getting holidays for year."""
        response = client.get("/api/v1/vacation/holidays/2027", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 11  # 10 fixed + Pasquetta


class TestVacationBridges:
    
    def test_get_bridges(self, client, auth_headers):
        """Test getting bridge opportunities."""
        response = client.get("/api/v1/vacation/bridges/2027", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
```

- [ ] Esegui: `pytest tests/test_vacation_balance.py -v`

---

## 🧪 4.6.7 - Run All Vacation Tests

### 4.6.7.1 - Run complete suite
- [ ] Esegui: `pytest tests/test_vacation*.py tests/test_user_holidays.py -v`
- [ ] Verifica tutti i test passano

### 4.6.7.2 - Coverage report
- [ ] Esegui: `pytest tests/test_vacation*.py tests/test_user_holidays.py --cov=app.routers.vacation --cov=app.crud --cov=app.utils.vacation_balance --cov-report=term-missing`
- [ ] Target: ≥70% coverage

### 4.6.7.3 - Commit
- [ ] Commit: `Add Pytest tests for vacation module with separate accrual (Phase 4.6)`

---

## 🎯 CHECKPOINT FASE 4.6

- [ ] ✅ test_vacation_settings.py - nuovi campi testati
- [ ] ✅ test_vacation_entries.py - validazione weekend/festività
- [ ] ✅ test_user_holidays.py - tutti passano
- [ ] ✅ test_vacation_bulk.py - skip holidays testato
- [ ] ✅ test_vacation_balance.py - totali aggregati testati
- [ ] ✅ Coverage ≥70%

**Test principali verificati:**
- [ ] ✅ Settings con maturazione separata (ferie/rol/permessi)
- [ ] ✅ Tracking start date e initial balance
- [ ] ✅ Ferie: ore automatiche da settings
- [ ] ✅ ROL/Permessi: ore manuali obbligatorie
- [ ] ✅ Validazione weekend bloccata
- [ ] ✅ Validazione festività nazionali bloccata
- [ ] ✅ Un solo entry per data (UniqueConstraint)
- [ ] ✅ Balance con breakdown + totali aggregati
- [ ] ✅ Calendar mostra festività nazionali e custom
- [ ] ✅ Bulk create skip weekend + holidays

**Tempo stimato:** 1-2 giorni  
 
**Prossimo:** FASE 5 - Frontend Integration

---

# FASE 5: Frontend Integration (5-7 giorni)

## 🎯 Obiettivo
Migrare frontend da localStorage a API calls, implementare autenticazione e connettere tutte le features.

---

### 5.1 - React Project Setup

#### 5.1.1 - Crea React app con Vite
- [ ] Apri terminal nella root del progetto
- [ ] Esegui:
```bash
npm create vite@latest frontend -- --template react
cd frontend
npm install
```

#### 5.1.2 - Installa dipendenze
- [ ] `npm install axios recharts date-fns`
- [ ] `npm install react-router-dom`
- [ ] `npm install -D tailwindcss postcss autoprefixer`
- [ ] `npx tailwindcss init -p`

#### 5.1.3 - Configura Tailwind
- [ ] 📝 Modifica `frontend/tailwind.config.js`

```js
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

- [ ] 📝 Aggiungi in `frontend/src/index.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

#### 5.1.4 - Test dev server
- [ ] `npm run dev`
- [ ] Apri http://localhost:5173
- [ ] Dovresti vedere app Vite di default

#### 5.1.5 - Commit frontend setup
- [ ] Commit: `Setup React frontend with Vite`

---

### 5.2 - API Service Layer

#### 5.2.1 - Axios instance
- [ ] 📝 Crea `frontend/src/services/api.js`

```javascript
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor per aggiungere token a ogni richiesta
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Interceptor per gestire errori auth
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;
```

#### 5.2.2 - Auth service
- [ ] 📝 Crea `frontend/src/services/authService.js`

```javascript
import api from './api';

export const authService = {
  async register(email, password, fullName) {
    const response = await api.post('/auth/register', {
      email,
      password,
      full_name: fullName,
    });
    return response.data;
  },

  async login(email, password) {
    const response = await api.post('/auth/login', { email, password });
    if (response.data.access_token) {
      localStorage.setItem('token', response.data.access_token);
      localStorage.setItem('user', JSON.stringify(response.data.user));
    }
    return response.data;
  },

  async getProfile() {
    const response = await api.get('/auth/me');
    return response.data;
  },

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    window.location.href = '/login';
  },

  getCurrentUser() {
    const userStr = localStorage.getItem('user');
    return userStr ? JSON.parse(userStr) : null;
  },

  isAuthenticated() {
    return !!localStorage.getItem('token');
  },
};
```

#### 5.2.3 - Account service
- [ ] 📝 Crea `frontend/src/services/accountService.js`

```javascript
import api from './api';

export const accountService = {
  async getAccounts() {
    const response = await api.get('/accounts');
    return response.data;
  },

  async createAccount(accountData) {
    const response = await api.post('/accounts', accountData);
    return response.data;
  },

  async updateAccount(id, accountData) {
    const response = await api.put(`/accounts/${id}`, accountData);
    return response.data;
  },

  async deleteAccount(id) {
    await api.delete(`/accounts/${id}`);
  },
};
```

#### 5.2.4 - Altri services
- [ ] 📝 Crea `frontend/src/services/transactionService.js`
- [ ] 📝 Crea `frontend/src/services/categoryService.js`
- [ ] 📝 Crea `frontend/src/services/transferService.js`
- [ ] 📝 Crea `frontend/src/services/analyticsService.js`

💡 Implementa pattern simile ad `accountService`

#### 5.2.5 - Environment variables
- [ ] 📝 Crea `frontend/.env`

```env
VITE_API_URL=http://localhost:8000/api/v1
```

⚠️ Aggiungi `.env` a `.gitignore` se non presente

#### 5.2.6 - Commit services
- [ ] Commit: `Add API service layer`

---

### 5.3 - Authentication Pages

#### 5.3.1 - Login page
- [ ] 📝 Crea `frontend/src/pages/Login.jsx`

```jsx
import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { authService } from '../services/authService';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      await authService.login(email, password);
      navigate('/dashboard');
    } catch (err) {
      setError(err.response?.data?.detail || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full space-y-8 p-8 bg-white rounded-lg shadow">
        <h2 className="text-3xl font-bold text-center">Login</h2>
        
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-gray-700">Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md"
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400"
          >
            {loading ? 'Loading...' : 'Login'}
          </button>
        </form>

        <p className="text-center text-sm text-gray-600">
          Don't have an account?{' '}
          <Link to="/register" className="text-blue-600 hover:text-blue-500">
            Register
          </Link>
        </p>
      </div>
    </div>
  );
}
```

#### 5.3.2 - Register page
- [ ] 📝 Crea `frontend/src/pages/Register.jsx`
- [ ] Implementa form registrazione simile a Login

#### 5.3.3 - Protected Route component
- [ ] 📝 Crea `frontend/src/components/ProtectedRoute.jsx`

```jsx
import { Navigate } from 'react-router-dom';
import { authService } from '../services/authService';

export default function ProtectedRoute({ children }) {
  if (!authService.isAuthenticated()) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
```

#### 5.3.4 - Commit auth pages
- [ ] Commit: `Add authentication pages`

---

### 5.4 - Main Application Layout

#### 5.4.1 - App Router
- [ ] 📝 Modifica `frontend/src/App.jsx`

```jsx
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import Accounts from './pages/Accounts';
import Transactions from './pages/Transactions';
import ProtectedRoute from './components/ProtectedRoute';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        
        <Route path="/dashboard" element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        } />
        
        <Route path="/accounts" element={
          <ProtectedRoute>
            <Accounts />
          </ProtectedRoute>
        } />
        
        <Route path="/transactions" element={
          <ProtectedRoute>
            <Transactions />
          </ProtectedRoute>
        } />
        
        <Route path="/" element={<Navigate to="/dashboard" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
```

#### 5.4.2 - Navigation component
- [ ] 📝 Crea `frontend/src/components/Navbar.jsx`
- [ ] Include links e logout button

#### 5.4.3 - Commit layout
- [ ] Commit: `Add application layout and routing`

---

### 5.5 - Dashboard Implementation

#### 5.5.1 - Dashboard page
- [ ] 📝 Crea `frontend/src/pages/Dashboard.jsx`
- [ ] Usa `analyticsService.getSummary()`
- [ ] Mostra:
  - [ ] Total balance
  - [ ] Total income (mese corrente)
  - [ ] Total expense (mese corrente)
  - [ ] Account cards
  - [ ] Recent transactions

#### 5.5.2 - Test dashboard
- [ ] Assicurati backend sia in esecuzione
- [ ] Avvia frontend: `npm run dev`
- [ ] Fai login
- [ ] Verifica che dashboard carichi dati da API

#### 5.5.3 - Commit dashboard
- [ ] Commit: `Implement dashboard with API integration`

---

### 5.6 - Accounts Management

#### 5.6.1 - Accounts page
- [ ] 📝 Crea `frontend/src/pages/Accounts.jsx`
- [ ] Lista accounts da API
- [ ] Form create/edit account
- [ ] Delete account con conferma

#### 5.6.2 - Test accounts CRUD
- [ ] Crea account
- [ ] Verifica apparizione lista
- [ ] Modifica account
- [ ] Elimina account

#### 5.6.3 - Commit accounts
- [ ] Commit: `Implement accounts management`

---

### 5.7 - Transactions Management

#### 5.7.1 - Transactions page
- [ ] 📝 Crea `frontend/src/pages/Transactions.jsx`
- [ ] Lista transactions con filtri
- [ ] Form create transaction
- [ ] Categories dropdown
- [ ] Accounts dropdown

#### 5.7.2 - Test transactions
- [ ] Crea transaction income
- [ ] Verifica balance account aggiornato
- [ ] Crea transaction expense
- [ ] Test filtri (date, account, category)

#### 5.7.3 - Commit transactions
- [ ] Commit: `Implement transactions management`

---

### 5.8 - Final Integration Tests

#### 5.8.1 - Test end-to-end workflow
1. [ ] Register nuovo utente
2. [ ] Crea 2-3 accounts
3. [ ] Crea categorie custom
4. [ ] Aggiungi 10+ transactions
5. [ ] Crea transfer tra account
6. [ ] Verifica dashboard aggiornata correttamente
7. [ ] Test filtri e ricerca
8. [ ] Test su diversi browser (Chrome, Firefox, Safari)

#### 5.8.2 - Bug fixing
- [ ] Lista bug trovati
- [ ] Prioritizza e correggi
- [ ] Re-test

#### 5.8.3 - Commit final integration
- [ ] Commit: `Final integration and bug fixes`

---

## 🎯 CHECKPOINT FASE 5

- [ ] ✅ React frontend connesso a backend API
- [ ] ✅ Authentication flow completo (register, login, logout)
- [ ] ✅ Protected routes funzionanti
- [ ] ✅ Dashboard con dati real-time
- [ ] ✅ Accounts CRUD completo
- [ ] ✅ Transactions CRUD completo
- [ ] ✅ Transfers funzionanti
- [ ] ✅ Balance accounts si aggiorna automaticamente
- [ ] ✅ Nessun uso di localStorage per dati (solo token)
- [ ] ✅ App testata end-to-end
- [ ] ✅ No critical bugs

**Test completo:**
- [ ] User può registrarsi, creare accounts e transactions
- [ ] Dati persistono nel database
- [ ] Logout e re-login mostra stessi dati
- [ ] Multi-user: User A non vede dati di User B

**Tempo stimato:** 5-7 giorni

# FASE 5.9: Frontend Vacation Module (3-4 giorni)

## 🎯 Obiettivo
Implementare l'interfaccia React per il modulo Vacation Planning con:
- Maturazione separata per tipo (Ferie/ROL/Permessi)
- Vista totali aggregati in dashboard
- Inserimento multiplo (bulk)
- Validazione weekend + festività
- Calendario interattivo

**AGGIORNAMENTI RISPETTO ALLA VERSIONE PRECEDENTE:**
- Settings: form con campi separati per ogni tipo + tracking start + saldo iniziale
- Balance: mostra totali aggregati + breakdown dettagliato
- Entry Modal: ferie no input ore, ROL/Permessi sì (invariato)
- **NUOVO:** Bulk Entry Modal per inserimento multiplo
- Calendar: mostra festività custom utente (invariato)

---

## 📋 Componenti da Creare

1. **VacationDashboard** - Overview con balance aggregato e prossime festività
2. **VacationCalendar** - Calendario mensile interattivo
3. **VacationEntryModal** - Modal per creare/modificare entry (singolo giorno)
4. **BulkEntryModal** - 🆕 Modal per inserimento multiplo (range date)
5. **VacationSettings** - 🔄 Form aggiornato con maturazione separata
6. **BridgeOpportunities** - Lista ponti disponibili
7. **VacationBalance** - 🔄 Widget con totali aggregati + breakdown
8. **UserHolidaysManager** - Gestione festività custom (patrono)

---

## 🛠️ 5.9.1 - API Service (AGGIORNATO)

### 5.9.1.1 - Crea vacation service
- [ ] 📝 Crea `frontend/src/services/vacationService.js`

```javascript
import api from './api';

const vacationService = {
  // Settings
  getSettings: () => api.get('/vacation/settings'),
  updateSettings: (data) => api.put('/vacation/settings', data),
  
  // Entries
  getEntries: (params) => api.get('/vacation/entries', { params }),
  createEntry: (data) => api.post('/vacation/entries', data),
  createBulkEntries: (data) => api.post('/vacation/entries/bulk', data),  // NEW!
  getEntry: (id) => api.get(`/vacation/entries/${id}`),
  updateEntry: (id, data) => api.put(`/vacation/entries/${id}`, data),
  deleteEntry: (id) => api.delete(`/vacation/entries/${id}`),
  
  // Balance
  getBalance: (params) => api.get('/vacation/balance', { params }),
  getProjection: (year) => api.get(`/vacation/projection/${year}`),
  
  // Calendar
  getCalendarMonth: (year, month) => api.get(`/vacation/calendar/${year}/${month}`),
  
  // Holidays
  getHolidays: (year) => api.get(`/vacation/holidays/${year}`),
  getBridges: (year) => api.get(`/vacation/bridges/${year}`),
  
  // User Holidays (custom - patrono)
  getUserHolidays: () => api.get('/vacation/user-holidays'),
  createUserHoliday: (data) => api.post('/vacation/user-holidays', data),
  deleteUserHoliday: (id) => api.delete(`/vacation/user-holidays/${id}`),
  
  // Entry types
  getEntryTypes: () => api.get('/vacation/entry-types'),
};

export default vacationService;
```

---

## 📅 5.9.2 - Vacation Calendar Component (INVARIATO)

Stesso codice del documento originale - funziona già correttamente.

---

## 📝 5.9.3 - Entry Modal Component (INVARIATO)

Stesso codice del documento originale - gestisce già correttamente Ferie (no input ore) vs ROL/Permessi (input ore).

---

## 🆕 5.9.4 - Bulk Entry Modal Component (NUOVO!)

- [ ] 📝 Crea `frontend/src/components/vacation/BulkEntryModal.jsx`

```jsx
import React, { useState, useEffect } from 'react';
import vacationService from '../../services/vacationService';

const BulkEntryModal = ({ onClose, onSave }) => {
  const [formData, setFormData] = useState({
    start_date: '',
    end_date: '',
    entry_type: 'ferie',
    hours_per_day: null,  // Only for ROL/Permessi
    skip_weekends: true,
    skip_holidays: true,
    notes: ''
  });
  const [entryTypes, setEntryTypes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [previewCount, setPreviewCount] = useState(null);

  useEffect(() => {
    loadEntryTypes();
  }, []);

  useEffect(() => {
    // Calculate preview count when dates change
    if (formData.start_date && formData.end_date) {
      calculatePreview();
    }
  }, [formData.start_date, formData.end_date, formData.skip_weekends, formData.skip_holidays]);

  const loadEntryTypes = async () => {
    try {
      const response = await vacationService.getEntryTypes();
      setEntryTypes(response.data);
    } catch (err) {
      console.error('Error loading entry types:', err);
    }
  };

  const calculatePreview = () => {
    // Simple client-side preview (approximation)
    const start = new Date(formData.start_date);
    const end = new Date(formData.end_date);
    let count = 0;
    let current = new Date(start);

    while (current <= end) {
      const dayOfWeek = current.getDay();
      
      // Skip weekends if enabled
      if (formData.skip_weekends && (dayOfWeek === 0 || dayOfWeek === 6)) {
        current.setDate(current.getDate() + 1);
        continue;
      }
      
      count++;
      current.setDate(current.getDate() + 1);
    }

    setPreviewCount(count);
  };

  // Check if current type requires manual hours
  const requiresManualHours = () => {
    const type = entryTypes.find(t => t.value === formData.entry_type);
    return type?.manual_hours === true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    try {
      // Build payload
      const payload = {
        start_date: formData.start_date,
        end_date: formData.end_date,
        entry_type: formData.entry_type,
        skip_weekends: formData.skip_weekends,
        skip_holidays: formData.skip_holidays,
        notes: formData.notes || null
      };
      
      // Only include hours_per_day for manual types
      if (requiresManualHours()) {
        if (!formData.hours_per_day) {
          setError('Le ore per giorno sono obbligatorie per ROL e Permessi');
          setLoading(false);
          return;
        }
        payload.hours_per_day = formData.hours_per_day;
      }
      
      const response = await vacationService.createBulkEntries(payload);
      const createdCount = response.data.length;
      
      alert(`✅ Create ${createdCount} voci con successo!`);
      onSave();
    } catch (err) {
      const detail = err.response?.data?.detail || 'Errore durante la creazione';
      setError(detail);
    }
    setLoading(false);
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content bulk-modal" onClick={e => e.stopPropagation()}>
        <h3>📅 Inserimento Multiplo Ferie</h3>
        <p className="modal-description">
          Crea ferie per un periodo continuativo. Il sistema salterà automaticamente weekend e festività.
        </p>
        
        {error && <div className="error-message">{error}</div>}
        
        <form onSubmit={handleSubmit}>
          {/* Date Range */}
          <div className="form-row">
            <div className="form-group">
              <label>Data Inizio</label>
              <input
                type="date"
                value={formData.start_date}
                onChange={e => setFormData({...formData, start_date: e.target.value})}
                required
              />
            </div>
            
            <div className="form-group">
              <label>Data Fine</label>
              <input
                type="date"
                value={formData.end_date}
                min={formData.start_date}
                onChange={e => setFormData({...formData, end_date: e.target.value})}
                required
              />
            </div>
          </div>
          
          {/* Entry Type */}
          <div className="form-group">
            <label>Tipo</label>
            <select
              value={formData.entry_type}
              onChange={e => setFormData({...formData, entry_type: e.target.value})}
              required
            >
              {entryTypes.map(t => (
                <option key={t.value} value={t.value}>{t.label}</option>
              ))}
            </select>
            {!requiresManualHours() && (
              <small className="help-text">
                Le ore saranno calcolate automaticamente dalle tue impostazioni
              </small>
            )}
          </div>
          
          {/* Hours per day - ONLY for ROL/Permessi */}
          {requiresManualHours() && (
            <div className="form-group">
              <label>Ore per giorno</label>
              <input
                type="number"
                min="0.5"
                max="24"
                step="0.5"
                value={formData.hours_per_day || ''}
                onChange={e => setFormData({...formData, hours_per_day: parseFloat(e.target.value)})}
                placeholder="Es: 4"
                required
              />
              <small className="help-text">
                Quante ore vuoi inserire per ogni giorno nel range
              </small>
            </div>
          )}
          
          {/* Options */}
          <div className="form-group checkbox-group">
            <label>
              <input
                type="checkbox"
                checked={formData.skip_weekends}
                onChange={e => setFormData({...formData, skip_weekends: e.target.checked})}
              />
              <span>Salta weekend (Sabato e Domenica)</span>
            </label>
          </div>
          
          <div className="form-group checkbox-group">
            <label>
              <input
                type="checkbox"
                checked={formData.skip_holidays}
                onChange={e => setFormData({...formData, skip_holidays: e.target.checked})}
              />
              <span>Salta festività (nazionali e custom)</span>
            </label>
          </div>
          
          {/* Notes */}
          <div className="form-group">
            <label>Note (opzionale)</label>
            <textarea
              value={formData.notes}
              onChange={e => setFormData({...formData, notes: e.target.value})}
              rows="2"
              placeholder="Es: Vacanza estiva"
            />
          </div>
          
          {/* Preview */}
          {previewCount !== null && (
            <div className="bulk-preview">
              <span className="preview-icon">📊</span>
              <span>
                Verranno create circa <strong>{previewCount} voci</strong>
                {formData.skip_holidays && ' (escludendo festività)'}
              </span>
            </div>
          )}
          
          {/* Actions */}
          <div className="modal-actions">
            <button type="button" onClick={onClose} disabled={loading}>
              Annulla
            </button>
            <button type="submit" disabled={loading} className="btn-primary">
              {loading ? 'Creazione...' : `✅ Crea Periodo`}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default BulkEntryModal;
```

---

## 💰 5.9.5 - Balance Widget (COMPLETAMENTE AGGIORNATO)

- [ ] 📝 Crea `frontend/src/components/vacation/VacationBalance.jsx`

**NUOVA STRUTTURA:** Mostra totali aggregati + breakdown dettagliato per tipo

```jsx
import React, { useState, useEffect } from 'react';
import vacationService from '../../services/vacationService';

const VacationBalance = () => {
  const [balance, setBalance] = useState(null);
  const [year, setYear] = useState(new Date().getFullYear());
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadBalance();
  }, [year]);

  const loadBalance = async () => {
    setLoading(true);
    try {
      const response = await vacationService.getBalance({ year });
      setBalance(response.data);
    } catch (error) {
      console.error('Error loading balance:', error);
    }
    setLoading(false);
  };

  const getTypeIcon = (type) => {
    const icons = {
      ferie: '🏖️',
      rol: '🕐',
      permesso: '📋'
    };
    return icons[type] || '📄';
  };

  const getTypeColor = (type) => {
    const colors = {
      ferie: 'blue',
      rol: 'green',
      permesso: 'purple'
    };
    return colors[type] || 'gray';
  };

  if (loading) return <div className="loading">Caricamento...</div>;
  if (!balance) return null;

  return (
    <div className="vacation-balance">
      {/* Header with Year Selector */}
      <div className="balance-header">
        <h3>📊 Riepilogo Ferie {balance.year}</h3>
        <div className="year-selector">
          <button onClick={() => setYear(year - 1)}>◀</button>
          <span>{year}</span>
          <button onClick={() => setYear(year + 1)}>▶</button>
        </div>
      </div>
      
      {/* === MAIN TOTAL (AGGREGATED) === */}
      <div className="balance-total-card">
        <div className="total-header">
          <h2>Totale Disponibile</h2>
          <p className="tracking-info">
            📅 Tracciamento dal {new Date(balance.tracking_start_date).toLocaleDateString('it-IT')}
            ({balance.months_worked} {balance.months_worked === 1 ? 'mese' : 'mesi'})
          </p>
        </div>
        
        <div className="total-values">
          <div className="total-days">
            <span className="value">{balance.total_days_available.toFixed(1)}</span>
            <span className="unit">giorni</span>
          </div>
          <div className="total-hours">
            <span className="value">{balance.total_hours_available.toFixed(1)}</span>
            <span className="unit">ore</span>
          </div>
        </div>
        
        <div className="total-breakdown-mini">
          <div className="mini-stat">
            <span className="label">Maturate</span>
            <span className="value">{balance.total_hours_accrued.toFixed(1)}h</span>
          </div>
          <div className="mini-stat separator">-</div>
          <div className="mini-stat">
            <span className="label">Usate</span>
            <span className="value">{balance.total_hours_used.toFixed(1)}h</span>
          </div>
          <div className="mini-stat separator">=</div>
          <div className="mini-stat highlight">
            <span className="label">Residue</span>
            <span className="value">{balance.total_hours_available.toFixed(1)}h</span>
          </div>
        </div>
      </div>
      
      {/* === BREAKDOWN BY TYPE === */}
      <div className="balance-breakdown">
        <h4>Dettaglio per Tipo</h4>
        
        <div className="breakdown-grid">
          {balance.breakdown.map((item) => (
            <div key={item.type} className={`balance-type-card ${getTypeColor(item.type)}`}>
              <div className="type-header">
                <span className="type-icon">{getTypeIcon(item.type)}</span>
                <h5>{item.label}</h5>
              </div>
              
              <div className="type-stats">
                <div className="stat-row">
                  <span className="stat-label">Maturate</span>
                  <span className="stat-value">
                    {item.days_accrued.toFixed(1)}gg
                    <small>({item.hours_accrued.toFixed(1)}h)</small>
                  </span>
                </div>
                
                <div className="stat-row">
                  <span className="stat-label">Usate</span>
                  <span className="stat-value">
                    {item.days_used.toFixed(1)}gg
                    <small>({item.hours_used.toFixed(1)}h)</small>
                  </span>
                </div>
                
                <div className="stat-row highlight">
                  <span className="stat-label">Disponibili</span>
                  <span className="stat-value">
                    <strong>{item.days_available.toFixed(1)}gg</strong>
                    <small>({item.hours_available.toFixed(1)}h)</small>
                  </span>
                </div>
              </div>
              
              {/* Progress Bar */}
              <div className="usage-bar">
                <div 
                  className="usage-fill" 
                  style={{ 
                    width: `${Math.min(100, (item.hours_used / item.hours_accrued) * 100)}%` 
                  }}
                ></div>
              </div>
              <div className="usage-label">
                {((item.hours_used / item.hours_accrued) * 100).toFixed(0)}% utilizzato
              </div>
            </div>
          ))}
        </div>
      </div>
      
      {/* === PROJECTION === */}
      <div className="balance-projection">
        <h4>📈 Proiezione Fine Anno</h4>
        <div className="projection-value">
          {balance.days_projected_eoy.toFixed(1)} giorni
          <small>({balance.hours_projected_eoy.toFixed(1)} ore)</small>
        </div>
        <p className="projection-note">
          Stima basata su maturazione senza ulteriori utilizzi
        </p>
      </div>
      
      {/* === SETTINGS REFERENCE === */}
      <div className="balance-settings">
        <details>
          <summary>ℹ️ Info Configurazione</summary>
          <div className="settings-details">
            <p>Ore giornaliere: {balance.settings.work_hours_per_day}h</p>
            <p>Maturazione mensile:</p>
            <ul>
              <li>Ferie: {balance.settings.ferie_days_per_month} giorni/mese</li>
              <li>ROL: {balance.settings.rol_hours_per_month} ore/mese</li>
              <li>Permessi: {balance.settings.permessi_hours_per_month} ore/mese</li>
            </ul>
          </div>
        </details>
      </div>
    </div>
  );
};

export default VacationBalance;
```

---

## ⚙️ 5.9.6 - Settings Component (COMPLETAMENTE RISCRITTO)

- [ ] 📝 Crea `frontend/src/components/vacation/VacationSettings.jsx`

**NUOVA STRUTTURA:** Form con maturazione separata + tracking start + saldo iniziale

```jsx
import React, { useState, useEffect } from 'react';
import vacationService from '../../services/vacationService';

const VacationSettings = () => {
  const [settings, setSettings] = useState(null);
  const [formData, setFormData] = useState({
    work_hours_per_day: 8.0,
    ferie_days_per_month: 1.83,
    rol_hours_per_month: 2.67,
    permessi_hours_per_month: 8.67,
    tracking_start_date: '',
    initial_balance_month: null,
    initial_balance_year: null,
    initial_ferie_days: 0,
    initial_rol_hours: 0,
    initial_permessi_hours: 0
  });
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);
  const [showInitialBalance, setShowInitialBalance] = useState(false);

  useEffect(() => {
    loadSettings();
  }, []);

  const loadSettings = async () => {
    setLoading(true);
    try {
      const response = await vacationService.getSettings();
      setSettings(response.data);
      
      // Populate form
      setFormData({
        work_hours_per_day: response.data.work_hours_per_day,
        ferie_days_per_month: response.data.ferie_days_per_month,
        rol_hours_per_month: response.data.rol_hours_per_month,
        permessi_hours_per_month: response.data.permessi_hours_per_month,
        tracking_start_date: response.data.tracking_start_date,
        initial_balance_month: response.data.initial_balance_month || null,
        initial_balance_year: response.data.initial_balance_year || null,
        initial_ferie_days: response.data.initial_ferie_days || 0,
        initial_rol_hours: response.data.initial_rol_hours || 0,
        initial_permessi_hours: response.data.initial_permessi_hours || 0
      });
      
      // Show initial balance section if data exists
      if (response.data.initial_balance_year) {
        setShowInitialBalance(true);
      }
    } catch (err) {
      console.error('Error loading settings:', err);
      setError('Errore nel caricamento delle impostazioni');
    }
    setLoading(false);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSaving(true);
    setError('');
    setSuccess(false);
    
    try {
      // Build payload
      const payload = {
        work_hours_per_day: formData.work_hours_per_day,
        ferie_days_per_month: formData.ferie_days_per_month,
        rol_hours_per_month: formData.rol_hours_per_month,
        permessi_hours_per_month: formData.permessi_hours_per_month,
        tracking_start_date: formData.tracking_start_date
      };
      
      // Add initial balance if enabled
      if (showInitialBalance) {
        payload.initial_balance_month = formData.initial_balance_month;
        payload.initial_balance_year = formData.initial_balance_year;
        payload.initial_ferie_days = formData.initial_ferie_days;
        payload.initial_rol_hours = formData.initial_rol_hours;
        payload.initial_permessi_hours = formData.initial_permessi_hours;
      }
      
      await vacationService.updateSettings(payload);
      setSuccess(true);
      setTimeout(() => setSuccess(false), 3000);
      
      // Reload to refresh
      loadSettings();
    } catch (err) {
      const detail = err.response?.data?.detail || 'Errore durante il salvataggio';
      setError(detail);
    }
    setSaving(false);
  };

  const calculateAnnual = (monthly) => {
    return (monthly * 12).toFixed(1);
  };

  if (loading) return <div className="loading">Caricamento...</div>;

  return (
    <div className="vacation-settings">
      <h3>⚙️ Configurazione Ferie</h3>
      
      {error && <div className="error-message">{error}</div>}
      {success && <div className="success-message">✅ Impostazioni salvate con successo!</div>}
      
      <form onSubmit={handleSubmit}>
        {/* === WORK CONFIGURATION === */}
        <section className="settings-section">
          <h4>💼 Configurazione Ore Lavorative</h4>
          
          <div className="form-group">
            <label>Ore lavorative al giorno</label>
            <input
              type="number"
              step="0.5"
              min="1"
              max="24"
              value={formData.work_hours_per_day}
              onChange={e => setFormData({...formData, work_hours_per_day: parseFloat(e.target.value)})}
              required
            />
            <small className="help-text">
              Usate per convertire giorni in ore (es: 1 giorno = {formData.work_hours_per_day}h)
            </small>
          </div>
        </section>
        
        {/* === ACCRUAL RATES === */}
        <section className="settings-section">
          <h4>📊 Maturazione Mensile</h4>
          <p className="section-description">
            Configura quante ferie, ROL e permessi maturi ogni mese secondo il tuo contratto.
          </p>
          
          <div className="form-group">
            <label>🏖️ Ferie (giorni al mese)</label>
            <input
              type="number"
              step="0.01"
              min="0"
              max="10"
              value={formData.ferie_days_per_month}
              onChange={e => setFormData({...formData, ferie_days_per_month: parseFloat(e.target.value)})}
              required
            />
            <small className="help-text">
              = {calculateAnnual(formData.ferie_days_per_month)} giorni/anno
              ({calculateAnnual(formData.ferie_days_per_month * formData.work_hours_per_day)} ore/anno)
            </small>
          </div>
          
          <div className="form-group">
            <label>🕐 ROL (ore al mese)</label>
            <input
              type="number"
              step="0.01"
              min="0"
              max="200"
              value={formData.rol_hours_per_month}
              onChange={e => setFormData({...formData, rol_hours_per_month: parseFloat(e.target.value)})}
              required
            />
            <small className="help-text">
              = {calculateAnnual(formData.rol_hours_per_month)} ore/anno
              ({(calculateAnnual(formData.rol_hours_per_month) / formData.work_hours_per_day).toFixed(1)} giorni/anno)
            </small>
          </div>
          
          <div className="form-group">
            <label>📋 Permessi (ore al mese)</label>
            <input
              type="number"
              step="0.01"
              min="0"
              max="200"
              value={formData.permessi_hours_per_month}
              onChange={e => setFormData({...formData, permessi_hours_per_month: parseFloat(e.target.value)})}
              required
            />
            <small className="help-text">
              = {calculateAnnual(formData.permessi_hours_per_month)} ore/anno
              ({(calculateAnnual(formData.permessi_hours_per_month) / formData.work_hours_per_day).toFixed(1)} giorni/anno)
            </small>
          </div>
          
          <div className="total-preview">
            <strong>Totale annuo:</strong> {' '}
            {(
              parseFloat(calculateAnnual(formData.ferie_days_per_month)) +
              (parseFloat(calculateAnnual(formData.rol_hours_per_month)) / formData.work_hours_per_day) +
              (parseFloat(calculateAnnual(formData.permessi_hours_per_month)) / formData.work_hours_per_day)
            ).toFixed(1)} giorni
          </div>
        </section>
        
        {/* === TRACKING START === */}
        <section className="settings-section">
          <h4>📅 Inizio Tracciamento</h4>
          <p className="section-description">
            Indica da quando hai iniziato a maturare ferie (es: data di assunzione o cambio contratto).
          </p>
          
          <div className="form-group">
            <label>Data inizio maturazione</label>
            <input
              type="date"
              value={formData.tracking_start_date}
              onChange={e => setFormData({...formData, tracking_start_date: e.target.value})}
              max={new Date().toISOString().split('T')[0]}
              required
            />
            <small className="help-text">
              Il sistema calcolerà automaticamente le ore maturate da questa data
            </small>
          </div>
        </section>
        
        {/* === INITIAL BALANCE (OPTIONAL) === */}
        <section className="settings-section">
          <h4>💰 Saldo Iniziale (Opzionale)</h4>
          
          <div className="form-group checkbox-group">
            <label>
              <input
                type="checkbox"
                checked={showInitialBalance}
                onChange={e => setShowInitialBalance(e.target.checked)}
              />
              <span>Ho già ore/giorni maturati prima dell'inizio tracking</span>
            </label>
          </div>
          
          {showInitialBalance && (
            <div className="initial-balance-form">
              <p className="section-description">
                Inserisci il saldo che avevi a un mese specifico, prima di iniziare a usare questa app.
              </p>
              
              <div className="form-row">
                <div className="form-group">
                  <label>Mese di riferimento</label>
                  <select
                    value={formData.initial_balance_month || ''}
                    onChange={e => setFormData({...formData, initial_balance_month: parseInt(e.target.value)})}
                    required={showInitialBalance}
                  >
                    <option value="">Seleziona mese</option>
                    {[...Array(12)].map((_, i) => (
                      <option key={i+1} value={i+1}>
                        {new Date(2000, i).toLocaleString('it-IT', { month: 'long' })}
                      </option>
                    ))}
                  </select>
                </div>
                
                <div className="form-group">
                  <label>Anno</label>
                  <input
                    type="number"
                    min="2000"
                    max={new Date().getFullYear()}
                    value={formData.initial_balance_year || ''}
                    onChange={e => setFormData({...formData, initial_balance_year: parseInt(e.target.value)})}
                    required={showInitialBalance}
                  />
                </div>
              </div>
              
              <div className="form-group">
                <label>🏖️ Ferie maturate (giorni)</label>
                <input
                  type="number"
                  step="0.5"
                  min="0"
                  value={formData.initial_ferie_days}
                  onChange={e => setFormData({...formData, initial_ferie_days: parseFloat(e.target.value) || 0})}
                />
                <small className="help-text">
                  Quanti giorni di ferie avevi già maturato
                </small>
              </div>
              
              <div className="form-group">
                <label>🕐 ROL maturate (ore)</label>
                <input
                  type="number"
                  step="0.5"
                  min="0"
                  value={formData.initial_rol_hours}
                  onChange={e => setFormData({...formData, initial_rol_hours: parseFloat(e.target.value) || 0})}
                />
              </div>
              
              <div className="form-group">
                <label>📋 Permessi maturati (ore)</label>
                <input
                  type="number"
                  step="0.5"
                  min="0"
                  value={formData.initial_permessi_hours}
                  onChange={e => setFormData({...formData, initial_permessi_hours: parseFloat(e.target.value) || 0})}
                />
              </div>
            </div>
          )}
        </section>
        
        {/* === ACTIONS === */}
        <div className="form-actions">
          <button type="submit" className="btn-primary" disabled={saving}>
            {saving ? 'Salvataggio...' : '💾 Salva Impostazioni'}
          </button>
        </div>
      </form>
      
      {/* === PRESETS === */}
      <section className="settings-section presets">
        <h4>⚡ Preset CCNL Comuni</h4>
        <div className="preset-buttons">
          <button 
            type="button"
            className="btn-secondary"
            onClick={() => setFormData({
              ...formData,
              ferie_days_per_month: 1.83,
              rol_hours_per_month: 2.67,
              permessi_hours_per_month: 8.67
            })}
          >
            CCNL Commercio
          </button>
          <button 
            type="button"
            className="btn-secondary"
            onClick={() => setFormData({
              ...formData,
              ferie_days_per_month: 2.0,
              rol_hours_per_month: 4.0,
              permessi_hours_per_month: 10.0
            })}
          >
            CCNL Metalmeccanico
          </button>
        </div>
        <small className="help-text">
          Clicca per applicare valori predefiniti comuni (poi personalizza se necessario)
        </small>
      </section>
    </div>
  );
};

export default VacationSettings;
```

---

Continua nel prossimo file...

## ⭐ 5.9.7 - User Holidays Manager (INVARIATO)

Stesso codice del documento originale - funziona già correttamente.

---

## 🌉 5.9.8 - Bridge Opportunities (INVARIATO)

Stesso codice del documento originale - funziona già correttamente.

---

## 📄 5.9.9 - Vacation Page (AGGIORNATO)

- [ ] 📝 Crea `frontend/src/pages/VacationPage.jsx`

```jsx
import React, { useState } from 'react';
import VacationCalendar from '../components/vacation/VacationCalendar';
import VacationBalance from '../components/vacation/VacationBalance';
import VacationSettings from '../components/vacation/VacationSettings';
import BridgeOpportunities from '../components/vacation/BridgeOpportunities';
import UserHolidaysManager from '../components/vacation/UserHolidaysManager';
import BulkEntryModal from '../components/vacation/BulkEntryModal';  // NEW!
import '../styles/vacation.css';

const VacationPage = () => {
  const [activeTab, setActiveTab] = useState('calendar');
  const [showBulkModal, setShowBulkModal] = useState(false);  // NEW!

  const tabs = [
    { id: 'calendar', label: '📅 Calendario', component: VacationCalendar },
    { id: 'balance', label: '📊 Riepilogo', component: VacationBalance },
    { id: 'bridges', label: '🌉 Ponti', component: BridgeOpportunities },
    { id: 'holidays', label: '⭐ Festività', component: UserHolidaysManager },
    { id: 'settings', label: '⚙️ Impostazioni', component: VacationSettings },
  ];

  const ActiveComponent = tabs.find(t => t.id === activeTab)?.component;

  const handleBulkSave = () => {
    setShowBulkModal(false);
    // Refresh calendar if active
    if (activeTab === 'calendar') {
      window.location.reload(); // Simple refresh, or use proper state management
    }
  };

  return (
    <div className="vacation-page">
      <div className="page-header">
        <h1>🏖️ Gestione Ferie</h1>
        
        {/* Bulk Insert Button - Show only on calendar tab */}
        {activeTab === 'calendar' && (
          <button 
            className="btn-primary bulk-button"
            onClick={() => setShowBulkModal(true)}
          >
            📅 Inserimento Multiplo
          </button>
        )}
      </div>
      
      <div className="vacation-tabs">
        {tabs.map(tab => (
          <button
            key={tab.id}
            className={`tab-button ${activeTab === tab.id ? 'active' : ''}`}
            onClick={() => setActiveTab(tab.id)}
          >
            {tab.label}
          </button>
        ))}
      </div>
      
      <div className="vacation-content">
        {ActiveComponent && <ActiveComponent />}
      </div>
      
      {/* Bulk Entry Modal */}
      {showBulkModal && (
        <BulkEntryModal
          onClose={() => setShowBulkModal(false)}
          onSave={handleBulkSave}
        />
      )}
    </div>
  );
};

export default VacationPage;
```

---

## 🎨 5.9.10 - CSS Styles (ESTESO)

- [ ] 📝 Crea/Aggiorna `frontend/src/styles/vacation.css`

```css
/* ========================================
   VACATION MODULE STYLES
   ======================================== */

.vacation-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.page-header h1 {
  margin: 0;
}

.bulk-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* === TABS === */
.vacation-tabs {
  display: flex;
  gap: 0.5rem;
  border-bottom: 2px solid var(--border-color);
  margin-bottom: 2rem;
}

.tab-button {
  background: none;
  border: none;
  padding: 1rem 1.5rem;
  cursor: pointer;
  font-size: 1rem;
  color: var(--text-secondary);
  border-bottom: 3px solid transparent;
  transition: all 0.2s;
}

.tab-button:hover {
  color: var(--primary-color);
  background: var(--bg-hover);
}

.tab-button.active {
  color: var(--primary-color);
  border-bottom-color: var(--primary-color);
  font-weight: 600;
}

/* ========================================
   BALANCE WIDGET
   ======================================== */

.vacation-balance {
  background: white;
  border-radius: 8px;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.balance-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.year-selector {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.year-selector button {
  background: var(--bg-secondary);
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  border-radius: 4px;
  font-size: 1rem;
}

.year-selector button:hover {
  background: var(--bg-hover);
}

/* Total Card (Aggregated) */
.balance-total-card {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  color: white;
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.total-header h2 {
  margin: 0 0 0.5rem 0;
  font-size: 1.2rem;
  font-weight: 600;
}

.tracking-info {
  margin: 0;
  opacity: 0.9;
  font-size: 0.9rem;
}

.total-values {
  display: flex;
  gap: 3rem;
  margin: 2rem 0;
  justify-content: center;
}

.total-days, .total-hours {
  text-align: center;
}

.total-days .value, .total-hours .value {
  display: block;
  font-size: 3rem;
  font-weight: 700;
  line-height: 1;
}

.total-days .unit, .total-hours .unit {
  display: block;
  font-size: 0.9rem;
  opacity: 0.9;
  margin-top: 0.5rem;
}

.total-breakdown-mini {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(255,255,255,0.3);
}

.mini-stat {
  text-align: center;
}

.mini-stat.separator {
  opacity: 0.5;
  font-size: 1.5rem;
}

.mini-stat .label {
  display: block;
  font-size: 0.85rem;
  opacity: 0.9;
  margin-bottom: 0.25rem;
}

.mini-stat .value {
  display: block;
  font-size: 1.1rem;
  font-weight: 600;
}

.mini-stat.highlight .value {
  font-size: 1.3rem;
}

/* Breakdown Grid */
.balance-breakdown {
  margin-bottom: 2rem;
}

.balance-breakdown h4 {
  margin-bottom: 1rem;
}

.breakdown-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}

.balance-type-card {
  background: white;
  border: 2px solid var(--border-color);
  border-radius: 8px;
  padding: 1.5rem;
  transition: transform 0.2s, box-shadow 0.2s;
}

.balance-type-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.balance-type-card.blue { border-color: #3b82f6; }
.balance-type-card.green { border-color: #10b981; }
.balance-type-card.purple { border-color: #8b5cf6; }

.type-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1rem;
  padding-bottom: 0.75rem;
  border-bottom: 2px solid var(--border-color);
}

.type-icon {
  font-size: 1.5rem;
}

.type-header h5 {
  margin: 0;
  font-size: 1.1rem;
}

.type-stats {
  margin-bottom: 1rem;
}

.stat-row {
  display: flex;
  justify-content: space-between;
  padding: 0.5rem 0;
  font-size: 0.95rem;
}

.stat-row.highlight {
  padding-top: 0.75rem;
  margin-top: 0.75rem;
  border-top: 1px solid var(--border-color);
}

.stat-label {
  color: var(--text-secondary);
}

.stat-value small {
  color: var(--text-secondary);
  font-size: 0.85rem;
  margin-left: 0.25rem;
}

.usage-bar {
  height: 8px;
  background: var(--bg-secondary);
  border-radius: 4px;
  overflow: hidden;
  margin-top: 1rem;
}

.usage-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--primary-color), var(--primary-dark));
  transition: width 0.3s;
}

.usage-label {
  text-align: center;
  font-size: 0.85rem;
  color: var(--text-secondary);
  margin-top: 0.5rem;
}

/* Projection */
.balance-projection {
  background: var(--bg-secondary);
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
}

.balance-projection h4 {
  margin: 0 0 1rem 0;
}

.projection-value {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--primary-color);
  margin-bottom: 0.5rem;
}

.projection-value small {
  font-size: 0.9rem;
  color: var(--text-secondary);
  font-weight: normal;
}

.projection-note {
  margin: 0;
  font-size: 0.9rem;
  color: var(--text-secondary);
}

/* Settings Info */
.balance-settings details {
  background: var(--bg-secondary);
  border-radius: 8px;
  padding: 1rem;
}

.balance-settings summary {
  cursor: pointer;
  font-weight: 600;
  user-select: none;
}

.balance-settings summary:hover {
  color: var(--primary-color);
}

.settings-details {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid var(--border-color);
}

.settings-details p {
  margin: 0.5rem 0;
}

.settings-details ul {
  margin: 0.5rem 0;
  padding-left: 1.5rem;
}

/* ========================================
   SETTINGS FORM
   ======================================== */

.vacation-settings {
  background: white;
  border-radius: 8px;
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.settings-section {
  margin-bottom: 2.5rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid var(--border-color);
}

.settings-section:last-of-type {
  border-bottom: none;
}

.settings-section h4 {
  margin: 0 0 0.5rem 0;
  color: var(--primary-color);
}

.section-description {
  color: var(--text-secondary);
  margin: 0 0 1.5rem 0;
  font-size: 0.95rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
}

.form-group input[type="number"],
.form-group input[type="date"],
.form-group select {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: 6px;
  font-size: 1rem;
  transition: border-color 0.2s;
}

.form-group input:focus,
.form-group select:focus {
  outline: none;
  border-color: var(--primary-color);
}

.help-text {
  display: block;
  margin-top: 0.5rem;
  font-size: 0.85rem;
  color: var(--text-secondary);
}

.form-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.checkbox-group label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}

.checkbox-group input[type="checkbox"] {
  width: auto;
}

.total-preview {
  background: var(--bg-secondary);
  border-radius: 6px;
  padding: 1rem;
  margin-top: 1rem;
  text-align: center;
  font-size: 1.1rem;
}

.initial-balance-form {
  background: var(--bg-secondary);
  border-radius: 8px;
  padding: 1.5rem;
  margin-top: 1rem;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 2rem;
}

/* Presets */
.presets {
  background: var(--bg-secondary);
  border-radius: 8px;
  padding: 1.5rem;
}

.preset-buttons {
  display: flex;
  gap: 1rem;
  margin: 1rem 0;
  flex-wrap: wrap;
}

/* ========================================
   BULK MODAL
   ======================================== */

.bulk-modal {
  max-width: 600px;
}

.modal-description {
  color: var(--text-secondary);
  margin: 0 0 1.5rem 0;
}

.bulk-preview {
  background: var(--bg-info);
  border-left: 4px solid var(--primary-color);
  padding: 1rem;
  margin: 1rem 0;
  border-radius: 4px;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.preview-icon {
  font-size: 1.5rem;
}

.bulk-preview strong {
  color: var(--primary-color);
}

/* ========================================
   RESPONSIVE
   ======================================== */

@media (max-width: 768px) {
  .vacation-page {
    padding: 1rem;
  }
  
  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
  
  .vacation-tabs {
    overflow-x: auto;
    flex-wrap: nowrap;
  }
  
  .tab-button {
    padding: 0.75rem 1rem;
    font-size: 0.9rem;
  }
  
  .total-values {
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .total-breakdown-mini {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .mini-stat.separator {
    display: none;
  }
  
  .breakdown-grid {
    grid-template-columns: 1fr;
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
}

/* ========================================
   UTILITY CLASSES
   ======================================== */

.loading {
  text-align: center;
  padding: 3rem;
  color: var(--text-secondary);
}

.error-message {
  background: var(--error-bg);
  color: var(--error-color);
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 1rem;
  border-left: 4px solid var(--error-color);
}

.success-message {
  background: var(--success-bg);
  color: var(--success-color);
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 1rem;
  border-left: 4px solid var(--success-color);
}

/* ========================================
   COLOR VARIABLES (Add to main CSS)
   ======================================== */

:root {
  --primary-color: #3b82f6;
  --primary-dark: #2563eb;
  --text-primary: #1f2937;
  --text-secondary: #6b7280;
  --border-color: #e5e7eb;
  --bg-secondary: #f9fafb;
  --bg-hover: #f3f4f6;
  --bg-info: #eff6ff;
  --error-bg: #fef2f2;
  --error-color: #dc2626;
  --success-bg: #f0fdf4;
  --success-color: #16a34a;
}
```

---

## 🔗 5.9.11 - Integration

### 5.9.11.1 - Aggiungi route
- [ ] 📝 Modifica `frontend/src/App.jsx`:

```jsx
import VacationPage from './pages/VacationPage';

// In routes:
<Route path="/vacation" element={<ProtectedRoute><VacationPage /></ProtectedRoute>} />
```

### 5.9.11.2 - Aggiungi link in navbar
- [ ] 📝 Modifica componente Navbar:

```jsx
<NavLink to="/vacation">🏖️ Ferie</NavLink>
```

---

## 🧪 5.9.12 - Testing Manuale

### Test Checklist:

**Settings:**
- [ ] Form carica con valori default
- [ ] Modificare maturazione separata (ferie/rol/permessi)
- [ ] Salvare con tracking start date
- [ ] Abilitare saldo iniziale e inserire valori
- [ ] Verificare validazione (balance date prima di tracking start)
- [ ] Preset CCNL funzionanti

**Calendar:**
- [ ] Festività nazionali visibili
- [ ] Festività custom visibili (dopo averle create)
- [ ] Weekend marcati
- [ ] Click su giorno apre modal entry
- [ ] Click su festività/weekend non apre modal
- [ ] Pulsante "Inserimento Multiplo" visibile

**Single Entry:**
- [ ] Modal FERIE: no input ore
- [ ] Modal ROL: input ore obbligatorio
- [ ] Modal PERMESSI: input ore obbligatorio
- [ ] Validazione: non permette weekend
- [ ] Validazione: non permette festività
- [ ] Entry salvata appare nel calendario

**Bulk Entry:**
- [ ] Modal si apre da pulsante
- [ ] Range date funzionante
- [ ] Preview count approssimativo
- [ ] Checkbox skip weekend/holidays
- [ ] Per FERIE: no input ore
- [ ] Per ROL/PERMESSI: input ore obbligatorio
- [ ] Creazione multipla funziona
- [ ] Messaggio successo mostra count creati

**Balance:**
- [ ] Mostra totale aggregato (giorni + ore)
- [ ] Mostra tracking info (data inizio + mesi)
- [ ] Breakdown per tipo con tutte le info
- [ ] Progress bar per tipo
- [ ] Proiezione fine anno
- [ ] Info configurazione espandibile

**Bridges:**
- [ ] Lista ponti per anno
- [ ] Descrizioni corrette
- [ ] Cambia anno funziona

**User Holidays:**
- [ ] Aggiungere patrono ricorrente
- [ ] Aggiungere festività non ricorrente
- [ ] Validazione giorno/mese
- [ ] Eliminare festività
- [ ] Festività appare nel calendario

---

## 🎯 CHECKPOINT FASE 5.9

**Services:**
- [ ] ✅ vacationService.js con tutti endpoint (incl. bulk)

**Components:**
- [ ] ✅ VacationCalendar funzionante
- [ ] ✅ VacationEntryModal (ferie no ore, ROL/Permessi sì)
- [ ] ✅ BulkEntryModal (NUOVO - inserimento multiplo)
- [ ] ✅ VacationBalance (totali aggregati + breakdown)
- [ ] ✅ VacationSettings (maturazione separata + tracking start + saldo iniziale)
- [ ] ✅ UserHolidaysManager
- [ ] ✅ BridgeOpportunities

**Page:**
- [ ] ✅ VacationPage con tabs
- [ ] ✅ Pulsante bulk visibile su tab calendario
- [ ] ✅ Route configurata
- [ ] ✅ Navbar link funzionante

**Styles:**
- [ ] ✅ vacation.css completo
- [ ] ✅ Responsive design
- [ ] ✅ Color scheme coerente

**Testing:**
- [ ] ✅ Tutti i test manuali passati
- [ ] ✅ Validazioni funzionanti
- [ ] ✅ UX fluida

---

## 📊 RIEPILOGO MODIFICHE FRONTEND

### Componenti Nuovi:
1. **BulkEntryModal** - Inserimento multiplo periodo

### Componenti Aggiornati:
1. **VacationSettings** - Form completamente riscritto con:
   - Maturazione separata (ferie/rol/permessi)
   - Tracking start date
   - Saldo iniziale opzionale (ferie in giorni!)
   - Preset CCNL
   
2. **VacationBalance** - Widget completamente riscritto con:
   - Totali aggregati prominenti
   - Breakdown dettagliato per tipo
   - Progress bar per tipo
   - Info tracking
   - Proiezione fine anno

3. **VacationPage** - Aggiunto pulsante bulk

### Componenti Invariati (già corretti):
- VacationCalendar
- VacationEntryModal
- UserHolidaysManager
- BridgeOpportunities

---

**Tempo stimato:** 3-4 giorni  
**Prossimo:** FASE 6 - Deployment

---

## 📝 Note Finali Implementazione

### UX Migliorata:
- ✅ Form settings più chiaro e intuitivo
- ✅ Vista totali aggregati immediata
- ✅ Inserimento multiplo facilita pianificazione
- ✅ Validazioni impediscono errori

### Architettura Coerente:
- ✅ Backend e Frontend allineati
- ✅ Maturazione separata per tipo funzionante end-to-end
- ✅ Conversioni automatiche (giorni ↔ ore)
- ✅ Calcoli aggregati corretti

### Pronti per Produzione:
- ✅ Tutti i componenti testati
- ✅ Validazioni lato client e server
- ✅ Error handling completo
- ✅ Responsive design

**Prossimo:** FASE 6 - Deployment

---

# FASE 6: Deployment (3-4 giorni)

## 🎯 Obiettivo
Deployare applicazione su piattaforma cloud (Render.com consigliato per MVP).

---

### 6.1 - Preparazione Deploy Backend

#### 6.1.1 - Production requirements
- [ ] 📝 Crea `backend/requirements.prod.txt`

```txt
# Production requirements
-r requirements.txt

# Production server
gunicorn==23.0.0

# Monitoring (opzionale)
sentry-sdk[fastapi]==2.20.0
```

#### 6.1.2 - Gunicorn config
- [ ] 📝 Crea `backend/gunicorn.conf.py`

```python
import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120
keepalive = 5
```

#### 6.1.3 - Procfile per Render
- [ ] 📝 Crea `backend/Procfile`

```
web: gunicorn -c gunicorn.conf.py main:app
```

#### 6.1.4 - Commit production files
- [ ] Commit: `Add production configuration`

---

### 6.2 - Database Production

#### 6.2.1 - Render.com PostgreSQL
- [ ] Vai su render.com e crea account
- [ ] New → PostgreSQL
- [ ] Nome: `budget-app-db`
- [ ] Plan: Free
- [ ] Crea database
- [ ] Salva `External Database URL`

#### 6.2.2 - Run migrations su production DB
- [ ] Copia connection string
- [ ] In locale, aggiorna `.env` temporaneamente con DB production
- [ ] Esegui:
```bash
alembic upgrade head
```
- [ ] Verifica tabelle create
- [ ] Ripristina `.env` con DB locale

---

### 6.3 - Deploy Backend su Render

#### 6.3.1 - Crea Web Service
- [ ] Su Render: New → Web Service
- [ ] Connetti repository GitHub
- [ ] Configurazione:
  - Name: `budget-app-api`
  - Environment: Python 3
  - Build Command: `cd backend && pip install -r requirements.prod.txt`
  - Start Command: `cd backend && gunicorn -c gunicorn.conf.py main:app`
  - Plan: Free

#### 6.3.2 - Environment variables
- [ ] In Render, vai a Environment
- [ ] Aggiungi tutte le variabili da `.env`:
  - `DATABASE_URL` = External Database URL da step 6.2
  - `SECRET_KEY` = genera nuovo strong secret
  - `DEBUG` = `False`
  - `CORS_ORIGINS` = `["https://your-frontend-url.onrender.com"]` (aggiornerai dopo)

#### 6.3.3 - Deploy
- [ ] Click "Create Web Service"
- [ ] Attendi deploy (5-10 minuti)
- [ ] Verifica logs per errori
- [ ] Apri URL: `https://budget-app-api.onrender.com`
- [ ] Dovresti vedere messaggio JSON

#### 6.3.4 - Test API production
- [ ] Apri `https://budget-app-api.onrender.com/docs`
- [ ] Test registration endpoint
- [ ] Verifica che utente sia salvato in production DB

---

### 6.4 - Deploy Frontend su Render

#### 6.4.1 - Update API URL
- [ ] 📝 Modifica `frontend/.env.production`

```env
VITE_API_URL=https://budget-app-api.onrender.com/api/v1
```

#### 6.4.2 - Build script
- [ ] 📝 Verifica `frontend/package.json` abbia:

```json
{
  "scripts": {
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

#### 6.4.3 - Crea Static Site su Render
- [ ] Render: New → Static Site
- [ ] Connetti stesso repository
- [ ] Configurazione:
  - Name: `budget-app-frontend`
  - Build Command: `cd frontend && npm install && npm run build`
  - Publish Directory: `frontend/dist`
  - Plan: Free

#### 6.4.4 - Deploy frontend
- [ ] Click "Create Static Site"
- [ ] Attendi build
- [ ] Apri URL: `https://budget-app-frontend.onrender.com`
- [ ] Dovresti vedere app

#### 6.4.5 - Update CORS
- [ ] Torna a backend su Render
- [ ] Environment variables
- [ ] Aggiorna `CORS_ORIGINS`:
```
["https://budget-app-frontend.onrender.com"]
```
- [ ] Salva (triggera re-deploy)

---

### 6.5 - Final Production Tests

#### 6.5.1 - Test completo production
1. [ ] Apri app production
2. [ ] Registra nuovo utente
3. [ ] Crea accounts
4. [ ] Crea transactions
5. [ ] Verifica tutto funzioni
6. [ ] Test da mobile browser
7. [ ] Test da diversi dispositivi

#### 6.5.2 - Performance check
- [ ] Apri Chrome DevTools
- [ ] Network tab
- [ ] Reload pagina
- [ ] Verifica tempi risposta API (<1s)

#### 6.5.3 - Security check
- [ ] Verifica HTTPS attivo
- [ ] Test CORS (solo frontend permesso)
- [ ] Test JWT expiration
- [ ] Test endpoints senza auth → 401

---

### 6.6 - Monitoring & Maintenance

#### 6.6.1 - Setup monitoring (opzionale)
- [ ] Sentry per error tracking
- [ ] Render Metrics per performance

#### 6.6.2 - Backup strategy
- [ ] Render PostgreSQL ha backup automatici
- [ ] Verifica retention policy

#### 6.6.3 - Documentazione deploy
- [ ] 📝 Crea `docs/DEPLOYMENT.md`
- [ ] Include URLs production
- [ ] Include procedure deploy
- [ ] Include troubleshooting

#### 6.6.4 - Commit deployment docs
- [ ] Commit: `Add deployment documentation`

---

## 🎯 CHECKPOINT FASE 6

- [ ] ✅ Backend deployed su Render
- [ ] ✅ Database production su Render PostgreSQL
- [ ] ✅ Frontend deployed su Render Static Site
- [ ] ✅ HTTPS attivo su entrambi
- [ ] ✅ CORS configurato correttamente
- [ ] ✅ Environment variables production settate
- [ ] ✅ Migrations eseguite su production DB
- [ ] ✅ App testata end-to-end in production
- [ ] ✅ Performance accettabili (<2s page load)
- [ ] ✅ No critical errors in logs

**URLs Production:**
- Backend API: `https://budget-app-api.onrender.com`
- Frontend App: `https://budget-app-frontend.onrender.com`
- API Docs: `https://budget-app-api.onrender.com/docs`

**Test finale production:**
1. [ ] User registration & login
2. [ ] Create 3 accounts
3. [ ] Add 10 transactions
4. [ ] Create 2 transfers
5. [ ] View dashboard statistics
6. [ ] Logout & re-login
7. [ ] Data persists correctly

**Tempo stimato:** 3-4 giorni  
**Prossimo:** Fase 7 - Sviluppi Futuri

---

# FASE 7: Sviluppi Futuri

## 🎯 Features Post-MVP

Queste sono le funzionalità che avevi chiesto come "suggerimenti extra". Implementale una volta che l'MVP è stabile e deployato.

---

### 7.1 - Advanced Features

#### 7.1.1 - Recurring Transactions
- [ ] Model `RecurringTransaction` con schedule
- [ ] Background job per auto-creazione
- [ ] UI per gestire ricorrenze

#### 7.1.2 - Budget Planning
- [ ] Model `Budget` per categoria/mese
- [ ] Tracking vs budget
- [ ] Alerts quando si supera budget

#### 7.1.3 - Multi-Currency Support
- [ ] API conversione valute (Exchange Rates API)
- [ ] Conversione automatica nei report
- [ ] Scelta valuta per account

#### 7.1.4 - Bill Reminders
- [ ] Model `Bill` con due date
- [ ] Notifiche email/push
- [ ] Mark as paid

#### 7.1.5 - Savings Goals
- [ ] Model `SavingsGoal` con target amount
- [ ] Progress tracking
- [ ] Auto-transfer to savings

---

### 7.2 - Enhanced Analytics

#### 7.2.1 - Advanced Charts
- [ ] Spending by category breakdown
- [ ] Year-over-year comparison
- [ ] Custom date range reports
- [ ] Export to PDF/Excel

#### 7.2.2 - AI Insights (avanzato)
- [ ] Pattern detection spese
- [ ] Suggerimenti risparmio
- [ ] Anomaly detection
- [ ] Forecast future expenses

#### 7.2.3 - Custom Reports Builder
- [ ] Drag & drop report builder
- [ ] Save custom reports
- [ ] Share reports (multi-user)

---

### 7.3 - Collaboration Features

#### 7.3.1 - Shared Accounts
- [ ] Model `AccountShare` per permessi
- [ ] Invite altri utenti
- [ ] Different permission levels (view/edit)

#### 7.3.2 - Family/Household Mode
- [ ] Multiple users, shared budget
- [ ] Individual + shared categories
- [ ] Expense approval workflow

---

### 7.4 - Integrations

#### 7.4.1 - Bank Sync (complesso)
- [ ] Integration con Plaid/Tink
- [ ] Auto-import transactions
- [ ] Reconciliation

#### 7.4.2 - Receipt Scanning
- [ ] OCR per receipts (Google Cloud Vision)
- [ ] Auto-fill transaction details
- [ ] Attach image to transaction

#### 7.4.3 - Export Integrations
- [ ] Export to Google Sheets
- [ ] Sync with Excel
- [ ] API webhooks

---

### 7.5 - Mobile App

#### 7.5.1 - React Native App
- [ ] Setup React Native project
- [ ] Reuse API services
- [ ] Mobile-optimized UI
- [ ] Push notifications
- [ ] Camera for receipt scan

---

### 7.6 - Admin Panel

#### 7.6.1 - Admin Dashboard
- [ ] User management
- [ ] System statistics
- [ ] Database backups
- [ ] Support tickets

---

### 7.7 - Performance & Scalability

#### 7.7.1 - Caching
- [ ] Redis per session storage
- [ ] Cache frequent queries
- [ ] Invalidate on updates

#### 7.7.2 - Background Jobs
- [ ] Celery per async tasks
- [ ] Email sending
- [ ] Report generation
- [ ] Data aggregations

#### 7.7.3 - Database Optimization
- [ ] Query optimization
- [ ] Additional indexes
- [ ] Partitioning large tables
- [ ] Read replicas

---

## 🎯 Priorità Sviluppi Futuri

**Alta Priorità (entro 3 mesi):**
1. Recurring Transactions
2. Budget Planning
3. Advanced Charts
4. Multi-Currency

**Media Priorità (6 mesi):**
5. Bill Reminders
6. Receipt Scanning
7. Custom Reports
8. Shared Accounts

**Bassa Priorità (1+ anno):**
9. Bank Sync
10. Mobile App
11. AI Insights
12. Admin Panel

---

## 📊 ROADMAP COMPLETA - SUMMARY

### Completato ✅
- [x] FASE 0: Setup Progetto (1 giorno)
- [x] FASE 1: Database Foundation (2-3 giorni)
- [x] FASE 2: Backend API - Autenticazione (3-4 giorni)
- [x] FASE 3: Backend API - Core Features (4-5 giorni)

### In Corso 🟡
- [ ] FASE 3.8: Backend API - Vacation Planning (3-4 giorni) ← NUOVO
- [ ] FASE 4: Testing & Debug Core (2 giorni)
- [ ] FASE 4.6: Testing Vacation Module (1-2 giorni) ← NUOVO
- [ ] FASE 5: Frontend Integration Core (5-7 giorni)
- [ ] FASE 5.9: Frontend Vacation Module (3-4 giorni) ← NUOVO
- [ ] FASE 6: Deployment (3-4 giorni)

### In Roadmap 📋
- [ ] FASE 7: Sviluppi Futuri (ongoing)

---

## 🎉 CONGRATULAZIONI!

Se sei arrivato qui, hai completato lo sviluppo completo di una **Budget Management SaaS Application**!

**Cosa hai costruito:**
- ✅ Backend API REST completa con FastAPI
- ✅ Database PostgreSQL multi-tenant
- ✅ Sistema autenticazione JWT
- ✅ Frontend React moderno
- ✅ Test automatici con Pytest
- ✅ Deployment production
- ✅ Documentazione completa

**Prossimi passi:**
1. Raccogli feedback da utenti beta
2. Itera e migliora
3. Implementa features dalla Fase 7
4. Scale!

**Condividi il progetto:**
- LinkedIn
- GitHub README con screenshots
- Portfolio personale
- ProductHunt launch

---

**Buon lavoro e buon coding! 🚀**

*Roadmap creata il 13 Novembre 2025*  
*Autore: Giovanni Mezzasalma*  
*Stack: Python FastAPI + PostgreSQL + React*
