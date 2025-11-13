# 🛠️ Development Guide - Budget App

**Guida rapida con tutti i comandi necessari per sviluppare Budget App**

---

## 📋 Indice Rapido

- [Setup Iniziale](#-setup-iniziale)
- [Comandi Quotidiani](#-comandi-quotidiani)
- [Backend Commands](#-backend-commands)
- [Frontend Commands](#-frontend-commands)
- [Database Commands](#-database-commands)
- [Docker Commands](#-docker-commands)
- [Git Commands](#-git-commands)
- [Testing Commands](#-testing-commands)
- [Troubleshooting](#-troubleshooting)

---

## 🚀 Setup Iniziale

### Prima Volta (One-Time Setup)

```bash
# 1. Clone repository
git clone https://github.com/TUO-USERNAME/budget-app-saas.git
cd budget-app-saas

# 2. Setup Backend
cd backend
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
pip install --upgrade pip
pip install -r requirements.txt

# 3. Crea file .env (copia da .env.example e compila)
cp .env.example .env
# Apri .env e inserisci le tue credenziali database

# 4. Test connessione database
python test_db_connection.py

# 5. Setup Frontend
cd ../frontend
npm install

# 6. Crea .env frontend
echo "VITE_API_URL=http://localhost:8000/api/v1" > .env
```

---

## ⚡ Comandi Quotidiani

### Avvia Tutto (Development)

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate
python run.py
```
✅ Backend disponibile su: http://localhost:8000  
✅ API Docs: http://localhost:8000/docs

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```
✅ Frontend disponibile su: http://localhost:5173

### Ferma Tutto

- Backend: `Ctrl + C` nel terminal 1
- Frontend: `Ctrl + C` nel terminal 2

---

## 🐍 Backend Commands

### Attiva Virtual Environment

```bash
cd backend
source venv/bin/activate  # macOS/Linux
# Windows: venv\Scripts\activate
```

Dovresti vedere `(venv)` nel prompt.

### Disattiva Virtual Environment

```bash
deactivate
```

### Installa Nuova Dipendenza

```bash
# Con venv attivo
pip install nome-package

# Aggiorna requirements.txt
pip freeze > requirements.txt
```

### Avvia Server Development

```bash
# Metodo 1 (consigliato)
python run.py

# Metodo 2 (diretto)
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Verifica Installazioni

```bash
# Python version
python --version

# Pip version
pip --version

# Lista packages installati
pip list

# Verifica FastAPI
python -c "import fastapi; print(f'FastAPI {fastapi.__version__}')"
```

### Formatta Codice (Black)

```bash
# Formatta tutto
black .

# Formatta singolo file
black app/main.py

# Check senza modificare
black --check .
```

### Linting (Flake8)

```bash
# Check tutto il codice
flake8 .

# Check singolo file
flake8 app/main.py
```

### Type Checking (MyPy)

```bash
# Check types
mypy app/
```

---

## ⚛️ Frontend Commands

### Installa Dipendenze

```bash
cd frontend
npm install
```

### Avvia Development Server

```bash
npm run dev
```

Server su: http://localhost:5173

### Build per Production

```bash
npm run build
```

Output in: `dist/`

### Preview Build

```bash
npm run preview
```

### Installa Nuova Libreria

```bash
npm install nome-libreria

# Con versione specifica
npm install nome-libreria@1.2.3

# Dev dependency
npm install -D nome-libreria
```

### Rimuovi Libreria

```bash
npm uninstall nome-libreria
```

### Pulisci e Reinstalla

```bash
rm -rf node_modules package-lock.json
npm install
```

---

## 🗄️ Database Commands

### Connessione Database (pgAdmin 4)

1. Apri **pgAdmin 4**
2. Connetti a **PostgreSQL 16**
3. Password: (la tua password PostgreSQL)
4. Naviga a: Databases → budget_app_dev

### SQL Queries in pgAdmin

1. Click destro su `budget_app_dev`
2. **Query Tool**
3. Scrivi/incolla SQL
4. Click **Execute** (⚡️ icona) o `F5`

### Query Utili

```sql
-- Vedi tutte le tabelle
SELECT table_name FROM information_schema.tables 
WHERE table_schema = 'public';

-- Conta utenti
SELECT COUNT(*) FROM users;

-- Vedi tutti gli account
SELECT * FROM accounts;

-- Vedi transazioni recenti
SELECT * FROM transactions 
ORDER BY date DESC 
LIMIT 10;

-- Totale balance tutti gli account
SELECT SUM(balance) as total_balance FROM accounts;

-- Reset sequence (se necessario)
ALTER SEQUENCE users_id_seq RESTART WITH 1;
```

### Backup Database

**In pgAdmin:**
1. Click destro su `budget_app_dev`
2. **Backup...**
3. Scegli percorso e formato (Custom o Plain)
4. Click **Backup**

**Da terminale:**
```bash
pg_dump -U budget_user -d budget_app_dev > backup_$(date +%Y%m%d).sql
```

### Restore Database

**In pgAdmin:**
1. Click destro su `budget_app_dev`
2. **Restore...**
3. Scegli file backup
4. Click **Restore**

**Da terminale:**
```bash
psql -U budget_user -d budget_app_dev < backup.sql
```

### Reset Database (⚠️ ATTENZIONE!)

```bash
# Usando script Python (quando disponibile)
cd backend
source venv/bin/activate
python reset_db.py
```

---

## 🔄 Database Migrations (Alembic)

### Verifica Configurazione

```bash
cd backend
source venv/bin/activate
alembic current
```

### Crea Nuova Migration (Auto-generate)

```bash
# Dopo aver modificato i models
alembic revision --autogenerate -m "Descrizione modifiche"

# Esempio
alembic revision --autogenerate -m "Add email_verified field to users"
```

### Applica Migrations

```bash
# Applica tutte le migrations pending
alembic upgrade head

# Applica una migration specifica
alembic upgrade +1  # Avanti di 1
```

### Rollback Migration

```bash
# Torna indietro di 1 migration
alembic downgrade -1

# Torna a migration specifica
alembic downgrade <revision_id>

# Torna all'inizio
alembic downgrade base
```

### Vedi Storia Migrations

```bash
# Lista tutte le migrations
alembic history

# Vedi dettagli migration corrente
alembic current --verbose
```

### Merge Migrations (conflitti)

```bash
alembic merge <rev1> <rev2> -m "Merge branches"
```

---

## 🐳 Docker Commands

### Build e Avvia

```bash
# Avvia tutti i servizi (database + backend)
docker-compose up -d

# Avvia mostrando logs
docker-compose up

# Rebuild e avvia
docker-compose up --build
```

### Ferma Servizi

```bash
# Ferma senza rimuovere
docker-compose stop

# Ferma e rimuovi container
docker-compose down

# Ferma e rimuovi tutto (inclusi volumi - ⚠️ elimina database!)
docker-compose down -v
```

### Vedi Status

```bash
# Lista servizi attivi
docker-compose ps

# Vedi logs
docker-compose logs -f

# Logs specifico servizio
docker-compose logs -f backend
docker-compose logs -f db
```

### Accedi ai Container

```bash
# Shell backend
docker-compose exec backend bash

# Shell database
docker-compose exec db bash

# Accedi a PostgreSQL
docker-compose exec db psql -U budget_user -d budget_app_dev
```

### Esegui Comandi in Container

```bash
# Run migrations
docker-compose exec backend alembic upgrade head

# Run tests
docker-compose exec backend pytest

# Test connessione DB
docker-compose exec backend python test_db_connection.py
```

### Rebuild Container Specifico

```bash
# Rebuild solo backend
docker-compose build backend

# Rebuild senza cache
docker-compose build --no-cache backend
```

### Pulisci Docker

```bash
# Rimuovi container non usati
docker container prune

# Rimuovi immagini non usate
docker image prune

# Rimuovi volumi non usati (⚠️ attenzione!)
docker volume prune

# Pulizia completa
docker system prune -a
```

---

## 📦 Git Commands

### Status e Info

```bash
# Vedi stato repository
git status

# Vedi log commits
git log --oneline

# Vedi differenze
git diff
```

### Workflow Standard

```bash
# 1. Pull ultime modifiche
git pull origin main

# 2. Crea branch per feature
git checkout -b feature/nome-feature

# 3. Lavora e commit
git add .
git commit -m "Descrizione modifiche"

# 4. Push branch
git push origin feature/nome-feature

# 5. Crea Pull Request su GitHub
```

### Comandi Utili

```bash
# Aggiungi file specifico
git add path/to/file.py

# Commit con messaggio dettagliato
git commit -m "Title" -m "Description"

# Ammend ultimo commit
git commit --amend

# Vedi branch
git branch -a

# Cambia branch
git checkout nome-branch

# Elimina branch locale
git branch -d nome-branch

# Stash modifiche temporanee
git stash
git stash pop
```

### Undo Changes

```bash
# Scarta modifiche file non staged
git checkout -- path/to/file

# Reset ultimo commit (mantieni file)
git reset HEAD~1

# Reset hard (⚠️ perdi modifiche!)
git reset --hard HEAD~1
```

---

## 🧪 Testing Commands

### Backend Tests (Pytest)

```bash
cd backend
source venv/bin/activate

# Run tutti i test
pytest

# Run con verbose
pytest -v

# Run specifico file
pytest tests/test_auth.py

# Run specifico test
pytest tests/test_auth.py::test_register_user

# Run con coverage
pytest --cov=app --cov-report=html

# Apri coverage report
open htmlcov/index.html  # macOS
```

### Frontend Tests (quando implementati)

```bash
cd frontend

# Run tests
npm test

# Run con coverage
npm test -- --coverage
```

### API Testing (Manual)

**Usando Swagger UI:**
1. Avvia backend
2. Apri http://localhost:8000/docs
3. Click "Try it out" su endpoint
4. Compila parametri
5. Click "Execute"

**Usando cURL:**
```bash
# Register
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"Test1234"}'

# Login
TOKEN=$(curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"Test1234"}' \
  | jq -r '.access_token')

# Get accounts
curl -X GET http://localhost:8000/api/v1/accounts \
  -H "Authorization: Bearer $TOKEN"
```

---

## 🔧 Troubleshooting

### Port Already in Use

**Problema:** `Address already in use`

**Soluzione:**
```bash
# Trova processo su porta 8000
lsof -ti:8000

# Uccidi processo
kill -9 $(lsof -ti:8000)
```

### Python Module Not Found

**Problema:** `ModuleNotFoundError: No module named 'fastapi'`

**Soluzione:**
```bash
cd backend
source venv/bin/activate  # Assicurati venv sia attivo!
pip install -r requirements.txt
```

### Database Connection Refused

**Problema:** `Connection refused` o `could not connect to server`

**Soluzione:**
```bash
# 1. Verifica PostgreSQL sia in esecuzione
# Apri pgAdmin 4 e controlla connessione

# 2. Verifica credenziali in .env
cat backend/.env

# 3. Test connessione
cd backend
source venv/bin/activate
python test_db_connection.py
```

### Docker Port Conflict

**Problema:** `port is already allocated`

**Soluzione:**
```bash
# Ferma PostgreSQL locale se in conflitto con Docker
brew services stop postgresql

# Oppure cambia porta in docker-compose.yml
# ports: "5433:5432"  # Usa 5433 invece di 5432
```

### Permission Denied (macOS)

**Problema:** `Permission denied` durante installazioni

**Soluzione:**
```bash
# Non usare sudo con pip!
# Usa virtual environment:
cd backend
python3 -m venv venv
source venv/bin/activate
pip install ...
```

### Git Push Rejected

**Problema:** `Updates were rejected`

**Soluzione:**
```bash
# Pull prima di push
git pull origin main --rebase
git push origin main
```

### npm ERR!

**Problema:** Errori durante `npm install`

**Soluzione:**
```bash
cd frontend

# Pulisci cache
npm cache clean --force

# Rimuovi e reinstalla
rm -rf node_modules package-lock.json
npm install
```

---

## 🔍 Comandi Debug Utili

### Verifica Versioni

```bash
# Python
python --version

# Node.js
node --version
npm --version

# PostgreSQL
psql --version

# Docker
docker --version
docker-compose --version

# Git
git --version
```

### Verifica Porte

```bash
# Vedi processi su porte
lsof -i :8000  # Backend
lsof -i :5173  # Frontend
lsof -i :5432  # Database
```

### Vedi Variabili Ambiente

```bash
# Backend
cd backend
cat .env

# Frontend
cd frontend
cat .env
```

### Test Singoli Componenti

```bash
# Test database
cd backend
source venv/bin/activate
python test_db_connection.py

# Test imports Python
python -c "import fastapi, sqlalchemy, alembic; print('OK')"

# Test API manualmente
curl http://localhost:8000/
```

---

## 📚 Quick Links

**Local:**
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Frontend: http://localhost:5173

**Documentazione:**
- [Roadmap](../roadmap.md)
- [Architecture](./ARCHITECTURE.md)
- [API Specs](./API_SPEC.md)
- [Docker Guide](./DOCKER.md)

**External:**
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [React Docs](https://react.dev/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

---

## 💡 Tips & Best Practices

### Development

✅ **DO:**
- Attiva sempre venv prima di lavorare sul backend
- Fai commit frequenti con messaggi descrittivi
- Testa localmente prima di push
- Usa branches per features
- Aggiorna requirements.txt quando installi librerie

❌ **DON'T:**
- Non committare file .env
- Non pushare node_modules o venv
- Non lavorare direttamente su main
- Non usare sudo con pip

### Workflow Consigliato

1. **Mattina:** Pull ultime modifiche
2. **Sviluppo:** Lavora su feature branch
3. **Test:** Verifica tutto funzioni
4. **Commit:** Salva progressi
5. **Sera:** Push e crea PR se feature completa

---

**Guida creata:** Novembre 2025  
**Ultima modifica:** Novembre 2025  
**Versione:** 1.0

**Suggerimenti? Apri una issue su GitHub!**
