def load_data(df, engine):
    df.to_sql(
        "fact_marketing_performance",
        engine,
        if_exists="append",
        index=False
    )