# Data Model – Marketing Analytics Pipeline

## 📊 Modeling Strategy

This project follows a **Star Schema** architecture optimized for analytical workloads.

The goal of the model is to:

- Simplify analytical queries
- Improve aggregation performance
- Separate descriptive data from transactional metrics
- Enable scalable reporting

---

## ⭐ Star Schema Overview

        dim_client
            |
            |
        dim_campaign —— dim_channel
            |
            |
 fact_marketing_performance
 
---

## 📌 Grain Definition

The grain of the fact table is:

> One row per campaign per date.

This ensures:

- Time-based analysis
- Campaign-level aggregation
- KPI computation per marketing unit

---

## 📂 Dimension Tables

### 1️⃣ dim_client

Stores client-level descriptive information.

Columns:
- client_id (PK)
- client_name
- created_at

Purpose:
- Enable filtering and grouping by client
- Support multi-client scalability

---

### 2️⃣ dim_channel

Stores marketing channel information.

Columns:
- channel_id (PK)
- channel_name

Purpose:
- Separate marketing channels (Google Ads, Meta Ads, etc.)
- Allow performance comparison by channel

---

### 3️⃣ dim_campaign

Stores campaign-level descriptive information.

Columns:
- campaign_id (PK)
- client_id (FK)
- channel_id (FK)
- campaign_name
- created_at

Purpose:
- Associate campaigns with clients and channels
- Enable detailed performance breakdown

---

## 📈 Fact Table

### fact_marketing_performance

Stores measurable marketing performance metrics.

Columns:
- performance_id (PK)
- date
- client_id (FK)
- campaign_id (FK)
- impressions
- clicks
- cost
- conversions
- revenue
- ctr
- cpc
- cpa
- roas
- created_at

Purpose:
- Store quantitative metrics
- Enable time-series analysis
- Support KPI computation

---

## ⚡ Indexing Strategy

Indexes were implemented on:

- date
- client_id
- campaign_id

Purpose:
- Improve filtering performance
- Optimize JOIN operations
- Support scalable growth

---

## 📊 Analytical View

An aggregated view was created:

`vw_marketing_performance_summary`

Purpose:

- Simplify BI consumption
- Standardize metric calculations
- Reduce query complexity for dashboards

---

## 🎯 Design Goals

- Analytical optimization
- Clear grain definition
- Separation of dimensions and facts
- Performance-aware design
- BI-ready structure