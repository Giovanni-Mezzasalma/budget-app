"""add_custom_charts_table

Revision ID: c744b8064fb0
Revises: 47144bbb59d5
Create Date: 2025-11-27 02:07:21.864675

Nota: Questa migration era originariamente vuota perché la tabella
custom_charts era stata creata manualmente via SQL.
Aggiornata per garantire consistenza con alembic downgrade/upgrade.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision: str = 'c744b8064fb0'
down_revision: Union[str, None] = '47144bbb59d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Crea enum type per chart_type
    chart_type_enum = sa.Enum('line', 'bar', 'pie', 'area', name='charttype')
    chart_type_enum.create(op.get_bind(), checkfirst=True)
    
    # Crea tabella custom_charts
    op.create_table(
        'custom_charts',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('user_id', sa.String(length=36), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('chart_type', chart_type_enum, nullable=False),
        sa.Column('config', JSONB, nullable=False),
        sa.Column('filters', JSONB, nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), onupdate=sa.func.now()),
    )
    
    # Crea indice per user_id
    op.create_index('ix_custom_charts_user_id', 'custom_charts', ['user_id'])


def downgrade() -> None:
    # Rimuovi indice
    op.drop_index('ix_custom_charts_user_id', table_name='custom_charts')
    
    # Rimuovi tabella
    op.drop_table('custom_charts')
    
    # Rimuovi enum type
    chart_type_enum = sa.Enum('line', 'bar', 'pie', 'area', name='charttype')
    chart_type_enum.drop(op.get_bind(), checkfirst=True)