"""Add current_balance to accounts

Revision ID: a1b2c3d4e5f6
Revises: c744b8064fb0
Create Date: 2025-12-04

Aggiunge colonna current_balance alla tabella accounts.
- initial_balance: rimane immutabile, rappresenta il saldo iniziale storico
- current_balance: viene aggiornato da transazioni e trasferimenti
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, None] = 'c744b8064fb0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Aggiungi colonna current_balance
    op.add_column(
        'accounts',
        sa.Column(
            'current_balance',
            sa.Numeric(precision=15, scale=2),
            nullable=True  # Temporaneamente nullable per la migrazione
        )
    )
    
    # Copia i valori esistenti da initial_balance a current_balance
    op.execute(
        "UPDATE accounts SET current_balance = initial_balance"
    )
    
    # Rendi la colonna NOT NULL dopo aver popolato i dati
    op.alter_column(
        'accounts',
        'current_balance',
        nullable=False
    )
    
    # Aggiungi indice per query performance
    op.create_index(
        'ix_accounts_user_current_balance',
        'accounts',
        ['user_id', 'current_balance'],
        unique=False
    )


def downgrade() -> None:
    # Rimuovi indice
    op.drop_index('ix_accounts_user_current_balance', table_name='accounts')
    
    # Prima di rimuovere current_balance, aggiorna initial_balance 
    # con il valore corrente (per non perdere dati)
    op.execute(
        "UPDATE accounts SET initial_balance = current_balance"
    )
    
    # Rimuovi colonna
    op.drop_column('accounts', 'current_balance')
