# 🗄️ Database Schema Design - Budget App

**Documento:** Design Schema Database  
**Database:** PostgreSQL 16  
**Versione:** 1.0  
**Data:** Novembre 2025

---

## 📋 Panoramica Tabelle

Budget App utilizza **6 tabelle principali** con relazioni chiare e vincoli di integrità.

```
users (1) ─────┬──────> (N) accounts
               ├──────> (N) categories
               ├──────> (N) transactions
               ├──────> (N) transfers
               └──────> (N) custom_charts

accounts (1) ──────> (N) transactions
categories (1) ────> (N) transactions
accounts (1) ──┬───> (N) transfers (from)
               └───> (N) transfers (to)
```

---

## 🔐 Tabella: users

**Descrizione:** Gestisce gli utenti dell'applicazione.

### Colonne

| Nome | Tipo | Constraints | Descrizione |
|------|------|-------------|-------------|
| id | UUID | PK | Identificatore univoco |
| email | VARCHAR(255) | UNIQUE, NOT NULL | Email utente |
| password_hash | VARCHAR(255) | NOT NULL | Password hashata (bcrypt) |
| full_name | VARCHAR(255) | NULL | Nome completo |
| is_active | BOOLEAN | DEFAULT TRUE | Account attivo |
| created_at | TIMESTAMP | DEFAULT NOW() | Data registrazione |
| updated_at | TIMESTAMP | DEFAULT NOW() | Ultimo aggiornamento |
| last_login | TIMESTAMP | NULL | Ultimo accesso |

### Indici

- **PK:** id
- **UNIQUE:** email

### Note

- Password **mai** in chiaro, solo hash bcrypt
- `is_active` per soft delete
- `last_login` aggiornato ad ogni login

---

## 💰 Tabella: accounts

**Descrizione:** Conti bancari, portafogli, carte di credito dell'utente.

### Colonne

| Nome | Tipo | Constraints | Descrizione |
|------|------|-------------|-------------|
| id | UUID | PK | Identificatore univoco |
| user_id | UUID | FK → users.id, NOT NULL | Proprietario account |
| name | VARCHAR(100) | NOT NULL | Nome account |
| account_type | ENUM | NOT NULL | Tipo account |
| balance | NUMERIC(12,2) | DEFAULT 0.00 | Saldo corrente |
| currency | VARCHAR(3) | DEFAULT 'EUR' | Valuta (ISO 4217) |
| color | VARCHAR(7) | NULL | Colore HEX (#RRGGBB) |
| icon | VARCHAR(50) | NULL | Emoji/icona |
| is_active | BOOLEAN | DEFAULT TRUE | Account attivo |
| created_at | TIMESTAMP | DEFAULT NOW() | Data creazione |
| updated_at | TIMESTAMP | DEFAULT NOW() | Ultimo aggiornamento |

### ENUM: account_type

- `checking` - Conto corrente
- `savings` - Risparmio
- `credit` - Carta di credito
- `cash` - Contanti
- `investment` - Investimenti

### Constraints

- **CHECK:** `balance >= 0` (nessun saldo negativo)
- **CASCADE:** DELETE user → DELETE accounts

### Indici

- **PK:** id
- **INDEX:** user_id
- **INDEX:** is_active

### Note

- `balance` aggiornato automaticamente dalle transactions
- `color` e `icon` per personalizzazione UI

---

## 📂 Tabella: categories

**Descrizione:** Categorie per classificare transazioni (income/expense).

### Colonne

| Nome | Tipo | Constraints | Descrizione |
|------|------|-------------|-------------|
| id | UUID | PK | Identificatore univoco |
| user_id | UUID | FK → users.id, NOT NULL | Proprietario categoria |
| name | VARCHAR(100) | NOT NULL | Nome categoria |
| type | ENUM | NOT NULL | income o expense |
| parent_category_id | UUID | FK → categories.id, NULL | Categoria padre (sottocategorie) |
| color | VARCHAR(7) | NULL | Colore HEX |
| icon | VARCHAR(50) | NULL | Emoji/icona |
| is_system | BOOLEAN | DEFAULT FALSE | Categoria predefinita |
| created_at | TIMESTAMP | DEFAULT NOW() | Data creazione |

### ENUM: transaction_type

- `income` - Entrata
- `expense` - Uscita

### Constraints

- **CASCADE:** DELETE user → DELETE categories
- **SET NULL:** DELETE category → SET NULL parent_category_id

### Indici

- **PK:** id
- **INDEX:** user_id
- **INDEX:** type

### Note

- `is_system = TRUE` per categorie predefinite (non eliminabili)
- Supporto sottocategorie tramite `parent_category_id`

---

## 💸 Tabella: transactions

**Descrizione:** Movimenti finanziari (entrate e uscite).

### Colonne

| Nome | Tipo | Constraints | Descrizione |
|------|------|-------------|-------------|
| id | UUID | PK | Identificatore univoco |
| user_id | UUID | FK → users.id, NOT NULL | Proprietario |
| account_id | UUID | FK → accounts.id, NOT NULL | Account coinvolto |
| category_id | UUID | FK → categories.id, NOT NULL | Categoria |
| amount | NUMERIC(12,2) | NOT NULL | Importo |
| type | ENUM | NOT NULL | income o expense |
| date | DATE | NOT NULL | Data transazione |
| description | VARCHAR(255) | NULL | Descrizione breve |
| notes | TEXT | NULL | Note dettagliate |
| tags | TEXT[] | NULL | Tag per ricerca |
| created_at | TIMESTAMP | DEFAULT NOW() | Data inserimento |
| updated_at | TIMESTAMP | DEFAULT NOW() | Ultimo aggiornamento |

### Constraints

- **CHECK:** `amount > 0`
- **CASCADE:** DELETE user → DELETE transactions
- **CASCADE:** DELETE account → DELETE transactions
- **RESTRICT:** DELETE category (blocca se ci sono transactions)

### Indici

- **PK:** id
- **INDEX:** user_id
- **INDEX:** account_id
- **INDEX:** category_id
- **INDEX:** date DESC (per query recenti)
- **COMPOSITE INDEX:** (user_id, date DESC)

### Note

- `type` duplicato per query veloci (già in category)
- `tags` array PostgreSQL per flessibilità
- `date` separato da `created_at` per backdating

---

## 🔄 Tabella: transfers

**Descrizione:** Trasferimenti tra account dello stesso utente.

### Colonne

| Nome | Tipo | Constraints | Descrizione |
|------|------|-------------|-------------|
| id | UUID | PK | Identificatore univoco |
| user_id | UUID | FK → users.id, NOT NULL | Proprietario |
| from_account_id | UUID | FK → accounts.id, NOT NULL | Account origine |
| to_account_id | UUID | FK → accounts.id, NOT NULL | Account destinazione |
| amount | NUMERIC(12,2) | NOT NULL | Importo |
| date | DATE | NOT NULL | Data trasferimento |
| description | VARCHAR(255) | NULL | Descrizione |
| created_at | TIMESTAMP | DEFAULT NOW() | Data inserimento |

### Constraints

- **CHECK:** `amount > 0`
- **CHECK:** `from_account_id != to_account_id`
- **CASCADE:** DELETE user → DELETE transfers
- **CASCADE:** DELETE account → DELETE transfers

### Indici

- **PK:** id
- **INDEX:** user_id
- **INDEX:** date DESC

### Note

- Aggiorna automaticamente balance di **entrambi** gli account
- NO categorie (è un movimento interno)

---

## 📊 Tabella: custom_charts

**Descrizione:** Configurazioni grafici personalizzati salvati dall'utente.

### Colonne

| Nome | Tipo | Constraints | Descrizione |
|------|------|-------------|-------------|
| id | UUID | PK | Identificatore univoco |
| user_id | UUID | FK → users.id, NOT NULL | Proprietario |
| name | VARCHAR(100) | NOT NULL | Nome grafico |
| chart_type | ENUM | NOT NULL | Tipo visualizzazione |
| config | JSONB | NOT NULL | Configurazione completa |
| filters | JSONB | NULL | Filtri applicati |
| created_at | TIMESTAMP | DEFAULT NOW() | Data creazione |
| updated_at | TIMESTAMP | DEFAULT NOW() | Ultimo aggiornamento |

### ENUM: chart_type

- `line` - Grafico a linee
- `bar` - Grafico a barre
- `pie` - Grafico a torta
- `area` - Grafico ad area

### Constraints

- **CASCADE:** DELETE user → DELETE custom_charts

### Indici

- **PK:** id
- **INDEX:** user_id

### Note

- `config` JSONB per massima flessibilità
- Memorizza axes, datasets, colors, etc.

---

## 🔗 Relazioni Tra Tabelle

### One-to-Many

```sql
users (1) ──────> (N) accounts
users (1) ──────> (N) categories
users (1) ──────> (N) transactions
users (1) ──────> (N) transfers
users (1) ──────> (N) custom_charts

accounts (1) ────> (N) transactions
categories (1) ──> (N) transactions

accounts (1) ────┬> (N) transfers (from)
                 └> (N) transfers (to)
```

### Self-Referential

```sql
categories (1) ──> (N) categories (parent_category_id)
```

---

## 🔒 Sicurezza & Isolamento Dati

### Row-Level Security

Ogni query **DEVE** filtrare per `user_id`:

```sql
-- ✅ CORRETTO
SELECT * FROM accounts WHERE user_id = 'current-user-uuid';

-- ❌ SBAGLIATO (vede dati di tutti!)
SELECT * FROM accounts;
```

### Foreign Keys

Tutti i FK con `ON DELETE CASCADE` per `user_id`:
- Elimina user → elimina automaticamente tutti i suoi dati
- Integrità referenziale garantita

### Constraints

- CHECK per validazione dati
- UNIQUE per unicità
- NOT NULL per campi obbligatori

---

## 📈 Performance

### Indici Strategici

```sql
-- Query più frequenti
CREATE INDEX idx_transactions_user_date ON transactions(user_id, date DESC);
CREATE INDEX idx_accounts_user_active ON accounts(user_id, is_active);
CREATE INDEX idx_categories_user_type ON categories(user_id, type);
```

### Partitioning (Futuro)

Per milioni di transactions:
```sql
-- Partition by year
CREATE TABLE transactions_2025 PARTITION OF transactions
FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');
```

---

## 🔮 Future Enhancements

### Da Implementare

- [ ] **Recurring Transactions**: Tabella `recurring_transactions`
- [ ] **Budgets**: Tabella `budgets` (per categoria/mese)
- [ ] **Bills**: Tabella `bills` (scadenze bollette)
- [ ] **Savings Goals**: Tabella `savings_goals`
- [ ] **Shared Accounts**: Tabella `account_shares` (multi-user)
- [ ] **Attachments**: Tabella `attachments` (scontrini, PDF)
- [ ] **Audit Log**: Tabella `audit_log` (tracking modifiche)

---

## 📊 Esempio Dati

### User
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "email": "giovanni@example.com",
  "full_name": "Giovanni Mezzasalma",
  "is_active": true
}
```

### Account
```json
{
  "id": "223e4567-e89b-12d3-a456-426614174000",
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "Conto Corrente Intesa",
  "account_type": "checking",
  "balance": 1500.50,
  "currency": "EUR",
  "color": "#3B82F6",
  "icon": "💳"
}
```

### Transaction
```json
{
  "id": "323e4567-e89b-12d3-a456-426614174000",
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "account_id": "223e4567-e89b-12d3-a456-426614174000",
  "category_id": "423e4567-e89b-12d3-a456-426614174000",
  "amount": 50.00,
  "type": "expense",
  "date": "2025-11-15",
  "description": "Spesa settimanale",
  "tags": ["alimentari", "supermercato"]
}
```

---

**Documento creato:** Novembre 2025  
**Database:** PostgreSQL 16  
**Versione Schema:** 1.0
