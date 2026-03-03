"""create star schema

Revision ID: 35326a44ad10
Revises: 
Create Date: 2026-03-03 00:08:25.545400

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '35326a44ad10'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        'dim_client',
        sa.Column('client_id', sa.Integer, primary_key=True),
        sa.Column('client_name', sa.String(100), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP'))
    )

    op.create_table(
        'dim_channel',
        sa.Column('channel_id', sa.Integer, primary_key=True),
        sa.Column('channel_name', sa.String(50), nullable=False, unique=True)
    )

    op.create_table(
        'dim_campaign',
        sa.Column('campaign_id', sa.Integer, primary_key=True),
        sa.Column('client_id', sa.Integer, sa.ForeignKey('dim_client.client_id')),
        sa.Column('channel_id', sa.Integer, sa.ForeignKey('dim_channel.channel_id')),
        sa.Column('campaign_name', sa.String(150), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP'))
    )

    op.create_table(
        'fact_marketing_performance',
        sa.Column('performance_id', sa.Integer, primary_key=True),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('client_id', sa.Integer, sa.ForeignKey('dim_client.client_id')),
        sa.Column('campaign_id', sa.Integer, sa.ForeignKey('dim_campaign.campaign_id')),
        sa.Column('impressions', sa.Integer),
        sa.Column('clicks', sa.Integer),
        sa.Column('cost', sa.Numeric(12, 2)),
        sa.Column('conversions', sa.Integer),
        sa.Column('revenue', sa.Numeric(12, 2)),
        sa.Column('ctr', sa.Numeric(10, 4)),
        sa.Column('cpc', sa.Numeric(10, 4)),
        sa.Column('cpa', sa.Numeric(10, 4)),
        sa.Column('roas', sa.Numeric(10, 4)),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP'))
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_table('fact_marketing_performance')
    op.drop_table('dim_campaign')
    op.drop_table('dim_channel')
    op.drop_table('dim_client')
