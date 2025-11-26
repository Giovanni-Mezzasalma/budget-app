"""
Analytics Router
Statistiche e dashboard data per Budget App
"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.crud import analytics as analytics_crud

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/summary")
async def get_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(None, description="Data inizio periodo (YYYY-MM-DD)"),
    end_date: Optional[date] = Query(None, description="Data fine periodo (YYYY-MM-DD)"),
    account_id: Optional[str] = Query(None, description="Filtra per account specifico")
):
    """
    Restituisce il riepilogo finanziario completo.
    
    **Metriche calcolate:**
    - Totale entrate (income)
    - Totale spese necessità (expense_necessity)
    - Totale spese extra (expense_extra)
    - Totale spese combinate
    - Saldo netto (income - expenses)
    - Balance totale accounts
    - Numero transazioni nel periodo
    
    **Filtri opzionali:**
    - `start_date`: Data inizio (default: inizio mese corrente)
    - `end_date`: Data fine (default: oggi)
    - `account_id`: Filtra per singolo account
    """
    return analytics_crud.calculate_summary(
        db=db,
        user_id=str(current_user.id),
        start_date=start_date,
        end_date=end_date,
        account_id=account_id
    )


@router.get("/monthly-trend")
async def get_monthly_trend(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    months: int = Query(12, ge=1, le=24, description="Numero di mesi da analizzare"),
    account_id: Optional[str] = Query(None, description="Filtra per account specifico")
):
    """
    Restituisce il trend mensile di entrate e uscite.
    
    **Dati restituiti per ogni mese:**
    - Totale income
    - Totale expense_necessity
    - Totale expense_extra
    - Totale expenses combinato
    - Saldo netto
    - Numero transazioni
    
    **Parametri:**
    - `months`: Numero di mesi passati da analizzare (1-24, default: 12)
    - `account_id`: Filtra per singolo account
    """
    return analytics_crud.calculate_monthly_trend(
        db=db,
        user_id=str(current_user.id),
        months=months,
        account_id=account_id
    )


@router.get("/by-category")
async def get_totals_by_category(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(None, description="Data inizio periodo"),
    end_date: Optional[date] = Query(None, description="Data fine periodo"),
    transaction_type: Optional[str] = Query(None, description="Filtra per tipo: income, expense_necessity, expense_extra")
):
    """
    Restituisce i totali raggruppati per categoria.
    
    Utile per grafici a torta e analisi per categoria.
    
    **Risposta:** Lista ordinata per totale decrescente con dettagli categoria.
    """
    return analytics_crud.calculate_totals_by_category(
        db=db,
        user_id=str(current_user.id),
        start_date=start_date,
        end_date=end_date,
        transaction_type=transaction_type
    )


@router.get("/by-account")
async def get_totals_by_account(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(None, description="Data inizio periodo"),
    end_date: Optional[date] = Query(None, description="Data fine periodo")
):
    """
    Restituisce i totali raggruppati per account.
    
    Include:
    - Balance attuale account
    - Totale income per account
    - Totale expenses per account
    - Numero transazioni
    """
    return analytics_crud.calculate_totals_by_account(
        db=db,
        user_id=str(current_user.id),
        start_date=start_date,
        end_date=end_date
    )


@router.get("/daily-breakdown")
async def get_daily_breakdown(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(None, description="Data inizio (default: 30 giorni fa)"),
    end_date: Optional[date] = Query(None, description="Data fine (default: oggi)"),
    account_id: Optional[str] = Query(None, description="Filtra per account")
):
    """
    Restituisce breakdown giornaliero delle transazioni.
    
    Utile per grafici a linee/area con granularità giornaliera.
    """
    return analytics_crud.calculate_daily_breakdown(
        db=db,
        user_id=str(current_user.id),
        start_date=start_date,
        end_date=end_date,
        account_id=account_id
    )


@router.get("/year-comparison")
async def get_year_comparison(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    year1: int = Query(..., description="Primo anno da confrontare"),
    year2: int = Query(..., description="Secondo anno da confrontare")
):
    """
    Confronta due anni side-by-side.
    
    Restituisce totali mensili per entrambi gli anni per facile confronto.
    """
    return analytics_crud.calculate_year_comparison(
        db=db,
        user_id=str(current_user.id),
        year1=year1,
        year2=year2
    )