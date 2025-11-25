"""Update category types to three values

Revision ID: d9555bc5b21b
Revises: 524a0b838c31
Create Date: 2025-11-22 16:55:02.751414

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9555bc5b21b'
down_revision: Union[str, None] = '524a0b838c31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Aggiorna le categorie esistenti di tipo 'expense' a 'expense_necessity'
    op.execute("""
        UPDATE categories 
        SET type = 'expense_necessity' 
        WHERE type = 'expense'
    """)
    
    # Aggiorna le transazioni esistenti
    op.execute("""
        UPDATE transactions 
        SET type = 'expense_necessity' 
        WHERE type = 'expense'
    """)


def downgrade() -> None:
    op.execute("""
        UPDATE categories 
        SET type = 'expense' 
        WHERE type IN ('expense_necessity', 'expense_extra')
    """)
    
    op.execute("""
        UPDATE transactions 
        SET type = 'expense' 
        WHERE type IN ('expense_necessity', 'expense_extra')
    """)