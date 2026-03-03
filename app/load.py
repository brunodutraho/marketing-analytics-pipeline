from sqlalchemy import text


def get_or_create_client(conn, client_name):
    result = conn.execute(
        text("SELECT client_id FROM dim_client WHERE client_name = :name"),
        {"name": client_name}
    ).fetchone()

    if result:
        return result[0]

    conn.execute(
        text("INSERT INTO dim_client (client_name) VALUES (:name)"),
        {"name": client_name}
    )

    return conn.execute(
        text("SELECT client_id FROM dim_client WHERE client_name = :name"),
        {"name": client_name}
    ).fetchone()[0]


def get_or_create_channel(conn, channel_name):
    result = conn.execute(
        text("SELECT channel_id FROM dim_channel WHERE channel_name = :name"),
        {"name": channel_name}
    ).fetchone()

    if result:
        return result[0]

    conn.execute(
        text("INSERT INTO dim_channel (channel_name) VALUES (:name)"),
        {"name": channel_name}
    )

    return conn.execute(
        text("SELECT channel_id FROM dim_channel WHERE channel_name = :name"),
        {"name": channel_name}
    ).fetchone()[0]


def get_or_create_campaign(conn, campaign_name, client_id, channel_id):
    result = conn.execute(
        text("""
            SELECT campaign_id
            FROM dim_campaign
            WHERE campaign_name = :name
            AND client_id = :client_id
            AND channel_id = :channel_id
        """),
        {
            "name": campaign_name,
            "client_id": client_id,
            "channel_id": channel_id
        }
    ).fetchone()

    if result:
        return result[0]

    conn.execute(
        text("""
            INSERT INTO dim_campaign (campaign_name, client_id, channel_id)
            VALUES (:name, :client_id, :channel_id)
        """),
        {
            "name": campaign_name,
            "client_id": client_id,
            "channel_id": channel_id
        }
    )

    return conn.execute(
        text("""
            SELECT campaign_id
            FROM dim_campaign
            WHERE campaign_name = :name
            AND client_id = :client_id
            AND channel_id = :channel_id
        """),
        {
            "name": campaign_name,
            "client_id": client_id,
            "channel_id": channel_id
        }
    ).fetchone()[0]


def load_data(df, engine):
    with engine.begin() as conn:
        for _, row in df.iterrows():

            client_id = get_or_create_client(conn, row["client_name"])
            channel_id = get_or_create_channel(conn, row["channel_name"])
            campaign_id = get_or_create_campaign(
                conn,
                row["campaign_name"],
                client_id,
                channel_id
            )

            conn.execute(
                text("""
                    INSERT INTO fact_marketing_performance
                    (date, client_id, campaign_id,
                     impressions, clicks, cost,
                     conversions, revenue, ctr, cpc, cpa, roas)
                    VALUES
                    (:date, :client_id, :campaign_id,
                     :impressions, :clicks, :cost,
                     :conversions, :revenue, :ctr, :cpc, :cpa, :roas)
                """),
                {
                    "date": row["date"],
                    "client_id": client_id,
                    "campaign_id": campaign_id,
                    "impressions": row["impressions"],
                    "clicks": row["clicks"],
                    "cost": row["cost"],
                    "conversions": row["conversions"],
                    "revenue": row["revenue"],
                    "ctr": row["ctr"],
                    "cpc": row["cpc"],
                    "cpa": row["cpa"],
                    "roas": row["roas"],
                }
            )