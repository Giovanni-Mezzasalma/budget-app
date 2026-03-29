# 📊 PROGRESS TRACKER - Budget App Development

**Progetto:** Budget Management SaaS
**Data Inizio:** _____________
**Developer:** Giovanni Mezzasalma
**Target Completion:** _____________

---

## 📅 TIMELINE OVERVIEW

| Fase | Descrizione          | Durata Stimata | Data Inizio | Data Fine | Status |
| ---- | -------------------- | -------------- | ----------- | --------- | ------ |
| 0    | Setup Progetto       | 1 giorno       |             |           | ⬜     |
| 1    | Database Foundation  | 2-3 giorni     |             |           | ⬜     |
| 2    | Backend - Auth       | 3-4 giorni     |             |           | ⬜     |
| 3    | Backend - Core       | 4-5 giorni     |             |           | ⬜     |
| 4    | Testing & Debug      | 2 giorni       |             |           | ⬜     |
| 5    | Frontend Integration | 5-7 giorni     |             |           | ⬜     |
| 6    | Deployment           | 3-4 giorni     |             |           | ⬜     |

**Legenda Status:** ⬜ Non iniziato | 🟡 In corso | ✅ Completato

---

## ✅ FASE 0: SETUP PROGETTO

**Data Inizio:** 13/11/2025 | **Data Fine:** 15/11/2025 | **Status:** ✅ Completato

### 0.1 - Configurazione Repository GitHub

- [X] Repository creato su GitHub
- [X] GitHub Desktop configurato
- [X] VS Code aperto sul progetto
- [X] Git verification ✓

### 0.2 - Struttura Cartelle

- [X] Cartella `backend/` creata
- [X] Cartella `frontend/` creata
- [X] Cartella `database/` creata
- [X] Cartella `docs/` creata
- [X] Cartella `docker/` creata
- [X] File `.gitkeep` in ogni cartella

### 0.3 - File Configurazione

- [X] `.gitignore` creato e popolato
- [X] `README.md` aggiornato con tech stack
- [X] Primo commit pushato

### 0.4 - Python Virtual Environment

- [X] `venv` creato in `backend/`
- [X] `venv` attivato con successo
- [X] `requirements.txt` creato
- [X] Tutte le dipendenze installate
- [X] `pip list` verificato
- [X] Commit dependencies

### 0.5 - Database PostgreSQL

- [X] pgAdmin 4 aperto
- [X] Database `budget_app_dev` creato
- [X] User `budget_user` creato (opzionale)
- [X] File `.env` creato (NON committato)
- [X] File `.env.example` creato e committato
- [X] `test_db_connection.py` creato
- [X] Test connessione passato ✅
- [X] Commit database setup

### 0.6 - Docker Setup

- [X] `docker-compose.yml` creato
- [X] `Dockerfile` backend creato
- [X] Commit Docker files

### 0.7 - Documentazione

- [X] `docs/ARCHITECTURE.md` creato
- [X] `docs/API_SPEC.md` creato
- [X] `docs/DEVELOPMENT.md` creato
- [X] Commit documentazione

**CHECKPOINT FASE 0:**

- [X] ✅ Tutti i task completati
- [X] ✅ Repository funzionante
- [X] ✅ Database connesso
- [X] ✅ Ready per FASE 1

---

## ✅ FASE 1: DATABASE FOUNDATION

**Data Inizio:** 15/11/2025 | **Data Fine:** 19/11/2025 | **Status:** ✅ Completato

### 1.1 - Schema Database SQL

- [X] `database/schema_design.md` creato
- [X] `database/01_create_schema.sql` creato
- [X] Script eseguito in pgAdmin
- [X] Tutte le 6 tabelle create
- [X] Tabelle visibili in pgAdmin
- [X] `database/02_seed_default_categories.sql` creato
- [X] Funzione seed eseguita
- [X] Commit database scripts

### 1.2 - Modelli SQLAlchemy

- [X] `backend/app/config.py` creato
- [X] `backend/app/database.py` creato
- [X] `backend/app/models/__init__.py` creato
- [X] `backend/app/models/user.py` creato
- [X] `backend/app/models/account.py` creato
- [X] `backend/app/models/category.py` creato
- [X] `backend/app/models/transaction.py` creato
- [X] `backend/app/models/transfer.py` creato
- [X] `backend/app/models/custom_chart.py` creato
- [X] Commit models

### 1.3 - Alembic Migrations

- [X] Alembic inizializzato (`alembic init`)
- [X] `alembic.ini` configurato
- [X] `alembic/env.py` modificato
- [X] Prima migration generata
- [X] Migration applicata (`alembic upgrade head`)
- [X] Tabella `alembic_version` creata
- [X] `backend/reset_db.py` creato
- [X] Commit migrations

**CHECKPOINT FASE 1:**

- [X] ✅ Schema database completo
- [X] ✅ Modelli SQLAlchemy funzionanti
- [X] ✅ Alembic configurato
- [X] ✅ Test `Base.metadata.tables.keys()` passato
- [X] ✅ Ready per FASE 2

---

## ✅ FASE 2: BACKEND API - AUTENTICAZIONE

**Data Inizio:** 19/11/2025 | **Data Fine:** 21/11/2025 | **Status:** ✅ Completato

### 2.1 - Security Utilities

- [X] `backend/app/utils/security.py` creato
- [X] `hash_password()` implementata
- [X] `verify_password()` implementata
- [X] `create_access_token()` implementata
- [X] `verify_token()` implementata
- [X] Commit security utils

### 2.2 - Pydantic Schemas

- [X] `backend/app/schemas/__init__.py` creato
- [X] `backend/app/schemas/user.py` completo
- [X] `backend/app/schemas/account.py` creato (base)
- [X] `backend/app/schemas/category.py` creato (base)
- [X] `backend/app/schemas/transaction.py` creato (base)
- [X] `backend/app/schemas/transfer.py` creato (base)
- [X] Commit schemas

### 2.3 - Authentication Dependencies

- [X] `backend/app/dependencies.py` creato
- [X] `get_current_user()` implementata
- [X] `get_current_active_user()` implementata
- [X] Commit dependencies

### 2.4 - Auth Router

- [X] `backend/app/crud/user.py` creato
- [X] `get_user_by_email()` implementata
- [X] `create_user()` implementata
- [X] `authenticate_user()` implementata
- [X] `backend/app/routers/auth.py` creato
- [X] POST `/auth/register` implementato
- [X] POST `/auth/login` implementato
- [X] GET `/auth/me` implementato
- [X] Commit auth router

### 2.5 - Main Application

- [X] `backend/main.py` creato
- [X] CORS middleware configurato
- [X] Auth router incluso
- [X] `backend/run.py` creato
- [X] Server avviato con successo
- [X] Swagger UI accessibile (http://localhost:8000/docs)
- [X] Commit main app

### 2.6 - Testing Authentication

- [X] Test registrazione in Swagger: SUCCESS
- [X] Test login in Swagger: SUCCESS
- [X] Test GET /me con token: SUCCESS
- [X] Utente visibile in pgAdmin
- [X] Password hashata (non in chiaro)
- [X] Test email duplicata: ERROR 400 ✓
- [X] Test password sbagliata: ERROR 401 ✓
- [X] Test /me senza token: ERROR 401 ✓
- [X] `docs/TESTING.md` creato
- [X] Commit testing docs

**CHECKPOINT FASE 2:**

- [X] ✅ Auth completa funzionante
- [X] ✅ JWT tokens generati correttamente
- [X] ✅ Swagger UI testato
- [X] ✅ Tutti gli error cases coperti
- [X] ✅ Ready per FASE 3

---

## 🟡 FASE 3: BACKEND API - CORE FEATURES

**Data Inizio:** 21/11/2025 | **Data Fine:** ________ | **Status:** 🟡 In corso (70% completato)

### 3.1 - Accounts CRUD & Router

- [X] `backend/app/schemas/account.py` completato
- [X] `backend/app/crud/account.py` creato
- [X] Tutte le funzioni CRUD implementate
- [X] `update_account_balance()` implementata
- [X] `backend/app/routers/accounts.py` creato
- [X] Tutti gli endpoints implementati
- [X] Router registrato in `main.py`
- [X] Test POST /accounts: SUCCESS
- [X] Test GET /accounts: SUCCESS
- [X] Test PUT /accounts/{id}: SUCCESS
- [X] Test DELETE /accounts/{id}: SUCCESS
- [X] Dati verificati in pgAdmin
- [X] Commit accounts

### 3.2 - Categories CRUD & Router

- [X] `backend/app/schemas/category.py` completato
- [X] `backend/app/crud/category.py` creato
- [X] `seed_default_categories()` implementata
- [X] `backend/app/routers/categories.py` creato
- [X] Router registrato in `main.py`
- [X] Test tutti gli endpoints: SUCCESS
- [X] Commit categories

### 3.3 - Transactions CRUD & Router

- [X] `backend/app/schemas/transaction.py` completato
- [X] `backend/app/crud/transaction.py` creato
- [X] `create_transaction()` con update balance
- [X] `backend/app/routers/transactions.py` creato
- [X] Query parameters per filtri implementati
- [X] Router registrato in `main.py`
- [X] Test creazione transaction: SUCCESS
- [X] Balance account aggiornato: VERIFIED ✓
- [X] Test filtri: SUCCESS
- [X] Commit transactions

### 3.4 - Transfers CRUD & Router

- [X] `backend/app/schemas/transfer.py` completato
- [X] `backend/app/crud/transfer.py` creato
- [X] `create_transfer()` con update 2 balance
- [X] `backend/app/routers/transfers.py` creato
- [X] Router registrato in `main.py`
- [X] Test transfer: SUCCESS
- [X] Entrambi i balance aggiornati: VERIFIED ✓
- [X] Commit transfers

### 3.5 - Custom Charts (opzionale)

- [X] Deciso: [x] Implementare ora [ ] Rimandare a Sviluppi Futuri
- [X] Se implementato: CRUD e router creati

### 3.6 - Analytics Endpoints

- [X] `backend/app/routers/analytics.py` creato
- [X] GET `/analytics/summary` implementato
- [X] GET `/analytics/monthly-trend` implementato
- [X] Router registrato in `main.py`
- [X] Test summary: SUCCESS
- [X] Test monthly trend: SUCCESS
- [X] Commit analytics

### 3.7 - Code Review & Bug Fixing

**Obiettivo:** Correggere incongruenze e bug identificati nella code review prima di procedere con Testing (Fase 4).

#### Problemi Critici

##### A. Strategia Balance Account

- [X] Analizzato problema `initial_balance` vs `current_balance`
- [X] Decisione presa: [ ] Opzione A (rinomina) / [ ] Opzione B (calcolo dinamico) / [x] Opzione C (campo separato)
- [X] Implementazione completata
- [X] File modificati:
  - [X] `app/models/account.py`
  - [X] `app/crud/account.py`
  - [X] `app/crud/transaction.py`
  - [X] `app/crud/transfer.py`
- [X] Test balance dopo transazione: PASS
- [X] Test balance dopo transfer: PASS

##### B. Allineamento Tipi Transazione (3 tipi)

- [X] Aggiornato commento in `app/models/category.py`
- [X] Aggiornato commento in `app/models/transaction.py`
- [X] Verificato che schema e CRUD usino stessi 3 tipi
- [X] Documentazione allineata

##### C. Path Correzione

- [X] Corretto `backend/Dockerfile`: `main:app` → `app.main:app` (Docker build funziona non ancora testato)

#### Problemi Medi

##### D. Centralizzazione Enum ChartType

- [X] Rimosso enum duplicato da `app/models/custom_chart.py`
- [X] Import da `app/schemas/custom_chart.py`
- [X] Test endpoint custom-charts funzionante

##### E. Validazione update_transfer

- [X] Revisione codice `app/crud/transfer.py`
- [X] Verificati tutti i casi edge
- [X] Aggiunta validazione mancante (se necessaria)

##### F. File SQL Obsoleti

- [X] Decisione: [x] Rimuovere / [ ] Archiviare / [ ] Aggiornare
- [X] Azione completata
- [X] Documentato in README se necessario

#### Note Documentate

##### G. Migration Vuota (c744b8064fb0)

- [X] ✅ Documentato: tabella `custom_charts` creata via SQL manuale
- [X] ✅ Non richiede fix, solo nota per riferimento futuro

##### H-J. Altri Minori

- [X] UUID String(36), modifica effettuata da `String(36)` a UIID
- [X] Commenti: decisione lingua presa
- [X] CORS_ORIGINS: testato parsing da .env

#### Test Finale Post-Correzioni

- [X] `cd backend && source venv/bin/activate`
- [X] `python -m app.main` o `python run.py` → Server UP
- [X] http://localhost:8000 → JSON response OK
- [X] http://localhost:8000/docs → Swagger UI OK
- [X] Login con utente esistente → Token OK
- [X] GET /accounts → Lista OK
- [X] POST /transactions (income) → Balance +amount
- [X] POST /transactions (expense) → Balance -amount
- [X] POST /transfers → From -amount, To +amount
- [X] GET /analytics/summary → Dati corretti

#### Commit Fase 3.7

- [X] Tutti i file modificati staged
- [X] Commit message: `fix: Code review corrections - balance strategy, path fixes, type alignment`
- [X] Push completato

---

**Note Implementazione:**

- Transazioni e trasferimenti per somme superiori all'account balance non sono bloccati (da sistemare in futuro)
- Balance strategy: Opzione C (campo separato) implementata
- File SQL obsoleti: rimossi
- Lingua commenti: EN per codice

**CHECKPOINT FASE 3:**

- [X] ✅ Tutti gli endpoints CRUD funzionanti
- [X] ✅ Balance updates automatici
- [X] ✅ Analytics calcolati correttamente
- [X] ✅ Test integrazione completa passato
- [X] ✅ Ready per FASE 4


---

## ✅ FASE 3.8: BACKEND VACATION PLANNING

**Data Inizio:** 10/03/2026 | **Data Fine:** 10/03/2026 | **Status:** ✅ Completato
**Tempo Stimato:** 3-4 giorni

### 3.8.1 - Database Models

- [X] `vacation_settings.py` creato (maturazione separata: ferie_days_per_month, rol_hours_per_month, permessi_hours_per_month)
- [X] `tracking_start_date` implementato (invece di carryover_year)
- [X] `initial_ferie_days` (in GIORNI), `initial_rol_hours`, `initial_permessi_hours` implementati
- [X] `vacation_entry.py` creato (NO malattia - solo ferie/rol/permesso)
- [X] `italian_holiday.py` creato
- [X] `user_holiday.py` creato
- [X] User model aggiornato con relationships
- [X] Models __init__.py aggiornato
- [X] Migration creata ed eseguita
- [X] Tabelle verificate in pgAdmin
- [X] Commit database models

### 3.8.2 - Utility Functions

- [X] `easter.py` creato (calcolo Pasqua con validazione year >= 1583)
- [X] `bridge_days.py` creato (calcolo ponti con validazione weekend/festività)
- [X] `vacation_balance.py` RISCRITTO con maturazione separata:
  - [X] Calcolo separato per tipo (Ferie/ROL/Permessi)
  - [X] Conversione automatica ferie giorni → ore
  - [X] Totali aggregati (total_hours_available, total_days_available)
  - [X] Breakdown per tipo con hours_available
- [X] Utils __init__.py aggiornato
- [X] Commit utilities

### 3.8.3 - Pydantic Schemas

- [X] `vacation.py` schemas creato:
  - [X] VacationSettingsBase con nuovi campi (ferie_days_per_month, etc.)
  - [X] BreakdownItem con hours_available, days_available
  - [X] VacationBalanceResponse con totali aggregati
  - [X] NO riferimenti a "malattia"
- [X] Schemas __init__.py aggiornato
- [X] Commit schemas

### 3.8.4 - CRUD Operations

- [X] `vacation_settings.py` CRUD creato
- [X] `vacation_entry.py` CRUD creato con validazioni:
  - [X] Blocco inserimento weekend
  - [X] Blocco inserimento festività nazionali
  - [X] Blocco inserimento festività custom utente
- [X] `italian_holiday.py` CRUD creato
- [X] `user_holiday.py` CRUD creato con validazione date (es. 31 Feb)
- [X] CRUD __init__.py aggiornato
- [X] Commit CRUD

### 3.8.5 - API Router

- [X] `vacation.py` router creato con endpoint:
  - [X] GET/PUT /vacation/settings (nuovi campi)
  - [X] POST/GET/PUT/DELETE /vacation/entries (con validazione festività)
  - [X] POST /vacation/entries/bulk (FIX validazione hours_per_day + skip festività)
  - [X] GET /vacation/balance (con breakdown completo + totali)
  - [X] GET /vacation/calendar (OTTIMIZZATO: 1 query invece di 4)
  - [X] GET /vacation/holidays
  - [X] GET /vacation/bridges
  - [X] POST/GET/DELETE /vacation/user-holidays
- [X] Router registrato in main.py
- [X] Commit router

### 3.8.6 - Manual Testing

- [X] GET/PUT /vacation/settings testato (maturazione separata)
- [X] POST /vacation/entries testato (validazione weekend PASS)
- [X] POST /vacation/entries testato (validazione festività PASS)
- [X] POST /vacation/entries/bulk testato (skip festività PASS)
- [X] GET /vacation/balance testato (totali aggregati corretti)
- [X] GET /vacation/calendar testato (festività custom visibili)
- [X] Commit test results

**CHECKPOINT FASE 3.8:**

- [X] ✅ Models con maturazione separata (Ferie/ROL/Permessi)
- [X] ✅ Tracking start date funzionante
- [X] ✅ Validazione weekend + festività attiva
- [X] ✅ Balance con totali aggregati corretto
- [X] ✅ NO malattia in sistema
- [X] ✅ Calcolo Pasqua corretto
- [X] ✅ Calcolo ponti corretto

**Note Implementazione:**

- Ferie: 1.83 giorni/mese = 22 giorni/anno
- ROL: 2.67 ore/mese = 32 ore/anno
- Permessi: 8.67 ore/mese = 104 ore/anno
- Initial balance: ferie in GIORNI, ROL/Permessi in ORE

---


## ✅ FASE 3.9: BACKEND BUDGET PLANNING

**Data Inizio:** 11/03/2026 | **Data Fine:** 11/03/2026 | **Status:** ✅ Completato

**Tempo Stimato:** 2-3 giorni

### 3.9.1 - Database Models

- [X] `budget.py` model creato con:
  - [X] Foreign keys: user_id, category_id (ON DELETE SET NULL)
  - [X] Fields: amount, period, start_date, is_active
  - [X] UniqueConstraint parziale (user_id, category_id, is_active WHERE is_active=true)
  - [X] Indexes: user_active, category, start_date
- [X] User model aggiornato con relationship budgets
- [X] Models __init__.py aggiornato
- [X] Migration creata ed eseguita
- [X] Tabella `budgets` verificata in pgAdmin
- [X] Commit database models

### 3.9.2 - Pydantic Schemas

- [X] `budget.py` schemas creato:
  - [X] BudgetBase con validazione amount > 0, period = "monthly"
  - [X] BudgetCreate, BudgetUpdate
  - [X] BudgetResponse
  - [X] CategoryInfo (minimal)
  - [X] BudgetWithStatus (con spent/remaining/percentage/status/indicator)
  - [X] BudgetSummaryResponse (con budgets list + totals)
- [X] Schemas __init__.py aggiornato
- [X] Commit schemas

### 3.9.3 - CRUD Operations

- [X] `budget.py` CRUD creato con:
  - [X] get_budgets (con filtri is_active, category_id)
  - [X] get_budget (singolo con ownership)
  - [X] create_budget (con validazioni: category exists, is expense type, no duplicate)
  - [X] update_budget
  - [X] delete_budget
  - [X] calculate_spent_for_month (real-time da transactions)
  - [X] get_budget_status (🟢🟡🔴🚨 basato su percentage)
  - [X] get_budget_with_spending (arricchisce budget con dati spesa)
  - [X] get_budgets_summary (dashboard con tutti i budget + totali)
- [X] CRUD __init__.py aggiornato
- [X] Commit CRUD

### 3.9.4 - API Router

- [X] `budgets.py` router creato con endpoints:
  - [X] GET /budgets (lista con filtri)
  - [X] GET /budgets/summary (dashboard principale - KEY ENDPOINT)
  - [X] GET /budgets/{id} (dettaglio)
  - [X] POST /budgets (crea con validazioni)
  - [X] PUT /budgets/{id} (update)
  - [X] DELETE /budgets/{id}
- [X] Router registrato in main.py
- [X] Commit router

### 3.9.5 - Manual Testing

- [X] Server avviato (http://localhost:8000/docs)
- [X] Setup: Registra utente + login + authorize
- [X] Crea 3 categorie expense (Ristoranti, Spesa, Benzina)
- [X] POST /budgets: Crea 3 budget (€200, €400, €100)
- [X] Test constraint: Crea budget duplicato → 400 Bad Request ✓
- [X] Crea transazioni: €150 Ristoranti, €30 Ristoranti, €380 Spesa, €45 Benzina
- [X] GET /budgets/summary: Verifica spent/percentage/indicators corretti:
  - [X] Ristoranti: €180/€200 (90%) 🔴
  - [X] Spesa: €380/€400 (95%) 🔴
  - [X] Benzina: €45/€100 (45%) 🟢
  - [X] Totali: €605/€700 (86.43%)
- [X] DELETE categoria "Ristoranti" → Budget diventa orfano
- [X] GET /budgets/summary: Verifica budget orfano:
  - [X] category_id: null
  - [X] category_name: "Categoria Eliminata"
  - [X] status: "orphan"
  - [X] indicator: "⚠️"
- [X] PUT /budgets/{id}: Modifica amount Spesa a €500
- [X] GET /budgets/summary: Verifica percentage aggiornata
- [X] PUT /budgets/{id}: Disattiva budget Benzina (is_active=false)
- [X] GET /budgets/summary: Verifica budget Benzina non compare
- [X] DELETE /budgets/{id}: Elimina budget Spesa
- [X] GET /budgets: Verifica budget eliminato
- [X] Verifica in pgAdmin: Query `SELECT * FROM budgets;`
- [X] `test_full_suite.py` creato con workflow
- [X] Commit testing documentation

**CHECKPOINT FASE 3.9:**

- [X] ✅ Tabella budgets con constraint UNIQUE parziale
- [X] ✅ Model Budget con ON DELETE SET NULL per category_id
- [X] ✅ Schemas con validazioni (amount > 0, period = "monthly")
- [X] ✅ CRUD con calcolo spesa real-time
- [X] ✅ get_budget_status restituisce indicatori 🟢🟡🔴🚨
- [X] ✅ get_budgets_summary funziona (endpoint chiave dashboard)
- [X] ✅ Validazione: solo expense categories
- [X] ✅ Constraint: un budget attivo per categoria
- [X] ✅ Budget orfani gestiti (category_id NULL)
- [X] ✅ Storico budget (is_active=false)
- [X] ✅ 6 endpoints testati e funzionanti
- [X] ✅ Ready per FASE 4.7

**Note Implementazione:**

- Period: solo "monthly" per MVP
- Calcolo: real-time (no cache)
- Unicità: un budget attivo per categoria
- Orfani: category_id NULL quando categoria eliminata
- Rollover: NO - budget riparte da zero ogni mese
- Alert: solo indicatori visivi (no email/push)
- Status: ok (<70%) | warning (70-90%) | danger (90-100%) | exceeded (>100%) | orphan (no category)

---


## 🟡 FASE 3.10: BACKEND CSV IMPORT

**Data Inizio:** 29/03/2026 | **Data Fine:** _______ | **Status:** 🟡 In corso

**Tempo Stimato:** 1 giorno (6-8 ore)

### 3.10.1 - Formato CSV & Template

- [ ] Formato CSV standard documentato:
  - [ ] 5 colonne: date, description, amount, category_name, notes
  - [ ] Regole specifiche (ISO date, amount +/-, UTF-8)
  - [ ] Max 1000 righe per file
- [ ] Template CSV creato in `backend/static/templates/template_transazioni.csv`:
  - [ ] Header corretto
  - [ ] 3 righe esempio
- [ ] Directory `backend/static/` configurata
- [ ] Static files mounted in main.py
- [ ] Endpoint GET `/csv-import/template` funzionante
- [ ] Template scaricabile da browser
- [ ] Commit template

### 3.10.2 - Pydantic Schemas

- [ ] `csv_import.py` creato in `backend/app/schemas/`:
  - [ ] CSVRowParsed con campi:
    - [ ] row_number, date, description, amount, category_name, notes
    - [ ] status (valid/warning/error/duplicate)
    - [ ] status_message
    - [ ] suggested_category_id, suggested_category_name, match_confidence
    - [ ] duplicate_transaction_id
  - [ ] CSVImportPreviewResponse:
    - [ ] Conteggi (total_rows, valid_rows, warning_rows, error_rows, duplicate_rows)
    - [ ] Lista rows parsed
    - [ ] account_id, account_name
  - [ ] CSVImportConfirmRequest (placeholder per fase 5.11)
  - [ ] CSVImportResult (report finale import)
- [ ] Schemas __init__.py aggiornato
- [ ] Commit schemas

### 3.10.3 - CSV Parser & Validator

- [ ] `csv_parser.py` creato in `backend/app/utils/`:
  - [ ] parse_csv_file():
    - [ ] Parsing CSV con DictReader
    - [ ] Check required columns (date, description, amount)
    - [ ] Limit 1000 righe
    - [ ] Error handling malformed CSV
  - [ ] parse_date():
    - [ ] Supporto ISO (YYYY-MM-DD)
    - [ ] Supporto Italian (DD/MM/YYYY)
    - [ ] Supporto DD-MM-YYYY
    - [ ] Return None se invalid
  - [ ] parse_amount():
    - [ ] Remove currency symbols (€, $, £)
    - [ ] Handle comma/point (IT vs US format)
    - [ ] Parse to Decimal
    - [ ] Return None se invalid
  - [ ] validate_row():
    - [ ] Valida date, amount, description
    - [ ] Return CSVRowParsed + is_valid bool
    - [ ] Errors list se invalid
  - [ ] find_similar_category():
    - [ ] Fuzzy matching con SequenceMatcher
    - [ ] Threshold 0.7
    - [ ] Return (id, name, confidence) o None
  - [ ] CSVParseError custom exception
  - [ ] similarity() helper function
- [ ] Commit parser utility

### 3.10.4 - CRUD Extension

- [ ] `transaction.py` aggiornato:
  - [ ] check_duplicate_transaction():
    - [ ] Match per: date + amount + description + account_id
    - [ ] Return UUID se duplicate, None altrimenti
  - [ ] bulk_create_transactions():
    - [ ] Loop su lista TransactionCreate
    - [ ] Usa create_transaction esistente (balance update incluso)
    - [ ] Error handling per singola transazione
    - [ ] Return (count_created, list_ids)
- [ ] Commit CRUD extension

### 3.10.5 - API Router

- [ ] `csv_import.py` creato in `backend/app/routers/`:
  - [ ] POST /csv-import/preview:
    - [ ] UploadFile parameter
    - [ ] account_id query parameter
    - [ ] Verify account exists + ownership
    - [ ] Read file + decode UTF-8
    - [ ] Parse CSV con parse_csv_file()
    - [ ] Get user categories per matching
    - [ ] Auto-create "Non Categorizzato" se mancante
    - [ ] Loop su righe:
      - [ ] Valida con validate_row()
      - [ ] Check duplicate con check_duplicate_transaction()
      - [ ] Category matching (exact + fuzzy)
      - [ ] Populate CSVRowParsed con status
    - [ ] Return CSVImportPreviewResponse
    - [ ] Error handling (malformed CSV, UTF-8 errors, etc.)
  - [ ] GET /csv-import/template:
    - [ ] FileResponse con template CSV
    - [ ] Content-type: text/csv
    - [ ] Filename: BudgetApp_Template_Transazioni.csv
  - [ ] POST /csv-import/confirm (placeholder):
    - [ ] Return 501 Not Implemented
    - [ ] Nota: "Will be implemented in Phase 5.11"
- [ ] Router registrato in main.py
- [ ] Commit router

### 3.10.6 - Testing Manuale

- [ ] File test preparato `backend/test_data/test_import.csv`:
  - [ ] 8 righe: valide, warnings, errors, duplicate
- [ ] Server avviato
- [ ] Test 1 - Download template:
  - [ ] GET /csv-import/template
  - [ ] Download funziona
  - [ ] File ha 3 righe esempio
- [ ] Test 2 - Preview success:
  - [ ] Login + token
  - [ ] Crea account test
  - [ ] POST /csv-import/preview con test_import.csv
  - [ ] Response corretta:
    - [ ] total_rows: 8
    - [ ] valid_rows: 3
    - [ ] warning_rows: 1
    - [ ] error_rows: 2
    - [ ] duplicate_rows: 1
  - [ ] Righe con status corretto
- [ ] Test 3 - File malformato:
  - [ ] CSV senza header
  - [ ] 400 Bad Request "Missing required columns"
- [ ] Test 4 - File troppo grande:
  - [ ] CSV con 1001 righe
  - [ ] 400 Bad Request "exceeds maximum"
- [ ] Test 5 - Fuzzy matching:
  - [ ] Categoria "Ristorazione" esiste
  - [ ] CSV ha "Ristorante"
  - [ ] Suggerisce "Ristorazione" con confidence ~0.8
- [ ] Verifica database:
  - [ ] "Non Categorizzato" auto-creata
  - [ ] Nessuna transazione creata (solo preview)
- [ ] `CSV_IMPORT_TESTING.md` creato in `backend/docs/`
- [ ] Commit testing docs

**CHECKPOINT FASE 3.10:**

- [ ] ✅ Template CSV scaricabile
- [ ] ✅ Formato standard documentato
- [ ] ✅ Parser gestisce 3 formati date
- [ ] ✅ Parser gestisce decimali IT/US
- [ ] ✅ Validazione completa righe
- [ ] ✅ Duplicate detection funziona
- [ ] ✅ Fuzzy matching categorie (threshold 0.7)
- [ ] ✅ Categoria "Non Categorizzato" auto-creata
- [ ] ✅ Preview endpoint completo
- [ ] ✅ Status corretto per ogni riga (valid/warning/error/duplicate)
- [ ] ✅ Error handling robusto
- [ ] ✅ Template endpoint funzionante
- [ ] ✅ Confirm endpoint placeholder (per fase 5.11)
- [ ] ✅ Testing manuale completo
- [ ] ✅ Documentation creata

**Note Implementazione:**

- Formato CSV: date (YYYY-MM-DD), description, amount (+/-), category_name, notes
- Max 1000 righe per file (MVP)
- Processing sincrono
- Duplicate match: date + amount + description + account
- Fuzzy matching: SequenceMatcher con threshold 0.7
- Endpoint /confirm è placeholder (completo in fase 5.11 frontend)

---


## ⬜ FASE 4: TESTING & DEBUG

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

### 4.1 - Setup Pytest

- [ ] Pytest dependencies verificate
- [ ] `backend/pytest.ini` creato
- [ ] `backend/tests/__init__.py` creato
- [ ] `backend/tests/conftest.py` creato
- [ ] Database test `budget_app_test` creato
- [ ] Commit test setup

### 4.2 - Test Authentication

- [ ] `backend/tests/test_auth.py` creato
- [ ] `test_register_user` implementato
- [ ] `test_register_duplicate_email` implementato
- [ ] `test_login_success` implementato
- [ ] `test_login_wrong_password` implementato
- [ ] `test_get_me_authenticated` implementato
- [ ] `test_get_me_without_token` implementato
- [ ] Tutti i test passano: `pytest tests/test_auth.py -v`
- [ ] Commit auth tests

### 4.3 - Test Accounts

- [ ] `backend/tests/test_accounts.py` creato
- [ ] Test create account
- [ ] Test list accounts
- [ ] Test get account detail
- [ ] Test update account
- [ ] Test delete account
- [ ] Test access denied
- [ ] Tutti i test passano
- [ ] Commit account tests

### 4.4 - Test Transactions & Transfers

- [ ] `backend/tests/test_transactions.py` creato
- [ ] Test creazione transaction
- [ ] Test balance update
- [ ] Test filtri
- [ ] `backend/tests/test_transfers.py` creato
- [ ] Test transfer
- [ ] Test entrambi i balance update
- [ ] Tutti i test passano: `pytest tests/ -v`
- [ ] Commit transaction/transfer tests

### 4.5 - Coverage Report

- [ ] `pytest-cov` installato
- [ ] `pytest --cov=app --cov-report=html` eseguito
- [ ] `htmlcov/` aggiunto a `.gitignore`
- [ ] Coverage report visualizzato
- [ ] Coverage ≥ 70%: [ ] YES [ ] NO
- [ ] Commit coverage config

**CHECKPOINT FASE 4:**

- [ ] ✅ Test suite completa
- [ ] ✅ Tutti i test passano
- [ ] ✅ Coverage soddisfacente
- [ ] ✅ CI/CD ready

---

## ⬜ FASE 4.6: TESTING VACATION MODULE

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

**Tempo Stimato:** 1-2 giorni

### 4.6.1 - Test Setup

- [ ] Fixtures vacation aggiunte a conftest.py:
  - [ ] `vacation_settings_data` con maturazione separata
  - [ ] `vacation_settings_with_initial_balance`
  - [ ] `vacation_entry_ferie_data` (date fisse per consistency)
  - [ ] `vacation_entry_rol_data`
  - [ ] `user_holiday_data`

### 4.6.2 - Test Vacation Settings

- [ ] `test_vacation_settings.py` creato:
  - [ ] Test default settings (ferie_days_per_month, rol_hours_per_month, permessi_hours_per_month)
  - [ ] Test update accrual rates
  - [ ] Test initial balance validation (balance_date < tracking_start_date)
  - [ ] Test tracking_start_date required
- [ ] Tutti i test passano

### 4.6.3 - Test Vacation Entries

- [ ] `test_vacation_entries.py` creato:
  - [ ] Test create ferie (ore automatiche)
  - [ ] Test create ROL (ore manuali obbligatorie)
  - [ ] Test validazione weekend (FAIL atteso)
  - [ ] Test validazione festività nazionali (FAIL atteso)
  - [ ] Test duplicate date (FAIL atteso)
  - [ ] Test update entry (solo note/ore)
  - [ ] Test delete entry
- [ ] Tutti i test passano

### 4.6.4 - Test User Holidays

- [ ] `test_user_holidays.py` creato:
  - [ ] Test create patron saint (recurring=True)
  - [ ] Test create company closure (recurring=False)
  - [ ] Test validazione date invalide (31 Feb → FAIL)
  - [ ] Test non-recurring senza year (FAIL atteso)
  - [ ] Test delete
- [ ] Tutti i test passano

### 4.6.5 - Test Bulk Entries

- [ ] `test_vacation_bulk.py` creato:
  - [ ] Test bulk create settimana
  - [ ] Test skip weekends
  - [ ] Test skip festività (nazionali + custom)
  - [ ] Test ROL bulk richiede hours_per_day
  - [ ] Test validazione range date
- [ ] Tutti i test passano

### 4.6.6 - Test Balance & Calendar

- [ ] `test_vacation_balance.py` creato:
  - [ ] Test balance structure (totali aggregati presenti)
  - [ ] Test breakdown per tipo (ferie, rol, permesso)
  - [ ] Test with initial balance
  - [ ] Test tracking_start_date calculation
  - [ ] Test calendar month (festività nazionali + custom visibili)
  - [ ] Test bridges calculation
- [ ] Tutti i test passano

### 4.6.7 - Coverage

- [ ] `pytest tests/test_vacation*.py -v --cov=app.routers.vacation --cov=app.crud --cov=app.utils.vacation_balance`
- [ ] Coverage vacation module ≥ 70%
- [ ] Commit all vacation tests

**CHECKPOINT FASE 4.6:**

- [ ] ✅ Test settings con maturazione separata PASS
- [ ] ✅ Test validazione weekend/festività PASS
- [ ] ✅ Test balance con totali aggregati PASS
- [ ] ✅ Test bulk con skip festività PASS
- [ ] ✅ NO test malattia (rimossa)
- [ ] ✅ Coverage ≥ 70%
- [ ] ✅ Ready per FASE 5

**Test Command:**

```bash
pytest tests/ -v --cov=app
```

**Test Scenarios Chiave:**

- [ ] Ferie: ore automatiche = work_hours_per_day ✓
- [ ] ROL: ore manuali obbligatorie ✓
- [ ] Weekend: inserimento bloccato ✓
- [ ] Festività: inserimento bloccato ✓
- [ ] Balance: totali aggregati corretti ✓
- [ ] Breakdown: separato per tipo ✓

---


## ⬜ FASE 4.7: TESTING BUDGET MODULE

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

**Tempo Stimato:** 1 giorno

### 4.7.1 - Setup Test Environment

- [ ] `pytest.ini` verificato
- [ ] `conftest.py` base verificato
- [ ] Budget fixtures aggiunte in `conftest.py`:
  - [ ] expense_categories (3 categorie expense)
  - [ ] income_category (per test rejection)
  - [ ] test_budget (singolo budget)
  - [ ] test_budgets (3 budget multipli)
  - [ ] test_transactions (con spese per calcolo)
  - [ ] orphaned_budget (category_id NULL)
- [ ] Database test accessibile
- [ ] Commit fixtures

### 4.7.2 - Test Budget CRUD (13 test)

- [ ] `test_budget_crud.py` creato con test:
  - [ ] test_create_budget (success)
  - [ ] test_create_budget_for_income_category_fails
  - [ ] test_create_duplicate_budget_fails
  - [ ] test_get_budgets
  - [ ] test_get_budgets_filter_by_active
  - [ ] test_get_budgets_filter_by_category
  - [ ] test_get_budget
  - [ ] test_get_budget_wrong_user
  - [ ] test_update_budget
  - [ ] test_delete_budget
  - [ ] test_delete_nonexistent_budget
- [ ] Run: `pytest tests/test_budget_crud.py -v`
- [ ] Tutti i 13 test passano ✓
- [ ] Commit CRUD tests

### 4.7.3 - Test Budget Logic (14 test)

- [ ] `test_budget_logic.py` creato con test:
  - [ ] test_calculate_spent_for_month
  - [ ] test_calculate_spent_for_month_multiple_transactions
  - [ ] test_calculate_spent_for_month_no_transactions
  - [ ] test_get_budget_status_ok (🟢)
  - [ ] test_get_budget_status_warning (🟡)
  - [ ] test_get_budget_status_danger (🔴)
  - [ ] test_get_budget_status_exceeded (🚨)
  - [ ] test_get_budget_with_spending
  - [ ] test_get_budget_with_spending_orphaned
  - [ ] test_get_budgets_summary (con totali)
  - [ ] test_get_budgets_summary_no_budgets
- [ ] Run: `pytest tests/test_budget_logic.py -v`
- [ ] Tutti i 14 test passano ✓
- [ ] Commit business logic tests

### 4.7.4 - Test Budget API (17 test)

- [ ] `test_budget_api.py` creato con test:
  - [ ] test_get_budgets
  - [ ] test_get_budgets_filter_active
  - [ ] test_get_budget_by_id
  - [ ] test_get_budget_not_found (404)
  - [ ] test_get_budgets_summary (KEY ENDPOINT)
  - [ ] test_create_budget
  - [ ] test_create_budget_for_income_fails (400)
  - [ ] test_create_duplicate_budget_fails (400)
  - [ ] test_create_budget_negative_amount_fails (422)
  - [ ] test_update_budget
  - [ ] test_update_budget_not_found (404)
  - [ ] test_delete_budget
  - [ ] test_delete_budget_not_found (404)
  - [ ] test_budgets_require_authentication (401)
- [ ] Run: `pytest tests/test_budget_api.py -v`
- [ ] Tutti i 17 test passano ✓
- [ ] Commit API tests

### 4.7.5 - Coverage & Verification

- [ ] Run coverage: `pytest tests/test_budget*.py -v --cov=app/models/budget --cov=app/crud/budget --cov=app/routers/budgets --cov-report=html`
- [ ] Coverage verificato:
  - [ ] app/models/budget.py: >90%
  - [ ] app/crud/budget.py: >85%
  - [ ] app/routers/budgets.py: >80%
- [ ] Coverage report aperto: `open htmlcov/index.html`
- [ ] Aree non coperte identificate (se <80%)
- [ ] Test aggiuntivi per coverage mancante (se necessario)
- [ ] Run full suite: `pytest -v`
- [ ] Tutti i test passano (inclusi precedenti)
- [ ] Totale test budget: ~44 test ✓
- [ ] `TESTING_BUDGET_COVERAGE.md` creato con:
  - [ ] Coverage percentages
  - [ ] Test count per file
  - [ ] Test scenarios covered
- [ ] Commit coverage report

**CHECKPOINT FASE 4.7:**

- [ ] ✅ 44 test budget implementati (13+14+17)
- [ ] ✅ Coverage >80% su tutto il modulo
- [ ] ✅ CRUD completamente testato
- [ ] ✅ Business logic testata (calcoli + status)
- [ ] ✅ API endpoints testati (6 endpoint + auth)
- [ ] ✅ Validations verificate (income reject, duplicate, negative)
- [ ] ✅ Edge cases coperti (orfani, user isolation)
- [ ] ✅ Coverage report documentato
- [ ] ✅ Full test suite passa
- [ ] ✅ Ready per FASE 5

**Note Testing:**

- CRUD: 13 test - create/read/update/delete + filters + validations
- Logic: 14 test - spent calculation + status indicators + summary
- API: 17 test - 6 endpoints + error handling + auth
- Coverage: >80% target per models/crud/router
- Fixtures: 6 fixtures per setup completo

---


## ⬜ FASE 4.8: TESTING CSV IMPORT MODULE

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

**Tempo Stimato:** 0.5 giorni (4 ore)

### 4.8.1 - Setup Test Fixtures

- [ ] Pytest setup verificato:
  - [ ] `backend/pytest.ini` configurato
  - [ ] `backend/tests/conftest.py` con fixtures base
- [ ] Fixtures CSV aggiunte a conftest.py:
  - [ ] valid_csv_content (3 righe valide)
  - [ ] csv_with_errors (5 righe con vari errori)
  - [ ] csv_with_duplicates (2 transazioni duplicate)
  - [ ] csv_malformed (testo non CSV)
  - [ ] csv_missing_columns (colonne mancanti)
  - [ ] csv_large_file (1001 righe, eccede limite)
  - [ ] test_categories_for_fuzzy (3 categorie)
  - [ ] test_transaction_for_duplicate (transazione esistente)
- [ ] Commit fixtures

### 4.8.2 - Test CSV Parser Functions (~40 test)

- [ ] `test_csv_parser.py` creato in `backend/tests/`:
  - [ ] Test parse_csv_file (5 test):
    - [ ] Valid CSV parsed correttamente
    - [ ] Missing columns → CSVParseError
    - [ ] Malformed → CSVParseError
    - [ ] Exceeds limit (1001 righe) → CSVParseError
    - [ ] Empty CSV → CSVParseError
  - [ ] Test parse_date (5 test):
    - [ ] ISO format (YYYY-MM-DD) → date object
    - [ ] Italian format (DD/MM/YYYY) → date object
    - [ ] Dash format (DD-MM-YYYY) → date object
    - [ ] Invalid date → None
    - [ ] Whitespace trimmed correttamente
  - [ ] Test parse_amount (8 test):
    - [ ] Simple decimal → Decimal
    - [ ] Currency symbols (€, $, £) → stripped
    - [ ] Italian format (comma decimal) → Decimal
    - [ ] US format (comma thousands) → Decimal
    - [ ] Spaces removed correttamente
    - [ ] Invalid → None
    - [ ] Edge cases (0, -0.01) → Decimal
    - [ ] Italian thousands (1.234,56) → Decimal
  - [ ] Test validate_row (7 test):
    - [ ] Valid row → status "valid", is_valid True
    - [ ] Missing date → status "error", is_valid False
    - [ ] Missing amount → status "error"
    - [ ] Missing description → status "error"
    - [ ] No category → status "warning", is_valid True
    - [ ] Multiple errors → status "error", all errors listed
    - [ ] Row_number corretto
  - [ ] Test similarity (5 test):
    - [ ] Exact match → 1.0
    - [ ] Case insensitive → 1.0
    - [ ] High similarity → >0.7
    - [ ] Low similarity → <0.3
    - [ ] Empty strings → 1.0
  - [ ] Test find_similar_category (5 test):
    - [ ] Exact match → (id, name, 1.0)
    - [ ] Fuzzy match → (id, name, >0.7)
    - [ ] No match → None
    - [ ] Best match selected (multiple candidates)
    - [ ] Empty categories list → None
- [ ] Run parser tests:
  - [ ] `pytest tests/test_csv_parser.py -v`
  - [ ] ~40 test passano
- [ ] Commit parser tests

### 4.8.3 - Test Duplicate Detection & CRUD (~7 test)

- [ ] `test_csv_import_crud.py` creato in `backend/tests/`:
  - [ ] Test check_duplicate_transaction (5 test):
    - [ ] Duplicate exists → returns UUID
    - [ ] No duplicate → returns None
    - [ ] Different amount → returns None
    - [ ] Different date → returns None
    - [ ] Different description → returns None
  - [ ] Test bulk_create_transactions (2 test):
    - [ ] Multiple transactions created → count + ids correct
    - [ ] Account balance updated correctly
- [ ] Run CRUD tests:
  - [ ] `pytest tests/test_csv_import_crud.py -v`
  - [ ] ~7 test passano
- [ ] Commit CRUD tests

### 4.8.4 - Test API Endpoints (~15 test)

- [ ] `test_csv_import_api.py` creato in `backend/tests/`:
  - [ ] Test preview valid CSV:
    - [ ] Status 200
    - [ ] total_rows correct
    - [ ] account_id correct
    - [ ] rows list populated
  - [ ] Test preview with errors:
    - [ ] Status 200
    - [ ] error_rows > 0
    - [ ] Error rows have status "error"
  - [ ] Test preview with duplicates:
    - [ ] Status 200
    - [ ] duplicate_rows >= 1
    - [ ] Duplicate row has duplicate_transaction_id
  - [ ] Test preview fuzzy matching:
    - [ ] Status 200
    - [ ] Row status "warning"
    - [ ] suggested_category_name correct
    - [ ] match_confidence > 0.7
  - [ ] Test preview invalid account:
    - [ ] Status 404
    - [ ] Error message "Account not found"
  - [ ] Test preview malformed CSV:
    - [ ] Status 400
    - [ ] Error message appropriate
  - [ ] Test preview missing columns:
    - [ ] Status 400
    - [ ] Error "Missing required columns"
  - [ ] Test preview file too large:
    - [ ] Status 400
    - [ ] Error "exceeds maximum"
  - [ ] Test preview non-UTF8:
    - [ ] Status 400
    - [ ] Error mentions "UTF-8"
  - [ ] Test preview creates "Non Categorizzato":
    - [ ] Category auto-created se non esiste
    - [ ] Category has correct name
  - [ ] Test download template:
    - [ ] Status 200
    - [ ] Content-type text/csv
    - [ ] Header presente nel contenuto
  - [ ] Test preview requires auth:
    - [ ] Status 401 without token
- [ ] Run API tests:
  - [ ] `pytest tests/test_csv_import_api.py -v`
  - [ ] ~15 test passano
- [ ] Commit API tests

### 4.8.5 - Coverage & Final Verification

- [ ] Run all CSV tests with coverage:
  - [ ] `pytest tests/test_csv*.py -v --cov=app/utils/csv_parser --cov=app/crud/transaction --cov=app/routers/csv_import --cov-report=html`
  - [ ] Coverage csv_parser.py: >85%
  - [ ] Coverage transaction.py (CSV functions): >80%
  - [ ] Coverage csv_import.py router: >75%
- [ ] Open coverage report:
  - [ ] `open htmlcov/index.html` (macOS) o `xdg-open htmlcov/index.html` (Linux)
  - [ ] Verifica aree non coperte
  - [ ] Aggiungi test se coverage <80%
- [ ] Run full test suite:
  - [ ] `pytest -v`
  - [ ] Tutti i test passano (inclusi CSV)
  - [ ] Totale CSV tests: ~62
    - [ ] test_csv_parser.py: ~40
    - [ ] test_csv_import_crud.py: ~7
    - [ ] test_csv_import_api.py: ~15
- [ ] Documenta coverage:
  - [ ] `CSV_IMPORT_TEST_COVERAGE.md` creato in `backend/docs/`
  - [ ] Coverage percentages per file
  - [ ] Test summary (totale test, passing)
  - [ ] Test scenarios covered
  - [ ] Next steps annotati
- [ ] Commit coverage report

**CHECKPOINT FASE 4.8:**

- [ ] ✅ ~62 test CSV import totali
- [ ] ✅ test_csv_parser.py (~40 test)
- [ ] ✅ test_csv_import_crud.py (~7 test)
- [ ] ✅ test_csv_import_api.py (~15 test)
- [ ] ✅ Tutti i test passano
- [ ] ✅ Coverage >80% su tutti i file:
  - [ ] csv_parser.py: >85%
  - [ ] transaction.py (CSV): >80%
  - [ ] csv_import.py: >75%
- [ ] ✅ Coverage report HTML generato
- [ ] ✅ Fixtures CSV completi (8 fixtures)
- [ ] ✅ Parser functions testati (parse_csv_file, parse_date, parse_amount, validate_row)
- [ ] ✅ Fuzzy matching testato (similarity, find_similar_category)
- [ ] ✅ Duplicate detection testato (check_duplicate_transaction)
- [ ] ✅ Bulk operations testate (bulk_create_transactions, balance update)
- [ ] ✅ API preview testato (valid, errors, duplicates, fuzzy)
- [ ] ✅ Error handling testato (malformed, missing columns, too large, non-UTF8, invalid account)
- [ ] ✅ Template download testato
- [ ] ✅ Authentication testata
- [ ] ✅ Auto-creation "Non Categorizzato" testata
- [ ] ✅ Documentation coverage creata

**Note Implementazione:**

- Test scenarios: parser (40), CRUD (7), API (15)
- Coverage target: >80% per tutto il modulo CSV
- Date formats testati: ISO, Italian (DD/MM/YYYY), Dash (DD-MM-YYYY)
- Amount formats testati: simple, currency symbols, IT comma, US comma, spaces
- Fuzzy matching threshold: 0.7
- Duplicate match: date + amount + description + account_id
- Max rows CSV: 1000 (limite testato)
- API confirm endpoint: placeholder (testato in fase 5.11)

---


## ⬜ FASE 5: FRONTEND INTEGRATION

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

### 5.1 - React Project Setup

- [ ] React app creata con Vite
- [ ] Dipendenze installate (axios, recharts, etc)
- [ ] Tailwind CSS configurato
- [ ] Dev server testato (http://localhost:5173)
- [ ] Commit frontend setup

### 5.2 - API Service Layer

- [ ] `frontend/src/services/api.js` creato
- [ ] Axios interceptors configurati
- [ ] `frontend/src/services/authService.js` creato
- [ ] `frontend/src/services/accountService.js` creato
- [ ] `frontend/src/services/transactionService.js` creato
- [ ] `frontend/src/services/categoryService.js` creato
- [ ] `frontend/src/services/transferService.js` creato
- [ ] `frontend/src/services/analyticsService.js` creato
- [ ] `frontend/.env` creato
- [ ] Commit services

### 5.3 - Authentication Pages

- [ ] `frontend/src/pages/Login.jsx` creato
- [ ] `frontend/src/pages/Register.jsx` creato
- [ ] `frontend/src/components/ProtectedRoute.jsx` creato
- [ ] Login page funzionante
- [ ] Register page funzionante
- [ ] Commit auth pages

### 5.4 - Main Application Layout

- [ ] `frontend/src/App.jsx` con routing
- [ ] `frontend/src/components/Navbar.jsx` creato
- [ ] Protected routes configurate
- [ ] Navigation funzionante
- [ ] Commit layout

### 5.5 - Dashboard Implementation

- [ ] `frontend/src/pages/Dashboard.jsx` creato
- [ ] API calls implementati
- [ ] Dashboard carica dati da backend
- [ ] Total balance visualizzato
- [ ] Income/expense visualizzati
- [ ] Account cards visualizzate
- [ ] Recent transactions visualizzate
- [ ] Commit dashboard

### 5.6 - Accounts Management

- [ ] `frontend/src/pages/Accounts.jsx` creato
- [ ] Lista accounts da API
- [ ] Form create account
- [ ] Form edit account
- [ ] Delete account con conferma
- [ ] Test CRUD completo: SUCCESS
- [ ] Commit accounts

### 5.7 - Transactions Management

- [ ] `frontend/src/pages/Transactions.jsx` creato
- [ ] Lista transactions con filtri
- [ ] Form create transaction
- [ ] Categories dropdown popolato
- [ ] Accounts dropdown popolato
- [ ] Test transaction income: SUCCESS
- [ ] Balance aggiornato: VERIFIED ✓
- [ ] Test transaction expense: SUCCESS
- [ ] Test filtri funzionanti
- [ ] Commit transactions

### 5.8 - Final Integration Tests

- [ ] Register nuovo utente: SUCCESS
- [ ] Create 2-3 accounts: SUCCESS
- [ ] Create categorie custom: SUCCESS
- [ ] Add 10+ transactions: SUCCESS
- [ ] Create transfer: SUCCESS
- [ ] Dashboard aggiornata: SUCCESS
- [ ] Test filtri e ricerca: SUCCESS
- [ ] Test Chrome: SUCCESS
- [ ] Test Firefox: SUCCESS
- [ ] Test Safari: SUCCESS
- [ ] Bug list creata
- [ ] Tutti i bug corretti
- [ ] Commit final integration

**CHECKPOINT FASE 5:**

- [ ] ✅ Frontend connesso a backend
- [ ] ✅ Authentication flow completo
- [ ] ✅ Dashboard real-time
- [ ] ✅ Tutti i CRUD funzionanti
- [ ] ✅ No localStorage per dati
- [ ] ✅ Multi-user tested
- [ ] ✅ Ready per FASE 6

**Test Multi-User:**

- [ ] User A: create data
- [ ] User B: create data
- [ ] User A non vede dati User B ✓
- [ ] User B non vede dati User A ✓

---

## ⬜ FASE 5.9: FRONTEND VACATION MODULE

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

**Tempo Stimato:** 3-4 giorni

### 5.9.1 - API Service

- [ ] `vacationService.js` creato con endpoints:
  - [ ] getSettings, updateSettings
  - [ ] getEntries, createEntry, updateEntry, deleteEntry
  - [ ] createBulkEntries (NUOVO)
  - [ ] getBalance, getProjection
  - [ ] getCalendarMonth
  - [ ] getHolidays, getBridges
  - [ ] getUserHolidays, createUserHoliday, deleteUserHoliday

### 5.9.2 - Calendar Component

- [ ] `VacationCalendar.jsx` creato (INVARIATO - già corretto)
- [ ] Navigazione mesi funziona
- [ ] Festività nazionali evidenziate
- [ ] Festività custom evidenziate
- [ ] Entries visibili
- [ ] Click su giorno apre modal

### 5.9.3 - Entry Modal

- [ ] `VacationEntryModal.jsx` creato (INVARIATO - già corretto):
  - [ ] FERIE: no input ore (automatiche)
  - [ ] ROL/Permessi: input ore obbligatorio
  - [ ] Edit mode: data/tipo DISABLED
  - [ ] Elimina funzionante
- [ ] CRUD entries funziona

### 5.9.4 - Bulk Entry Modal

- [ ] `BulkEntryModal.jsx` creato:
  - [ ] Form range date (start_date, end_date)
  - [ ] Dropdown tipo (ferie/rol/permesso)
  - [ ] Input ore (solo per ROL/Permessi)
  - [ ] Checkbox "Skip weekend"
  - [ ] Checkbox "Skip festività"
  - [ ] Preview count approssimativo
  - [ ] Submit crea multiple entries
- [ ] Modal testato e funzionante

### 5.9.5 - Balance Widget

- [ ] `VacationBalance.jsx` creato:
  - [ ] Totale disponibile aggregato (GRANDE e prominente)
  - [ ] Info tracking (data inizio + mesi lavorati)
  - [ ] Breakdown per tipo (Ferie, ROL, Permessi):
    - [ ] Maturate (ore + giorni)
    - [ ] Usate (ore + giorni)
    - [ ] Disponibili (ore + giorni)
    - [ ] Progress bar per tipo
  - [ ] Proiezione fine anno
  - [ ] Info configurazione (espandibile)
- [ ] Dati corretti visualizzati
- [ ] Year selector funzionante

### 5.9.6 - Settings Component

- [ ] `VacationSettings.jsx` creato:
  - [ ] Sezione Ore Lavorative (work_hours_per_day)
  - [ ] Sezione Maturazione Mensile:
    - [ ] Ferie (giorni/mese) con anteprima annuale
    - [ ] ROL (ore/mese) con anteprima annuale
    - [ ] Permessi (ore/mese) con anteprima annuale
    - [ ] Totale annuale calcolato
  - [ ] Sezione Inizio Tracciamento (tracking_start_date)
  - [ ] Sezione Saldo Iniziale (opzionale, collapsible):
    - [ ] Mese/anno riferimento
    - [ ] Ferie iniziali (in GIORNI)
    - [ ] ROL iniziali (in ore)
    - [ ] Permessi iniziali (in ore)
  - [ ] Preset CCNL (Commercio, Metalmeccanico)
  - [ ] Validazione: balance_date ≤ tracking_start_date
- [ ] Salvataggio funziona

### 5.9.7 - Bridge Opportunities

- [ ] `BridgeOpportunities.jsx` creato (INVARIATO - già corretto)
- [ ] Lista ponti corretta per anno
- [ ] Descrizioni chiare

### 5.9.8 - User Holidays Manager

- [ ] `UserHolidaysManager.jsx` creato (INVARIATO - già corretto)
- [ ] Form add patron saint
- [ ] Form add company closure
- [ ] Lista holidays con delete
- [ ] Validazione date funzionante

### 5.9.9 - Main Page

- [ ] `VacationPage.jsx` creato:
  - [ ] Tabs (Calendario, Riepilogo, Ponti, Festività, Impostazioni)
  - [ ] Pulsante "Inserimento Multiplo" visibile su tab Calendario
  - [ ] Tab switching funzionante
- [ ] Tutti i componenti integrati

### 5.9.10 - Styles

- [ ] `vacation.css` creato con:
  - [ ] Balance total card (gradient, prominente)
  - [ ] Breakdown grid (3 colonne responsive)
  - [ ] Progress bars per tipo
  - [ ] Settings form (sezioni ben separate)
  - [ ] Bulk modal styles
  - [ ] Responsive design (mobile-friendly)

### 5.9.11 - Integration

- [ ] Route `/vacation` aggiunta in App.jsx
- [ ] Link "🏖️ Ferie" aggiunto in Navbar
- [ ] Dashboard widget opzionale (se desiderato)

### 5.9.12 - Manual Testing

- [ ] Settings: salvataggio maturazione separata PASS
- [ ] Settings: tracking start date PASS
- [ ] Settings: saldo iniziale (ferie in giorni) PASS
- [ ] Calendar: festività nazionali visibili PASS
- [ ] Calendar: festività custom visibili PASS
- [ ] Entry modal: ferie NO ore, ROL/Permessi SÌ ore PASS
- [ ] Entry modal: edit mode (data/tipo disabled) PASS
- [ ] Bulk modal: apertura da pulsante PASS
- [ ] Bulk modal: preview count PASS
- [ ] Bulk modal: creazione multipla PASS
- [ ] Balance: totali aggregati corretti PASS
- [ ] Balance: breakdown per tipo corretto PASS
- [ ] Bridges: lista ponti corretta PASS
- [ ] User Holidays: CRUD funzionante PASS
- [ ] Responsive: mobile test PASS

**CHECKPOINT FASE 5.9:**

- [ ] ✅ BulkEntryModal implementato e funzionante
- [ ] ✅ Settings form con maturazione separata
- [ ] ✅ Balance widget con totali aggregati
- [ ] ✅ Tutti i componenti integrati
- [ ] ✅ CSS completo e responsive
- [ ] ✅ Test manuali passati
- [ ] ✅ NO malattia in UI
- [ ] ✅ Ready per FASE 6 (Deployment)

**Features Implementate:**

- ✅ Maturazione separata (Ferie/ROL/Permessi)
- ✅ Tracking start date
- ✅ Saldo iniziale (ferie in giorni!)
- ✅ Inserimento multiplo (bulk)
- ✅ Totali aggregati prominenti
- ✅ Validazione festività
- ✅ Preset CCNL
- ✅ Mobile responsive

---


## ⬜ FASE 5.10: FRONTEND BUDGET MODULE

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

**Tempo Stimato:** 2-3 giorni

### 5.10.1 - Budget API Service

- [ ] `budgetService.js` creato in `src/services/`:
  - [ ] getBudgets(params)
  - [ ] getBudgetsSummary(year, month)
  - [ ] getBudget(budgetId)
  - [ ] createBudget(budgetData)
  - [ ] updateBudget(budgetId, updates)
  - [ ] deleteBudget(budgetId)
  - [ ] Helper: formatCurrency()
  - [ ] Helper: getStatusColor()
  - [ ] Helper: getProgressColor()
- [ ] Service testato in browser console
- [ ] Commit service

### 5.10.2 - Budget Dashboard Component

- [ ] `BudgetDashboard.jsx` creato in `src/components/budget/`:
  - [ ] State: summary, loading, error
  - [ ] useEffect: loadSummary() on mount
  - [ ] Header con titolo + mese + bottone "Nuovo Budget"
  - [ ] Totals summary card (gradient blue):
    - [ ] Budget totale
    - [ ] Speso
    - [ ] Disponibile
    - [ ] Percentuale utilizzo + progress bar
  - [ ] Orphan budgets warning (yellow banner)
  - [ ] Active budgets grid (responsive: 3→2→1)
  - [ ] Empty state con CTA
  - [ ] Orphan budgets section (separata)
  - [ ] Loading state (skeleton)
  - [ ] Error state (alert)
  - [ ] Modals integration (create + edit)
- [ ] Component testato
- [ ] Commit dashboard

### 5.10.3 - Budget Card Component

- [ ] `BudgetCard.jsx` creato in `src/components/budget/`:
  - [ ] Header: category name + color dot + indicator emoji
  - [ ] Orphan indicator (se category NULL)
  - [ ] Edit/Delete buttons
  - [ ] Amounts grid (Budget/Speso/Disponibile)
  - [ ] Progress bar animated con color dinamico
  - [ ] Utilizzo percentage
  - [ ] Status badge (ok/warning/danger/exceeded/orphan)
  - [ ] Border yellow per orphan
  - [ ] Hover effects
- [ ] Component testato
- [ ] Commit card

### 5.10.4 - Budget Create Modal

- [ ] `BudgetCreateModal.jsx` creato in `src/components/budget/`:
  - [ ] Modal overlay (fixed + backdrop)
  - [ ] Header con close button
  - [ ] Form fields:
    - [ ] Category selector (solo expense categories)
    - [ ] Amount input (number, min 0.01)
    - [ ] Start date (default: oggi)
  - [ ] Error message display
  - [ ] Info box (reset automatico mensile)
  - [ ] Submit button con loading state
  - [ ] Cancel button
  - [ ] Form validation (category + amount required)
  - [ ] API call createBudget()
  - [ ] Success → onSuccess() callback
  - [ ] Error handling
- [ ] Modal testato
- [ ] Commit create modal

### 5.10.5 - Budget Edit Modal

- [ ] `BudgetEditModal.jsx` creato in `src/components/budget/`:
  - [ ] Modal overlay
  - [ ] Header con close button
  - [ ] Current budget info card (category + spent + percentage)
  - [ ] Form fields:
    - [ ] Amount input (nuovo importo)
    - [ ] is_active checkbox toggle
    - [ ] Help text per is_active
  - [ ] Error message display
  - [ ] Info box (tip storico)
  - [ ] Submit button con loading state
  - [ ] Cancel button
  - [ ] Form validation
  - [ ] API call updateBudget()
  - [ ] Success → onSuccess() callback
  - [ ] Error handling
- [ ] Modal testato
- [ ] Commit edit modal

### 5.10.6 - Routing & Integration

- [ ] `App.jsx` aggiornato:
  - [ ] Import BudgetDashboard
  - [ ] Route `/budgets` aggiunta
- [ ] `Navbar.jsx` aggiornato:
  - [ ] Link "Budget" aggiunto con icona 💰
- [ ] Navigation testata
- [ ] Commit routing

### 5.10.7 - Testing & Refinement

- [ ] Test complete workflow:
  - [ ] Dashboard load: summary + cards visibili ✓
  - [ ] Totals summary: calcoli corretti ✓
  - [ ] Progress bars: animano correttamente ✓
  - [ ] Status indicators: 🟢🟡🔴🚨 corretti ✓
  - [ ] Colors: corrispondono agli status ✓
- [ ] Test Create Budget:
  - [ ] Modal apre ✓
  - [ ] Category selector: solo expense ✓
  - [ ] Amount validation ✓
  - [ ] Submit → Budget creato ✓
  - [ ] Dashboard refresh automatico ✓
- [ ] Test Edit Budget:
  - [ ] Modal apre con dati correnti ✓
  - [ ] Modifica amount ✓
  - [ ] Toggle is_active ✓
  - [ ] Submit → Modifiche salvate ✓
  - [ ] Dashboard aggiornato ✓
- [ ] Test Delete Budget:
  - [ ] Confirm dialog ✓
  - [ ] Budget eliminato ✓
  - [ ] Dashboard refresh ✓
- [ ] Test Budget Orfano:
  - [ ] Elimina categoria con budget ✓
  - [ ] Budget appare come orphan ✓
  - [ ] Warning banner visibile ✓
  - [ ] Indicator ⚠️ corretto ✓
- [ ] Test Validations:
  - [ ] Income category → Errore ✓
  - [ ] Budget duplicato → Errore ✓
  - [ ] Amount negativo → Errore validazione ✓
  - [ ] Amount zero → Errore validazione ✓
- [ ] Test Responsive:
  - [ ] Desktop: 3 colonne ✓
  - [ ] Tablet: 2 colonne ✓
  - [ ] Mobile: 1 colonna ✓
  - [ ] Modals responsive ✓
- [ ] Bug fixing (se trovati)
- [ ] UX improvements
- [ ] `BUDGET_TESTING.md` creato in `frontend/docs/`
- [ ] Commit testing results

### 5.10.8 - Mobile Optimization

- [ ] Layout mobile verificato:
  - [ ] Cards leggibili
  - [ ] Touch targets sufficienti (min 44px)
  - [ ] Modals fullscreen su mobile
  - [ ] Form inputs accessibili
- [ ] Touch interactions testate
- [ ] Scroll behavior ottimizzato
- [ ] Commit mobile optimizations

**CHECKPOINT FASE 5.10:**

- [ ] ✅ budgetService.js con 9 metodi
- [ ] ✅ BudgetDashboard component completo
- [ ] ✅ BudgetCard con progress + indicators
- [ ] ✅ BudgetCreateModal con validazioni
- [ ] ✅ BudgetEditModal funzionante
- [ ] ✅ Routing `/budgets` attivo
- [ ] ✅ Navigation link presente
- [ ] ✅ Dashboard mostra tutti i budget
- [ ] ✅ Totals summary card funzionante
- [ ] ✅ Status indicators corretti (🟢🟡🔴🚨⚠️)
- [ ] ✅ Progress bars animate
- [ ] ✅ Create workflow completo
- [ ] ✅ Edit workflow completo
- [ ] ✅ Delete con conferma
- [ ] ✅ Orphan budgets handling
- [ ] ✅ Responsive design (desktop/tablet/mobile)
- [ ] ✅ Error handling implementato
- [ ] ✅ Loading states implementati
- [ ] ✅ Real-time data da API
- [ ] ✅ Mobile ottimizzato
- [ ] ✅ Ready per MVP launch

**Note Implementazione:**

- Components: 5 (Dashboard, Card, CreateModal, EditModal, Service)
- API Integration: budgetService con 6 endpoints
- Status Indicators: 🟢 ok (<70%) | 🟡 warning (70-90%) | 🔴 danger (90-100%) | 🚨 exceeded (>100%) | ⚠️ orphan
- Colors: Tailwind semantic (green/yellow/red/gray)
- Layout: CSS Grid responsive (3→2→1)
- Modals: Fixed overlay + backdrop blur

---


## ⬜ FASE 5.11: FRONTEND CSV IMPORT UI

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

**Tempo Stimato:** 1 giorno (6-8 ore)

### 5.11.1 - CSV Import Service

- [ ] `csvImportService.js` creato in `frontend/src/services/`:
  - [ ] previewCSVImport(file, accountId):
    - [ ] FormData con file CSV
    - [ ] POST /csv-import/preview
    - [ ] Return preview data
  - [ ] confirmCSVImport(accountId, rowNumbers, rows):
    - [ ] Filter selected rows
    - [ ] Transform to transaction format
    - [ ] POST /transactions/bulk
    - [ ] Return result summary
  - [ ] downloadCSVTemplate():
    - [ ] Create `<a>` element
    - [ ] Link to /csv-import/template
    - [ ] Trigger download
  - [ ] getStatusDisplay(status):
    - [ ] Return color, icon, label, borderColor
    - [ ] 5 status types: valid, warning, error, duplicate, orphan
  - [ ] formatAmount(amount):
    - [ ] Format con € e decimali IT (virgola)
    - [ ] Sign +/- corretto
  - [ ] formatDateDisplay(dateStr):
    - [ ] Convert ISO → DD/MM/YYYY
- [ ] Backend bulk endpoint verificato/creato:
  - [ ] POST /transactions/bulk in backend
  - [ ] Accepts List[TransactionCreate]
  - [ ] Returns { created, transaction_ids }
- [ ] Service testato in browser console
- [ ] Commit service

### 5.11.2 - CSV Import Modal Component

- [ ] `CSVImportModal.jsx` creato in `frontend/src/components/transactions/`:
  - [ ] Props: isOpen, onClose, accounts, onSuccess
  - [ ] State management:
    - [ ] step: 'upload' | 'preview' | 'importing'
    - [ ] selectedAccountId
    - [ ] file
    - [ ] previewData
    - [ ] selectedRows
    - [ ] loading
    - [ ] error
  - [ ] Reset state on modal open (useEffect)
  - [ ] Step 1 - Upload:
    - [ ] Instructions box (blue, 4 steps)
    - [ ] Download template button (prominent)
    - [ ] Account selection dropdown
    - [ ] File input (accept .csv)
    - [ ] File validation (type, size <5MB)
    - [ ] Error display
  - [ ] Step 2 - Preview:
    - [ ] Render CSVPreviewTable
    - [ ] Pass previewData, selectedRows, onSelectedRowsChange
  - [ ] Step 3 - Importing:
    - [ ] Loading spinner
    - [ ] Status message
    - [ ] Progress text
  - [ ] handleFileChange:
    - [ ] Validate .csv extension
    - [ ] Validate size <5MB
    - [ ] Set file state
  - [ ] handlePreview:
    - [ ] Validate file + account selected
    - [ ] Call previewCSVImport
    - [ ] Auto-select valid + warning rows
    - [ ] Set step to 'preview'
    - [ ] Error handling
  - [ ] handleConfirmImport:
    - [ ] Validate selectedRows.length > 0
    - [ ] Call confirmCSVImport
    - [ ] Call onSuccess callback
    - [ ] Close modal
    - [ ] Error handling
  - [ ] handleBack:
    - [ ] Reset to upload step
  - [ ] Header:
    - [ ] Title con emoji 📥
    - [ ] Close button (×)
  - [ ] Footer:
    - [ ] Selected count display
    - [ ] Buttons context-aware per step
    - [ ] Disabled states corretti
- [ ] Component testato
- [ ] Commit modal

### 5.11.3 - CSV Preview Table Component

- [ ] `CSVPreviewTable.jsx` creato in `frontend/src/components/transactions/`:
  - [ ] Props: previewData, selectedRows, onSelectedRowsChange
  - [ ] Summary stats cards (grid responsive):
    - [ ] Totale Righe (gray)
    - [ ] 🟢 Valide (green)
    - [ ] 🟡 Attenzione (yellow)
    - [ ] 🔴 Errori (red)
    - [ ] 🟣 Duplicati (purple)
  - [ ] Info banners:
    - [ ] Red banner se error_rows > 0
    - [ ] Purple banner se duplicate_rows > 0
  - [ ] Table structure:
    - [ ] Header: Checkbox | Riga | Status | Data | Descrizione | Importo | Categoria | Note
    - [ ] Rows map con styling condizionale
    - [ ] Status badge con icon + label
    - [ ] Status message sotto badge
    - [ ] Date formattata DD/MM/YYYY
    - [ ] Amount con colore (red/green)
    - [ ] Category con confidence % se fuzzy
  - [ ] handleToggleRow:
    - [ ] Add/remove da selectedRows array
  - [ ] handleToggleAll:
    - [ ] Se tutti selezionati → deselect all
    - [ ] Altrimenti → select valid + warning only
  - [ ] Row styling:
    - [ ] Hover effect
    - [ ] Opacity ridotta per error/duplicate
    - [ ] Checkbox disabled per error rows
  - [ ] Legend box (gray):
    - [ ] 5 status con spiegazione
  - [ ] Responsive (overflow-x-auto)
- [ ] Component testato
- [ ] Commit preview table

### 5.11.4 - Integration with Transactions Page

- [ ] `TransactionList.jsx` (o pagina transazioni) aggiornata:
  - [ ] Import CSVImportModal
  - [ ] State: showImportModal
  - [ ] Bottone "📥 Importa CSV":
    - [ ] Posizionato in toolbar
    - [ ] Blue button style
    - [ ] onClick → setShowImportModal(true)
  - [ ] CSVImportModal renderizzato:
    - [ ] isOpen={showImportModal}
    - [ ] onClose={() => setShowImportModal(false)}
    - [ ] accounts={accounts}
    - [ ] onSuccess={handleImportSuccess}
  - [ ] handleImportSuccess implementato:
    - [ ] Toast success message con count
    - [ ] fetchTransactions() per refresh lista
    - [ ] Optional: filter to today's imports
- [ ] Integration testata
- [ ] Commit integration

### 5.11.5 - Testing & Refinement

- [ ] Test 1 - Happy Path:
  - [ ] Click "Importa CSV"
  - [ ] Download template funziona
  - [ ] Compilato template (5 righe valide)
  - [ ] Account selezionato
  - [ ] File caricato
  - [ ] "Analizza File" → preview OK
  - [ ] 5 righe verdi, tutte selezionate
  - [ ] "Importa 5 Transazioni" → success
  - [ ] Toast appare
  - [ ] Transazioni visibili in lista
- [ ] Test 2 - Validation Errors:
  - [ ] CSV con date invalide, amount mancante
  - [ ] Preview mostra righe rosse
  - [ ] Righe rosse NON selezionabili
  - [ ] Status message chiaro
- [ ] Test 3 - Warnings (Fuzzy):
  - [ ] CSV con "Ristorante" (simile a "Ristorazione")
  - [ ] Riga gialla con suggestion
  - [ ] Match confidence % mostrato
  - [ ] Riga selezionabile
  - [ ] Import assegna categoria suggerita
- [ ] Test 4 - Duplicates:
  - [ ] Transazione esistente in DB
  - [ ] CSV con stessa transazione
  - [ ] Riga viola (duplicato)
  - [ ] NON selezionata di default
  - [ ] User può forzare con checkbox
- [ ] Test 5 - Mixed Statuses:
  - [ ] CSV: 3 valid, 2 warning, 1 error, 1 duplicate
  - [ ] Stats: 3+2+1+1=7 ✓
  - [ ] Auto-selected: 5 (valid+warning) ✓
  - [ ] Error+duplicate deselezionati ✓
- [ ] Test 6 - Edge Cases:
  - [ ] File non CSV → error message
  - [ ] File >5MB → error "troppo grande"
  - [ ] UTF-8 caratteri italiani → OK
  - [ ] Nessun account → error
  - [ ] Nessuna riga selezionata → button disabled
- [ ] Test 7 - UX Flow:
  - [ ] Modal apre/chiude correttamente
  - [ ] Download template funziona
  - [ ] File input funziona
  - [ ] "Indietro" torna a upload
  - [ ] "Annulla" chiude modal
  - [ ] Loading states visibili
  - [ ] Success redirect OK
- [ ] Browser compatibility:
  - [ ] Chrome ✓
  - [ ] Firefox ✓
  - [ ] Safari ✓
  - [ ] Mobile responsive ✓
- [ ] Bug fixing:
  - [ ] Fix bugs trovati
  - [ ] Polish animations
  - [ ] Verifica loading states
  - [ ] Error messages chiari
- [ ] `CSV_IMPORT_TESTING.md` aggiornato in `frontend/docs/`
- [ ] Commit testing results

**CHECKPOINT FASE 5.11:**

- [ ] ✅ csvImportService.js completo (6 functions)
- [ ] ✅ CSVImportModal.jsx completo (3 steps)
- [ ] ✅ CSVPreviewTable.jsx completo (table + stats)
- [ ] ✅ Integration con TransactionList
- [ ] ✅ Bottone "Importa CSV" visibile
- [ ] ✅ Download template funzionante
- [ ] ✅ Account selection implementata
- [ ] ✅ File upload con validazione
- [ ] ✅ Preview table interattiva
- [ ] ✅ Status colors (🟢🟡🔴🟣⚠️)
- [ ] ✅ Summary stats cards (5)
- [ ] ✅ Checkbox select/deselect
- [ ] ✅ Auto-selection smart (valid+warning)
- [ ] ✅ handleToggleRow funziona
- [ ] ✅ handleToggleAll funziona
- [ ] ✅ Error handling completo
- [ ] ✅ Loading states implementati
- [ ] ✅ Success callback con refresh
- [ ] ✅ Toast notifications
- [ ] ✅ Happy path testato ✓
- [ ] ✅ Validation errors testati ✓
- [ ] ✅ Warnings (fuzzy) testati ✓
- [ ] ✅ Duplicates testati ✓
- [ ] ✅ Mixed statuses testati ✓
- [ ] ✅ Edge cases testati ✓
- [ ] ✅ UX flow testato ✓
- [ ] ✅ Browser compatibility OK
- [ ] ✅ Mobile responsive OK
- [ ] ✅ Documentation aggiornata
- [ ] ✅ Ready per produzione MVP

**Note Implementazione:**

- 3-step workflow: upload → preview → importing
- Auto-selection: valid + warning rows (exclude errors + duplicates)
- Status indicators: 🟢 valid, 🟡 warning, 🔴 error, 🟣 duplicate, ⚠️ orphan
- Template download: /csv-import/template endpoint
- Bulk import: /transactions/bulk endpoint
- File validation: .csv extension, max 5MB
- Date format display: DD/MM/YYYY (Italian)
- Amount format: € XX,XX con sign +/-
- Fuzzy matching: confidence % displayed
- Components: 2 (Modal + PreviewTable)
- Service functions: 6 (preview, confirm, download, getStatus, formatAmount, formatDate)

---


## ⬜ FASE 6: DEPLOYMENT

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

### 6.1 - Preparazione Deploy Backend

- [ ] `backend/requirements.prod.txt` creato
- [ ] `backend/gunicorn.conf.py` creato
- [ ] `backend/Procfile` creato
- [ ] Commit production files

### 6.2 - Database Production

- [ ] Account Render.com creato
- [ ] PostgreSQL database creato su Render
- [ ] External Database URL salvato
- [ ] Migrations eseguite su production DB
- [ ] Tabelle create verificate

### 6.3 - Deploy Backend su Render

- [ ] Web Service creato su Render
- [ ] Repository connesso
- [ ] Build/Start commands configurati
- [ ] Environment variables settate
- [ ] Deploy completato
- [ ] URL backend accessibile
- [ ] `/docs` accessibile
- [ ] Test registration endpoint: SUCCESS

### 6.4 - Deploy Frontend su Render

- [ ] `.env.production` aggiornato con API URL
- [ ] Build script verificato
- [ ] Static Site creato su Render
- [ ] Build/Publish config settato
- [ ] Deploy completato
- [ ] URL frontend accessibile
- [ ] CORS aggiornato in backend
- [ ] Re-deploy backend completato

### 6.5 - Final Production Tests

- [ ] Register nuovo utente: SUCCESS
- [ ] Create accounts: SUCCESS
- [ ] Create transactions: SUCCESS
- [ ] Tutto funziona in production
- [ ] Test da mobile: SUCCESS
- [ ] Test da diversi dispositivi: SUCCESS
- [ ] Performance check (<1s API)
- [ ] Security check (HTTPS, CORS, JWT)

### 6.6 - Monitoring & Maintenance

- [ ] Monitoring setup (opzionale)
- [ ] Backup strategy verificata
- [ ] `docs/DEPLOYMENT.md` creato
- [ ] Commit deployment docs

**CHECKPOINT FASE 6:**

- [ ] ✅ Backend deployed e accessibile
- [ ] ✅ Frontend deployed e accessibile
- [ ] ✅ Database production funzionante
- [ ] ✅ HTTPS attivo
- [ ] ✅ CORS configurato
- [ ] ✅ Test production completo
- [ ] ✅ Performance OK
- [ ] ✅ App LIVE! 🚀

**URLs Production:**

- Backend API: _______________________
- Frontend App: _______________________
- API Docs: _______________________

---

## 🎉 MVP COMPLETATO!

**Data Completamento:** _____________

### Final Checklist

- [ ] ✅ Tutte le 6 fasi completate
- [ ] ✅ App deployed e live
- [ ] ✅ Documentazione completa
- [ ] ✅ Test passanti
- [ ] ✅ Performance OK
- [ ] ✅ Security verificata

### Post-Launch Tasks

- [ ] Condiviso su LinkedIn
- [ ] Aggiunto a portfolio
- [ ] README con screenshots
- [ ] Demo video creato
- [ ] Feedback raccolto da beta users

---

## 📈 METRICS & STATS

**Development Time:**

- Planned: 6-8 settimane
- Actual: _____ settimane
- Difference: _____

**Code Stats:**

- Backend files: _____
- Frontend files: _____
- Total lines of code: _____
- Test coverage: _____%

**Commits:**

- Total commits: _____
- Commit frequency: _____ per day

**Database:**

- Tables: 6
- Users (production): _____
- Transactions (production): _____

---

## 🚀 NEXT STEPS - FASE 7

**Features da Implementare:**

- [ ] Recurring Transactions
- [ ] Budget Planning
- [ ] Multi-Currency
- [ ] Advanced Charts
- [ ] Bill Reminders
- [ ] Receipt Scanning
- [ ] Shared Accounts
- [ ] Mobile App

**Priority Order:** (da definire)

1. ---
2. ---
3. ---

---

## 📝 NOTES & LEARNINGS

**Challenges Encountered:**

- Challenge 1: _____________________
- Challenge 2: _____________________
- Challenge 3: _____________________

**Lessons Learned:**

- Lesson 1: _____________________
- Lesson 2: _____________________
- Lesson 3: _____________________

**What Went Well:**

- Win 1: _____________________
- Win 2: _____________________
- Win 3: _____________________

**What Could Be Improved:**

- Improvement 1: _____________________
- Improvement 2: _____________________

---

**Progress Tracker creato:** 13 Novembre 2025
**Progetto:** Budget App SaaS
**Developer:** Giovanni Mezzasalma
