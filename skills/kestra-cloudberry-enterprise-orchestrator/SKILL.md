---
name: kestra-cloudberry-enterprise-orchestrator
description: >-
  Enterprise Declarative Workflows, MPP Data Warehousing & Open-SaaS Architecture (S102). Fuses Kestra Orchestrator, Apache Cloudberry MPP DB, Wasp Open-SaaS, Coder Code-Server, Ghost CMS, and Terraform LiteLLM for petabyte-scale analytical data pipelines, event-driven DAG automation, and production cloud infrastructure.
---

# 🏭 Super-Skill S102: Kestra & Cloudberry Enterprise Orchestrator
> **Super-Skill ID**: `S102` | **Kategori**: Workflow Orchestration, Big Data MPP, Open-SaaS & Cloud Infrastructure
> **Sumber Utama**: Kestra (`kestra-io/kestra`), Apache (`apache/cloudberry`), Wasp (`wasp-lang/open-saas`), Coder (`coder/code-server`), Ghost (`TryGhost/Ghost`), BerriAI (`terraform-google-litellm`).
> **Integrasi**: Dola AI v4.0, `/omni-auto`, Docker, PostgreSQL, Terraform, Kubernetes, dan Obsidian Vault.

---

## 🧭 1. Arsitektur Enterprise Workflow & MPP Warehousing

Skill ini mengintegrasikan otomasi alur kerja data skala industri (*event-driven DAGs*), pergudangan data analitik skala besar (*MPP Big Data*), serta infrastruktur pengembangan cloud mandiri:

```mermaid
flowchart TD
    subgraph KestraWorkflows ["1. Kestra Declarative YAML Orchestration Engine"]
        EVENT["Pemicu Event / Webhook / Jadwal Cron"] --> DAG["Kestra Declarative YAML Flow Definition"]
        DAG --> TASK1["Task 1: Ekstraksi Data (API / Database / Web)"]
        DAG --> TASK2["Task 2: Pembersihan & Transformasi Python / SQL"]
        DAG --> TASK3["Task 3: Notifikasi, Alert & Ekspor Deliverable"]
    end

    subgraph CloudberryMPP ["2. Apache Cloudberry Petabyte-Scale MPP Database"]
        TASK2 --> MPP["Apache Cloudberry (PostgreSQL-Compatible Shared-Nothing MPP)"]
        MPP --> ANALYTICS["Pemrosesan Kueri Analitik Masif (OLAP) & Agregasi Cepat"]
    end

    subgraph OpenSaaSDeploy ["3. Open-SaaS, Cloud IDE & Publishing"]
        ANALYTICS --> SAAS["Wasp Open-SaaS (React + Node + Prisma + Stripe)"]
        SAAS --> CODER["Coder Code-Server (VS Code di Browser Mandiri)"]
        SAAS --> GHOST["Ghost Headless Publishing & Newsletter CMS"]
    end
```

---

## ⚡ 2. Fitur Unggulan

### 1. Kestra Declarative Workflows (`kestra`)
- Seluruh pipeline data didefinisikan dalam format **YAML deklaratif** yang dapat dibaca manusia dan agen AI.
- Memiliki 10,000+ plugin ekosistem (BigQuery, PostgreSQL, S3, Slack, Python, dbt, Spark).
- Eksekusi bebas server yang tangguh (*fault-tolerant*) dengan pencatatan status (*retry, fallback, alerting*).

### 2. Apache Cloudberry MPP Analytic Database (`cloudberry`)
- Basis data analitik berskala masif berbasis arsitektur *Shared-Nothing MPP* (kompatibel penuh dengan sintaks PostgreSQL).
- Mampu memproses ratusan juta baris data survei kependudukan atau transaksi finansial dalam hitungan detik.

### 3. Wasp Open-SaaS & Coder Code-Server (`open-saas`, `code-server`)
- Template SaaS modern siap pakai dengan autentikasi, pembayaran Stripe, dan dashboard analitik.
- Menjalankan lingkungan IDE VS Code lengkap di dalam browser pada server lokal atau cloud pribadi.

---

## 🛠️ 3. Cara Penggunaan di Omni-Auto

```text
# 1. Rancang Alur Kerja Deklaratif Kestra
/omni-auto kestra flow: Create declarative ETL pipeline extracting [source] and loading to [target]

# 2. Desain Skema Analitik Apache Cloudberry
/omni-auto cloudberry: Architect MPP partitioned table schema for [large_dataset] with optimized distribution keys

# 3. Deploy SaaS Boilerplate Open-SaaS
/omni-auto open-saas: Scaffold full-stack SaaS project for [use_case] with Stripe and Prisma
```
