# 🐳 Docker Setup Guide - Budget App

Questa guida spiega come usare Docker per sviluppo e deployment dell'applicazione Budget App.

---

## 📋 Prerequisiti

- **Docker Desktop** installato e in esecuzione
- **Docker Compose** (incluso in Docker Desktop)

Verifica installazione:
```bash
docker --version
docker-compose --version
```

---

## 🚀 Quick Start

### 1. Avvia Tutti i Servizi

Dalla root del progetto:

```bash
docker-compose up -d
```

Questo avvierà:
- **PostgreSQL database** su `localhost:5432`
- **Backend API** su `localhost:8000`

**Opzioni utili:**
```bash
# Avvia e mostra logs in tempo reale
docker-compose up

# Avvia in background
docker-compose up -d

# Ricompila le immagini prima di avviare
docker-compose up --build
```

### 2. Verifica Stato Servizi

```bash
docker-compose ps
```

Output atteso:
```
NAME                    STATUS              PORTS
budget_app_backend      Up 30 seconds       0.0.0.0:8000->8000/tcp
budget_app_db           Up 30 seconds       0.0.0.0:5432->5432/tcp
```

### 3. Testa API

Apri browser: **http://localhost:8000/docs**

Dovresti vedere Swagger UI con la documentazione API.

### 4. Ferma Servizi

```bash
# Ferma senza rimuovere container
docker-compose stop

# Ferma e rimuovi container
docker-compose down

# Ferma, rimuovi container E volumi (⚠️ elimina database!)
docker-compose down -v
```

---

## 📊 Comandi Utili

### Logs

```bash
# Tutti i servizi
docker-compose logs -f

# Solo backend
docker-compose logs -f backend

# Solo database
docker-compose logs -f db

# Ultimi 100 log
docker-compose logs --tail=100
```

### Accesso Container

```bash
# Shell nel container backend
docker-compose exec backend bash

# Shell nel database
docker-compose exec db psql -U budget_user -d budget_app_dev

# Esegui comando nel backend
docker-compose exec backend python test_db_connection.py
```

### Database Management

```bash
# Backup database
docker-compose exec db pg_dump -U budget_user budget_app_dev > backup.sql

# Restore database
docker-compose exec -T db psql -U budget_user budget_app_dev < backup.sql

# Reset database (⚠️ elimina tutti i dati!)
docker-compose down -v
docker-compose up -d
```

### Rebuild

```bash
# Rebuild solo backend
docker-compose build backend

# Rebuild tutto
docker-compose build

# Rebuild forzato (no cache)
docker-compose build --no-cache
```

---

## 🔧 Configurazione

### Environment Variables

Le variabili d'ambiente sono definite in **`docker-compose.yml`**.

Per override, crea file **`.env.docker`**:

```env
# .env.docker
POSTGRES_PASSWORD=my_secure_password
SECRET_KEY=my_super_secret_jwt_key
```

Poi usa:
```bash
docker-compose --env-file .env.docker up
```

### Ports

Di default:
- **Database**: `5432` → `localhost:5432`
- **Backend API**: `8000` → `localhost:8000`

Per cambiare, modifica `docker-compose.yml`:
```yaml
ports:
  - "8080:8000"  # Backend ora su localhost:8080
```

---

## 🧪 Development Workflow

### Hot Reload

Il backend usa **volume mounting** per hot reload:
```yaml
volumes:
  - ./backend:/app
```

Modifiche al codice Python → Auto-reload immediato! 🔥

### Database Migrations

```bash
# Genera migration
docker-compose exec backend alembic revision --autogenerate -m "Description"

# Applica migrations
docker-compose exec backend alembic upgrade head

# Rollback
docker-compose exec backend alembic downgrade -1
```

### Testing

```bash
# Run tests
docker-compose exec backend pytest tests/ -v

# Con coverage
docker-compose exec backend pytest tests/ --cov=app
```

---

## 🚢 Production Deployment

### Build Production Image

```bash
# Build ottimizzata per production
docker build -t budget-app-backend:latest ./backend

# Tag per registry
docker tag budget-app-backend:latest your-registry.com/budget-app:v1.0.0

# Push to registry
docker push your-registry.com/budget-app:v1.0.0
```

### Production Environment

⚠️ **NON usare** `docker-compose.yml` in production!

Usa invece:
- **Kubernetes** per orchestrazione
- **Railway/Render** per hosting managed
- **AWS ECS/Fargate** per AWS
- **Google Cloud Run** per GCP

---

## 🐛 Troubleshooting

### Container non si avvia

```bash
# Vedi logs errore
docker-compose logs backend

# Rebuild forzato
docker-compose down
docker-compose build --no-cache
docker-compose up
```

### Database connection refused

1. Verifica database sia healthy:
   ```bash
   docker-compose ps
   ```
2. Attendi health check (10-15 secondi primo avvio)
3. Verifica credenziali in `docker-compose.yml`

### Port già in uso

Errore: `Bind for 0.0.0.0:5432 failed: port is already allocated`

**Soluzione:**
- Ferma PostgreSQL locale: `brew services stop postgresql`
- Oppure cambia porta in `docker-compose.yml`

### Volumi persistenti

Se vuoi ricominciare da zero:
```bash
docker-compose down -v  # ⚠️ Elimina database!
docker volume prune
docker-compose up
```

---

## 📚 Riferimenti

- [Docker Docs](https://docs.docker.com/)
- [Docker Compose Docs](https://docs.docker.com/compose/)
- [FastAPI Docker](https://fastapi.tiangolo.com/deployment/docker/)
- [PostgreSQL Docker](https://hub.docker.com/_/postgres)

---

## ✅ Checklist Deploy

Quando usi Docker per la prima volta:

- [ ] Docker Desktop installato e in esecuzione
- [ ] File `docker-compose.yml` configurato
- [ ] File `Dockerfile` in `backend/`
- [ ] File `.dockerignore` in `backend/`
- [ ] Run `docker-compose up -d`
- [ ] Verifica `docker-compose ps` (tutti UP)
- [ ] Test API: http://localhost:8000/docs
- [ ] Run migrations: `docker-compose exec backend alembic upgrade head`

**🎉 You're all set!**

---

*Guida creata: Novembre 2025*  
*Per domande: consulta la documentazione Docker ufficiale*
