"""
FastAPI Main Application
Entry point dell'API Budget App
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import settings
from app.database import engine, Base
from app.routers.auth import router as auth_router
from app.routers.accounts import router as accounts_router
from app.routers.categories import router as categories_router  # AGGIUNGI QUESTA

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gestisce eventi startup e shutdown dell'applicazione.
    """
    # Startup
    print("🚀 Starting Budget App API...")
    print(f"📊 Database: {settings.DATABASE_URL.split('@')[-1]}")  # Mostra solo host/db, non password
    print(f"🔒 Debug mode: {settings.DEBUG}")
    
    # In development, crea tabelle se non esistono
    if settings.DEBUG:
        print("⚠️  DEBUG MODE: Auto-creating tables if not exist...")
        Base.metadata.create_all(bind=engine)
    
    yield
    
    # Shutdown
    print("👋 Shutting down Budget App API...")


# Inizializza FastAPI app
app = FastAPI(
    title="Budget App API",
    description="""
    API per gestione budget personali multi-utente.
    
    ## Features
    
    * **Authentication** - Registrazione, login, JWT tokens
    * **Accounts** - Gestione conti bancari e portafogli
    * **Categories** - Categorizzazione transazioni
    * **Transactions** - Tracking entrate e uscite
    * **Transfers** - Trasferimenti tra account
    * **Analytics** - Statistiche e report
    
    ## Authentication
    
    Usa il pulsante **Authorize** per fare login con email e password.
    Il token JWT verrà automaticamente incluso in tutte le richieste successive.
    """,
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix=settings.API_V1_PREFIX)
app.include_router(accounts_router, prefix=settings.API_V1_PREFIX)
app.include_router(categories_router, prefix=settings.API_V1_PREFIX)

# Health check endpoints
@app.get("/", tags=["Health"])
async def root():
    """
    Root endpoint - verifica che l'API sia attiva.
    """
    return {
        "message": "Budget App API is running",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint per monitoring.
    """
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
