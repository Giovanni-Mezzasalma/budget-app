# 📊 PROGRESS TRACKER - Budget App Development

**Progetto:** Budget Management SaaS  
**Data Inizio:** _____________  
**Developer:** Giovanni Mezzasalma  
**Target Completion:** _____________

---

## 📅 TIMELINE OVERVIEW

| Fase | Descrizione | Durata Stimata | Data Inizio | Data Fine | Status |
|------|-------------|----------------|-------------|-----------|--------|
| 0 | Setup Progetto | 1 giorno | | | ⬜ |
| 1 | Database Foundation | 2-3 giorni | | | ⬜ |
| 2 | Backend - Auth | 3-4 giorni | | | ⬜ |
| 3 | Backend - Core | 4-5 giorni | | | ⬜ |
| 4 | Testing & Debug | 2 giorni | | | ⬜ |
| 5 | Frontend Integration | 5-7 giorni | | | ⬜ |
| 6 | Deployment | 3-4 giorni | | | ⬜ |

**Legenda Status:** ⬜ Non iniziato | 🟡 In corso | ✅ Completato

---

## ✅ FASE 0: SETUP PROGETTO

**Data Inizio:** 13/11/2025 | **Data Fine:** 15/11/2025 | **Status:** ✅ Completato

### 0.1 - Configurazione Repository GitHub
- [x] Repository creato su GitHub
- [x] GitHub Desktop configurato
- [x] VS Code aperto sul progetto
- [x] Git verification ✓

### 0.2 - Struttura Cartelle
- [x] Cartella `backend/` creata
- [x] Cartella `frontend/` creata
- [x] Cartella `database/` creata
- [x] Cartella `docs/` creata
- [x] Cartella `docker/` creata
- [x] File `.gitkeep` in ogni cartella

### 0.3 - File Configurazione
- [x] `.gitignore` creato e popolato
- [x] `README.md` aggiornato con tech stack
- [x] Primo commit pushato

### 0.4 - Python Virtual Environment
- [x] `venv` creato in `backend/`
- [x] `venv` attivato con successo
- [x] `requirements.txt` creato
- [x] Tutte le dipendenze installate
- [x] `pip list` verificato
- [x] Commit dependencies

### 0.5 - Database PostgreSQL
- [x] pgAdmin 4 aperto
- [x] Database `budget_app_dev` creato
- [x] User `budget_user` creato (opzionale)
- [x] File `.env` creato (NON committato)
- [x] File `.env.example` creato e committato
- [x] `test_db_connection.py` creato
- [x] Test connessione passato ✅
- [x] Commit database setup

### 0.6 - Docker Setup
- [x] `docker-compose.yml` creato
- [x] `Dockerfile` backend creato
- [x] Commit Docker files

### 0.7 - Documentazione
- [x] `docs/ARCHITECTURE.md` creato
- [x] `docs/API_SPEC.md` creato
- [x] `docs/DEVELOPMENT.md` creato
- [x] Commit documentazione

**CHECKPOINT FASE 0:**
- [x] ✅ Tutti i task completati
- [x] ✅ Repository funzionante
- [x] ✅ Database connesso
- [x] ✅ Ready per FASE 1

---

## ✅ FASE 1: DATABASE FOUNDATION

**Data Inizio:** 15/11/2025 | **Data Fine:** 19/11/2025 | **Status:** ✅ Completato

### 1.1 - Schema Database SQL
- [x] `database/schema_design.md` creato
- [x] `database/01_create_schema.sql` creato
- [x] Script eseguito in pgAdmin
- [x] Tutte le 6 tabelle create
- [x] Tabelle visibili in pgAdmin
- [x] `database/02_seed_default_categories.sql` creato
- [x] Funzione seed eseguita
- [x] Commit database scripts

### 1.2 - Modelli SQLAlchemy
- [x] `backend/app/config.py` creato
- [x] `backend/app/database.py` creato
- [x] `backend/app/models/__init__.py` creato
- [x] `backend/app/models/user.py` creato
- [x] `backend/app/models/account.py` creato
- [x] `backend/app/models/category.py` creato
- [x] `backend/app/models/transaction.py` creato
- [x] `backend/app/models/transfer.py` creato
- [x] `backend/app/models/custom_chart.py` creato
- [x] Commit models

### 1.3 - Alembic Migrations
- [x] Alembic inizializzato (`alembic init`)
- [x] `alembic.ini` configurato
- [x] `alembic/env.py` modificato
- [x] Prima migration generata
- [x] Migration applicata (`alembic upgrade head`)
- [x] Tabella `alembic_version` creata
- [x] `backend/reset_db.py` creato
- [x] Commit migrations

**CHECKPOINT FASE 1:**
- [x] ✅ Schema database completo
- [x] ✅ Modelli SQLAlchemy funzionanti
- [x] ✅ Alembic configurato
- [x] ✅ Test `Base.metadata.tables.keys()` passato
- [x] ✅ Ready per FASE 2

---

## ✅ FASE 2: BACKEND API - AUTENTICAZIONE

**Data Inizio:** 19/11/2025 | **Data Fine:** 21/11/2025 | **Status:** ✅ Completato

### 2.1 - Security Utilities
- [x] `backend/app/utils/security.py` creato
- [x] `hash_password()` implementata
- [x] `verify_password()` implementata
- [x] `create_access_token()` implementata
- [x] `verify_token()` implementata
- [x] Commit security utils

### 2.2 - Pydantic Schemas
- [x] `backend/app/schemas/__init__.py` creato
- [x] `backend/app/schemas/user.py` completo
- [x] `backend/app/schemas/account.py` creato (base)
- [x] `backend/app/schemas/category.py` creato (base)
- [x] `backend/app/schemas/transaction.py` creato (base)
- [x] `backend/app/schemas/transfer.py` creato (base)
- [x] Commit schemas

### 2.3 - Authentication Dependencies
- [x] `backend/app/dependencies.py` creato
- [x] `get_current_user()` implementata
- [x] `get_current_active_user()` implementata
- [x] Commit dependencies

### 2.4 - Auth Router
- [x] `backend/app/crud/user.py` creato
- [x] `get_user_by_email()` implementata
- [x] `create_user()` implementata
- [x] `authenticate_user()` implementata
- [x] `backend/app/routers/auth.py` creato
- [x] POST `/auth/register` implementato
- [x] POST `/auth/login` implementato
- [x] GET `/auth/me` implementato
- [x] Commit auth router

### 2.5 - Main Application
- [x] `backend/main.py` creato
- [x] CORS middleware configurato
- [x] Auth router incluso
- [x] `backend/run.py` creato
- [x] Server avviato con successo
- [x] Swagger UI accessibile (http://localhost:8000/docs)
- [x] Commit main app

### 2.6 - Testing Authentication
- [x] Test registrazione in Swagger: SUCCESS
- [x] Test login in Swagger: SUCCESS
- [x] Test GET /me con token: SUCCESS
- [x] Utente visibile in pgAdmin
- [x] Password hashata (non in chiaro)
- [x] Test email duplicata: ERROR 400 ✓
- [x] Test password sbagliata: ERROR 401 ✓
- [x] Test /me senza token: ERROR 401 ✓
- [x] `docs/TESTING.md` creato
- [x] Commit testing docs

**CHECKPOINT FASE 2:**
- [x] ✅ Auth completa funzionante
- [x] ✅ JWT tokens generati correttamente
- [x] ✅ Swagger UI testato
- [x] ✅ Tutti gli error cases coperti
- [x] ✅ Ready per FASE 3

---

## ✅ FASE 3: BACKEND API - CORE FEATURES

**Data Inizio:** 21/11/2025 | **Data Fine:** ________ | **Status:** 🟡 In corso (90% completato)

### 3.1 - Accounts CRUD & Router
- [x] `backend/app/schemas/account.py` completato
- [x] `backend/app/crud/account.py` creato
- [x] Tutte le funzioni CRUD implementate
- [x] `update_account_balance()` implementata
- [x] `backend/app/routers/accounts.py` creato
- [x] Tutti gli endpoints implementati
- [x] Router registrato in `main.py`
- [x] Test POST /accounts: SUCCESS
- [x] Test GET /accounts: SUCCESS
- [x] Test PUT /accounts/{id}: SUCCESS
- [x] Test DELETE /accounts/{id}: SUCCESS
- [x] Dati verificati in pgAdmin
- [x] Commit accounts

### 3.2 - Categories CRUD & Router
- [x] `backend/app/schemas/category.py` completato
- [x] `backend/app/crud/category.py` creato
- [x] `seed_default_categories()` implementata
- [x] `backend/app/routers/categories.py` creato
- [x] Router registrato in `main.py`
- [x] Test tutti gli endpoints: SUCCESS
- [x] Commit categories

### 3.3 - Transactions CRUD & Router
- [x] `backend/app/schemas/transaction.py` completato
- [x] `backend/app/crud/transaction.py` creato
- [x] `create_transaction()` con update balance
- [x] `backend/app/routers/transactions.py` creato
- [x] Query parameters per filtri implementati
- [x] Router registrato in `main.py`
- [x] Test creazione transaction: SUCCESS
- [x] Balance account aggiornato: VERIFIED ✓
- [x] Test filtri: SUCCESS
- [x] Commit transactions

### 3.4 - Transfers CRUD & Router
- [x] `backend/app/schemas/transfer.py` completato
- [x] `backend/app/crud/transfer.py` creato
- [x] `create_transfer()` con update 2 balance
- [x] `backend/app/routers/transfers.py` creato
- [x] Router registrato in `main.py`
- [x] Test transfer: SUCCESS
- [x] Entrambi i balance aggiornati: VERIFIED ✓
- [x] Commit transfers

### 3.5 - Custom Charts (opzionale)
- [x] Deciso: [x] Implementare ora [ ] Rimandare a Sviluppi Futuri
- [x] Se implementato: CRUD e router creati

### 3.6 - Analytics Endpoints
- [x] `backend/app/routers/analytics.py` creato
- [x] GET `/analytics/summary` implementato
- [x] GET `/analytics/monthly-trend` implementato
- [x] Router registrato in `main.py`
- [x] Test summary: SUCCESS
- [x] Test monthly trend: SUCCESS
- [x] Commit analytics

# SEZIONE 3.7 - Code Review & Bug Fixing

> **Inserire questa sezione nel process_tracker.md dopo la sezione 3.6 (Analytics Endpoints) e prima del CHECKPOINT FASE 3**

---

### 3.7 - Code Review & Bug Fixing

**Obiettivo:** Correggere incongruenze e bug identificati nella code review prima di procedere con Testing (Fase 4).

#### Problemi Critici

##### A. Strategia Balance Account
- [x] Analizzato problema `initial_balance` vs `current_balance`
- [x] Decisione presa: [ ] Opzione A (rinomina) / [ ] Opzione B (calcolo dinamico) / [x] Opzione C (campo separato)
- [x] Implementazione completata
- [x] File modificati:
  - [x] `app/models/account.py`
  - [x] `app/crud/account.py`
  - [x] `app/crud/transaction.py`
  - [x] `app/crud/transfer.py`
- [x] Test balance dopo transazione: PASS
- [x] Test balance dopo transfer: PASS

##### B. Allineamento Tipi Transazione (3 tipi)
- [x] Aggiornato commento in `app/models/category.py`
- [x] Aggiornato commento in `app/models/transaction.py`
- [x] Verificato che schema e CRUD usino stessi 3 tipi
- [x] Documentazione allineata

##### C. Path Correzione
- [x] Corretto `backend/Dockerfile`: `main:app` → `app.main:app` (Docker build funziona non ancora testato)

#### Problemi Medi

##### D. Centralizzazione Enum ChartType
- [x] Rimosso enum duplicato da `app/models/custom_chart.py`
- [x] Import da `app/schemas/custom_chart.py`
- [x] Test endpoint custom-charts funzionante

##### E. Validazione update_transfer
- [x] Revisione codice `app/crud/transfer.py`
- [x] Verificati tutti i casi edge
- [x] Aggiunta validazione mancante (se necessaria)

##### F. File SQL Obsoleti
- [x] Decisione: [x] Rimuovere / [ ] Archiviare / [ ] Aggiornare
- [x] Azione completata
- [x] Documentato in README se necessario

#### Note Documentate

##### G. Migration Vuota (c744b8064fb0)
- [x] ✅ Documentato: tabella `custom_charts` creata via SQL manuale
- [x] ✅ Non richiede fix, solo nota per riferimento futuro

##### H-J. Altri Minori
- [x] UUID String(36), modifica effettuata da `String(36)` a UIID
- [x] Commenti: decisione lingua presa
- [x] CORS_ORIGINS: testato parsing da .env

#### Test Finale Post-Correzioni

- [x] `cd backend && source venv/bin/activate`
- [x] `python -m app.main` o `python run.py` → Server UP
- [x] http://localhost:8000 → JSON response OK
- [x] http://localhost:8000/docs → Swagger UI OK
- [x] Login con utente esistente → Token OK
- [x] GET /accounts → Lista OK
- [x] POST /transactions (income) → Balance +amount
- [x] POST /transactions (expense) → Balance -amount
- [x] POST /transfers → From -amount, To +amount
- [x] GET /analytics/summary → Dati corretti

#### Commit Fase 3.7

- [x] Tutti i file modificati staged
- [x] Commit message: `fix: Code review corrections - balance strategy, path fixes, type alignment`
- [x] Push completato

---

## Note Aggiuntive per Fase 3.7
è possibile effettuare transazionie e trasferimenti per somme superiori all'account balance questa è una cosa da sistemare!
**Tempo stimato:** 2-4 ore

**Priorità correzioni:**
1. 🔴 Path `run.py` e `Dockerfile` (5 min) - BLOCCANTE per avvio
2. 🔴 Commenti tipi transazione (10 min) - Allineamento documentazione
3. 🟡 Strategia balance (30-60 min) - Dipende da opzione scelta
4. 🟡 Enum centralizzazione (15 min)
5. 🟢 File SQL obsoleti (5 min)
6. 🟢 Note documentazione (10 min)

**Decisioni da prendere:**

| Decisione | Opzioni | Raccomandazione |
|-----------|---------|-----------------|
| Balance strategy | A/B/C | **Opzione A** (rinomina) per MVP, B per v2 |
| File SQL | Rimuovi/Archivia/Aggiorna | **Archivia** in `database/archive/` |
| Lingua commenti | IT/EN | **EN** per codice |

---

**NOTA:** Dopo aver completato questa sezione, procedere con il CHECKPOINT FASE 3 aggiornato e poi FASE 4 (Testing).

**CHECKPOINT FASE 3:**
- [x] ✅ Tutti gli endpoints CRUD funzionanti
- [x] ✅ Balance updates automatici
- [x] ✅ Analytics calcolati correttamente
- [x] ✅ Test integrazione completa passato
- [x] ✅ Ready per FASE 4

**Test End-to-End Fase 3:**
- [x] 1. Utente registrato
- [x] 2. 2 account creati
- [x] 3. Categorie create
- [x] 4. Transactions create (balance OK)
- [x] 5. Transfer creato (balance OK)
- [x] 6. Analytics corretti
- [x] 7. Tutto funziona! 🎉

---

## ✅ FASE 3.8: BACKEND VACATION PLANNING

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

**Tempo Stimato:** 3-4 giorni

### 3.8.1 - Database Models
- [ ] `vacation_settings.py` creato (maturazione separata: ferie_days_per_month, rol_hours_per_month, permessi_hours_per_month)
- [ ] `tracking_start_date` implementato (invece di carryover_year)
- [ ] `initial_ferie_days` (in GIORNI), `initial_rol_hours`, `initial_permessi_hours` implementati
- [ ] `vacation_entry.py` creato (NO malattia - solo ferie/rol/permesso)
- [ ] `italian_holiday.py` creato
- [ ] `user_holiday.py` creato
- [ ] User model aggiornato con relationships
- [ ] Models __init__.py aggiornato
- [ ] Migration creata ed eseguita
- [ ] Tabelle verificate in pgAdmin
- [ ] Commit database models

### 3.8.2 - Utility Functions
- [ ] `easter.py` creato (calcolo Pasqua con validazione year >= 1583)
- [ ] `bridge_days.py` creato (calcolo ponti con validazione weekend/festività)
- [ ] `vacation_balance.py` RISCRITTO con maturazione separata:
  - [ ] Calcolo separato per tipo (Ferie/ROL/Permessi)
  - [ ] Conversione automatica ferie giorni → ore
  - [ ] Totali aggregati (total_hours_available, total_days_available)
  - [ ] Breakdown per tipo con hours_available
- [ ] Utils __init__.py aggiornato
- [ ] Commit utilities

### 3.8.3 - Pydantic Schemas
- [ ] `vacation.py` schemas creato:
  - [ ] VacationSettingsBase con nuovi campi (ferie_days_per_month, etc.)
  - [ ] BreakdownItem con hours_available, days_available
  - [ ] VacationBalanceResponse con totali aggregati
  - [ ] NO riferimenti a "malattia"
- [ ] Schemas __init__.py aggiornato
- [ ] Commit schemas

### 3.8.4 - CRUD Operations
- [ ] `vacation_settings.py` CRUD creato
- [ ] `vacation_entry.py` CRUD creato con validazioni:
  - [ ] Blocco inserimento weekend
  - [ ] Blocco inserimento festività nazionali
  - [ ] Blocco inserimento festività custom utente
- [ ] `italian_holiday.py` CRUD creato
- [ ] `user_holiday.py` CRUD creato con validazione date (es. 31 Feb)
- [ ] CRUD __init__.py aggiornato
- [ ] Commit CRUD

### 3.8.5 - API Router
- [ ] `vacation.py` router creato con endpoint:
  - [ ] GET/PUT /vacation/settings (nuovi campi)
  - [ ] POST/GET/PUT/DELETE /vacation/entries (con validazione festività)
  - [ ] POST /vacation/entries/bulk (FIX validazione hours_per_day + skip festività)
  - [ ] GET /vacation/balance (con breakdown completo + totali)
  - [ ] GET /vacation/calendar (OTTIMIZZATO: 1 query invece di 4)
  - [ ] GET /vacation/holidays
  - [ ] GET /vacation/bridges
  - [ ] POST/GET/DELETE /vacation/user-holidays
- [ ] Router registrato in main.py
- [ ] Commit router

### 3.8.6 - Manual Testing
- [ ] GET/PUT /vacation/settings testato (maturazione separata)
- [ ] POST /vacation/entries testato (validazione weekend PASS)
- [ ] POST /vacation/entries testato (validazione festività PASS)
- [ ] POST /vacation/entries/bulk testato (skip festività PASS)
- [ ] GET /vacation/balance testato (totali aggregati corretti)
- [ ] GET /vacation/calendar testato (festività custom visibili)
- [ ] Commit test results

**CHECKPOINT FASE 3.8:**
- [ ] ✅ Models con maturazione separata (Ferie/ROL/Permessi)
- [ ] ✅ Tracking start date funzionante
- [ ] ✅ Validazione weekend + festività attiva
- [ ] ✅ Balance con totali aggregati corretto
- [ ] ✅ NO malattia in sistema
- [ ] ✅ Calcolo Pasqua corretto
- [ ] ✅ Calcolo ponti corretto
- [ ] ✅ Ready per FASE 4

**Note Implementazione:**
- Ferie: 1.83 giorni/mese = 22 giorni/anno
- ROL: 2.67 ore/mese = 32 ore/anno
- Permessi: 8.67 ore/mese = 104 ore/anno
- Initial balance: ferie in GIORNI, ROL/Permessi in ORE

## ✅ FASE 3.9: BACKEND BUDGET PLANNING

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

**Tempo Stimato:** 2-3 giorni

### 3.9.1 - Database Models
- [ ] `budget.py` model creato con:
  - [ ] Foreign keys: user_id, category_id (ON DELETE SET NULL)
  - [ ] Fields: amount, period, start_date, is_active
  - [ ] UniqueConstraint parziale (user_id, category_id, is_active WHERE is_active=true)
  - [ ] Indexes: user_active, category, start_date
- [ ] User model aggiornato con relationship budgets
- [ ] Models __init__.py aggiornato
- [ ] Migration creata ed eseguita
- [ ] Tabella `budgets` verificata in pgAdmin
- [ ] Commit database models

### 3.9.2 - Pydantic Schemas
- [ ] `budget.py` schemas creato:
  - [ ] BudgetBase con validazione amount > 0, period = "monthly"
  - [ ] BudgetCreate, BudgetUpdate
  - [ ] BudgetResponse
  - [ ] CategoryInfo (minimal)
  - [ ] BudgetWithStatus (con spent/remaining/percentage/status/indicator)
  - [ ] BudgetSummaryResponse (con budgets list + totals)
- [ ] Schemas __init__.py aggiornato
- [ ] Commit schemas

### 3.9.3 - CRUD Operations
- [ ] `budget.py` CRUD creato con:
  - [ ] get_budgets (con filtri is_active, category_id)
  - [ ] get_budget (singolo con ownership)
  - [ ] create_budget (con validazioni: category exists, is expense type, no duplicate)
  - [ ] update_budget
  - [ ] delete_budget
  - [ ] calculate_spent_for_month (real-time da transactions)
  - [ ] get_budget_status (🟢🟡🔴🚨 basato su percentage)
  - [ ] get_budget_with_spending (arricchisce budget con dati spesa)
  - [ ] get_budgets_summary (dashboard con tutti i budget + totali)
- [ ] CRUD __init__.py aggiornato
- [ ] Commit CRUD

### 3.9.4 - API Router
- [ ] `budgets.py` router creato con endpoints:
  - [ ] GET /budgets (lista con filtri)
  - [ ] GET /budgets/summary (dashboard principale - KEY ENDPOINT)
  - [ ] GET /budgets/{id} (dettaglio)
  - [ ] POST /budgets (crea con validazioni)
  - [ ] PUT /budgets/{id} (update)
  - [ ] DELETE /budgets/{id}
- [ ] Router registrato in main.py
- [ ] Commit router

### 3.9.5 - Manual Testing
- [ ] Server avviato (http://localhost:8000/docs)
- [ ] Setup: Registra utente + login + authorize
- [ ] Crea 3 categorie expense (Ristoranti, Spesa, Benzina)
- [ ] POST /budgets: Crea 3 budget (€200, €400, €100)
- [ ] Test constraint: Crea budget duplicato → 400 Bad Request ✓
- [ ] Crea transazioni: €150 Ristoranti, €30 Ristoranti, €380 Spesa, €45 Benzina
- [ ] GET /budgets/summary: Verifica spent/percentage/indicators corretti:
  - [ ] Ristoranti: €180/€200 (90%) 🔴
  - [ ] Spesa: €380/€400 (95%) 🔴
  - [ ] Benzina: €45/€100 (45%) 🟢
  - [ ] Totali: €605/€700 (86.43%)
- [ ] DELETE categoria "Ristoranti" → Budget diventa orfano
- [ ] GET /budgets/summary: Verifica budget orfano:
  - [ ] category_id: null
  - [ ] category_name: "Categoria Eliminata"
  - [ ] status: "orphan"
  - [ ] indicator: "⚠️"
- [ ] PUT /budgets/{id}: Modifica amount Spesa a €500
- [ ] GET /budgets/summary: Verifica percentage aggiornata
- [ ] PUT /budgets/{id}: Disattiva budget Benzina (is_active=false)
- [ ] GET /budgets/summary: Verifica budget Benzina non compare
- [ ] DELETE /budgets/{id}: Elimina budget Spesa
- [ ] GET /budgets: Verifica budget eliminato
- [ ] Verifica in pgAdmin: Query `SELECT * FROM budgets;`
- [ ] `TESTING_BUDGETS.md` creato con workflow
- [ ] Commit testing documentation

**CHECKPOINT FASE 3.9:**
- [ ] ✅ Tabella budgets con constraint UNIQUE parziale
- [ ] ✅ Model Budget con ON DELETE SET NULL per category_id
- [ ] ✅ Schemas con validazioni (amount > 0, period = "monthly")
- [ ] ✅ CRUD con calcolo spesa real-time
- [ ] ✅ get_budget_status restituisce indicatori 🟢🟡🔴🚨
- [ ] ✅ get_budgets_summary funziona (endpoint chiave dashboard)
- [ ] ✅ Validazione: solo expense categories
- [ ] ✅ Constraint: un budget attivo per categoria
- [ ] ✅ Budget orfani gestiti (category_id NULL)
- [ ] ✅ Storico budget (is_active=false)
- [ ] ✅ 6 endpoints testati e funzionanti
- [ ] ✅ Ready per FASE 4.7

**Note Implementazione:**
- Period: solo "monthly" per MVP
- Calcolo: real-time (no cache)
- Unicità: un budget attivo per categoria
- Orfani: category_id NULL quando categoria eliminata
- Rollover: NO - budget riparte da zero ogni mese
- Alert: solo indicatori visivi (no email/push)
- Status: ok (<70%) | warning (70-90%) | danger (90-100%) | exceeded (>100%) | orphan (no category)

## ✅ FASE 3.10: BACKEND CSV IMPORT

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

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

## ✅ FASE 3.11: BACKEND EXCEL EXPORT

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

**Tempo Stimato:** 0.5 giorni (4 ore)

**Nota Strategica:** Export Excel sarà principalmente CLIENT-SIDE (frontend genera file). Backend fornisce solo endpoint helper aggregato per evitare multiple API calls.

### 3.11.1 - Export Data Schemas
- [ ] `export.py` creato in `backend/app/schemas/`:
  - [ ] TransactionExport:
    - [ ] date, account_name, category_name
    - [ ] type, description, amount, notes
  - [ ] CategoryTotal:
    - [ ] macro_category (Entrate/Spese Necessarie/Spese Extra)
    - [ ] category_name
    - [ ] total_amount, transaction_count
    - [ ] percentage (% sul totale del tipo)
  - [ ] AccountTotal:
    - [ ] account_name
    - [ ] initial_balance (calcolato: current - delta period)
    - [ ] total_income, total_expense
    - [ ] final_balance (current balance)
    - [ ] variation (final - initial)
  - [ ] TransferExport:
    - [ ] date, from_account, to_account
    - [ ] amount, transfer_type, notes
  - [ ] ExportDataResponse (master schema):
    - [ ] Period: start_date, end_date, generated_at
    - [ ] Summary: total_income, total_expense_necessity, total_expense_extra, total_expense, net_balance, total_net_worth
    - [ ] Data: transactions, categories_breakdown, accounts_breakdown, transfers
    - [ ] Metadata: user_email, total_transactions, total_accounts
- [ ] Schemas aggiunti a `backend/app/schemas/__init__.py`
- [ ] Commit schemas

### 3.11.2 - Export CRUD Logic
- [ ] `export.py` creato in `backend/app/crud/`:
  - [ ] get_export_data(db, user_id, start_date, end_date, account_id):
    - [ ] Default dates: start_date = first day current month, end_date = today
    - [ ] Get user info
    - [ ] Query transactions con JOIN (Account, Category)
    - [ ] Filter by date range + optional account_id
    - [ ] Transform to TransactionExport list
    - [ ] Calculate summary stats:
      - [ ] total_income (sum positive amounts)
      - [ ] total_expense_necessity (sum abs where type = expense_necessity)
      - [ ] total_expense_extra (sum abs where type = expense_extra)
      - [ ] total_expense (necessity + extra)
      - [ ] net_balance (income - expense)
    - [ ] Call _calculate_categories_breakdown()
    - [ ] Call _calculate_accounts_breakdown()
    - [ ] Calculate total_net_worth (sum all account balances)
    - [ ] Query transfers in period
    - [ ] Transform to TransferExport list
    - [ ] Return ExportDataResponse
  - [ ] _calculate_categories_breakdown(db, user_id, start_date, end_date, account_id):
    - [ ] Query: group by category.name, category.type
    - [ ] Aggregate: sum(abs(amount)), count(*)
    - [ ] Filter by date range + optional account_id
    - [ ] Calculate totals by type per percentages
    - [ ] Map type to macro_category (income → Entrate, etc.)
    - [ ] Calculate percentage per category
    - [ ] Sort by total_amount desc
    - [ ] Return List[CategoryTotal]
  - [ ] _calculate_accounts_breakdown(db, user_id, start_date, end_date):
    - [ ] Get all user accounts
    - [ ] For each account:
      - [ ] Query transactions in period
      - [ ] Calculate income (sum positive)
      - [ ] Calculate expense (sum abs negative)
      - [ ] Calculate delta (income - expense)
      - [ ] Calculate initial_balance (current - delta)
      - [ ] variation = delta
    - [ ] Return List[AccountTotal]
- [ ] Helper functions importate in `backend/app/crud/__init__.py`
- [ ] Commit CRUD logic

### 3.11.3 - Export API Router
- [ ] `export.py` creato in `backend/app/routers/`:
  - [ ] GET /export/data:
    - [ ] Query params: start_date, end_date, account_id (all optional)
    - [ ] Requires authentication (get_current_user)
    - [ ] Call export_crud.get_export_data()
    - [ ] Return ExportDataResponse
    - [ ] Docstring: explains single endpoint strategy, client-side generation
  - [ ] GET /export/info:
    - [ ] Return export capabilities metadata
    - [ ] available_formats: ["excel"]
    - [ ] generation_method: "client-side"
    - [ ] supported_sheets: list of 5-6 sheet names
    - [ ] Notes about xlsx.js usage
- [ ] Router registrato in `backend/app/main.py`:
  - [ ] `from app.routers import export`
  - [ ] `app.include_router(export.router, prefix="/api/v1")`
- [ ] Commit router

### 3.11.4 - Testing Manuale
- [ ] Dati test preparati:
  - [ ] User test loggato
  - [ ] 3 account creati (Checking, Savings, Cash)
  - [ ] 5 categorie create (Stipendio, Spesa, Ristorazione, Trasporti, Abbonamenti)
  - [ ] 10-15 transazioni create (mix income/expenses, date varie)
  - [ ] 2 transfers creati
- [ ] Server avviato: `python run.py`
- [ ] Swagger aperto: http://localhost:8000/docs
- [ ] Test 1 - Export default period:
  - [ ] Login + Authorize
  - [ ] GET `/api/v1/export/data` (no params)
  - [ ] Response 200 OK
  - [ ] start_date = first day current month
  - [ ] end_date = today
  - [ ] total_income correct
  - [ ] total_expense correct
  - [ ] net_balance = income - expense
  - [ ] total_net_worth = sum all accounts
  - [ ] transactions list populated
  - [ ] categories_breakdown populated
  - [ ] accounts_breakdown populated
  - [ ] transfers populated
- [ ] Test 2 - Custom period:
  - [ ] GET `/export/data?start_date=2025-01-01&end_date=2025-01-31`
  - [ ] Response 200 OK
  - [ ] Period dates correct
  - [ ] Transactions filtered correctly
- [ ] Test 3 - Single account filter:
  - [ ] GET `/export/data?account_id={account_uuid}`
  - [ ] Response 200 OK
  - [ ] Transactions only from that account
  - [ ] Summary reflects only that account
  - [ ] accounts_breakdown still includes all accounts
- [ ] Test 4 - Export info:
  - [ ] GET `/api/v1/export/info`
  - [ ] Response 200 OK
  - [ ] Metadata correct (formats, method, sheets)
- [ ] Test 5 - Large dataset:
  - [ ] Create 100+ transactions
  - [ ] GET `/export/data`
  - [ ] Response time <2 seconds
  - [ ] JSON size reasonable (<1MB)
- [ ] Verifica aggregazioni:
  - [ ] Categories breakdown:
    - [ ] Totals correct per category
    - [ ] Percentages sum to ~100% per type
    - [ ] Sorted by total_amount desc
  - [ ] Accounts breakdown:
    - [ ] initial_balance = final_balance - variation
    - [ ] variation = total_income - total_expense
    - [ ] final_balance = current account.balance
  - [ ] Summary:
    - [ ] total_income = sum all positive amounts
    - [ ] total_expense = sum all negative amounts (abs)
    - [ ] net_balance = income - expense
    - [ ] total_net_worth = sum all account balances (current)
- [ ] `EXPORT_TESTING.md` creato in `backend/docs/`:
  - [ ] Test workflow documented
  - [ ] Expected responses documented
  - [ ] Aggregation formulas explained
- [ ] Commit testing docs

**CHECKPOINT FASE 3.11:**
- [ ] ✅ 5 schemas creati (Transaction, Category, Account, Transfer, ExportDataResponse)
- [ ] ✅ export.py CRUD con 3 funzioni (get_export_data + 2 helpers)
- [ ] ✅ export.py router con 2 endpoints (GET /data, GET /info)
- [ ] ✅ Router registrato in main.py
- [ ] ✅ Export default period funziona (current month)
- [ ] ✅ Export custom period funziona
- [ ] ✅ Export single account filter funziona
- [ ] ✅ Export info metadata corretto
- [ ] ✅ Large dataset performance OK (<2 sec)
- [ ] ✅ Categories breakdown: aggregazione corretta
- [ ] ✅ Categories breakdown: percentages corrette
- [ ] ✅ Accounts breakdown: initial_balance calcolato correttamente
- [ ] ✅ Accounts breakdown: variation corretta
- [ ] ✅ Summary stats: totals verified
- [ ] ✅ Summary: net_worth = sum all accounts
- [ ] ✅ Transactions: include account_name, category_name
- [ ] ✅ Transfers: populated se esistono
- [ ] ✅ Swagger docs chiare
- [ ] ✅ Testing documentation completa

**Note Implementazione:**
- Backend fornisce solo dati JSON aggregati (NO generazione file Excel)
- Frontend (Fase 5.12) genererà Excel client-side con xlsx.js
- Single endpoint /export/data evita multiple API calls (1 instead of 5-6)
- Pre-calcoli: aggregazioni fatte backend per performance
- Default period: current month (inizio mese → oggi)
- Optional filters: date range, single account
- Response structure: summary + transactions + breakdowns + transfers
- Scalabilità: zero file temporanei, zero carico server per file generation
- Performance target: <2 sec per 100+ transactions

---

## ✅ FASE 4: TESTING & DEBUG

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

## ✅ FASE 4.6: TESTING VACATION MODULE

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

## ✅ FASE 4.7: TESTING BUDGET MODULE

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

## ✅ FASE 4.8: TESTING CSV IMPORT MODULE

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

## ✅ FASE 4.9: TESTING EXCEL EXPORT BACKEND

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

**Tempo Stimato:** 0.25 giorni (2 ore)

### 4.9.1 - Setup Test Fixtures
- [ ] Pytest setup verificato:
  - [ ] `backend/pytest.ini` configurato
  - [ ] `backend/tests/conftest.py` con fixtures base
- [ ] Fixtures export aggiunte a conftest.py:
  - [ ] export_test_data:
    - [ ] 3 accounts creati (Checking, Savings, Cash)
    - [ ] Checking: test_account esistente
    - [ ] Savings: balance €5000, type savings
    - [ ] Cash: balance €200, type cash
    - [ ] 5 categories create:
      - [ ] Stipendio (income)
      - [ ] Spesa (expense_necessity)
      - [ ] Ristorazione (expense_extra)
      - [ ] Trasporti (expense_necessity)
      - [ ] Abbonamenti (expense_extra)
    - [ ] 11 transactions create (current month):
      - [ ] 2 income (€2500 + €500 = €3000)
      - [ ] 4 expense_necessity (€45.50 + €67.80 + €50 + €30 = €193.30)
      - [ ] 5 expense_extra (€35 + €42.50 + €25 + €9.99 + €14.99 = €127.48)
    - [ ] 2 transfers creati:
      - [ ] Checking → Savings (€1000, type savings)
      - [ ] Savings → Cash (€100, type withdrawal)
    - [ ] Return dict con: user, accounts, categories, transactions, transfers, period_start, period_end
  - [ ] previous_month_data:
    - [ ] 1 transaction in previous month
    - [ ] Used for date filtering tests
- [ ] Commit fixtures

### 4.9.2 - Test Export CRUD Functions (~12 test)
- [ ] `test_export_crud.py` creato in `backend/tests/`:
  - [ ] test_get_export_data_basic:
    - [ ] Call get_export_data with period dates
    - [ ] Verify start_date, end_date correct
    - [ ] Verify user_email present
    - [ ] Verify 11 transactions returned
    - [ ] Verify 3 accounts in breakdown
  - [ ] test_get_export_data_summary_calculations:
    - [ ] total_income = €3000
    - [ ] total_expense_necessity = €193.30
    - [ ] total_expense_extra = €127.48
    - [ ] total_expense = €320.78
    - [ ] net_balance = €2679.22
  - [ ] test_get_export_data_categories_breakdown:
    - [ ] 5 categories in breakdown
    - [ ] Find "Spesa" category
    - [ ] Verify total_amount = €113.30 (45.50 + 67.80)
    - [ ] Verify transaction_count = 2
    - [ ] Verify macro_category = "Spese Necessarie"
    - [ ] Verify percentage > 0
  - [ ] test_get_export_data_accounts_breakdown:
    - [ ] Find Checking account
    - [ ] Verify final_balance = current account.balance
    - [ ] Verify total_income > 0
    - [ ] Verify total_expense > 0
    - [ ] Verify variation = final - initial
  - [ ] test_get_export_data_with_account_filter:
    - [ ] Call with account_id = Checking
    - [ ] All transactions from Checking only
    - [ ] accounts_breakdown still has 3 accounts
  - [ ] test_get_export_data_with_date_filter:
    - [ ] Call with current month dates
    - [ ] Previous month transaction NOT included
  - [ ] test_get_export_data_transfers:
    - [ ] 2 transfers returned
    - [ ] from_account, to_account, amount present
  - [ ] test_get_export_data_default_dates:
    - [ ] Call without dates
    - [ ] start_date = first day current month
    - [ ] end_date = today
  - [ ] test_calculate_categories_breakdown_percentages:
    - [ ] Group by macro_category
    - [ ] Sum percentages per type
    - [ ] Necessity percentages sum to ~100
    - [ ] Extra percentages sum to ~100
  - [ ] test_calculate_accounts_breakdown_balance_logic:
    - [ ] For each account:
      - [ ] variation = final - initial
      - [ ] variation = income - expense
  - [ ] test_export_data_net_worth_calculation:
    - [ ] total_net_worth = sum all account final_balances
- [ ] Run CRUD tests:
  - [ ] `pytest tests/test_export_crud.py -v`
  - [ ] ~12 test passano
- [ ] Commit CRUD tests

### 4.9.3 - Test Export API Endpoint (~11 test)
- [ ] `test_export_api.py` creato in `backend/tests/`:
  - [ ] test_get_export_data_endpoint:
    - [ ] GET /api/v1/export/data with dates
    - [ ] Status 200
    - [ ] Response has: start_date, end_date, total_income, transactions, categories_breakdown, accounts_breakdown
  - [ ] test_get_export_data_default_period:
    - [ ] GET /export/data (no params)
    - [ ] Status 200
    - [ ] start_date = first day current month
    - [ ] end_date = today
  - [ ] test_get_export_data_with_account_filter:
    - [ ] GET with account_id param
    - [ ] Status 200
    - [ ] All transactions from that account only
  - [ ] test_get_export_data_custom_date_range:
    - [ ] GET with start_date=2025-01-01, end_date=2025-01-31
    - [ ] Status 200
    - [ ] Dates in response match
  - [ ] test_get_export_data_requires_auth:
    - [ ] GET without auth token
    - [ ] Status 401
  - [ ] test_get_export_info_endpoint:
    - [ ] GET /api/v1/export/info
    - [ ] Status 200
    - [ ] Has: available_formats, generation_method, supported_sheets
    - [ ] available_formats contains "excel"
    - [ ] generation_method = "client-side"
  - [ ] test_export_data_response_structure:
    - [ ] GET /export/data
    - [ ] Status 200
    - [ ] Period fields: start_date, end_date, generated_at
    - [ ] Summary fields: total_income, total_expense_necessity, total_expense_extra, total_expense, net_balance, total_net_worth
    - [ ] Data arrays: transactions (list), categories_breakdown (list), accounts_breakdown (list), transfers (list)
    - [ ] Metadata: user_email, total_transactions, total_accounts
  - [ ] test_export_transaction_structure:
    - [ ] GET /export/data
    - [ ] First transaction has: date, account_name, category_name, type, description, amount
  - [ ] test_export_category_breakdown_structure:
    - [ ] GET /export/data
    - [ ] First category has: macro_category, category_name, total_amount, transaction_count, percentage
  - [ ] test_export_account_breakdown_structure:
    - [ ] GET /export/data
    - [ ] First account has: account_name, initial_balance, total_income, total_expense, final_balance, variation
- [ ] Run API tests:
  - [ ] `pytest tests/test_export_api.py -v`
  - [ ] ~11 test passano
- [ ] Commit API tests

### 4.9.4 - Coverage & Final Verification
- [ ] Run all export tests with coverage:
  - [ ] `pytest tests/test_export*.py -v --cov=app/crud/export --cov=app/routers/export --cov-report=html`
  - [ ] Coverage app/crud/export.py: >85%
  - [ ] Coverage app/routers/export.py: >80%
- [ ] Open coverage report:
  - [ ] `open htmlcov/index.html` (macOS) or `xdg-open htmlcov/index.html` (Linux)
  - [ ] Identify uncovered areas
  - [ ] Add tests if coverage <80%
- [ ] Run full test suite:
  - [ ] `pytest -v`
  - [ ] All tests pass (including export)
  - [ ] Total export tests: ~23
    - [ ] test_export_crud.py: ~12
    - [ ] test_export_api.py: ~11
- [ ] Document coverage:
  - [ ] `EXPORT_TEST_COVERAGE.md` created in `backend/docs/`
  - [ ] Coverage percentages per file
  - [ ] Test summary (total, passing)
  - [ ] Test scenarios covered
  - [ ] Next steps
- [ ] Commit coverage report

**CHECKPOINT FASE 4.9:**
- [ ] ✅ test_export_crud.py (~12 test)
- [ ] ✅ test_export_api.py (~11 test)
- [ ] ✅ Totale: ~23 test export module
- [ ] ✅ Tutti i test passano
- [ ] ✅ Coverage export.py CRUD: >85%
- [ ] ✅ Coverage export.py router: >80%
- [ ] ✅ Coverage report HTML generato
- [ ] ✅ Fixtures export completi (export_test_data, previous_month_data)
- [ ] ✅ Basic export data retrieval testato
- [ ] ✅ Summary calculations verified (income, expenses, balance)
- [ ] ✅ Categories breakdown: aggregation + percentages
- [ ] ✅ Accounts breakdown: initial/final balance logic
- [ ] ✅ Date filtering testato (default + custom)
- [ ] ✅ Account filtering testato
- [ ] ✅ Transfers included in export
- [ ] ✅ Percentages sum to 100% verified
- [ ] ✅ Balance calculations verified (variation = final - initial)
- [ ] ✅ Net worth calculation verified (sum all accounts)
- [ ] ✅ API endpoint /export/data testato
- [ ] ✅ Default period (current month) testato
- [ ] ✅ Custom date range testato
- [ ] ✅ Account filter testato
- [ ] ✅ Authentication required verified
- [ ] ✅ API /export/info metadata testato
- [ ] ✅ Response structure complete (all fields)
- [ ] ✅ Transaction object structure verified
- [ ] ✅ Category breakdown object structure verified
- [ ] ✅ Account breakdown object structure verified
- [ ] ✅ Documentation created (EXPORT_TEST_COVERAGE.md)
- [ ] ✅ Ready per FASE 5

**Note Implementazione:**
- Test focus: data aggregation accuracy (NOT file generation)
- Fixtures: comprehensive dataset (3 accounts, 5 categories, 11 transactions, 2 transfers)
- CRUD tests: verify calculations (summary, percentages, balances)
- API tests: verify endpoint behavior + response structure
- Coverage target: >80% for export module
- File generation testing: will be in Phase 5.12 (frontend)
- Expected totals: income €3000, expense €320.78, net €2679.22
- Categories percentages: sum to ~100% per type (allow ±1% rounding)
- Account balance logic: variation = final - initial = income - expense
- Net worth: sum of all account current balances
- Default period: first day of current month → today
- API structure: single call returns all data (summary + transactions + breakdowns)

---

## ✅ FASE 5: FRONTEND INTEGRATION

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜

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

## ✅ FASE 5.9: FRONTEND VACATION MODULE

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

### 5.9.4 - Bulk Entry Modal (NUOVO)
- [ ] `BulkEntryModal.jsx` creato:
  - [ ] Form range date (start_date, end_date)
  - [ ] Dropdown tipo (ferie/rol/permesso)
  - [ ] Input ore (solo per ROL/Permessi)
  - [ ] Checkbox "Skip weekend"
  - [ ] Checkbox "Skip festività"
  - [ ] Preview count approssimativo
  - [ ] Submit crea multiple entries
- [ ] Modal testato e funzionante

### 5.9.5 - Balance Widget (COMPLETAMENTE RISCRITTO)
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

### 5.9.6 - Settings Component (COMPLETAMENTE RISCRITTO)
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

## ✅ FASE 5.10: FRONTEND BUDGET MODULE

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

## ✅ FASE 5.11: FRONTEND CSV IMPORT UI

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
    - [ ] Create <a> element
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

## ✅ FASE 5.12: FRONTEND EXCEL GENERATION

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜ Non iniziato

**Tempo Stimato:** 1 giorno (6-8 ore)

### 5.12.1 - Install XLSX Library
- [ ] Libreria xlsx installata:
  - [ ] Terminal: `cd frontend`
  - [ ] `npm install xlsx` or `yarn add xlsx`
  - [ ] Verifica in package.json: "xlsx": "^0.18.x"
- [ ] `xlsxHelper.js` creato in `frontend/src/utils/`:
  - [ ] calculateColumnWidths(data):
    - [ ] Loop su righe per trovare max length per colonna
    - [ ] Min width: 10, Max width: 50
    - [ ] Return array { wch: width }
  - [ ] formatCurrency(amount):
    - [ ] Absolute value, 2 decimals
    - [ ] Replace point with comma (IT format)
    - [ ] Return "€ XX,XX"
  - [ ] formatDate(dateStr):
    - [ ] Parse ISO date
    - [ ] Return "DD/MM/YYYY"
  - [ ] styleHeaderRow(worksheet, headers, color):
    - [ ] Set cell style: bold font, white text, colored background
    - [ ] Add borders
    - [ ] Center alignment
  - [ ] formatCurrencyColumns(worksheet, columns, startRow, endRow):
    - [ ] Apply "€ #,##0.00" format to specified columns
  - [ ] Default export object
- [ ] Commit utilities

### 5.12.2 - Excel Generation Service
- [ ] `excelService.js` creato in `frontend/src/services/`:
  - [ ] Import XLSX library: `import * as XLSX from 'xlsx'`
  - [ ] Import api, xlsxHelper utilities
  - [ ] fetchExportData(startDate, endDate, accountId):
    - [ ] Build URL: `/export/data?start_date=...&end_date=...`
    - [ ] If accountId: append `&account_id=...`
    - [ ] GET request via api
    - [ ] Return response.data
  - [ ] generateExcelFile(exportData, options):
    - [ ] Destructure options: includeRiepilogo, includeTransazioni, etc.
    - [ ] Create workbook: XLSX.utils.book_new()
    - [ ] If includeRiepilogo: append Riepilogo sheet
    - [ ] If includeTransazioni: append Transazioni sheet
    - [ ] If includeCategorie: append Per Categoria sheet
    - [ ] If includeAccount: append Per Account sheet
    - [ ] If includeTrasferimenti + transfers exist: append Trasferimenti sheet
    - [ ] If includeBudget + budgets exist: append Budget sheet
    - [ ] Write workbook: XLSX.write(workbook, { bookType: 'xlsx', type: 'array' })
    - [ ] Return Blob
  - [ ] createRiepilogoSheet(data):
    - [ ] Build array of arrays (summary data)
    - [ ] Rows: title, period, generated_at, totals (income, expenses, balance, net_worth), statistics
    - [ ] Convert to worksheet: XLSX.utils.aoa_to_sheet()
    - [ ] Set column widths: [30, 20]
    - [ ] Return worksheet
  - [ ] createTransazioniSheet(data):
    - [ ] Map transactions to objects: Data, Account, Categoria, Tipo, Descrizione, Importo, Note
    - [ ] mapTypeToItalian() helper for Tipo field
    - [ ] Convert to worksheet: XLSX.utils.json_to_sheet()
    - [ ] Set autofilter: worksheet['!autofilter']
    - [ ] Set freeze panes: worksheet['!freeze'] = { xSplit: 0, ySplit: 1 }
    - [ ] Set column widths: [12, 15, 20, 18, 30, 12, 25]
    - [ ] Return worksheet
  - [ ] createCategorieSheet(data):
    - [ ] Map categories_breakdown to objects: Macro-Categoria, Sotto-Categoria, Totale Speso, N° Transazioni, % sul Totale
    - [ ] Convert to worksheet: XLSX.utils.json_to_sheet()
    - [ ] Set column widths: [20, 25, 15, 15, 12]
    - [ ] Return worksheet
  - [ ] createAccountSheet(data):
    - [ ] Map accounts_breakdown to objects: Account, Saldo Iniziale, Entrate, Uscite, Saldo Finale, Variazione
    - [ ] Convert to worksheet: XLSX.utils.json_to_sheet()
    - [ ] Set column widths: [20, 15, 12, 12, 15, 12]
    - [ ] Return worksheet
  - [ ] createTrasferimentiSheet(data):
    - [ ] Map transfers to objects: Data, Da Account, A Account, Importo, Tipo, Note
    - [ ] mapTransferType() helper for Tipo field
    - [ ] Convert to worksheet: XLSX.utils.json_to_sheet()
    - [ ] Set column widths: [12, 20, 20, 12, 15, 25]
    - [ ] Return worksheet
  - [ ] createBudgetSheet(data):
    - [ ] Map budgets (if exist) to objects
    - [ ] Placeholder for now (budgets not yet implemented)
    - [ ] Return worksheet
  - [ ] downloadExcel(blob, filename):
    - [ ] Create object URL from blob
    - [ ] Create <a> element
    - [ ] Set href, download attribute
    - [ ] Append to body, click, remove
    - [ ] Revoke object URL
  - [ ] mapTypeToItalian(type):
    - [ ] Map: income → Entrata, expense_necessity → Spesa Necessaria, expense_extra → Spesa Extra
  - [ ] mapTransferType(type):
    - [ ] Map: internal → Interno, savings → Risparmio, withdrawal → Prelievo, deposit → Deposito
  - [ ] Default export object
- [ ] Service testato in browser console
- [ ] Commit service

### 5.12.3 - Excel Export Modal Component
- [ ] `ExcelExportModal.jsx` creato in `frontend/src/components/reports/`:
  - [ ] Props: isOpen, onClose, accounts
  - [ ] Import services: fetchExportData, generateExcelFile, downloadExcel
  - [ ] State management:
    - [ ] loading (boolean)
    - [ ] error (string | null)
    - [ ] periodType: 'this_month' | 'last_month' | 'last_3_months' | 'last_6_months' | 'this_year' | 'last_year' | 'custom'
    - [ ] startDate (string YYYY-MM-DD)
    - [ ] endDate (string YYYY-MM-DD)
    - [ ] selectedAccountId (string | '')
    - [ ] includeRiepilogo (boolean, default true)
    - [ ] includeTransazioni (boolean, default true)
    - [ ] includeCategorie (boolean, default true)
    - [ ] includeAccount (boolean, default true)
    - [ ] includeTrasferimenti (boolean, default true)
    - [ ] includeBudget (boolean, default false)
  - [ ] useEffect: initialize dates on modal open
  - [ ] updateDatesForPeriod(type):
    - [ ] Switch on type
    - [ ] Calculate start/end dates per period
    - [ ] this_month: first day of month → today
    - [ ] last_month: first day last month → last day last month
    - [ ] last_3_months: 3 months ago → today
    - [ ] last_6_months: 6 months ago → today
    - [ ] this_year: Jan 1 → today
    - [ ] last_year: Jan 1 prev year → Dec 31 prev year
    - [ ] custom: keep current dates
    - [ ] setStartDate, setEndDate
  - [ ] handleExport():
    - [ ] Validate startDate, endDate present
    - [ ] setLoading(true), setError(null)
    - [ ] try-catch block:
      - [ ] Call fetchExportData(startDate, endDate, selectedAccountId)
      - [ ] Call generateExcelFile(exportData, options)
      - [ ] Generate filename: `BudgetApp_Export_${startDate}_${endDate}.xlsx`
      - [ ] Call downloadExcel(blob, filename)
      - [ ] onClose()
      - [ ] Optional: success toast
    - [ ] catch: setError with message
    - [ ] finally: setLoading(false)
  - [ ] Modal structure:
    - [ ] Header: title "📊 Esporta Excel", close button
    - [ ] Content (p-6):
      - [ ] Period selection:
        - [ ] Label "Periodo"
        - [ ] Grid 3x2 quick buttons (this_month, last_month, etc.)
        - [ ] Custom button
        - [ ] If custom: show date inputs (Da, A)
      - [ ] Account filter:
        - [ ] Label "Account"
        - [ ] Select dropdown: "Tutti gli account" + accounts map
      - [ ] Sheet options:
        - [ ] Label "Fogli da includere"
        - [ ] Checkboxes: Riepilogo, Transazioni, Per Categoria, Per Account, Trasferimenti, Budget (disabled)
      - [ ] Error display (if error)
    - [ ] Footer (border-t, bg-gray-50):
      - [ ] Left: "Formato: Excel (.xlsx)"
      - [ ] Right: Annulla button, "📥 Esporta Excel" button
  - [ ] Styling: Tailwind classes, responsive
- [ ] Component testato
- [ ] Commit modal

### 5.12.4 - Integration with App
- [ ] Pagina/dashboard aggiornata (es. Dashboard.jsx or Reports.jsx):
  - [ ] Import ExcelExportModal
  - [ ] State: showExportModal (boolean)
  - [ ] Bottone "📊 Esporta Excel":
    - [ ] Green button (bg-green-600)
    - [ ] onClick: setShowExportModal(true)
  - [ ] ExcelExportModal renderizzato:
    - [ ] isOpen={showExportModal}
    - [ ] onClose={() => setShowExportModal(false)}
    - [ ] accounts={accounts}
  - [ ] Accounts array disponibile (fetch se necessario)
- [ ] Integration testata
- [ ] Commit integration

### 5.12.5 - Testing & Refinement
- [ ] Test 1 - Basic Export (This Month):
  - [ ] Click "Esporta Excel"
  - [ ] Period: "Questo mese" selected by default
  - [ ] All sheets checked
  - [ ] Click "📥 Esporta Excel"
  - [ ] Loading state visible
  - [ ] File downloads: `BudgetApp_Export_2025-02-01_2025-02-06.xlsx`
  - [ ] Open file in Excel/LibreOffice
  - [ ] 5 sheets present: Riepilogo, Transazioni, Per Categoria, Per Account, Trasferimenti
  - [ ] Riepilogo sheet:
    - [ ] Title row
    - [ ] Period dates correct
    - [ ] Summary totals: income, expenses, net balance, net worth
    - [ ] Statistics: transaction count, account count
  - [ ] Transazioni sheet:
    - [ ] All transactions present
    - [ ] Headers: Data, Account, Categoria, Tipo, Descrizione, Importo, Note
    - [ ] Auto-filter enabled (dropdown arrows on headers)
    - [ ] Freeze panes work (header stays visible on scroll)
    - [ ] Dates formatted DD/MM/YYYY
    - [ ] Tipo translated to Italian
  - [ ] Per Categoria sheet:
    - [ ] Categories aggregated correctly
    - [ ] Headers: Macro-Categoria, Sotto-Categoria, Totale Speso, N° Transazioni, % sul Totale
    - [ ] Percentages calculated
  - [ ] Per Account sheet:
    - [ ] All accounts listed
    - [ ] Headers: Account, Saldo Iniziale, Entrate, Uscite, Saldo Finale, Variazione
    - [ ] Balances correct
  - [ ] Trasferimenti sheet:
    - [ ] Transfers listed (if exist)
    - [ ] Headers: Data, Da Account, A Account, Importo, Tipo, Note
- [ ] Test 2 - Custom Period:
  - [ ] Click "📅 Personalizzato"
  - [ ] Date inputs appear
  - [ ] Set Da: 2025-01-01, A: 2025-01-31
  - [ ] Export
  - [ ] Filename: `BudgetApp_Export_2025-01-01_2025-01-31.xlsx`
  - [ ] Only January transactions in file
- [ ] Test 3 - Single Account Filter:
  - [ ] Select specific account from dropdown
  - [ ] Export
  - [ ] Only transactions from that account in Transazioni sheet
  - [ ] Per Account sheet still shows all accounts
- [ ] Test 4 - Selective Sheets:
  - [ ] Uncheck "Trasferimenti"
  - [ ] Export
  - [ ] File has only 4 sheets (no Trasferimenti)
- [ ] Test 5 - Large Dataset:
  - [ ] Create 100+ transactions in DB
  - [ ] Select "Quest'anno"
  - [ ] Export
  - [ ] Generation time <5 seconds
  - [ ] All 100+ transactions in file
  - [ ] File size reasonable (<2MB)
- [ ] Test 6 - Edge Cases:
  - [ ] No account selected (default "Tutti") → all transactions exported
  - [ ] No transactions in period → sheets empty but no error
  - [ ] Missing end date → "Esporta" button disabled
  - [ ] Period with only transfers → Trasferimenti sheet populated
- [ ] Excel file quality check:
  - [ ] Formatting:
    - [ ] Headers bold (if styled)
    - [ ] Column widths readable
    - [ ] Currency format: € XX,XX
    - [ ] Date format: DD/MM/YYYY
    - [ ] Auto-filter works on Transazioni
    - [ ] Freeze panes work
  - [ ] Data accuracy:
    - [ ] Summary totals match dashboard
    - [ ] Transaction count correct
    - [ ] Categories breakdown adds up to 100%
    - [ ] Account balances match app
    - [ ] Net worth = sum of all account balances
- [ ] Browser compatibility:
  - [ ] Chrome: export + download works
  - [ ] Firefox: export + download works
  - [ ] Safari: export + download works
  - [ ] Mobile (Chrome/Safari): download works
- [ ] Bug fixing:
  - [ ] Fix bugs trovati
  - [ ] Polish loading spinner
  - [ ] Improve error messages
  - [ ] Add success toast (optional)
- [ ] `EXCEL_EXPORT_TESTING.md` creato in `frontend/docs/`:
  - [ ] Test scenarios documented
  - [ ] Expected results
  - [ ] Browser compatibility notes
- [ ] Commit testing results

**CHECKPOINT FASE 5.12:**
- [ ] ✅ xlsx library installata (SheetJS)
- [ ] ✅ xlsxHelper.js utilities (5 functions)
- [ ] ✅ excelService.js completo:
  - [ ] fetchExportData()
  - [ ] generateExcelFile()
  - [ ] 5 sheet creators (Riepilogo, Transazioni, Categorie, Account, Trasferimenti)
  - [ ] downloadExcel()
  - [ ] Helper functions (mapType, mapTransferType)
- [ ] ✅ ExcelExportModal.jsx completo:
  - [ ] Period selection (6 presets + custom)
  - [ ] Account filter
  - [ ] Sheet options (6 checkboxes)
  - [ ] Loading/error states
  - [ ] Export handler
- [ ] ✅ Integration: "Esporta Excel" button in app
- [ ] ✅ Modal opens/closes correctly
- [ ] ✅ Basic export works (this month, all sheets)
- [ ] ✅ Custom period works
- [ ] ✅ Account filter works
- [ ] ✅ Selective sheets works
- [ ] ✅ Large dataset (<5 sec generation)
- [ ] ✅ Edge cases handled
- [ ] ✅ Excel file quality:
  - [ ] 5 sheets generated
  - [ ] Riepilogo: summary correct
  - [ ] Transazioni: auto-filter, freeze panes
  - [ ] Per Categoria: aggregations correct
  - [ ] Per Account: balances correct
  - [ ] Trasferimenti: transfers listed
  - [ ] Formatting: readable, professional
  - [ ] Data accuracy: matches app
- [ ] ✅ Browser compatibility OK (Chrome, Firefox, Safari, Mobile)
- [ ] ✅ Documentation created
- [ ] ✅ Ready per MVP production

**Note Implementazione:**
- Client-side generation: zero server load, instant download
- Library: SheetJS (xlsx) v0.18+
- 5 sheets: Riepilogo, Transazioni, Per Categoria, Per Account, Trasferimenti (+Budget placeholder)
- Period presets: 6 quick options (this_month, last_month, last_3_months, last_6_months, this_year, last_year)
- Custom period: date pickers for Da/A
- Account filter: dropdown "Tutti" + individual accounts
- Sheet selection: checkboxes to include/exclude
- Filename format: `BudgetApp_Export_{start}_{end}.xlsx`
- Auto-filter: enabled on Transazioni sheet
- Freeze panes: header row stays visible on scroll
- Italian labels: Tipo field translated (Entrata, Spesa Necessaria, etc.)
- Currency format: € XX,XX (Italian comma)
- Date format: DD/MM/YYYY
- Performance: <5 sec for 100+ transactions
- Single API call: /export/data returns all data at once
- Error handling: API errors, validation errors displayed in modal

---

## ✅ FASE 6: DEPLOYMENT

**Data Inizio:** _______ | **Data Fine:** _______ | **Status:** ⬜

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
1. _____________________
2. _____________________
3. _____________________

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
