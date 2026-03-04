import pandas as pd
import random
from datetime import datetime, timedelta


def generate_mock_data():
    clients = [f"Client {i}" for i in range(1, 6)]
    channels = ["Google Ads", "Meta Ads", "LinkedIn Ads"]

    data = []
    start_date = datetime.today() - timedelta(days=180)

    for day in range(180):
        current_date = start_date + timedelta(days=day)

        for client in clients:
            for campaign_id in range(1, 5):
                channel = random.choice(channels)

                impressions = random.randint(1000, 10000)
                clicks = int(impressions * random.uniform(0.01, 0.08))
                cost = round(clicks * random.uniform(0.5, 2.5), 2)
                conversions = int(clicks * random.uniform(0.02, 0.15))
                revenue = round(conversions * random.uniform(50, 200), 2)

                data.append([
                    current_date.date(),
                    client,
                    channel,
                    f"Campaign {campaign_id}",
                    impressions,
                    clicks,
                    cost,
                    conversions,
                    revenue
                ])

    df = pd.DataFrame(data, columns=[
        "date",
        "client_name",
        "channel_name",
        "campaign_name",
        "impressions",
        "clicks",
        "cost",
        "conversions",
        "revenue"
    ])

    return df