# 💰 Budget App - Multi-User Personal Finance Manager

<div align="center">

![Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Python](https://img.shields.io/badge/Python-3.12.4-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688)
![React](https://img.shields.io/badge/React-18-61DAFB)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791)
![License](https://img.shields.io/badge/License-MIT-green)

**Una moderna applicazione web per la gestione del budget personale con supporto multi-utente e pianificazione ferie**

[Features](#-features) • [Tech Stack](#-tech-stack) • [Setup](#-setup-locale) • [Roadmap](#-roadmap) • [Contributing](#-contributing)

</div>

---

## 📖 Descrizione

Budget App è una **web application SaaS** per la gestione delle finanze personali che permette agli utenti di:
- Tracciare entrate e uscite su **account multipli**
- Categorizzare le transazioni
- Visualizzare **statistiche e grafici** in tempo reale
- Creare **report personalizzati**
- Pianificare budget mensili
- **🆕 Gestire ferie e permessi** con calcolo automatico maturazione

Il progetto nasce come evoluzione di un prototipo Excel, trasformato in un'applicazione web scalabile con autenticazione multi-utente e database PostgreSQL.

---

## ✨ Features

### 🎯 Core Features (MVP)

#### 💰 Gestione Finanziaria

- ✅ **Dashboard Interattiva**: Visualizzazione real-time di balance, income, expense
- ✅ **Multi-Account Management**: Gestione conti corrente, risparmio, contanti, investimenti
- ✅ **Categorizzazione Smart**: Categorie predefinite + custom categories
- ✅ **Transazioni Complete**: Tracking entrate/uscite con descrizione, note, tags
- ✅ **Trasferimenti tra Account**: Gestione automatica balance
- ✅ **Filtri Avanzati**: Per data, account, categoria, tipo
- ✅ **Statistiche Mensili**: Trend income/expense, grafici a torta per categorie
- ✅ **Custom Chart Builder**: Crea e salva grafici personalizzati

#### 📊 Sistema di Categorizzazione Gerarchico

La piattaforma utilizza un **sistema di categorizzazione a due livelli** progettato per garantire flessibilità e controllo granulare delle finanze:

**Macro-Categorie (Fisse):**

La piattaforma organizza tutte le transazioni in **3 macro-categorie principali**:

1. **Entrate** (`income`) - Per tutte le fonti di reddito
2. **Spese di Necessità** (`expense_necessity`) - Spese essenziali e ricorrenti
3. **Spese Extra** (`expense_extra`) - Spese discrezionali e non essenziali

Queste macro-categorie sono **fisse e non modificabili** dall'utente, garantendo una struttura organizzativa coerente e facilitando l'analisi del budget secondo il metodo 50/30/20 (necessità/desideri/risparmi).

**Sotto-Categorie (Completamente Customizzabili):**

All'interno di ogni macro-categoria, gli utenti possono:

- ✅ **Utilizzare categorie predefinite**: Al momento della registrazione, il sistema crea automaticamente un set di sotto-categorie comuni (es. Stipendio, Affitto, Spesa, Trasporti, Svago, ecc.)
- ✅ **Creare nuove sotto-categorie**: Personalizzare completamente le proprie categorie in base alle esigenze specifiche
- ✅ **Modificare categorie esistenti**: Cambiare nome, colore, icona delle categorie
- ✅ **Eliminare/disattivare categorie**: Rimuovere categorie non più necessarie (preservando lo storico delle transazioni associate)

**Struttura Gerarchica:**

```
📁 Entrate
  ├── 💰 Reddito
  │   ├── Reddito Principale
  │   └── Reddito Secondario
  ├── 🏠 Affitto (da locazione)
  ├── 🏷️ Vendita
  └── 🔄 Rimborsi

📁 Spese di Necessità
  ├── 🏠 Casa
  │   ├── Mutuo/Affitto
  │   ├── Elettricità
  │   ├── Gas
  │   └── Acqua
  ├── 🚗 Trasporti
  │   ├── Benzina
  │   ├── Assicurazione Auto
  │   └── Manutenzione
  └── 🏥 Salute
      ├── Medicinali
      └── Visite mediche

📁 Spese Extra
  ├── 🎭 Svago
  │   ├── Ristoranti
  │   ├── Cinema/Eventi
  │   └── Shopping
  └── 🐾 Animali
      ├── Cibo
      └── Veterinario
```

**Vantaggi del Sistema:**

- 🎯 **Organizzazione chiara**: Le 3 macro-categorie forniscono una struttura mentale semplice per gestire le finanze
- 🔧 **Massima flessibilità**: Ogni utente può personalizzare completamente le sotto-categorie secondo le proprie esigenze
- 📊 **Analytics potenti**: Possibilità di analizzare le spese sia per macro-categoria (visione d'insieme) che per sotto-categoria (dettaglio granulare)
- 🎨 **Personalizzazione visiva**: Ogni categoria può avere colore ed emoji personalizzati per una UI intuitiva
- 🔄 **Evoluzione nel tempo**: Aggiungi nuove categorie man mano che le tue esigenze cambiano

**Profondità Massima:**

Il sistema supporta una profondità massima di **2 livelli** (macro-categoria → sotto-categoria) per mantenere la struttura semplice e gestibile. Non è possibile creare sotto-categorie di sotto-categorie.

#### 💡 Gestione Budget (Budget Planning)

La piattaforma include un **sistema di budgeting proattivo** che ti permette di pianificare e monitorare le tue spese per categoria, aiutandoti a mantenere il controllo delle finanze.

**Funzionalità Budget:**

- ✅ **Budget per Sotto-Categoria**: Crea budget mensili per ogni sotto-categoria personalizzata (es. "Ristoranti": €200/mese, "Spesa": €400/mese)
- ✅ **Tracking Real-Time**: Confronto automatico tra budget pianificato e spesa effettiva
- ✅ **Indicatori Visivi**: Sistema a semaforo (verde/giallo/rosso) per monitorare l'utilizzo del budget
- ✅ **Percentuale di Utilizzo**: Visualizzazione chiara di quanto budget hai già utilizzato (es. "€150/€200 - 75%")
- ✅ **Storico Budget**: Mantieni lo storico dei budget anche quando le categorie vengono modificate o eliminate
- ✅ **Flessibilità**: Modifica, disattiva o elimina budget in qualsiasi momento

**Come Funziona:**

1. **Crea un Budget**
   - Seleziona una sotto-categoria (es. "Ristoranti")
   - Imposta l'importo mensile (es. €200)
   - Attiva il budget

2. **Monitora l'Utilizzo**
   - Ogni transazione nella categoria viene automaticamente conteggiata
   - La dashboard mostra in tempo reale: "€150/€200 (75%)"
   - Indicatore visivo:
     - 🟢 Verde: < 70% utilizzato
     - 🟡 Giallo: 70-90% utilizzato
     - 🔴 Rosso: > 90% utilizzato

3. **Gestione Intelligente delle Categorie**
   - Se rinomini una categoria, il budget si aggiorna automaticamente
   - Se elimini una categoria con budget attivo, ricevi un avviso:
     ```
     ⚠️ Questa categoria ha budget attivi
     Vuoi: [Riassegnare] [Eliminare budget] [Annulla]
     ```

**Esempio Pratico:**

```
📊 I Tuoi Budget (Gennaio 2025)

🍽️ Ristoranti
€150 / €200 (75%) 🟡
Ancora disponibili: €50

🛒 Spesa
€380 / €400 (95%) 🔴
Quasi esaurito! Ancora €20

🚗 Benzina
€45 / €100 (45%) 🟢
Ben sotto budget!

⚠️ Budget Orfani: 1
[Gestisci Budget Orfani]
```

**Vantaggi:**

- 🎯 **Controllo Proattivo**: Non solo tracking passivo, ma pianificazione attiva delle spese
- 📊 **Visibilità Immediata**: Vedi subito dove stai spendendo troppo
- 🔔 **Nessuna Sorpresa**: Gli indicatori visivi ti avvisano prima di sforare
- 🔧 **Flessibile**: Budget adattabili alla tua situazione che cambia nel tempo
- 📈 **Analytics Potenziate**: Confronta budget vs spesa effettiva per analisi approfondite

**Gestione Budget Orfani:**

Se elimini una categoria che ha budget attivi, questi diventano "budget orfani". Il sistema:
- Li mantiene attivi e visibili
- Mostra un avviso nella dashboard
- Ti permette di riassegnarli a un'altra categoria o eliminarli
- Preserva lo storico delle spese associate

Questo approccio "permissivo" ti dà massima flessibilità nella gestione delle tue categorie senza perdere dati o controllo sui tuoi budget.

## 📥 CSV Import & 📊 Data Export

### CSV Import

Importa massivamente transazioni da file CSV con preview interattiva e validazione intelligente.

**Caratteristiche:**
- ✅ **Template CSV** scaricabile con formato standard
- ✅ **Preview Interattiva** con status per ogni riga (🟢 valid, 🟡 warning, 🔴 error, 🟣 duplicate)
- ✅ **Fuzzy Matching** categorie (es. "Ristorante" → "Ristorazione")
- ✅ **Rilevamento Duplicati** automatico
- ✅ **Import Selettivo** (escludi righe con errori)

**Formato CSV:**
```csv
date,description,amount,category_name,notes
2025-01-15,Spesa Supermercato,-45.50,Spesa,Settimanale
2025-01-16,Stipendio,2500.00,Stipendio,Gennaio 2025
```

**User Flow:** Upload → Preview con validazione → Correggi errori → Conferma import

**Limiti:** Max 1000 righe per file, UTF-8 encoding

---

### Data Export (Excel)

Esporta report finanziari completi in Excel multi-sheet con generazione client-side.

**Caratteristiche:**
- ✅ **5-6 Fogli Excel**: Riepilogo, Transazioni, Per Categoria, Per Account, Trasferimenti, Budget
- ✅ **Generazione Client-Side** (zero carico server, download istantaneo)
- ✅ **Period Presets**: Questo mese, ultimi 3/6 mesi, quest'anno, anno scorso, custom
- ✅ **Filtri**: Esporta tutti gli account o singolo account
- ✅ **Formattazione Professionale**: Auto-filter, freeze panes, headers colorati

**Fogli Generati:**
1. **Riepilogo**: Statistiche periodo (entrate, uscite, saldo, patrimonio)
2. **Transazioni**: Lista completa con auto-filter
3. **Per Categoria**: Aggregazione spese con percentuali
4. **Per Account**: Breakdown movimenti per account
5. **Trasferimenti**: Lista trasferimenti tra account
6. **Budget vs Actual**: Confronto budget pianificato vs speso *(futuro)*

**User Flow:** Configura periodo → Seleziona fogli → Download Excel

**File generato:** `BudgetApp_Export_2025-01-01_2025-01-31.xlsx`

---

### Implementazione Tecnica

**Backend:**
- `app/utils/csv_parser.py`: Parsing e validazione CSV
- `app/crud/export.py`: Aggregazione dati export
- `app/routers/csv_import.py`: Endpoint import (preview, template)
- `app/routers/export.py`: Endpoint export (data aggregation)

**Frontend:**
- Libreria `xlsx` (SheetJS) per generazione Excel client-side
- `components/transactions/CSVImportModal.jsx`: Modal import
- `components/reports/ExcelExportModal.jsx`: Modal export
- `services/csvImportService.js` & `excelService.js`: API integration

**Testing:**
- Backend: 85+ test con >80% coverage
- Fixtures: CSV test files, export data mocks

#### 🏖️ Gestione Ferie (Vacation Planning)

- ✅ **Maturazione Separata per Tipo**: Tracciamento indipendente Ferie, ROL, Permessi
  - Ferie: giorni/mese (es. 1.83 giorni = 22 giorni/anno)
  - ROL: ore/mese (es. 2.67 ore = 32 ore/anno)
  - Permessi: ore/mese (es. 8.67 ore = 104 ore/anno)
- ✅ **Tracking Start Date**: Data inizio maturazione invece di riporto anno precedente
- ✅ **Saldo Iniziale Opzionale**: Per migrare da altri sistemi (ferie in giorni, ROL/Permessi in ore)
- ✅ **Calendario Interattivo**: Visualizzazione mensile con festività evidenziate
- ✅ **Festività Italiane**: Calendario pre-popolato con festività nazionali + calcolo automatico Pasqua/Pasquetta
- ✅ **Festività Custom**: Aggiungi patrono locale o chiusure aziendali
- ✅ **Inserimento Multiplo**: Crea ferie per intere settimane con auto-skip weekend/festività
- ✅ **Validazione Intelligente**: Blocco inserimento nei weekend e festività
- ✅ **Balance con Totali Aggregati**: Vista riepilogo prominente con breakdown dettagliato per tipo
- ✅ **Calcolo Ponti Automatico**: Identificazione opportunità ponte (es. Martedì → Lunedì)
- ✅ **Proiezione Fine Anno**: Stima ore residue basata su maturazione
- ✅ **Preset CCNL**: Configurazioni rapide per contratti comuni (Commercio, Metalmeccanico)

#### 🔒 Sicurezza & Multi-Utente

- 🔒 **Sistema di Autenticazione**: JWT-based authentication
- 🔒 **Multi-User Support**: Isolamento dati per utente
- 🔒 **API REST Completa**: Backend FastAPI documentato

### 🚀 Planned Features (Post-MVP)

#### Finanza
- [ ] **Recurring Transactions**: Auto-generazione transazioni ricorrenti
- [ ] **Budget Planning**: Impostazione budget mensile per categoria
- [ ] **Bill Reminders**: Notifiche scadenze bollette
- [ ] **Multi-Currency**: Supporto valute multiple con conversione
- [ ] **Receipt Scanning**: OCR per estrarre dati da scontrini
- [ ] **Shared Accounts**: Condivisione account tra più utenti
- [ ] **Bank Sync**: Integrazione con conti bancari (Plaid/Tink)
- [ ] **AI Insights**: Pattern detection e suggerimenti risparmio

#### Ferie
- [ ] **Export iCal**: Esporta ferie in calendario Apple/Google
- [ ] **Smart Suggestions**: Suggerimenti periodo migliore per ferie (basato su ponti)
- [ ] **Team View**: Vista condivisa ferie team (per piccole aziende)
- [ ] **Approvazione Workflow**: Sistema approvazione richieste ferie
- [ ] **Storico Multi-Anno**: Archivio ferie anni precedenti

#### General
- [ ] **Mobile App**: React Native app per iOS/Android
- [ ] **Dark Mode**: Tema scuro per UI
- [ ] **Multi-Language**: Supporto lingue multiple

---

## 🛠️ Tech Stack

### Backend

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) 0.115.0
- **Language**: Python 3.12.4
- **Database**: PostgreSQL 16
- **ORM**: SQLAlchemy 2.0
- **Migrations**: Alembic
- **Authentication**: JWT (python-jose)
- **Security**: Bcrypt password hashing, CORS protection
- **Testing**: Pytest + Coverage
- **Server**: Uvicorn / Gunicorn

### Frontend

- **Framework**: [React](https://react.dev/) 18
- **Build Tool**: Vite
- **Styling**: TailwindCSS
- **Charts**: Recharts
- **HTTP Client**: Axios
- **Routing**: React Router
- **State Management**: React Context + Hooks

### DevOps

- **Containerization**: Docker + Docker Compose
- **Version Control**: Git + GitHub
- **CI/CD**: GitHub Actions (planned)
- **Hosting Backend**: Render.com
- **Hosting Frontend**: Vercel / Render Static
- **Database Hosting**: Render PostgreSQL

### Development Tools

- **IDE**: Visual Studio Code
- **Database UI**: pgAdmin 4
- **API Testing**: Swagger UI (FastAPI auto-generated)
- **Git GUI**: GitHub Desktop

---

## 📦 Setup Locale

### Prerequisiti

- **Python** 3.12+ ([Download](https://www.python.org/downloads/))
- **Node.js** 18+ e npm ([Download](https://nodejs.org/))
- **PostgreSQL** 16+ ([Download](https://www.postgresql.org/download/))
- **Git** ([Download](https://git-scm.com/downloads))

### 1. Clone Repository

```bash
git clone https://github.com/TUO-USERNAME/budget-app-saas.git
cd budget-app-saas
```

### 2. Setup Backend

```bash
# Naviga nella cartella backend
cd backend

# Crea virtual environment
python3 -m venv venv

# Attiva virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# Installa dipendenze
pip install --upgrade pip
pip install -r requirements.txt

# Configura database (vedi sezione Database)
```

### 3. Setup Database

**Usando pgAdmin 4:**

1. Apri pgAdmin 4
2. Connetti al server PostgreSQL locale
3. Click destro su "Databases" → Create → Database
4. Nome: `budget_app_dev`
5. Click "Save"

**Configurazione .env:**

Crea file `backend/.env`:

```env
# Database
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/budget_app_dev
DB_HOST=localhost
DB_PORT=5432
DB_NAME=budget_app_dev
DB_USER=postgres
DB_PASSWORD=your_password

# Security
SECRET_KEY=your-super-secret-key-min-32-characters
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# Application
DEBUG=True
HOST=0.0.0.0
PORT=8000

# CORS
CORS_ORIGINS=["http://localhost:5173","http://localhost:3000"]
```

**Run migrations:**

```bash
# Da backend/ con venv attivo
alembic upgrade head
```

### 4. Setup Frontend

```bash
# Naviga nella cartella frontend
cd ../frontend

# Installa dipendenze
npm install

# Configura API URL
echo "VITE_API_URL=http://localhost:8000/api/v1" > .env
```

### 5. Avvia Applicazione

**Backend (Terminal 1):**

```bash
cd backend
source venv/bin/activate  # se non già attivo
python run.py
```

Backend disponibile su: **http://localhost:8000**  
API Docs (Swagger): **http://localhost:8000/docs**

**Frontend (Terminal 2):**

```bash
cd frontend
npm run dev
```

Frontend disponibile su: **http://localhost:5173**

---

## 🧪 Testing

### Backend Tests

```bash
cd backend
source venv/bin/activate

# Run tutti i test (finanza + ferie)
pytest tests/ -v

# Run solo test finanza
pytest tests/test_auth.py tests/test_accounts.py tests/test_transactions.py -v

# Run solo test ferie
pytest tests/test_vacation*.py tests/test_user_holidays.py -v

# Run con coverage
pytest tests/ -v --cov=app --cov-report=html

# Apri coverage report
open htmlcov/index.html  # macOS
```

### Frontend Tests

```bash
cd frontend

# Run tests (da implementare)
npm test
```

---

## 📚 Documentazione API

La documentazione API completa è disponibile tramite **Swagger UI** quando il backend è in esecuzione:

👉 **http://localhost:8000/docs**

### Endpoints Principali

#### Authentication
- `POST /api/v1/auth/register` - Registrazione nuovo utente
- `POST /api/v1/auth/login` - Login e JWT token
- `GET /api/v1/auth/me` - Profilo utente autenticato

#### Accounts
- `GET /api/v1/accounts` - Lista account utente
- `POST /api/v1/accounts` - Crea nuovo account
- `PUT /api/v1/accounts/{id}` - Modifica account
- `DELETE /api/v1/accounts/{id}` - Elimina account

#### Transactions
- `GET /api/v1/transactions` - Lista transazioni (con filtri)
- `POST /api/v1/transactions` - Crea transazione
- `PUT /api/v1/transactions/{id}` - Modifica transazione
- `DELETE /api/v1/transactions/{id}` - Elimina transazione

#### Analytics
- `GET /api/v1/analytics/summary` - Summary dashboard
- `GET /api/v1/analytics/monthly-trend` - Trend mensile

#### Vacation Planning 🆕
- `GET /api/v1/vacation/settings` - Configurazione ferie utente
- `PUT /api/v1/vacation/settings` - Aggiorna configurazione
- `GET /api/v1/vacation/entries` - Lista ferie/permessi
- `POST /api/v1/vacation/entries` - Crea singola entry
- `POST /api/v1/vacation/entries/bulk` - Crea multiple entries (range date)
- `PUT /api/v1/vacation/entries/{id}` - Modifica entry (solo note/ore)
- `DELETE /api/v1/vacation/entries/{id}` - Elimina entry
- `GET /api/v1/vacation/balance` - Balance con totali aggregati + breakdown
- `GET /api/v1/vacation/calendar/{year}/{month}` - Calendario mensile
- `GET /api/v1/vacation/holidays/{year}` - Festività nazionali italiane
- `GET /api/v1/vacation/bridges/{year}` - Opportunità ponti
- `GET /api/v1/vacation/user-holidays` - Festività custom utente
- `POST /api/v1/vacation/user-holidays` - Aggiungi festività custom
- `DELETE /api/v1/vacation/user-holidays/{id}` - Rimuovi festività custom

Vedi [API_SPEC.md](docs/API_SPEC.md) per documentazione dettagliata.

---

## 📁 Struttura Progetto

```
budget-app-saas/
├── backend/                  # FastAPI Backend
│   ├── alembic/             # Database migrations
│   │   └── versions/        # Migration files
│   ├── app/                 # Application code
│   │   ├── crud/            # Database CRUD operations
│   │   │   ├── account.py
│   │   │   ├── transaction.py
│   │   │   ├── vacation_entry.py      # 🆕 Ferie CRUD
│   │   │   ├── vacation_settings.py   # 🆕 Settings CRUD
│   │   │   └── italian_holiday.py     # 🆕 Festività CRUD
│   │   ├── models/          # SQLAlchemy models
│   │   │   ├── account.py
│   │   │   ├── transaction.py
│   │   │   ├── vacation_entry.py      # 🆕 Ferie model
│   │   │   ├── vacation_settings.py   # 🆕 Settings model
│   │   │   ├── italian_holiday.py     # 🆕 Festività model
│   │   │   └── user_holiday.py        # 🆕 Festività custom model
│   │   ├── routers/         # API routes
│   │   │   ├── auth.py
│   │   │   ├── accounts.py
│   │   │   ├── transactions.py
│   │   │   └── vacation.py            # 🆕 Vacation router
│   │   ├── schemas/         # Pydantic schemas
│   │   │   ├── account.py
│   │   │   ├── transaction.py
│   │   │   └── vacation.py            # 🆕 Vacation schemas
│   │   └── utils/           # Utility functions
│   │       ├── security.py
│   │       ├── easter.py              # 🆕 Calcolo Pasqua
│   │       ├── bridge_days.py         # 🆕 Calcolo ponti
│   │       └── vacation_balance.py    # 🆕 Balance calculator
│   ├── tests/               # Pytest tests
│   │   ├── test_auth.py
│   │   ├── test_accounts.py
│   │   ├── test_transactions.py
│   │   ├── test_vacation_settings.py  # 🆕
│   │   ├── test_vacation_entries.py   # 🆕
│   │   ├── test_vacation_bulk.py      # 🆕
│   │   ├── test_vacation_balance.py   # 🆕
│   │   └── test_user_holidays.py      # 🆕
│   ├── .env                 # Environment variables (not committed)
│   ├── .env.example         # Environment template
│   ├── main.py              # FastAPI app entry point
│   ├── requirements.txt     # Python dependencies
│   └── run.py               # Development server runner
│
├── frontend/                # React Frontend
│   ├── public/              # Static files
│   ├── src/                 # Source code
│   │   ├── components/      # React components
│   │   │   └── vacation/    # 🆕 Vacation components
│   │   │       ├── VacationCalendar.jsx
│   │   │       ├── VacationEntryModal.jsx
│   │   │       ├── BulkEntryModal.jsx         # 🆕 Inserimento multiplo
│   │   │       ├── VacationBalance.jsx        # 🆕 Balance widget
│   │   │       ├── VacationSettings.jsx       # 🆕 Settings form
│   │   │       ├── BridgeOpportunities.jsx
│   │   │       └── UserHolidaysManager.jsx
│   │   ├── pages/           # Page components
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Accounts.jsx
│   │   │   ├── Transactions.jsx
│   │   │   └── VacationPage.jsx               # 🆕 Vacation main page
│   │   ├── services/        # API services
│   │   │   ├── api.js
│   │   │   ├── authService.js
│   │   │   ├── accountService.js
│   │   │   └── vacationService.js             # 🆕 Vacation API service
│   │   ├── styles/          # CSS files
│   │   │   └── vacation.css                   # 🆕 Vacation styles
│   │   ├── App.jsx          # Main App component
│   │   └── main.jsx         # Entry point
│   ├── .env                 # Environment variables
│   ├── package.json         # Node dependencies
│   └── vite.config.js       # Vite configuration
│
├── database/                # Database scripts
│   ├── 01_create_schema.sql
│   ├── 02_seed_data.sql
│   └── schema_design.md
│
├── docs/                    # Documentation
│   ├── ARCHITECTURE.md      # System architecture
│   ├── API_SPEC.md          # API specifications
│   ├── DEPLOYMENT.md        # Deployment guide
│   ├── TESTING.md           # Testing guide
│   ├── fase_3_8_backend_vacation_UPDATED.md    # 🆕 Vacation backend guide
│   ├── fase_4_6_testing_vacation_UPDATED.md    # 🆕 Vacation testing guide
│   └── fase_5_9_frontend_vacation_UPDATED.md   # 🆕 Vacation frontend guide
│
├── docker/                  # Docker configuration
│   ├── docker-compose.yml
│   └── Dockerfile.backend
│
├── .gitignore              # Git ignore rules
├── README.md               # This file
├── roadmap.md              # Development roadmap
└── process_tracker.md      # Progress tracking
```

---

## 🗺️ Roadmap

### ✅ Fase 0: Setup Progetto (Completata)
- [x] Repository GitHub
- [x] Struttura cartelle
- [x] Frontend React prototipo
- [x] Backend Python setup
- [x] Database PostgreSQL

### ✅ Fase 1: Database Foundation (Completata)
- [x] Schema database completo
- [x] SQLAlchemy models
- [x] Alembic migrations

### ✅ Fase 2: Backend API - Autenticazione (Completata)
- [x] JWT authentication
- [x] User registration/login
- [x] Protected endpoints

### ✅ Fase 3: Backend API - Core Features (Completata)
- [x] Accounts CRUD
- [x] Transactions CRUD
- [x] Categories CRUD
- [x] Transfers CRUD
- [x] Analytics endpoints

### 🆕 Fase 3.8: Backend Vacation Planning (In corso)
- [ ] Models con maturazione separata (Ferie/ROL/Permessi)
- [ ] Tracking start date + initial balance
- [ ] Calcolo automatico Pasqua/Pasquetta
- [ ] Validazione weekend + festività
- [ ] Balance con totali aggregati
- [ ] Bulk entry endpoint
- [ ] Bridge calculator

### 📅 Fase 4: Testing & Debug
- [ ] Pytest suite completa finanza
- [ ] Pytest suite completa ferie
- [ ] Coverage >70%
- [ ] Bug fixing

### 📅 Fase 4.6: Testing Vacation Module
- [ ] Test settings con maturazione separata
- [ ] Test validazione weekend/festività
- [ ] Test balance aggregato
- [ ] Test bulk entries
- [ ] Test user holidays

### 📅 Fase 5: Frontend Integration
- [ ] Connessione API backend
- [ ] Rimozione localStorage
- [ ] User authentication flow
- [ ] Real-time data sync

### 📅 Fase 5.9: Frontend Vacation Module
- [ ] VacationSettings (form con preset CCNL)
- [ ] VacationBalance (totali aggregati prominenti)
- [ ] VacationCalendar (con festività)
- [ ] BulkEntryModal (inserimento multiplo)
- [ ] BridgeOpportunities
- [ ] UserHolidaysManager
- [ ] Responsive design

### 📅 Fase 6: Deployment
- [ ] Backend deployment (Render.com)
- [ ] Frontend deployment (Vercel)
- [ ] Database production
- [ ] CI/CD setup

### 🔮 Fase 7: Sviluppi Futuri
- [ ] Recurring transactions
- [ ] Budget planning
- [ ] Multi-currency
- [ ] Receipt scanning
- [ ] Export iCal ferie
- [ ] Mobile app

**Timeline:** 8-10 settimane  
**Vedi**: [roadmap.md](roadmap.md) per dettagli completi

---

## 🎨 Screenshots

> 📸 Screenshots coming soon! L'applicazione è attualmente in sviluppo.

### Dashboard
*Dashboard principale con overview finanziaria*

### Accounts Management
*Gestione account multipli*

### Transactions
*Lista transazioni con filtri avanzati*

### Analytics
*Grafici e statistiche personalizzate*

### 🆕 Vacation Calendar
*Calendario ferie con festività italiane e custom*

### 🆕 Vacation Balance
*Balance aggregato con breakdown dettagliato Ferie/ROL/Permessi*

### 🆕 Vacation Settings
*Configurazione maturazione separata con preset CCNL*

---

## 🏖️ Guida Vacation Planning

### Configurazione Iniziale

1. **Accedi a Impostazioni Ferie** (`/vacation` → Tab "Impostazioni")

2. **Configura Ore Lavorative**
   ```
   Ore lavorative al giorno: 8.0 (default)
   ```

3. **Imposta Maturazione Mensile**
   ```
   Ferie: 1.83 giorni/mese (= 22 giorni/anno)
   ROL: 2.67 ore/mese (= 32 ore/anno)
   Permessi: 8.67 ore/mese (= 104 ore/anno)
   
   💡 Usa i preset CCNL per configurazioni rapide!
   ```

4. **Tracking Start Date**
   ```
   Data inizio maturazione: 01/01/2026 (esempio)
   ```

5. **Saldo Iniziale (opzionale)**
   ```
   Se hai già ore maturate prima del tracking:
   - Mese riferimento: Dicembre
   - Anno riferimento: 2025
   - Ferie: 10 giorni (in GIORNI!)
   - ROL: 16 ore
   - Permessi: 40 ore
   ```

### Uso Quotidiano

**Inserimento Singolo:**
1. Vai al Calendario
2. Click su un giorno (solo giorni lavorativi)
3. Seleziona tipo (Ferie/ROL/Permesso)
4. Per ROL/Permessi: inserisci ore
5. Per Ferie: ore automatiche da settings
6. Aggiungi note opzionali
7. Salva

**Inserimento Multiplo:**
1. Click su "📅 Inserimento Multiplo"
2. Seleziona range date (es. 15/07 - 19/07)
3. Tipo: Ferie
4. ✓ Skip weekend
5. ✓ Skip festività
6. Crea → Sistema genera automaticamente 5 entries (Lun-Ven)

**Visualizza Balance:**
- Tab "Riepilogo"
- Totale disponibile prominente (giorni + ore)
- Breakdown dettagliato per tipo:
  - Ferie: maturate, usate, disponibili
  - ROL: maturate, usate, disponibili
  - Permessi: maturate, usate, disponibili
- Proiezione fine anno

**Trova Ponti:**
- Tab "Ponti"
- Lista automatica opportunità
- Es: "Ponte Liberazione 25 Apr: prendi Venerdì 26 per 4 giorni off"

**Festività Custom:**
- Tab "Festività"
- Aggiungi patrono (es. Sant'Ambrogio 7/12 Milano)
- Aggiungi chiusure aziendali
- Recurring: si ripete ogni anno

### Regole Importanti

✅ **Puoi modificare:**
- Note (sempre)
- Ore (solo per ROL/Permessi esistenti)

❌ **NON puoi modificare:**
- Data (elimina e ricrea)
- Tipo (elimina e ricrea)

❌ **NON puoi inserire:**
- Weekend (validazione blocca)
- Festività nazionali (validazione blocca)
- Festività custom (validazione blocca)

### Calcoli Automatici

**Maturazione:**
```
Ferie: initial_ferie_days + (ferie_days_per_month × mesi_lavorati) × 8h/day
ROL: initial_rol_hours + (rol_hours_per_month × mesi_lavorati)
Permessi: initial_permessi_hours + (permessi_hours_per_month × mesi_lavorati)
```

**Totale Disponibile:**
```
Total = (Ferie disponibili) + (ROL disponibili) + (Permessi disponibili)
Visualizzato sia in ORE che in GIORNI
```

**Proiezione Fine Anno:**
```
Projected = Disponibile ora + (Maturazione mesi rimanenti)
```

---

## 🤝 Contributing

Questo è attualmente un progetto personale in sviluppo. Contributi, issues e feature requests sono benvenuti!

### Come Contribuire

1. **Fork** il repository
2. **Crea** un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** le tue modifiche (`git commit -m 'Add some AmazingFeature'`)
4. **Push** al branch (`git push origin feature/AmazingFeature`)
5. **Apri** una Pull Request

### Linee Guida

- Segui le convenzioni di codice esistenti
- Aggiungi test per nuove features
- Aggiorna la documentazione
- Mantieni i commit atomici e descrittivi

---

## 🐛 Bug Reports & Feature Requests

Per segnalare bug o richiedere nuove features, apri una [GitHub Issue](https://github.com/TUO-USERNAME/budget-app-saas/issues).

**Template Bug Report:**
```
**Descrizione del Bug**
Breve descrizione del problema

**Come Riprodurre**
1. Vai a '...'
2. Click su '...'
3. Vedi errore

**Comportamento Atteso**
Cosa dovrebbe accadere

**Screenshots**
Se applicabile

**Ambiente**
- OS: [es. macOS 14]
- Browser: [es. Chrome 120]
- Versione: [es. 1.0.0]
```

---

## 📄 License

Questo progetto è rilasciato sotto licenza **MIT License** - vedi il file [LICENSE](LICENSE) per dettagli.

```
MIT License

Copyright (c) 2025 Giovanni Mezzasalma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👤 Author

**Giovanni Mezzasalma**  
Chemical Engineer & Project Engineer  
Specializing in AVEVA PI System implementations

- 🌐 Location: Sicily, Italy
- 💼 Company: Pimsoft
- 🔧 Expertise: Industrial automation, data solutions, full-stack development
- 📧 Email: [your-email@example.com]
- 💼 LinkedIn: [Your LinkedIn Profile]
- 🐙 GitHub: [@TUO-USERNAME](https://github.com/TUO-USERNAME)

---

## 🙏 Acknowledgments

- Progetto nato come evoluzione di un sistema di gestione budget Excel
- Ispirato da moderne SaaS financial apps
- Vacation planning module progettato per lavoratori italiani (CCNL Commercio/Metalmeccanico)
- Built with ❤️ in Sicily

---

## 📊 Project Stats

![GitHub repo size](https://img.shields.io/github/repo-size/TUO-USERNAME/budget-app-saas)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/TUO-USERNAME/budget-app-saas)
![GitHub last commit](https://img.shields.io/github/last-commit/TUO-USERNAME/budget-app-saas)

---

<div align="center">

**⭐ Se questo progetto ti è utile, lascia una stella! ⭐**

Made with ☕ and 💻 by [Giovanni Mezzasalma](https://github.com/TUO-USERNAME)

</div>