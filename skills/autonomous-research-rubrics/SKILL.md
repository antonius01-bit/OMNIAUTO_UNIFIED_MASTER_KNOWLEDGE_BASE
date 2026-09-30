---
name: autonomous-research-rubrics
description: >-
  Autonomous scientific research loop and automated rubric evaluation engine inspired by Karpathy's AutoResearch, AutoAgent, and AutoSkill. Automates iterative hypothesis testing, experiment execution, self-grading rubrics, and automated peer-review scoring.
---

# 🔬 Autonomous Research & Auto-Rubric Engine (Karpathy AutoResearch + AutoAgent Fusion)

Use this skill when running end-to-end autonomous research sprints, generating objective grading rubrics, iterating on ML experiment loops, or conducting automated paper review scoring.

## Autonomous Research Iteration Loop

```mermaid
flowchart TD
    subgraph IterationLoop ["Autonomous Research Sprint Loop"]
        H["1. Hypothesis Generation"] --> E["2. Experiment Code Synthesis"]
        E --> R["3. Execution & Metric Logging"]
        R --> G["4. Multi-Criteria Rubric Grading (AutoRubric)"]
        G --> C{"Pass Benchmark Threshold?"}
        C -- No --> REF["5. Self-Reflection & Error Analysis"]
        REF --> H
        C -- Yes --> PUB["6. Academic Synthesis & Paper Drafting"]
    end
```

## Core Capabilities
1. **Karpathy-Style AutoResearch Loop**: Generates an initial hypothesis, executes training/testing scripts, parses metric output, reflects on failures, and iterates autonomously until a target metric is reached.
2. **AutoRubric Evaluation Engine**: Formulates multi-dimensional scoring rubrics (Novelty, Methodological Rigor, Statistical Validity, Reproducibility, Clarity) and assigns quantitative grades ($0-100\%$).
3. **Automated Peer Review & Gap Audit**: Simulates harsh academic peer review (NeurIPS/ICML/ICLR standard), pointing out unproven assumptions and baseline deficiencies.

## How to Use
`Run autonomous research sprint for [problem/dataset] with hypothesis iteration, metric logging, and AutoRubric validation.`
