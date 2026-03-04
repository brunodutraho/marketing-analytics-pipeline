import numpy as np
def transform_data(df):

    df["ctr"] = np.where(df["impressions"] > 0,
                        df["clicks"] / df["impressions"], 0)

    df["cpc"] = np.where(df["clicks"] > 0,
                        df["cost"] / df["clicks"], 0)

    df["cpa"] = np.where(df["conversions"] > 0,
                        df["cost"] / df["conversions"], 0)

    df["roas"] = np.where(df["cost"] > 0,
                        df["revenue"] / df["cost"], 0)

    return df