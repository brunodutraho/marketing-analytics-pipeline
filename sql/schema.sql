CREATE TABLE dim_client (
    client_id SERIAL PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dim_channel (
    channel_id SERIAL PRIMARY KEY,
    channel_name VARCHAR(50) NOT NULL
);

CREATE TABLE dim_campaign (
    campaign_id SERIAL PRIMARY KEY,
    client_id INT REFERENCES dim_client(client_id),
    channel_id INT REFERENCES dim_channel(channel_id),
    campaign_name VARCHAR(150),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE fact_marketing_performance (
    performance_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    client_id INT REFERENCES dim_client(client_id),
    campaign_id INT REFERENCES dim_campaign(campaign_id),
    impressions INT,
    clicks INT,
    cost NUMERIC(12,2),
    conversions INT,
    revenue NUMERIC(12,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);