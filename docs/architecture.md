# Marketing Analytics Pipeline – Architecture

## 🧭 Overview

This project implements a modular and scalable data pipeline designed to process, model, and analyze digital marketing performance data.

The architecture follows modern Data Engineering best practices:

- Separation of concerns
- Dimensional modeling (Star Schema)
- Database versioning with Alembic
- Transaction-safe loading
- Analytical layer optimization

The goal is to simulate a production-ready marketing analytics environment.

---

## 🏗 High-Level Architecture
````
Data Source
↓
Ingestion Layer (Python)
↓
Transformation Layer (Business Logic)
↓
Load Layer (PostgreSQL - Star Schema)
↓
Analytical View
↓
BI / Dashboard
````

---

## 🔹 Architecture Layers

### 1️⃣ Ingestion Layer

**Responsibility:** Extract raw marketing data.

Currently implemented as a simulated dataset for development purposes.

Future-ready for:
- Google Ads API
- Meta Ads API
- Google Analytics Data API

**File:** `app/ingestion.py`

---

### 2️⃣ Transformation Layer

**Responsibility:** Apply business rules and compute marketing KPIs.

Calculated Metrics:
- CTR (Click-Through Rate)
- CPC (Cost per Click)
- CPA (Cost per Acquisition)
- ROAS (Return on Ad Spend)

This layer ensures:
- Clean metric calculations
- Reproducibility
- Business logic centralization

**File:** `app/transformation.py`

---

### 3️⃣ Load Layer

**Responsibility:** Persist data into PostgreSQL using a dimensional model.

Key characteristics:
- Idempotent dimension loading (get-or-create logic)
- Transactional inserts using SQLAlchemy
- Referential integrity enforcement
- Optimized inserts into fact table

**File:** `app/load.py`

---

### 4️⃣ Orchestration Layer

**Responsibility:** Control pipeline execution flow.

Steps:
1. Extract data
2. Transform data
3. Load into Data Warehouse

Ensures separation between execution and business logic.

**File:** `app/main.py`

---

## 🗄 Database Architecture

### Modeling Strategy

The project uses a **Star Schema** optimized for analytical queries.

### Dimension Tables

- `dim_client`
- `dim_channel`
- `dim_campaign`

### Fact Table

- `fact_marketing_performance`

Grain definition:

> One row per campaign per date.

---

## 📊 Analytical Layer

An analytical SQL view was created to:

- Aggregate campaign performance
- Simplify BI consumption
- Improve query readability
- Standardize executive metrics

Database indexes were added to optimize:

- Date filtering
- Client filtering
- Campaign filtering

---

## 🔄 Database Versioning

All schema changes are controlled via:

- Alembic migrations

This ensures:

- Version control of database structure
- Reproducibility across environments
- Production-ready schema management

---

## ⚙️ Stack

- Python 3.12
- Pandas
- SQLAlchemy
- PostgreSQL
- Alembic
- python-dotenv

---

## 🚀 Scalability Considerations

This architecture is designed to support:

- Multi-client environments
- API-based ingestion
- Scheduled execution (cron / Airflow ready)
- Docker containerization
- Cloud deployment

Future improvements may include:

- Incremental loading
- Data validation layer
- Logging & monitoring
- Multi-tenant data isolation
- REST API for client dashboards

---

## 📌 Design Principles Applied

- Separation of concerns
- Reproducible pipelines
- Analytics-first modeling
- Database normalization in dimensions
- Query optimization via indexing
- Clean project structure

---

## 🎯 Architectural Goal

To demonstrate practical knowledge of:

- Data Engineering fundamentals
- Dimensional modeling
- KPI modeling
- SQL performance optimization
- Production-oriented pipeline structure

This project simulates a real-world marketing analytics data warehouse environment.