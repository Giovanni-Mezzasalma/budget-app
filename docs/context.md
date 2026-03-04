# BudgetApp — Project Context

> File di contesto per Claude. Posizione: `budget-app/docs/context.md`  
> Caricalo all'inizio di ogni sessione di lavoro per fornire contesto completo senza dover riepilogare ogni volta.

---

## 🧑‍💻 Developer

**Giovanni Mezzasalma** — Ingegnere chimico / project engineer con background in automazione industriale (AVEVA PI System). Full-stack development autodidatta. Obiettivo a lungo termine: fondare una software house. BudgetApp è sia un progetto concreto sia un portfolio MVP da mostrare a potenziali investitori o co-founder.

---

## 🎯 Progetto: BudgetApp

Applicazione SaaS di personal finance per il **mercato italiano**. Nata come evoluzione di un sistema Excel personale, ora è una web app per la gestione delle finanze personali di un singolo utente.

**Differenziatori chiave:**
- Integrazione CCNL (Commercio / Metalmeccanico) per pianificazione ferie
- Calcolo automatico Pasqua/Pasquetta (algoritmo di Butcher)
- Identificazione automatica bridge days (ponti ottimali)
- Maturazione separata per tipo (Ferie / ROL / Permessi)

**Pricing previsto (post-MVP):**
- Personal: €2.99/mese
- Personal+: €4.99/mese (investimenti, crypto)
- Freelance: €9.99/mese (fatturazione, clienti, progetti)

---

## 🛠 Stack Tecnico

| Layer | Tecnologia |
|-------|-----------|
| Backend | Python 3.12 + FastAPI |
| Database | PostgreSQL (UUID nativo) |
| ORM | SQLAlchemy |
| Validazione | Pydantic v2 |
| Migrations | Alembic |
| Testing | Pytest + pytest-cov |
| Frontend | React (Vite) + TailwindCSS |
| HTTP Client | Axios |
| Charts | Recharts |
| Auth | JWT 7gg + bcrypt |
| Containerizzazione | Docker + Docker Compose |

---

## 📁 Struttura Progetto
```
budget-app/
├── backend/
│   ├── alembic/versions/
│   ├── app/
│   │   ├── crud/          # account, category, transaction, transfer,
│   │   │                  # analytics, vacation_entry, vacation_settings,
│   │   │                  # italian_holiday, user_holiday
│   │   ├── models/        # SQLAlchemy models (stessi moduli di crud)
│   │   ├── routers/       # auth, accounts, categories, transactions,
│   │   │                  # transfers, analytics, vacation
│   │   ├── schemas/       # Pydantic schemas
│   │   └── utils/         # security, easter, bridge_days, vacation_balance
│   ├── tests/             # conftest + test per ogni modulo
│   └── requirements.txt
├── frontend/src/
│   ├── services/          # Axios API layer
│   ├── pages/
│   └── components/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API_SPEC.md
│   ├── DEVELOPMENT.md
│   └── context.md         # ← questo file
├── roadmap.md
└── process_tracker.md
```

---

## 📊 Stato Avanzamento (~80% MVP)

### ✅ Completato

- **Fase 0** — Setup, repo, Docker, documentazione base
- **Fase 1** — Schema PostgreSQL, modelli, migrations Alembic, UUID refactoring nativo
- **Fase 2** — Auth: register, login, JWT, `GET /auth/me`
- **Fase 3** — Backend core:
  - Accounts CRUD + balance tracking
  - Categories CRUD + `seed_default_categories()` (Income / Expense Necessity / Expense Extra)
  - Transactions CRUD con aggiornamento balance automatico
  - Transfers CRUD con doppio aggiornamento balance
  - Analytics: `/summary`, `/monthly-trend`
  - Custom Charts
  - Code review: UUID types, enum alignment, path fixes, commenti → English
- **Fase 3.8** — Vacation module backend completo:
  - Maturazione separata (ferie/ROL/permessi), saldo iniziale, `tracking_start_date`
  - 10 festività fisse + Pasquetta dinamica
  - Validazioni: no weekend, no festività, no duplicati
  - Bulk entry con skip weekend/festività
  - Balance aggregato + breakdown per tipo
  - Calendario mensile, bridge opportunities, festività custom utente

### 🔲 Da Completare

- **Fase 4** — Pytest completo (priorità: vacation module, target ≥70% coverage)
- **Fase 3.9** — CSV import / Excel export (documentazione già scritta)
- **Fase 5** — Frontend React (auth → dashboard → moduli → vacation UI)
- **Fase 6** — Deployment (VPS, Docker Compose, HTTPS)

---

## 🔑 Decisioni Architetturali

| Decisione | Scelta | Motivazione |
|-----------|--------|-------------|
| Balance strategy | Campo `balance` aggiornato ad ogni tx | Semplicità vs calcolo dinamico |
| Transaction types | 3 tipi: `income`, `expense_necessity`, `expense_extra` | Coerente con Excel originale |
| UUID | Nativo PostgreSQL | Performance, no conversioni string |
| Vacation entry editing | Solo `notes` e `hours` modificabili | No ricalcolo balance ferie |
| Lingua commenti | English only | Uniformità e professionalità |

---

## 🧠 Principi di Sviluppo

- Ship first, iterate later — MVP funzionante > perfezione tecnica
- Documentazione prima del codice (`roadmap.md` + `process_tracker.md` sempre aggiornati)
- Modifiche in ordine logico: model → schema → CRUD → router
- No over-engineering — funzionalità non-MVP → Fase 7

---

## 📋 API

**Base URL locale:** `http://localhost:8000/api/v1`  
**Swagger UI:** `http://localhost:8000/docs`

| Modulo | Endpoints principali |
|--------|---------------------|
| Auth | `POST /auth/register`, `POST /auth/login`, `GET /auth/me` |
| Accounts | `GET/POST /accounts`, `GET/PUT/DELETE /accounts/{id}` |
| Categories | `GET/POST /categories`, `PUT/DELETE /categories/{id}` |
| Transactions | `GET/POST /transactions`, `PUT/DELETE /transactions/{id}` |
| Transfers | `GET/POST /transfers`, `DELETE /transfers/{id}` |
| Analytics | `GET /analytics/summary`, `GET /analytics/monthly-trend` |
| Vacation | `/vacation/settings`, `/vacation/entries`, `/vacation/entries/bulk`, `/vacation/balance`, `/vacation/calendar/{year}/{month}`, `/vacation/bridges/{year}`, `/vacation/holidays/{year}` |

---

## 🚀 Avvio Locale
```bash
# Backend
cd backend
source venv/bin/activate
uvicorn app.main:app --reload
# Docs: http://localhost:8000/docs

# Frontend
cd frontend
npm run dev
# App: http://localhost:5173
```

---

*Ultimo aggiornamento: Marzo 2026 | Giovanni Mezzasalma*