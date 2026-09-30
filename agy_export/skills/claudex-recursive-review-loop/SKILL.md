---
name: claudex-recursive-review-loop
description: >-
  Recursive self-correcting code review loop, pull-request auditor, and visual UI/UX taste critic engine powered by ClaudeX, Claude Review Loop, and Taste-Skill.
---

# 🔄 ClaudeX Recursive Review Loop & Taste Critic Suite

Use this skill when auditing code diffs iteratively, running multi-pass self-correcting refinement loops before committing, or critiquing UI/UX design aesthetics and typography against top-tier design standards.

## Architecture

```mermaid
flowchart TD
    subgraph InitialCode ["1. Candidate Code / Design"]
        RAW["Draft Code Changes or UI Design Spec"] --> R1["First-Pass Generation"]
    end

    subgraph ReviewLoop ["2. Recursive Review Loop (ClaudeX & Claude-Review-Loop)"]
        R1 --> CRITIC["Critic Agent: Syntax, Performance, Edge Cases & Security"]
        CRITIC -->|Found Defects| FIX["Self-Correction & Patch Refinement"]
        FIX --> CRITIC
    end

    subgraph TasteCritic ["3. Aesthetic Taste & Visual Audit (Taste-Skill)"]
        CRITIC -->|Clean Code| TASTE["Design Critic: Visual Rhythm, Hierarchy, Typography, Spacing"]
    end

    subgraph FinalMerge ["4. Production Ready Approval"]
        TASTE --> MERGE["100% Verified, Tastefully Crafted Output"]
    end
```

## Key Capabilities
1. **Recursive Multi-Pass Review (ClaudeX Loop)**: Loops 3–5 iterations of critique and repair until all lint, logic, and edge-case errors reach zero.
2. **Taste-Skill Visual Discrimination**: Critiques frontend interfaces using high-end human aesthetic principles (contrast ratios, whitespace breathing room, font pairing, micro-interactions).
3. **Automated PR Diff Summarizer**: Generates executive pull-request descriptions with risk analysis and verification steps.

## How to Use
`Execute recursive review loop on [code/repo/component] applying ClaudeX self-correction and Taste-Skill aesthetic critique.`
