# 🏗️ System Architecture - Budget App

**Documento:** Architettura Sistema  
**Versione:** 1.0  
**Data:** Novembre 2025  
**Autore:** Giovanni Mezzasalma

---

## 📋 Indice

1. [Overview](#overview)
2. [Architettura Alto Livello](#architettura-alto-livello)
3. [Backend Architecture](#backend-architecture)
4. [Frontend Architecture](#frontend-architecture)
5. [Database Design](#database-design)
6. [Security Architecture](#security-architecture)
7. [Data Flow](#data-flow)
8. [Deployment Architecture](#deployment-architecture)

---

## 🎯 Overview

Budget App è una **Single Page Application (SPA)** multi-tenant per gestione finanze personali, costruita con architettura **client-server** separata.

### Caratteristiche Architetturali

- **Multi-Tenant**: Isolamento completo dati per utente
- **RESTful API**: Backend espone API REST documentate
- **JWT Authentication**: Stateless authentication
- **Responsive Design**: Frontend ottimizzato per desktop e mobile
- **Docker-Ready**: Containerizzazione per deployment
- **Database-First**: PostgreSQL come single source of truth

---

## 🏛️ Architettura Alto Livello

```
┌─────────────────────────────────────────────────────────────┐
│                         FRONTEND                            │
│  ┌────────────────────────────────────────────────────┐    │
│  │         React SPA (Vite + TailwindCSS)             │    │
│  │                                                     │    │
│  │  • Dashboard                                        │    │
│  │  • Account Management                               │    │
│  │  • Transaction Management                           │    │
│  │  • Analytics & Charts                               │    │
│  └────────────────────────────────────────────────────┘    │
│                           ↕                                 │
│                    HTTPS / REST API                         │
└─────────────────────────────────────────────────────────────┘
                            ↕
┌─────────────────────────────────────────────────────────────┐
│                         BACKEND                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │          FastAPI (Python 3.12)                      │    │
│  │                                                     │    │
│  │  • API Endpoints (REST)                             │    │
│  │  • Authentication (JWT)                             │    │
│  │  • Business Logic                                   │    │
│  │  • Data Validation (Pydantic)                       │    │
│  └────────────────────────────────────────────────────┘    │
│                           ↕                                 │
│  ┌────────────────────────────────────────────────────┐    │
│  │          SQLAlchemy ORM                             │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                            ↕
┌─────────────────────────────────────────────────────────────┐
│                        DATABASE                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │          PostgreSQL 16                              │    │
│  │                                                     │    │
│  │  • User Data                                        │    │
│  │  • Financial Transactions                           │    │
│  │  • Multi-tenant Isolation                           │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 Backend Architecture

### Struttura Moduli

```
backend/
├── app/
│   ├── api/                    # API Layer
│   │   └── endpoints/          # Route handlers
│   │       ├── auth.py         # Authentication endpoints
│   │       ├── accounts.py     # Account CRUD
│   │       ├── transactions.py # Transaction CRUD
│   │       ├── categories.py   # Category CRUD
│   │       ├── transfers.py    # Transfer operations
│   │       └── analytics.py    # Statistics & reports
│   │
│   ├── crud/                   # Data Access Layer
│   │   ├── user.py             # User database operations
│   │   ├── account.py          # Account database operations
│   │   └── ...                 # Altri CRUD operations
│   │
│   ├── models/                 # SQLAlchemy Models
│   │   ├── user.py             # User model
│   │   ├── account.py          # Account model
│   │   ├── transaction.py      # Transaction model
│   │   └── ...                 # Altri models
│   │
│   ├── schemas/                # Pydantic Schemas
│   │   ├── user.py             # User validation schemas
│   │   ├── account.py          # Account validation schemas
│   │   └── ...                 # Altri schemas
│   │
│   ├── utils/                  # Utilities
│   │   └── security.py         # JWT, password hashing
│   │
│   ├── config.py               # Configuration management
│   ├── database.py             # Database connection
│   └── dependencies.py         # FastAPI dependencies
│
├── alembic/                    # Database Migrations
├── tests/                      # Test Suite
├── main.py                     # FastAPI app entry point
└── run.py                      # Development server
```

### Layers & Responsibilities

#### 1. **API Layer** (`app/api/endpoints/`)
- Gestisce richieste HTTP
- Validazione input (Pydantic)
- Autenticazione/Autorizzazione
- Serializzazione output
- Error handling

#### 2. **Business Logic Layer** (`app/crud/`)
- Logica di business
- Operazioni database (CRUD)
- Transazioni complesse
- Calcoli e aggregazioni

#### 3. **Data Layer** (`app/models/`)
- Definizione schema database (SQLAlchemy)
- Relazioni tra entità
- Constraints e validazioni DB

---

## 💻 Frontend Architecture

### Struttura Componenti

```
frontend/
├── src/
│   ├── components/             # Reusable Components
│   │   ├── Navbar.jsx          # Navigation
│   │   ├── AccountCard.jsx     # Account display
│   │   ├── TransactionList.jsx # Transaction list
│   │   └── ...
│   │
│   ├── pages/                  # Page Components
│   │   ├── Login.jsx           # Login page
│   │   ├── Register.jsx        # Registration
│   │   ├── Dashboard.jsx       # Main dashboard
│   │   ├── Accounts.jsx        # Account management
│   │   ├── Transactions.jsx    # Transaction management
│   │   └── Analytics.jsx       # Charts & statistics
│   │
│   ├── services/               # API Services
│   │   ├── api.js              # Axios instance
│   │   ├── authService.js      # Auth API calls
│   │   ├── accountService.js   # Account API calls
│   │   └── ...
│   │
│   ├── utils/                  # Utilities
│   │   ├── formatters.js       # Date, currency formatting
│   │   └── validators.js       # Form validations
│   │
│   ├── App.jsx                 # Main app component
│   └── main.jsx                # Entry point
```

### Component Hierarchy

```
App
├── Router
    ├── Public Routes
    │   ├── Login
    │   └── Register
    │
    └── Protected Routes (require auth)
        ├── Dashboard
        │   ├── AccountSummary
        │   ├── RecentTransactions
        │   └── QuickStats
        │
        ├── Accounts
        │   ├── AccountList
        │   ├── AccountForm
        │   └── AccountCard
        │
        ├── Transactions
        │   ├── TransactionList
        │   ├── TransactionForm
        │   └── FilterBar
        │
        └── Analytics
            ├── TrendChart
            ├── CategoryPieChart
            └── CustomChartBuilder
```

---

## 🗄️ Database Design

### Schema Relazionale

```sql
users
├── id (PK, UUID)
├── email (UNIQUE)
├── password_hash
├── full_name
├── created_at
└── is_active

accounts
├── id (PK, UUID)
├── user_id (FK → users.id)
├── name
├── account_type (ENUM)
├── balance
├── currency
└── is_active

categories
├── id (PK, UUID)
├── user_id (FK → users.id)
├── name
├── type (income/expense)
├── color
└── is_system

transactions
├── id (PK, UUID)
├── user_id (FK → users.id)
├── account_id (FK → accounts.id)
├── category_id (FK → categories.id)
├── amount
├── type (income/expense)
├── date
└── description

transfers
├── id (PK, UUID)
├── user_id (FK → users.id)
├── from_account_id (FK → accounts.id)
├── to_account_id (FK → accounts.id)
├── amount
└── date
```

### Relazioni

- **User → Accounts**: One-to-Many
- **User → Categories**: One-to-Many
- **User → Transactions**: One-to-Many
- **Account → Transactions**: One-to-Many
- **Category → Transactions**: One-to-Many

### Indici

```sql
-- Performance optimization
CREATE INDEX idx_transactions_user_date ON transactions(user_id, date DESC);
CREATE INDEX idx_transactions_account ON transactions(account_id);
CREATE INDEX idx_accounts_user ON accounts(user_id);
```

---

## 🔒 Security Architecture

### Authentication Flow

```
1. User Registration
   ↓
   Password → bcrypt hash → Store in DB
   
2. User Login
   ↓
   Verify password → Generate JWT token → Return to client
   
3. Protected Request
   ↓
   Client sends JWT in Authorization header
   ↓
   Backend validates JWT
   ↓
   Extract user_id → Fetch user → Process request
```

### Security Measures

#### Backend
- ✅ **Password Hashing**: Bcrypt con salt
- ✅ **JWT Tokens**: Stateless authentication
- ✅ **CORS**: Whitelist frontend origins
- ✅ **SQL Injection**: SQLAlchemy ORM parametrized queries
- ✅ **Rate Limiting**: (da implementare)
- ✅ **HTTPS Only**: Production
- ✅ **Input Validation**: Pydantic schemas

#### Database
- ✅ **Row-Level Security**: `user_id` in ogni query
- ✅ **Foreign Keys**: Referential integrity
- ✅ **Constraints**: Check constraints per validazione
- ✅ **Backup**: Automatico (production)

#### Frontend
- ✅ **Token Storage**: localStorage (con expiration)
- ✅ **XSS Protection**: React auto-escaping
- ✅ **CSRF**: JWT non in cookies
- ✅ **HTTPS**: Secure communication

---

## 🔄 Data Flow

### Esempio: Create Transaction

```
1. USER ACTION
   Frontend: User fills transaction form
   
2. VALIDATION
   Frontend: Client-side validation
   
3. API CALL
   POST /api/v1/transactions
   Headers: Authorization: Bearer <JWT>
   Body: { account_id, category_id, amount, type, date }
   
4. AUTHENTICATION
   Backend: Verify JWT → Extract user_id
   
5. AUTHORIZATION
   Backend: Verify account belongs to user
   
6. BUSINESS LOGIC
   Backend: 
   - Create transaction record
   - Update account balance (+/- amount)
   - Both in same database transaction
   
7. RESPONSE
   Backend: Return transaction object
   
8. UI UPDATE
   Frontend: Update transaction list & account balance
```

---

## 🚀 Deployment Architecture

### Development

```
Local Machine
├── PostgreSQL (localhost:5432)
├── Backend FastAPI (localhost:8000)
└── Frontend Vite Dev Server (localhost:5173)
```

### Production (Planned)

```
                    ┌──────────────┐
                    │   Cloudflare │
                    │     (CDN)    │
                    └──────┬───────┘
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
   ┌────▼────┐                          ┌────▼────┐
   │ Vercel  │                          │ Render  │
   │Frontend │                          │ Backend │
   │  (SPA)  │                          │ FastAPI │
   └─────────┘                          └────┬────┘
                                             │
                                      ┌──────▼──────┐
                                      │   Render    │
                                      │ PostgreSQL  │
                                      └─────────────┘
```

### CI/CD Pipeline (Planned)

```
GitHub Push
    ↓
GitHub Actions
    ↓
├── Backend Tests
├── Frontend Tests
└── Build
    ↓
Deploy to Production
```

---

## 📊 Performance Considerations

### Database
- **Indexing**: Strategico su colonne filtrate frequentemente
- **Connection Pooling**: SQLAlchemy pool
- **Query Optimization**: SELECT solo colonne necessarie
- **Pagination**: Limit/Offset per liste lunghe

### Backend
- **Async Operations**: FastAPI async/await
- **Caching**: (da implementare - Redis)
- **Compression**: Gzip response

### Frontend
- **Code Splitting**: Vite automatic
- **Lazy Loading**: React.lazy per routes
- **Asset Optimization**: Minification, compression
- **CDN**: Static assets

---

## 🔮 Future Enhancements

### Scalability
- [ ] Redis per session/cache
- [ ] Message Queue (Celery) per jobs asincroni
- [ ] Database Read Replicas
- [ ] Microservices architecture (se necessario)

### Monitoring
- [ ] Sentry per error tracking
- [ ] Application Performance Monitoring (APM)
- [ ] Database query monitoring
- [ ] User analytics

---

## 📚 Riferimenti

- [FastAPI Best Practices](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [React Architecture Patterns](https://react.dev/learn/thinking-in-react)
- [RESTful API Design](https://restfulapi.net/)

---

**Documento creato:** Novembre 2025  
**Ultima modifica:** Novembre 2025  
**Versione:** 1.0
