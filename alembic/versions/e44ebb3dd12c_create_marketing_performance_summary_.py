"""create marketing performance summary view

Revision ID: e44ebb3dd12c
Revises: b3465fb49440
Create Date: 2026-03-03 10:15:57.135855

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e44ebb3dd12c'
down_revision: Union[str, Sequence[str], None] = 'b3465fb49440'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE VIEW vw_marketing_performance_summary AS
        SELECT
            f.date,
            c.client_name,
            ch.channel_name,
            cp.campaign_name,
            
            SUM(f.impressions) AS impressions,
            SUM(f.clicks) AS clicks,
            SUM(f.cost) AS cost,
            SUM(f.conversions) AS conversions,
            SUM(f.revenue) AS revenue,

            CASE 
                WHEN SUM(f.impressions) > 0 
                THEN SUM(f.clicks)::float / SUM(f.impressions)
                ELSE 0
            END AS ctr,

            CASE 
                WHEN SUM(f.clicks) > 0
                THEN SUM(f.cost) / SUM(f.clicks)
                ELSE 0
            END AS cpc,

            CASE 
                WHEN SUM(f.conversions) > 0
                THEN SUM(f.cost) / SUM(f.conversions)
                ELSE 0
            END AS cpa,

            CASE 
                WHEN SUM(f.cost) > 0
                THEN SUM(f.revenue) / SUM(f.cost)
                ELSE 0
            END AS roas

        FROM fact_marketing_performance f
        JOIN dim_client c ON f.client_id = c.client_id
        JOIN dim_campaign cp ON f.campaign_id = cp.campaign_id
        JOIN dim_channel ch ON cp.channel_id = ch.channel_id

        GROUP BY
            f.date,
            c.client_name,
            ch.channel_name,
            cp.campaign_name
    """)


def downgrade() -> None:
    op.execute("DROP VIEW IF EXISTS vw_marketing_performance_summary")
