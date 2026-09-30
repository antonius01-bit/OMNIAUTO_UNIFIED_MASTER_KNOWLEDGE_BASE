---
name: hyper-visual-pptx-orchestrator
description: >-
  Ultra-fast visual presentation, slide deck, and infographic design orchestrator fusing Pabrik AI (PPT from Word/TXT, Infographic, MomentsAI, Banner Studio) with Dola MarkItDown document parsing and Generative UI widgets.
---

# 🎨 Hyper Visual & PPTX Orchestrator (Pabrik AI + MarkItDown + PPTX Deck Fusion)

Use this skill when converting unstructured text, research papers, Word docs, or business plans into professional presentation decks (PPTX), infographic data layouts, promotional banners, or product card mockups.

## Architecture

```mermaid
flowchart LR
    subgraph Ingestion ["1. Document Parsing"]
        DOC["Word / TXT / Markdown Document"] --> M["Dola MarkItDown Structure Extractor"]
    end

    subgraph Structuring ["2. Slide & Visual Decomposition"]
        M --> S["Pabrik AI Slide Decomposition (Title, Key Takeaway, Bullet Points)"]
        S --> VIS["Visual Prompt & Card Layout Generator (MomentsAI / Infographic)"]
    end

    subgraph Production ["3. Multi-Format Output"]
        VIS --> P1["Formatted PPTX Slide Deck (.pptx / python-pptx)"]
        VIS --> P2["Interactive HTML Generative UI Presentation"]
        VIS --> P3["Social Media Banner & Product Showcase Prompts"]
    end
```

## Capabilities
1. **Automated Word/TXT to PPTX Deck**: Converts raw meeting notes, thesis chapters, or business pitches into structured 10-20 slide presentations with presenter speaker notes.
2. **Infographic & Data Visualization**: Transforms dense statistics and tables into clean infographic visual schemas and mermaid diagrams.
3. **Studio Banner & Product Card Creator**: Generates high-converting marketing banner text layouts and product card designs.

## How to Use
`Convert document [file/text] into professional PPTX presentation deck with executive summary, bullet points, speaker notes, and infographic diagrams.`
