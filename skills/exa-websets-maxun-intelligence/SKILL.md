---
name: exa-websets-maxun-intelligence
description: >-
  Real-Time Websets Intelligence, News Monitoring & No-Code Web Scraping Engine (S101). Fuses Exa Labs Websets MCP Server, Websets News Monitor, Maxun No-Code Visual Web Scraper, Prism Scanner, and OpenPanel Analytics for continuous real-time internet perception, scheduled automated data pipelines, and deep semantic entity search.
---

# 🌐 Super-Skill S101: Exa Websets & Maxun Intelligence
> **Super-Skill ID**: `S101` | **Kategori**: Web Intelligence, Live News Monitoring, Scraping & Event Telemetry
> **Sumber Utama**: Exa Labs (`exa-labs/websets-mcp-server`, `websets-news-monitor`), Maxun (`getmaxun/maxun`), Prism Scanner (`aidongise-cell/prism-scanner`), OpenPanel (`Openpanel-dev/openpanel`).
> **Integrasi**: Dola AI v4.0, `/omni-auto`, Model Context Protocol (MCP), Firecrawl, dan Webhook Pipelines.

---

## 🧭 1. Arsitektur Persepsi Internet Real-Time

Skill ini menghadirkan kemampuan pemantauan web dan pengumpulan data dinamis berkala tanpa biaya API perorangan yang mahal:

```mermaid
flowchart TD
    subgraph ExaIntelligence ["1. Exa Websets Semantic Engine & News Monitor"]
        QUERY["Kueri Semantik / Kata Kunci Industri"] --> EXA["Exa Websets MCP Server (Pencarian Berbasis Makna)"]
        EXA --> NEWS["Websets News Monitor (Tracking Berita & Regulasi 24/7)"]
        NEWS --> ALERT["Deteksi Tren & Anomali Industri"]
    end

    subgraph MaxunScraping ["2. Maxun Visual No-Code Robot Builder"]
        URL["Website Target Dinamis (SPA / JavaScript)"] --> MAXUN["Maxun Visual Robot Builder (Point-and-Click Selector)"]
        MAXUN --> PAG["Auto-Pagination & Proxy Handling"]
        PAG --> EXTRACT["Ekstraksi Data Terstruktur (.json / .csv)"]
    end

    subgraph TelemetryAnalysis ["3. Prism Scanner & OpenPanel Telemetry"]
        EXTRACT & ALERT --> PRISM["Prism Scanner (Audit Endpoint & Validasi Payload)"]
        PRISM --> OPENPANEL["OpenPanel Product & Event Telemetry Hub"]
        OPENPANEL --> VAULT["Simpan ke Obsidian Vault 04_DATA / 05_OPERATIONS"]
    end
```

---

## ⚡ 2. Fitur Unggulan

### 1. Exa Websets MCP Server (`websets-mcp-server`)
- Melakukan pencarian semantik tingkat lanjut menggunakan embedding berbasis tautan (*link-based neural embeddings*).
- Menemukan dataset tersembunyi, artikel jurnal terbaru, dan siaran pers korporat yang tidak muncul di pencarian Google biasa.

### 2. Websets News Monitor (`websets-news-monitor`)
- Memantau perubahan regulasi perburuhan (Kemnaker/DPR), pergerakan suku bunga perbankan (BI/OJK), dan pengumuman akuisisi perusahaan secara *real-time*.

### 3. Maxun No-Code Visual Scraper (`maxun`)
- Memungkinkan pengguna dan agen AI mengekstrak data dari tabel web interaktif tanpa menulis kode selector CSS/XPath manual.
- Menjadwalkan pengunduhan data berkala (harian/mingguan).

### 4. OpenPanel Telemetry (`openpanel`)
- Menyimpan metrik dan log kejadian secara open-source dan *self-hosted* untuk transparansi audit.

---

## 🛠️ 3. Cara Penggunaan di Omni-Auto

```text
# 1. Pantau Berita dan Regulasi Real-Time
/omni-auto news-monitor: Track [topic/entity] across news websets with hourly alerts

# 2. Ekstrak Data Web Dinamis dengan Maxun
/omni-auto maxun scrape: Build visual extraction robot for [url] capturing [fields]

# 3. Kueri Semantik via Exa MCP
/omni-auto exa search: Find high-authority academic/industry resources on [topic]
```
