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
- [ ] **Problema:** Definito sia in `models/custom_chart.py` che in `schemas/custom_chart.py`
- [ ] **Rischio:** Potrebbero andare out of sync
- [ ] **Azione:** Centralizzare in un unico file (es. `schemas/custom_chart.py`) e importare nel model

##### E. Validazione incompleta in `update_transfer`
- [ ] **Problema:** La validazione della direzione transfer potrebbe non coprire tutti i casi edge
- [ ] **File:** `app/crud/transfer.py`
- [ ] **Azione:** Verificare e completare validazione

##### F. File SQL in `database/` obsoleti
- [ ] **Problema:** I file SQL originali sono out of sync con i model attuali
- [ ] **File:**
  - `database/01_create_schema.sql`
  - `database/02_seed_default_categories.sql`
- [ ] **Azione:** 
  - Opzione A: Rimuovere (Alembic gestisce tutto)
  - Opzione B: Aggiornare e tenere come documentazione
  - Opzione C: Spostare in `database/archive/` con nota

#### 3.7.3 - Problemi Minori / Note

##### G. Migration `c744b8064fb0` vuota
- [ ] **Nota:** La migration per `custom_charts` è vuota perché la tabella era già stata creata via SQL manuale
- [ ] **Impatto:** Nessuno per il funzionamento attuale
- [ ] **Rischio:** Se si fa `alembic downgrade` completo e poi `upgrade`, la tabella potrebbe non essere ricreata
- [ ] **Azione:** Documentare, non richiede fix immediato

##### H. UUID come String(36) invece di UUID nativo
- [ ] **Nota:** I model usano `String(36)` invece del tipo UUID nativo PostgreSQL
- [ ] **Impatto:** Funziona ma perde ottimizzazioni PostgreSQL
- [ ] **Azione:** Nessuna per MVP, considerare per futuro refactoring

##### I. Commenti misti italiano/inglese
- [ ] **Nota:** Inconsistenza nella lingua dei commenti e docstring
- [ ] **Azione:** Uniformare (suggerimento: inglese per codice, italiano per docs utente)

##### J. CORS_ORIGINS parsing
- [ ] **Nota:** `.env.example` usa stringa JSON, `config.py` si aspetta lista
- [ ] **Impatto:** Pydantic-settings dovrebbe gestirlo, ma verificare
- [ ] **Azione:** Testare parsing da `.env`

#### 3.7.4 - Checklist Correzioni

**Critiche (fare ora):**
- [ ] Decidere e implementare strategia balance (A/B/C)
- [ ] Aggiornare commenti model per 3 tipi transazione
- [ ] Correggere path in `run.py`: `app.main:app`
- [ ] Correggere path in `Dockerfile`: `app.main:app`

**Medie (fare prima di Fase 6):**
- [ ] Centralizzare `ChartType` enum
- [ ] Verificare validazione `update_transfer`
- [ ] Gestire file SQL obsoleti

**Minori (nice to have):**
- [ ] Uniformare lingua commenti
- [ ] Documentare nota su migration vuota
- [ ] Testare parsing CORS_ORIGINS

#### 3.7.5 - Test Post-Correzioni

Dopo le correzioni, verificare:
- [ ] Server avvia senza errori: `python run.py` (o con path corretto)
- [ ] Swagger UI accessibile: http://localhost:8000/docs
- [ ] Test creazione transaction → balance aggiornato correttamente
- [ ] Test creazione transfer → entrambi i balance aggiornati
- [ ] Test analytics/summary → dati corretti
- [ ] Nessun errore nei log

#### 3.7.6 - Commit
- [ ] Commit: `Code review fixes - Phase 3.7`
- [ ] Push

---

## 🎯 CHECKPOINT FASE 3 (AGGIORNATO)

Verifica che tutti questi endpoint funzionino E che le correzioni 3.7 siano applicate:

[... resto del checkpoint esistente ...]

**Aggiunte Fase 3.7:**
- [ ] ✅ Path `run.py` e `Dockerfile` corretti
- [ ] ✅ Strategia balance definita e implementata
- [ ] ✅ Commenti model allineati con schema
- [ ] ✅ Test post-correzioni passati

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

**Tempo stimato:** 4-5 giorni  
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
- [x] FASE 4: Testing & Debug (2 giorni)
- [x] FASE 5: Frontend Integration (5-7 giorni)
- [x] FASE 6: Deployment (3-4 giorni)

**Totale: 6-8 settimane** ✅

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
