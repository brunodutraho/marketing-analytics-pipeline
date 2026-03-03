"""add indexes to fact_marketing_performance

Revision ID: b3465fb49440
Revises: 35326a44ad10
Create Date: 2026-03-03 10:04:09.842401

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3465fb49440'
down_revision: Union[str, Sequence[str], None] = '35326a44ad10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


from alembic import op


def upgrade() -> None:
    # Índice para filtros por data
    op.create_index(
        "idx_fact_marketing_date",
        "fact_marketing_performance",
        ["date"],
    )

    # Índice para joins/filtros por cliente
    op.create_index(
        "idx_fact_marketing_client_id",
        "fact_marketing_performance",
        ["client_id"],
    )

    # Índice para joins/filtros por campanha
    op.create_index(
        "idx_fact_marketing_campaign_id",
        "fact_marketing_performance",
        ["campaign_id"],
    )


def downgrade() -> None:
    op.drop_index("idx_fact_marketing_campaign_id", table_name="fact_marketing_performance")
    op.drop_index("idx_fact_marketing_client_id", table_name="fact_marketing_performance")
    op.drop_index("idx_fact_marketing_date", table_name="fact_marketing_performance")
