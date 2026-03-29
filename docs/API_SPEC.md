# 📡 API Specifications - Budget App

**Documento:** Specifiche API REST  
**Versione:** 1.0  
**Base URL:** `http://localhost:8000/api/v1`  
**Production URL:** `https://api.budget-app.com/api/v1`  
**Data:** Novembre 2025

---

## 📋 Indice

1. [Overview](#overview)
2. [Authentication](#authentication)
3. [Endpoints - Auth](#endpoints---authentication)
4. [Endpoints - Accounts](#endpoints---accounts)
5. [Endpoints - Categories](#endpoints---categories)
6. [Endpoints - Transactions](#endpoints---transactions)
7. [Endpoints - Transfers](#endpoints---transfers)
8. [Endpoints - Analytics](#endpoints---analytics)
9. [Endpoints - Vacation Planning](#endpoints---vacation-planning)
10. [Endpoints - Budget Planning](#endpoints---budget-planning)
11. [Endpoints - CSV Import](#endpoints---csv-import)
13. [Error Responses](#error-responses)
14. [Rate Limiting](#rate-limiting)

---

## 🎯 Overview

### API Design Principles

- **RESTful**: Resource-based URLs
- **JSON**: All requests/responses in JSON
- **Stateless**: JWT-based authentication
- **Versioned**: `/api/v1/` prefix
- **CRUD**: Standard Create, Read, Update, Delete
- **Pagination**: Limit/offset for lists
- **Filtering**: Query parameters for filtering

### Content Types

```
Content-Type: application/json
Accept: application/json
```

---

## 🔒 Authentication

### JWT Token-Based Authentication

Tutti gli endpoints (eccetto `/auth/register` e `/auth/login`) richiedono autenticazione.

### Header Format

```http
Authorization: Bearer <JWT_TOKEN>
```

### Token Lifecycle

- **Expiration**: 7 giorni (10080 minuti)
- **Refresh**: Non implementato in MVP (re-login richiesto)
- **Storage**: Client-side (localStorage)

### Example

```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
     http://localhost:8000/api/v1/accounts
```

---

## 🔐 Endpoints - Authentication

### POST `/auth/register`

Registrazione nuovo utente.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123",
  "full_name": "John Doe"
}
```

**Validation:**
- Email: valido, univoco
- Password: min 8 caratteri, 1 numero, 1 maiuscola
- Full name: opzionale, max 255 caratteri

**Response:** `201 Created`
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "full_name": "John Doe",
    "is_active": true,
    "created_at": "2025-11-14T10:30:00Z"
  }
}
```

**Errors:**
- `400`: Email già registrata
- `422`: Validazione fallita

---

### POST `/auth/login`

Login utente esistente.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123"
}
```

**Response:** `200 OK`
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "full_name": "John Doe",
    "is_active": true,
    "created_at": "2025-11-14T10:30:00Z",
    "last_login": "2025-11-15T14:20:00Z"
  }
}
```

**Errors:**
- `401`: Credenziali errate
- `403`: Account disabilitato

---

### GET `/auth/me`

Recupera profilo utente autenticato.

**Headers:** `Authorization: Bearer <token>`

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "full_name": "John Doe",
  "is_active": true,
  "created_at": "2025-11-14T10:30:00Z",
  "last_login": "2025-11-15T14:20:00Z"
}
```

**Errors:**
- `401`: Token invalido/scaduto

---

### POST `/auth/logout`

Logout (client-side, rimuove token).

**Response:** `200 OK`
```json
{
  "message": "Successfully logged out"
}
```

---

## 💰 Endpoints - Accounts

### GET `/accounts`

Lista tutti gli account dell'utente.

**Headers:** `Authorization: Bearer <token>`

**Query Parameters:**
- `skip` (int, default=0): Offset pagination
- `limit` (int, default=100): Max risultati

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "name": "Conto Corrente",
    "account_type": "checking",
    "balance": 1500.50,
    "currency": "EUR",
    "color": "#3B82F6",
    "icon": "💳",
    "is_active": true,
    "created_at": "2025-11-01T10:00:00Z",
    "updated_at": "2025-11-15T14:30:00Z"
  },
  {
    "id": "uuid",
    "name": "Risparmio",
    "account_type": "savings",
    "balance": 5000.00,
    "currency": "EUR",
    "color": "#10B981",
    "icon": "🏦",
    "is_active": true,
    "created_at": "2025-11-01T10:05:00Z",
    "updated_at": "2025-11-15T14:30:00Z"
  }
]
```

---

### POST `/accounts`

Crea nuovo account.

**Headers:** `Authorization: Bearer <token>`

**Request:**
```json
{
  "name": "Nuovo Conto",
  "account_type": "checking",
  "balance": 0.00,
  "currency": "EUR",
  "color": "#3B82F6",
  "icon": "💳"
}
```

**Account Types:**
- `checking`: Conto corrente
- `savings`: Risparmio
- `credit`: Carta di credito
- `cash`: Contanti
- `investment`: Investimenti

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "name": "Nuovo Conto",
  "account_type": "checking",
  "balance": 0.00,
  "currency": "EUR",
  "color": "#3B82F6",
  "icon": "💳",
  "is_active": true,
  "created_at": "2025-11-15T15:00:00Z",
  "updated_at": "2025-11-15T15:00:00Z"
}
```

---

### GET `/accounts/{account_id}`

Dettagli singolo account.

**Headers:** `Authorization: Bearer <token>`

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "name": "Conto Corrente",
  "account_type": "checking",
  "balance": 1500.50,
  "currency": "EUR",
  "color": "#3B82F6",
  "icon": "💳",
  "is_active": true,
  "created_at": "2025-11-01T10:00:00Z",
  "updated_at": "2025-11-15T14:30:00Z"
}
```

**Errors:**
- `404`: Account non trovato

---

### PUT `/accounts/{account_id}`

Modifica account esistente.

**Headers:** `Authorization: Bearer <token>`

**Request:** (tutti i campi opzionali)
```json
{
  "name": "Nuovo Nome",
  "color": "#EF4444",
  "icon": "🏦",
  "is_active": false
}
```

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "name": "Nuovo Nome",
  "account_type": "checking",
  "balance": 1500.50,
  "currency": "EUR",
  "color": "#EF4444",
  "icon": "🏦",
  "is_active": false,
  "created_at": "2025-11-01T10:00:00Z",
  "updated_at": "2025-11-15T16:00:00Z"
}
```

**Errors:**
- `404`: Account non trovato

---

### DELETE `/accounts/{account_id}`

Elimina account.

**Headers:** `Authorization: Bearer <token>`

**Response:** `204 No Content`

**Errors:**
- `404`: Account non trovato
- `400`: Account ha transazioni collegate (da gestire)

---

## 📂 Endpoints - Categories

### GET `/categories`

Lista categorie dell'utente.

**Headers:** `Authorization: Bearer <token>`

**Query Parameters:**
- `type` (income/expense): Filtra per tipo

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "name": "Stipendio",
    "type": "income",
    "color": "#10B981",
    "icon": "💰",
    "is_system": true,
    "created_at": "2025-11-01T10:00:00Z"
  },
  {
    "id": "uuid",
    "name": "Alimentari",
    "type": "expense",
    "color": "#F59E0B",
    "icon": "🛒",
    "is_system": true,
    "created_at": "2025-11-01T10:00:00Z"
  }
]
```

---

### POST `/categories`

Crea nuova categoria.

**Request:**
```json
{
  "name": "Palestra",
  "type": "expense",
  "color": "#8B5CF6",
  "icon": "🏋️"
}
```

**Response:** `201 Created`

---

### PUT `/categories/{category_id}`

Modifica categoria (solo se non `is_system`).

---

### DELETE `/categories/{category_id}`

Elimina categoria (solo se non `is_system`).

---

## 💸 Endpoints - Transactions

### GET `/transactions`

Lista transazioni con filtri.

**Headers:** `Authorization: Bearer <token>`

**Query Parameters:**
- `skip` (int): Pagination offset
- `limit` (int, max 100): Risultati per pagina
- `account_id` (uuid): Filtra per account
- `category_id` (uuid): Filtra per categoria
- `type` (income/expense): Filtra per tipo
- `start_date` (date, YYYY-MM-DD): Data inizio
- `end_date` (date, YYYY-MM-DD): Data fine

**Example:**
```
GET /transactions?account_id=xxx&start_date=2025-11-01&end_date=2025-11-30
```

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "account_id": "uuid",
    "category_id": "uuid",
    "amount": 50.00,
    "type": "expense",
    "date": "2025-11-15",
    "description": "Spesa supermercato",
    "notes": "Acquisti settimanali",
    "tags": ["spesa", "alimentari"],
    "created_at": "2025-11-15T10:30:00Z",
    "updated_at": "2025-11-15T10:30:00Z"
  }
]
```

---

### POST `/transactions`

Crea nuova transazione.

**Request:**
```json
{
  "account_id": "uuid",
  "category_id": "uuid",
  "amount": 50.00,
  "type": "expense",
  "date": "2025-11-15",
  "description": "Spesa supermercato",
  "notes": "Acquisti settimanali",
  "tags": ["spesa", "alimentari"]
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "account_id": "uuid",
  "category_id": "uuid",
  "amount": 50.00,
  "type": "expense",
  "date": "2025-11-15",
  "description": "Spesa supermercato",
  "notes": "Acquisti settimanali",
  "tags": ["spesa", "alimentari"],
  "created_at": "2025-11-15T10:30:00Z",
  "updated_at": "2025-11-15T10:30:00Z"
}
```

**Side Effect:** Account balance aggiornato automaticamente.

---

### PUT `/transactions/{transaction_id}`

Modifica transazione esistente.

**Side Effect:** Account balance ricalcolato.

---

### DELETE `/transactions/{transaction_id}`

Elimina transazione.

**Side Effect:** Account balance ricalcolato.

---

## 🔄 Endpoints - Transfers

### GET `/transfers`

Lista trasferimenti tra account.

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "from_account_id": "uuid",
    "to_account_id": "uuid",
    "amount": 100.00,
    "date": "2025-11-15",
    "description": "Risparmio mensile",
    "created_at": "2025-11-15T11:00:00Z"
  }
]
```

---

### POST `/transfers`

Crea nuovo trasferimento.

**Request:**
```json
{
  "from_account_id": "uuid",
  "to_account_id": "uuid",
  "amount": 100.00,
  "date": "2025-11-15",
  "description": "Risparmio mensile"
}
```

**Validations:**
- `from_account_id` ≠ `to_account_id`
- `amount` > 0
- Entrambi gli account appartengono all'utente

**Response:** `201 Created`

**Side Effects:** 
- Account origine: balance -= amount
- Account destinazione: balance += amount

---

### DELETE `/transfers/{transfer_id}`

Elimina trasferimento.

**Side Effects:** Rollback balance su entrambi gli account.

---

## 📊 Endpoints - Analytics

### GET `/analytics/summary`

Summary finanziaria.

**Headers:** `Authorization: Bearer <token>`

**Query Parameters:**
- `start_date` (YYYY-MM-DD): Inizio periodo
- `end_date` (YYYY-MM-DD): Fine periodo

**Response:** `200 OK`
```json
{
  "total_income": 3000.00,
  "total_expense": 1500.00,
  "net": 1500.00,
  "total_balance": 6500.50,
  "accounts_count": 3,
  "period": {
    "start_date": "2025-11-01",
    "end_date": "2025-11-30"
  }
}
```

---

### GET `/analytics/monthly-trend`

Trend mensile income/expense.

**Query Parameters:**
- `months` (int, default=12): Numero mesi

**Response:** `200 OK`
```json
{
  "2025-01": {
    "income": 2500.00,
    "expense": 1200.00
  },
  "2025-02": {
    "income": 2500.00,
    "expense": 1350.00
  },
  "2025-03": {
    "income": 3000.00,
    "expense": 1450.00
  }
}
```

---

### GET `/analytics/category-breakdown`

Breakdown spese per categoria (periodo).

**Response:** `200 OK`
```json
[
  {
    "category_name": "Alimentari",
    "category_id": "uuid",
    "total": 450.00,
    "percentage": 30.0,
    "transaction_count": 15
  },
  {
    "category_name": "Trasporti",
    "category_id": "uuid",
    "total": 200.00,
    "percentage": 13.3,
    "transaction_count": 8
  }
]
```

---

## 🏖️ Endpoints - Vacation Planning

> Modulo per la gestione di ferie, ROL e permessi con maturazione separata per tipo, festività italiane e calcolo automatico ponti. **Implementato in Fase 3.8.**

### GET `/vacation/settings`

Recupera la configurazione ferie dell'utente (maturazione mensile, saldo iniziale, data inizio tracking).

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "work_hours_per_day": 8.0,
  "ferie_days_per_month": 1.83,
  "rol_hours_per_month": 2.67,
  "permessi_hours_per_month": 8.67,
  "tracking_start_date": "2026-01-01",
  "initial_ferie_days": 0.0,
  "initial_rol_hours": 0.0,
  "initial_permessi_hours": 0.0
}
```

---

### PUT `/vacation/settings`

Aggiorna configurazione ferie. Supporta preset CCNL (Commercio, Metalmeccanico).

**Request:**
```json
{
  "ferie_days_per_month": 1.83,
  "rol_hours_per_month": 2.67,
  "permessi_hours_per_month": 8.67,
  "tracking_start_date": "2026-01-01"
}
```

---

### GET `/vacation/entries`

Lista tutte le entry ferie/ROL/permessi dell'utente.

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "date": "2026-03-15",
    "entry_type": "ferie",
    "hours": 8.0,
    "notes": "Vacanza pasquale"
  }
]
```

---

### POST `/vacation/entries`

Crea una singola entry. Validazioni: no weekend, no festività nazionali/custom, no duplicati.

**Request:**
```json
{
  "date": "2026-03-15",
  "entry_type": "ferie",
  "notes": "Vacanza"
}
```

**Entry types:** `ferie` (ore auto da settings) · `rol` (ore manuali) · `permesso` (ore manuali)

**Errors:**
- `400`: Giorno festivo, weekend o duplicato

---

### POST `/vacation/entries/bulk`

Crea entry per un range di date, saltando automaticamente weekend e festività.

**Request:**
```json
{
  "start_date": "2026-07-14",
  "end_date": "2026-07-18",
  "entry_type": "ferie",
  "skip_weekends": true,
  "skip_holidays": true
}
```

---

### PUT `/vacation/entries/{entry_id}`

Modifica una entry esistente. Solo `notes` e `hours` (per ROL/permessi) sono modificabili.

---

### DELETE `/vacation/entries/{entry_id}`

Elimina una entry.

---

### GET `/vacation/balance`

Calcola il saldo disponibile con breakdown per tipo.

**Response:** `200 OK`
```json
{
  "total_hours_available": 196.0,
  "total_days_available": 24.5,
  "breakdown": {
    "ferie": {
      "accrued_hours": 176.0, "used_hours": 64.0, "available_hours": 112.0, "available_days": 14.0
    },
    "rol": {
      "accrued_hours": 32.0, "used_hours": 12.0, "available_hours": 20.0, "available_days": 2.5
    },
    "permessi": {
      "accrued_hours": 104.0, "used_hours": 40.0, "available_hours": 64.0, "available_days": 8.0
    }
  }
}
```

---

### GET `/vacation/calendar/{year}/{month}`

Restituisce il calendario mensile con entry, festività nazionali e custom evidenziate.

---

### GET `/vacation/holidays/{year}`

Lista festività nazionali italiane per anno (include Pasqua e Pasquetta calcolati dinamicamente).

---

### GET `/vacation/bridges/{year}`

Calcola le opportunità di ponte ottimali per l'anno.

---

### GET `/vacation/user-holidays`

Lista festività custom dell'utente (patrono locale, chiusure aziendali).

---

### POST `/vacation/user-holidays`

Aggiunge una festività custom. Supporta ricorrenza annuale.

**Request:**
```json
{
  "name": "Patrono locale",
  "month": 12,
  "day": 7,
  "recurring": true
}
```

---

### DELETE `/vacation/user-holidays/{holiday_id}`

Rimuove una festività custom.

---

## 💹 Endpoints - Budget Planning

> Modulo per la creazione e il monitoraggio di budget mensili per sotto-categoria, con calcolo spesa real-time e indicatori visivi. **Implementato in Fase 3.9.**

### GET `/budgets`

Lista budget dell'utente con filtri.

**Query Parameters:**
- `is_active` (bool): Filtra per budget attivi/inattivi
- `category_id` (uuid): Filtra per categoria

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "category_id": "uuid",
    "category_name": "Ristoranti",
    "amount": 200.00,
    "period": "monthly",
    "is_active": true,
    "start_date": "2026-01-01"
  }
]
```

---

### GET `/budgets/summary`

Dashboard principale budget: lista tutti i budget attivi con spesa corrente del mese, percentuale utilizzo e indicatore status.

**Response:** `200 OK`
```json
{
  "budgets": [
    {
      "id": "uuid",
      "category_name": "Ristoranti",
      "amount": 200.00,
      "spent": 150.00,
      "remaining": 50.00,
      "percentage": 75.0,
      "status": "warning",
      "indicator": "🟡"
    }
  ],
  "totals": {
    "total_budgeted": 700.00,
    "total_spent": 605.00,
    "total_remaining": 95.00,
    "overall_percentage": 86.4
  }
}
```

**Status indicators:** `🟢` <70% · `🟡` 70–90% · `🔴` 90–100% · `🚨` >100% · `⚠️` budget orfano

---

### GET `/budgets/{budget_id}`

Dettaglio singolo budget con spending data.

---

### POST `/budgets`

Crea un nuovo budget mensile per una sotto-categoria.

**Request:**
```json
{
  "category_id": "uuid",
  "amount": 200.00,
  "period": "monthly"
}
```

**Validations:**
- Solo categorie `expense` accettate
- Un solo budget attivo per categoria (constraint unicità)
- `amount` > 0

**Errors:**
- `400`: Budget già esistente per questa categoria, o categoria non expense

---

### PUT `/budgets/{budget_id}`

Modifica un budget esistente (amount, is_active).

---

### DELETE `/budgets/{budget_id}`

Elimina un budget. Budget orfani (categoria eliminata) vengono gestiti con `category_id: null`.

---

## 📥 Endpoints - CSV Import

> Importazione massiva di transazioni da file CSV con preview interattiva, fuzzy matching categorie e rilevamento duplicati. **Implementato in Fase 3.10.**

### GET `/csv-import/template`

Scarica il template CSV standard.

**Response:** File `template_transazioni.csv`

**Formato CSV:**
```csv
date,description,amount,category_name,notes
2026-01-15,Spesa Supermercato,-45.50,Spesa,Settimanale
2026-01-16,Stipendio,2500.00,Stipendio,Gennaio 2026
```

---

### POST `/csv-import/preview`

Carica un file CSV e restituisce la preview con validazione riga per riga.

**Request:** `multipart/form-data` con file CSV (max 1000 righe, UTF-8)

**Response:** `200 OK`
```json
{
  "total_rows": 50,
  "valid": 45,
  "warnings": 3,
  "errors": 1,
  "duplicates": 1,
  "rows": [
    {
      "row_number": 1,
      "status": "valid",
      "date": "2026-01-15",
      "description": "Spesa",
      "amount": -45.50,
      "category_name": "Spesa",
      "category_suggestion": null
    },
    {
      "row_number": 2,
      "status": "warning",
      "category_suggestion": "Ristorazione"
    }
  ]
}
```

**Row status:** `valid` 🟢 · `warning` 🟡 · `error` 🔴 · `duplicate` 🟣

---

### POST `/csv-import/confirm`

Conferma e importa le righe selezionate dalla preview.

**Request:**
```json
{
  "account_id": "uuid",
  "row_numbers": [1, 2, 3, 45]
}
```

---

## ❌ Error Responses

### Standard Error Format

```json
{
  "detail": "Error message describing what went wrong"
}
```

### HTTP Status Codes

| Code | Meaning | Usage |
|------|---------|-------|
| 200 | OK | Successful GET/PUT |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Invalid data |
| 401 | Unauthorized | Invalid/missing token |
| 403 | Forbidden | Valid token, no permission |
| 404 | Not Found | Resource doesn't exist |
| 422 | Unprocessable Entity | Validation errors |
| 500 | Internal Server Error | Server error |

### Example Validation Error

```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error.email"
    }
  ]
}
```

---

## ⏱️ Rate Limiting

### Limits (da implementare)

- **Anonymous**: 10 requests/minute
- **Authenticated**: 100 requests/minute
- **Burst**: 20 requests/second

### Headers

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1637000000
```

---

## 🧪 Testing API

### Swagger UI

Documentazione interattiva: **http://localhost:8000/docs**

### Postman Collection

(da creare)

### cURL Examples

**Register:**
```bash
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"Test1234"}'
```

**Get Accounts:**
```bash
TOKEN="your_jwt_token_here"

curl -X GET http://localhost:8000/api/v1/accounts \
  -H "Authorization: Bearer $TOKEN"
```

---

**Documento creato:** Novembre 2025
**Ultima modifica:** Marzo 2026
**Versione:** 2.0
**Formato:** JSON  
**Authentication:** JWT Bearer Token
