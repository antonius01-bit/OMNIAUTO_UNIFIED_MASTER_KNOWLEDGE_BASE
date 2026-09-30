---
name: notebooklm-research-synthesizer
description: >-
  Multi-document grounded synthesis, audio overview podcast scripting, and source-cited analysis powered by Google NotebookLM skills, notebooklm-py, and robonuggets workflows.
---

# 📖 NotebookLM Research Synthesizer & Audio Overview Engine

Use this skill when processing collections of research papers, generating source-grounded study guides, drafting dual-host podcast audio dialogues, or synthesizing complex PDF libraries with strict factual attribution.

## Architecture

```mermaid
flowchart TD
    subgraph Ingestion ["1. Multi-Source Ingestion"]
        DOCS["Research Papers / PDFs / Notes / Web Articles"] --> RAG["NotebookLM Python Engine (notebooklm-py)"]
    end

    subgraph Grounding ["2. Grounded Synthesis & Citation Matching"]
        RAG --> CIT["Source-Cited Factual Q&A Matrix"]
        RAG --> SG["Executive Study Guide & FAQ Briefing"]
        RAG --> POD["Dual-Host Audio Overview / Podcast Script"]
    end

    subgraph Publication ["3. Validated Output"]
        CIT & SG & POD --> OUT["100% Attributed Academic Briefing with Exact Page References"]
    end
```

## Key Capabilities
1. **Multi-Document Grounding**: Synthesizes up to 50+ source documents simultaneously with explicit inline citations.
2. **Audio Overview Podcast Scripting**: Formats conversational, natural dual-host dialogue scripts (Deep Dive style) explaining dense academic topics.
3. **Source Attributed Briefings**: Generates study guides, timelines, briefings, and FAQ documents directly tied to source coordinates.

## How to Use
`Synthesize sources [file_paths] using NotebookLM engine: generate [study guide / audio podcast script / citation matrix].`
