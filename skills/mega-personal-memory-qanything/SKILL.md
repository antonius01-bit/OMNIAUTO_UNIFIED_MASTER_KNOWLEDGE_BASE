---
name: mega-personal-memory-qanything
description: >-
  Hierarchical Personal Memory Engine & 2-Stage Local RAG (S100). Fuses NetEase Youdao QAnything, IAI Personal Memory Engine, MegaMemory, MEGA, and Box Sandboxing for multi-tiered cross-session agent memory, sub-second 2-stage cross-encoder document retrieval, and persistent personal knowledge graph indexing.
---

# 🧠 Super-Skill S100: Mega Personal Memory & QAnything Engine
> **Super-Skill ID**: `S100` | **Kategori**: Memory Systems, Local RAG, Knowledge Graph & Agent Persistence
> **Sumber Utama**: NetEase Youdao (`netease-youdao/QAnything`), CodeAbra (`CodeAbra/iai-personal-memory-engine`), Kevin (`0xK3vin/MegaMemory`), Dyamin (`dyamin/MEGA`), Haehnchen (`my-mega-memory`), Jegly (`Box`).
> **Integrasi**: Dola AI v4.0, `/omni-auto`, Obsidian Vault, SQLite/DuckDB, pgvector, dan Local Embeddings.

---

## 🧭 1. Arsitektur Memori Hirarkis 4-Level & 2-Stage RAG

Skill ini menyediakan infrastruktur memori jangka panjang dan penelusuran dokumen lokal tanpa biaya langganan cloud:

```mermaid
flowchart TD
    subgraph MemoryHierarchy ["Hierarki Memori Agen 4-Level (MEGA Engine)"]
        L1["L1: Working Scratchpad (RAM / Active Context Window)"]
        L2["L2: Episodic Session Memory (Percakapan & Milestone Terkini)"]
        L3["L3: Semantic Entity Knowledge Graph (IAI Personal Memory)"]
        L4["L4: Permanent Cold Archive (Obsidian Vault & Parquet Datasets)"]
        L1 <--> L2 <--> L3 <--> L4
    end

    subgraph QAnythingEngine ["2-Stage Document RAG Pipeline (NetEase Youdao QAnything)"]
        DOCS["Dokumen: PDF / DOCX / PPTX / XLSX / Gambar"] --> CHUNK["Smart Structural Chunking & Parsing"]
        CHUNK --> STAGE1["Stage 1: Dense Vector Retrieval (Top-100 Candidates)"]
        STAGE1 --> STAGE2["Stage 2: Cross-Encoder Reranker (Top-5 Precise Chunks)"]
        STAGE2 --> CONTEXT["Grounding Truth Injected into LLM Prompt"]
    end

    subgraph Sandboxing ["Box Sandboxed Context Isolation"]
        BOX["Box Container: Isolasi Topik Riset A vs Riset B (Zero Context-Bleed)"]
    end

    MemoryHierarchy <--> QAnythingEngine
    QAnythingEngine <--> Sandboxing
```

---

## ⚡ 2. Fitur Unggulan

### 1. 2-Stage RAG QAnything (`QAnything`)
- **Stage 1**: Pencarian cepat menggunakan embedding vektor (*Dense Retrieval*) untuk menyaring 100 kandidat teks paling relevan.
- **Stage 2**: Pemeringkat ulang (*Cross-Encoder Reranker*) yang mengevaluasi interaksi kata per kata antara kueri dan dokumen untuk menghasilkan 3–5 potongan teks dengan presisi ekstrem (akurasi mendekati 100%).
- Mendukung berbagai format: PDF hasil scan, tabel Excel rumit, presentasi PPTX, dan naskah Word.

### 2. IAI Personal Memory Engine (`iai-personal-memory-engine`)
- Membangun graf hubungan entitas pengguna:
  - *Preferensi Penelitian*: Metodologi favorit, struktur bab tesis, gaya kutipan Mendeley.
  - *Entitas Proyek*: Variabel penelitian, hipotesis aktif, nama dosen pembimbing, batas waktu pengiriman.
  - *Riwayat Interaksi*: Keputusan arsitektur yang disetujui pengguna sebelumnya.

### 3. Box Sandboxed Context Isolation (`Box`)
- Mengisolasi memori antar proyek berbeda di laptop Anda. Riset Tesis MM-HR tidak akan tercampur dengan proyek Software Engineering atau Finansial.

---

## 🛠️ 3. Cara Penggunaan di Omni-Auto

```text
# 1. Simpan Fakta ke Memori Permanen
/omni-auto memory store: [entity_name] -> [property/relationship/fact]

# 2. Ambil Riwayat Kontekstual Lintas Sesi
/omni-auto memory recall: Query personal preferences and project milestones for [project_name]

# 3. Kueri Dokumen dengan Reranking 2-Stage QAnything
/omni-auto qanything query: Ask [question] against document collection [path/to/docs] with cross-encoder verification
```
