# Marketing Analytics Pipeline

Data pipeline for analyzing digital marketing campaign performance using a dimensional data model (Star Schema), database version control with Alembic, and an analytical layer ready for BI consumption.

---

## 🎯 Objective

Build a scalable data architecture to centralize marketing performance metrics such as:

- Impressions  
- Clicks  
- Cost  
- Conversions  
- Revenue  

Enabling executive-level analysis like:

- ROAS  
- CPA  
- CPC  
- CTR  
- Performance by client  
- Performance by channel  
- Performance by campaign  

This project simulates a real-world corporate Data Warehouse scenario.

---

## 🧱 Architecture
````
Ingestion (Python)
        ↓
Transformation
        ↓
PostgreSQL (Star Schema)
        ↓
Analytical View
        ↓
BI / Dashboard
````

### 🛠 Tech Stack

- Python  
- Pandas  
- PostgreSQL  
- SQLAlchemy  
- Alembic (database migrations)  

---

## 🗂 Project Structure
````
marketing-analytics-pipeline/
│
├── app/
│ ├── config.py
│ ├── database.py
│ ├── ingestion.py
│ └── load.py
│
├── alembic/
│
├── docs/
│ └── architecture.md
│
└── README.md
````
---

## 📊 Data Model

### Dimensions
- `dim_client`
- `dim_channel`
- `dim_campaign`

### Fact Table
- `fact_marketing_performance`

The model follows a **Star Schema architecture**, optimized for analytical queries.

---

## 📈 Analytical Layer

An aggregated analytical view was created to simplify executive analysis, including:

- Total revenue  
- Total cost  
- Conversions  
- ROAS  
- CPC  
- CPA  
- CTR  

Database indexes were implemented to optimize query performance.

---

## 🛠 How to Run

1. Clone the repository  
2. Create a `.env` file with your `DATABASE_URL`  
3. Install dependencies:
````bash
pip install -r requirements.txt
````
4. Run database migrations:
````bash
alembic upgrade head
````
5. Execute the pipeline:
````bash
python -m app.main
````
---

## 🚀 Next Steps

- [ ] Integration with official marketing APIs (Google Ads / Meta Ads)
- [ ] Dockerization
- [ ] Cloud deployment
- [ ] BI dashboard connected to the warehouse

---

## 📌 Project Status

Under development — focusing on data architecture and analytical engineering.
