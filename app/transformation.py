def transform_data(df):
    df["ctr"] = df["clicks"] / df["impressions"]
    df["cpc"] = df["cost"] / df["clicks"]
    df["cpa"] = df["cost"] / df["conversions"]
    df["roas"] = df["revenue"] / df["cost"]

    return df