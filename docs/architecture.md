# Marketing Analytics Pipeline - Architecture

## Overview

This project implements a modular data pipeline for marketing performance analysis using Python and PostgreSQL.

## Architecture Layers

### 1. Ingestion
Responsible for extracting raw marketing data.
File: `app/ingestion.py`

### 2. Transformation
Responsible for business logic and KPI calculations:
- CTR
- CPC
- CPA
- ROAS

File: `app/transformation.py`

### 3. Load
Responsible for persisting data into PostgreSQL.

File: `app/load.py`

### 4. Orchestration
The main pipeline entrypoint that connects all layers.

File: `app/main.py`

## Database

Table: `fact_marketing_performance`

Metrics stored:
- impressions
- clicks
- cost
- conversions
- revenue
- ctr
- cpc
- cpa
- roas

## Stack

- Python 3.12
- Pandas
- SQLAlchemy
- PostgreSQL
- python-dotenv