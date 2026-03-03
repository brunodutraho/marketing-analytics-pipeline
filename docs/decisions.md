# Architectural Decisions – Marketing Analytics Pipeline

This document outlines the key architectural decisions made during the development of this project.

---

## 1️⃣ Why Star Schema?

Star Schema was chosen because:

- It is optimized for analytical queries
- It simplifies aggregation
- It improves BI tool compatibility
- It separates descriptive attributes from metrics

Alternative considered:
- Fully normalized OLTP schema

Rejected because:
- Higher query complexity
- Less efficient aggregation

---

## 2️⃣ Why Use Alembic for Migrations?

Alembic was implemented to:

- Version control database schema
- Ensure reproducibility
- Simulate production-ready workflows
- Avoid manual SQL schema scripts

This reflects real-world engineering practices.

---

## 3️⃣ Why Calculate KPIs in the Transformation Layer?

KPIs such as:

- CTR
- CPC
- CPA
- ROAS

Are calculated during transformation to:

- Centralize business logic
- Ensure reproducibility
- Avoid inconsistent BI-level calculations

---

## 4️⃣ Why Create an Analytical View?

The analytical view was created to:

- Standardize metric aggregation
- Simplify BI queries
- Reduce dashboard complexity
- Improve maintainability

This mimics a semantic layer in modern data stacks.

---

## 5️⃣ Why Implement Indexes?

Indexes were added to:

- Improve performance on large datasets
- Optimize filtering by date
- Speed up JOIN operations

This simulates real production data warehouse optimization.

---

## 6️⃣ Why Use SQLAlchemy Instead of Raw SQL Scripts?

SQLAlchemy provides:

- Transaction safety
- Engine abstraction
- Cleaner integration with Python
- Production-level database interaction

---

## 7️⃣ Why Modular Architecture?

The pipeline is divided into:

- Ingestion
- Transformation
- Load
- Orchestration

This ensures:

- Separation of concerns
- Easier testing
- Maintainability
- Future scalability

---

## 🎯 Final Design Philosophy

This project was built to simulate:

- Real-world marketing analytics infrastructure
- Analytics engineering practices
- Scalable data modeling
- Performance-aware architecture

It demonstrates practical understanding of:

- Dimensional modeling
- Database versioning
- KPI structuring
- Analytical system design