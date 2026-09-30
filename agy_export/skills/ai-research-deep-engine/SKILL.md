---
name: ai-research-deep-engine
description: >-
  Autonomous deep scientific research engine covering multi-database citation graphs (arXiv/PubMed/OpenAlex), state-of-the-art literature synthesis, automated hypothesis generation, and LaTeX academic drafting.
---

# 🔬 AI Research Deep Engine (Orchestra-Research + SOTA Literature Synthesis)

Use this skill when performing deep academic literature reviews, mapping citation graphs across arXiv/PubMed/OpenAlex, identifying research gaps, generating scientific hypotheses, or drafting LaTeX papers.

## Deep Research Pipeline

```mermaid
flowchart TD
    subgraph Discovery ["1. Multi-Source Literature Discovery"]
        Q["Research Domain / Question"] --> SR["Multi-Source Query (arXiv, PubMed, OpenAlex, Semantic Scholar)"]
        SR --> G["Citation Graph Traversal (Seminal -> SOTA)"]
    end

    subgraph Synthesis ["2. Critical Gap Analysis & Hypothesis"]
        G --> M["Matrix of Existing Methodologies & Baselines"]
        M --> GAP["Identified Research Gaps & Limitations"]
        GAP --> HYP["Hypothesis & Novel Architectural Formulation"]
    end

    subgraph Experimentation ["3. Experiment Design & Verification"]
        HYP --> EXP["Ablation Study Matrix & Baseline Benchmarks"]
        EXP --> CODE["Python / PyTorch Experiment Code Scaffold"]
    end

    subgraph Publication ["4. Academic Manuscript Deliverable"]
        CODE --> DRAFT["LaTeX / DOCX Scientific Manuscript (APA/IEEE)"]
        DRAFT --> RIS["Synchronized Mendeley [N#E] Citations"]
    end
```

## Capabilities
1. **Citation Graph Traversal**: Automatically follows forward/backward citations to identify both foundational root papers and current year frontiers.
2. **Methodology Comparison Matrix**: Summarizes datasets, model architectures, metrics, and compute costs across top-20 benchmarked papers.
3. **Hypothesis & Novelty Verification**: Evaluates whether a proposed approach has prior art or represents genuine scientific novelty.
4. **Reproducible Experiment Scaffolding**: Generates clean evaluation harnesses, baseline comparisons, and statistical significance tests ($p$-value, confidence intervals).

## How to Use
`Conduct deep scientific literature review on [research topic] across arXiv/OpenAlex, map key baselines, identify gaps, and formulate experiment design.`
