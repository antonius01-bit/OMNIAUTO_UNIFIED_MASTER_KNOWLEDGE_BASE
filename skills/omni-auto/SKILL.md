---
name: omni-auto
description: >-
  Head Meta-Router & Master Prompt Optimizer v4.0. Intercepts and optimizes raw user commands into token-efficient execution workflows, selects optimal Super-Skills (S1–S32), and executes multi-pass verified, hallucination-free generation of dual-language documents (.docx), presentation decks (.pptx), and Mendeley citation libraries (.ris).
---

# 👑 `/omni-auto` — Head Meta-Router & Master Prompt Optimizer v4.0

Use this skill unconditionally as the **Head Pre-Processor** for all complex commands, research workflows, academic theses, software engineering, and business modeling tasks.

## Head Architecture & Workflow Routing

```mermaid
flowchart TD
    subgraph HeadEngine ["1. Head Prompt Master & Token Optimizer"]
        RAW["Raw User Command / Idea / Prompt"] --> PO["Token Compressor & Intent Distiller (Prompt Master Pack)"]
        PO --> TPL["Universal Template (Role, Objective, Context, Task, Inputs, Constraints, Method, Output)"]
        PO --> EV["Evidence Separation (FACT / INFERENCE / ASSUMPTION / UNKNOWN)"]
    end

    subgraph Router ["2. Super-Skill Dispatcher & Workflow Mapping"]
        TPL --> ROUTE{"Master Skill Router (S1–S32)"}
        ROUTE -->|Academic / Thesis| ACAD["omni-auto + publication-shield + mendeley-ris-linker (S1-S4)"]
        ROUTE -->|Coding / Architecture| CODE["agentic-engineering-suite + master-software-engineer (S7, S9, S27)"]
        ROUTE -->|AI / ML / DeepSeek| ML["deepseek-harness-optimizer + master-ai-ml-engineer (S10, S28)"]
        ROUTE -->|Copywriting & SEO| COPY["hyper-copywriting-seo-suite (S30)"]
        ROUTE -->|Visual / PPTX| PPT["hyper-visual-pptx-orchestrator (S31)"]
        ROUTE -->|Finance / Business| BIZ["enterprise-business-financial-analyzer (S32)"]
    end

    subgraph ForensicShield ["3. Multi-Pass Verification & Zero-Hallucination Shield"]
        ACAD & CODE & ML & COPY & PPT & BIZ --> SC["Source-to-Claim Evidence Chain (Claim → Evidence → Source → Limitation)"]
        SC --> FK16["FK-16: Plagiarism & Similarity Audit (Target ≤ 5%)"]
        SC --> FK17["FK-17: 29-Pattern Anti-AI Cliché Humanizer"]
        SC --> FK19["FK-19: Real Citation & Authenticity Forensics"]
    end

    subgraph Deliverables ["4. 100% Guaranteed Working Deliverables"]
        FK16 & FK17 & FK19 --> D1["Dual-Language Academic Manuscript (.docx) with matched [N#E]"]
        FK16 & FK17 & FK19 --> D2["Professional Formatted Slide Deck (.pptx)"]
        FK16 & FK17 & FK19 --> D3["Mendeley / Zotero 1-Click Library (.ris)"]
        FK16 & FK17 & FK19 --> D4["100% Working Verified Code / Business Model"]
    end
```

## Core Pre-Processing Protocols

### 1. Token & Credit Compression
- Strips redundant tokens and filler phrasing while preserving 100% of underlying user intent.
- Structures request into: **Role**, **Objective**, **Context**, **Task**, **Inputs**, **Constraints**, **Method**, **Output Format**, **Quality Control**, and **Failure Handling**.

### 2. Zero-Hallucination & Anti-Bias Forensics
- **Evidence Separation**: Clearly demarcates verified facts from inferences and assumptions.
- **Missing Data Rule**: Never fabricates DOIs, statistics, citations, or regulations. Uses `"DATA TIDAK TERSEDIA"` or queries live databases when unverified.
- **Source-to-Claim Chain**: Every claim is grounded in peer-reviewed Scopus/WoS literature or authentic datasets.

### 3. Guaranteed Deliverable Production
- **Bahasa Indonesia `.docx`**: Complete structured naskah with `[N#E]` numbered claims.
- **English `.docx`**: Exact 1-to-1 matching `[N#E]` numbered claims and terminology.
- **Presentation `.pptx`**: Structured slide deck with clear narrative flow and presenter notes.
- **Daftar Pustaka `.ris`**: Matching `ID - N` metadata for 1-click import into Mendeley/Zotero.

## Command Syntaxes
```text
/omni-auto [Thesis / Journal]: [Topic]. Type: [QUANTITATIVE/QUALITATIVE/MIXED]. Variables: [...]. Region: [...]. Years: [...].
/omni-auto prompt [raw idea] -> Optimizes into high-density master prompt.
/omni-auto [any task] -> Automatic head routing and verified execution.
```
