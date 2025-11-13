# 💰 Budget App - Multi-User Personal Finance Manager

<div align="center">

![Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Python](https://img.shields.io/badge/Python-3.12.4-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688)
![React](https://img.shields.io/badge/React-18-61DAFB)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791)
![License](https://img.shields.io/badge/License-MIT-green)

**Una moderna applicazione web per la gestione del budget personale con supporto multi-utente**

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

Il progetto nasce come evoluzione di un prototipo Excel, trasformato in un'applicazione web scalabile con autenticazione multi-utente e database PostgreSQL.

---

## ✨ Features

### 🎯 Core Features (MVP)

- ✅ **Dashboard Interattiva**: Visualizzazione real-time di balance, income, expense
- ✅ **Multi-Account Management**: Gestione conti corrente, risparmio, contanti, investimenti
- ✅ **Categorizzazione Smart**: Categorie predefinite + custom categories
- ✅ **Transazioni Complete**: Tracking entrate/uscite con descrizione, note, tags
- ✅ **Trasferimenti tra Account**: Gestione automatica balance
- ✅ **Filtri Avanzati**: Per data, account, categoria, tipo
- ✅ **Statistiche Mensili**: Trend income/expense, grafici a torta per categorie
- ✅ **Custom Chart Builder**: Crea e salva grafici personalizzati
- 🔒 **Sistema di Autenticazione**: JWT-based authentication
- 🔒 **Multi-User Support**: Isolamento dati per utente
- 🔒 **API REST Completa**: Backend FastAPI documentato

### 🚀 Planned Features (Post-MVP)

- [ ] **Recurring Transactions**: Auto-generazione transazioni ricorrenti
- [ ] **Budget Planning**: Impostazione budget mensile per categoria
- [ ] **Bill Reminders**: Notifiche scadenze bollette
- [ ] **Multi-Currency**: Supporto valute multiple con conversione
- [ ] **Receipt Scanning**: OCR per estrarre dati da scontrini
- [ ] **Shared Accounts**: Condivisione account tra più utenti
- [ ] **Mobile App**: React Native app per iOS/Android
- [ ] **Bank Sync**: Integrazione con conti bancari (Plaid/Tink)
- [ ] **AI Insights**: Pattern detection e suggerimenti risparmio

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

# Run tutti i test
pytest tests/ -v

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

Vedi [API_SPEC.md](docs/API_SPEC.md) per documentazione dettagliata.

---

## 📁 Struttura Progetto

```
budget-app-saas/
├── backend/                  # FastAPI Backend
│   ├── alembic/             # Database migrations
│   │   └── versions/        # Migration files
│   ├── app/                 # Application code
│   │   ├── api/             # API routes
│   │   │   └── endpoints/   # Endpoint modules
│   │   ├── core/            # Core functionality
│   │   ├── crud/            # Database CRUD operations
│   │   ├── models/          # SQLAlchemy models
│   │   ├── schemas/         # Pydantic schemas
│   │   └── utils/           # Utility functions
│   ├── tests/               # Pytest tests
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
│   │   ├── pages/           # Page components
│   │   ├── services/        # API services
│   │   ├── utils/           # Utility functions
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
│   └── TESTING.md           # Testing guide
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

### ✅ Fase 0: Setup Progetto (Completata ~60%)
- [x] Repository GitHub
- [x] Struttura cartelle
- [x] Frontend React prototipo
- [ ] Backend Python setup
- [ ] Database PostgreSQL

### 🚧 Fase 1: Database Foundation (In corso)
- [ ] Schema database completo
- [ ] SQLAlchemy models
- [ ] Alembic migrations

### 📅 Fase 2: Backend API - Autenticazione
- [ ] JWT authentication
- [ ] User registration/login
- [ ] Protected endpoints

### 📅 Fase 3: Backend API - Core Features
- [ ] Accounts CRUD
- [ ] Transactions CRUD
- [ ] Categories CRUD
- [ ] Transfers CRUD
- [ ] Analytics endpoints

### 📅 Fase 4: Testing & Debug
- [ ] Pytest suite completa
- [ ] Coverage >70%
- [ ] Bug fixing

### 📅 Fase 5: Frontend Integration
- [ ] Connessione API backend
- [ ] Rimozione localStorage
- [ ] User authentication flow
- [ ] Real-time data sync

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
- [ ] Mobile app

**Timeline:** 6-8 settimane  
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
