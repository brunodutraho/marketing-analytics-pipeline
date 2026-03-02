# Marketing Analytics Pipeline

Pipeline de dados de marketing com ingestão via API oficial, modelagem dimensional em PostgreSQL e dashboard executivo com controle de acesso por cliente.

## 🎯 Objetivo

Automatizar coleta e atualização diária de métricas de marketing digital (Google Analytics, Google Ads e Meta Ads), estruturando os dados em modelo dimensional para análise executiva.

## 🧱 Arquitetura (Fase 1)

API → Python ETL → PostgreSQL → Dashboard (Metabase)

## 🗂 Estrutura do Projeto
````
marketing-analytics-pipeline/
│
├── sql/
│ └── schema.sql
│
├── docs/
└── README.md
````

## 📊 Modelo de Dados

- dim_client
- dim_channel
- dim_campaign
- fact_marketing_performance

## 🚀 Próximas Etapas

- [ ] Inserção automatizada via Python
- [ ] Integração com Google Analytics Data API
- [ ] Automação via cron
- [ ] Deploy com Docker
- [ ] Dashboard com controle de acesso