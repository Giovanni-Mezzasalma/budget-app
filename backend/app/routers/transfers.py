"""
Transfers Router
Managing transfers between user accounts
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from decimal import Decimal

from app.database import get_db
from app.schemas.transfer import (
    TransferCreate,
    TransferUpdate,
    TransferResponse,
    TransferWithDetails,
    TransferTypeInfo,
    VALID_TRANSFER_TYPES,
    TRANSFER_TYPE_LABELS,
    TRANSFER_TYPE_USAGE
)
from app.crud import transfer as transfer_crud
from app.crud import account as account_crud
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/transfers", tags=["Transfers"])


@router.get("/types", response_model=List[TransferTypeInfo])
async def get_transfer_types():
    """
    Returns all available transfer types.

    Useful for populating dropdowns in the frontend.

    **Available types:**
    - `generic`: Generic transfer / Bank transfer
    - `withdrawal`: Withdrawal (Account → Cash)
    - `deposit`: Deposit (Cash → Account)
    - `savings`: Savings (Current → Savings)
    - `investment`: Investment (Current → Investment)
    - `loan_given`: Loan given (Current → Loans to third parties)
    - `loan_received`: Loan received (Loans to third parties → Current)
    """
    return [
        TransferTypeInfo(
            value=t_type,
            label=TRANSFER_TYPE_LABELS[t_type],
            usage=TRANSFER_TYPE_USAGE[t_type]
        )
        for t_type in VALID_TRANSFER_TYPES
    ]

@router.get("/types/rules")
async def get_transfer_type_rules():
    """
    Returns the direction rules for each transfer type.

    Useful for front-end validation and to show the user
    which accounts are valid for each transfer type.
    """
    from app.schemas.transfer import TRANSFER_TYPE_DIRECTION_RULES, TRANSFER_TYPE_LABELS
    
    rules = []
    for t_type, rule in TRANSFER_TYPE_DIRECTION_RULES.items():
        rules.append({
            "type": t_type,
            "label": TRANSFER_TYPE_LABELS.get(t_type, t_type),
            "from_account_types": rule.get("from_account_types"),
            "to_account_types": rule.get("to_account_types"),
            "description": rule.get("description")
        })
    
    return rules

@router.get("/", response_model=List[TransferResponse])
async def get_transfers(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Numero di record da saltare"),
    limit: int = Query(100, ge=1, le=500, description="Numero massimo di risultati"),
    type: Optional[str] = Query(None, description="Filtra per tipo: generic, withdrawal, deposit, savings, investment, loan_given, loan_received"),
    from_account_id: Optional[str] = Query(None, description="Filtra per account origine"),
    to_account_id: Optional[str] = Query(None, description="Filtra per account destinazione"),
    start_date: Optional[date] = Query(None, description="Data inizio periodo (YYYY-MM-DD)"),
    end_date: Optional[date] = Query(None, description="Data fine periodo (YYYY-MM-DD)")
):
    """
    List all user transfers with optional filters.

    **Available filters:**
    - **type**: Filter by transfer type
    - **from_account_id**: Filter by source account
    - **to_account_id**: Filter by destination account
    - **start_date / end_date**: Filter by period

    **Sort:** By date descending (newest first)
    """
    # Valida il tipo se fornito
    if type is not None and type not in VALID_TRANSFER_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid type. Must be one of: {', '.join(VALID_TRANSFER_TYPES)}"
        )
    
    transfers = transfer_crud.get_transfers(
        db,
        user_id=str(current_user.id),
        skip=skip,
        limit=limit,
        transfer_type=type,
        from_account_id=from_account_id,
        to_account_id=to_account_id,
        start_date=start_date,
        end_date=end_date
    )
    
    return transfers


@router.get("/statistics")
async def get_transfer_statistics(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(None, description="Data inizio periodo"),
    end_date: Optional[date] = Query(None, description="Data fine periodo")
):
    """
    Returns transfer statistics grouped by type.

    Response includes:

    - Total number of transfers
    - Total amount transferred
    - Total fees paid
    - Average transfer amount
    - Breakdown by type
    """
    stats = transfer_crud.get_transfer_statistics(
        db,
        user_id=str(current_user.id),
        start_date=start_date,
        end_date=end_date
    )
    
    # Converti Decimal a float per JSON serialization
    result = {
        "total_transfers": stats["total_transfers"],
        "total_amount_transferred": float(stats["total_amount_transferred"]),
        "total_fees_paid": float(stats["total_fees_paid"]),
        "average_transfer_amount": float(stats["average_transfer_amount"]),
        "by_type": {}
    }
    
    for t_type, data in stats["by_type"].items():
        result["by_type"][t_type] = {
            "label": TRANSFER_TYPE_LABELS[t_type],
            "count": data["count"],
            "total_amount": float(data["total_amount"]),
            "total_fees": float(data["total_fees"])
        }
    
    return result


@router.get("/loans")
async def get_loans_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Returns a summary of loans (issued and received).

    Useful for the loans page.

    Response includes:

    - Total loans issued
    - Total loans received
    - Net balance (positive = you lent more)
    - Detailed list of loans
    """
    summary = transfer_crud.get_loans_summary(
        db,
        user_id=str(current_user.id)
    )
    
    return {
        "loans_given_count": summary["loans_given_count"],
        "loans_given_total": float(summary["loans_given_total"]),
        "loans_received_count": summary["loans_received_count"],
        "loans_received_total": float(summary["loans_received_total"]),
        "net_loans": float(summary["net_loans"]),
        "loans_given": [
            {
                "id": t.id,
                "amount": float(t.amount),
                "date": t.date.isoformat(),
                "description": t.description,
                "to_account": t.to_account.name if t.to_account else None
            }
            for t in summary["loans_given"]
        ],
        "loans_received": [
            {
                "id": t.id,
                "amount": float(t.amount),
                "date": t.date.isoformat(),
                "description": t.description,
                "from_account": t.from_account.name if t.from_account else None
            }
            for t in summary["loans_received"]
        ]
    }


@router.post("/", response_model=TransferResponse, status_code=status.HTTP_201_CREATED)
async def create_transfer(
    transfer: TransferCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create a new transfer between two accounts.

    **Required fields:**
    - **from_account_id**: Source account ID
    - **to_account_id**: Destination account ID
    - **amount**: Amount to transfer (always positive)
    - **date**: Transfer date

    **Optional fields:**
    - **type**: Transfer type (default: generic)
    - **description**: Description (e.g., "Loan to Mario")
    - **notes**: Additional notes
    - **exchange_rate**: Exchange rate
    - **fee**: Fee

    **Available types:**
    - `generic`: Generic transfer
    - `withdrawal`: Withdrawal (Account → Cash)
    - `deposit`: Deposit (Cash → Account)
    - `savings`: Savings (Current → Savings)
    - `investment`: Investment (Current → Investment)
    - `loan_given`: Loan given
    - `loan_received`: Loan received

    ✅ The balances of both accounts are automatically updated.

    **Loan example:**
```json
    {
        "from_account_id": "uuid-conto-corrente",
        "to_account_id": "uuid-prestiti-terzi",
        "type": "loan_given",
        "amount": 500.00,
        "date": "2025-01-15",
        "description": "Prestito a Mario"
    }
```
    """
    # Verify that both accounts exist and belong to the user
    from_account = account_crud.get_account(db, transfer.from_account_id, str(current_user.id))
    if not from_account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Source account not found"
        )
    
    to_account = account_crud.get_account(db, transfer.to_account_id, str(current_user.id))
    if not to_account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Destination account not found"
        )
    
    # Verify that the accounts are active
    if not from_account.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Source account is inactive"
        )
    
    if not to_account.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Destination account is inactive"
        )
    
    try:
        db_transfer = transfer_crud.create_transfer(
            db,
            transfer=transfer,
            user_id=str(current_user.id)
        )
        return db_transfer
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/{transfer_id}", response_model=TransferWithDetails)
async def get_transfer(
    transfer_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Retrieve the details of a single transfer.

    Includes account information and Italian labels.
    """
    transfer = transfer_crud.get_transfer(
        db,
        transfer_id=transfer_id,
        user_id=str(current_user.id)
    )
    
    if not transfer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transfer not found"
        )
    
    # Build response with details
    response = TransferWithDetails(
        id=transfer.id,
        user_id=transfer.user_id,
        from_account_id=transfer.from_account_id,
        to_account_id=transfer.to_account_id,
        type=transfer.type,
        amount=transfer.amount,
        date=transfer.date,
        description=transfer.description,
        notes=transfer.notes,
        exchange_rate=transfer.exchange_rate,
        fee=transfer.fee,
        created_at=transfer.created_at,
        updated_at=transfer.updated_at,
        from_account_name=transfer.from_account.name if transfer.from_account else None,
        from_account_currency=transfer.from_account.currency if transfer.from_account else None,
        to_account_name=transfer.to_account.name if transfer.to_account else None,
        to_account_currency=transfer.to_account.currency if transfer.to_account else None,
        converted_amount=transfer.converted_amount,
        type_label=TRANSFER_TYPE_LABELS.get(transfer.type),
        type_usage=TRANSFER_TYPE_USAGE.get(transfer.type)
    )
    
    return response


@router.put("/{transfer_id}", response_model=TransferResponse)
async def update_transfer(
    transfer_id: str,
    transfer_update: TransferUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Update an existing transfer.

    ⚠️ If you change the amount, fee, exchange rate, or accounts,
    the balances are automatically recalculated.
    """
    existing = transfer_crud.get_transfer(db, transfer_id, str(current_user.id))
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transfer not found"
        )
    
    if transfer_update.from_account_id is not None:
        from_account = account_crud.get_account(db, transfer_update.from_account_id, str(current_user.id))
        if not from_account:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="New source account not found"
            )
        if not from_account.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="New source account is inactive"
            )
    
    if transfer_update.to_account_id is not None:
        to_account = account_crud.get_account(db, transfer_update.to_account_id, str(current_user.id))
        if not to_account:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="New destination account not found"
            )
        if not to_account.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="New destination account is inactive"
            )
    
    try:
        updated_transfer = transfer_crud.update_transfer(
            db,
            transfer_id=transfer_id,
            transfer_update=transfer_update,
            user_id=str(current_user.id)
        )
        return updated_transfer
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.delete("/{transfer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transfer(
    transfer_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Cancel a transfer.

    ✅ Account balances are automatically restored.
    """
    success = transfer_crud.delete_transfer(
        db,
        transfer_id=transfer_id,
        user_id=str(current_user.id)
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transfer not found"
        )
    
    return None