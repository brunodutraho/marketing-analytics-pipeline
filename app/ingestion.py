import pandas as pd

def extract_data():
    data = {
        "date": ["2025-01-03"],
        "client_id": [1],
        "campaign_id": [1],
        "impressions": [2000],
        "clicks": [250],
        "cost": [600.00],
        "conversions": [30],
        "revenue": [2400.00]
    }

    df = pd.DataFrame(data)
    return df