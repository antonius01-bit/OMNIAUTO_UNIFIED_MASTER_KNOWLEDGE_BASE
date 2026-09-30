---
name: reasoning-multimodal-recsys
description: >-
  Advanced reasoning-augmented and multimodal recommendation system engine based on ReaRec and GENIUS (CVPR 2025). Integrates visual-textual foundation models, chain-of-thought user intent reasoning, and multi-modal candidate generation.
---

# 🎯 Reasoning & Multimodal Recommendation Engine (ReaRec + GENIUS CVPR'25 Fusion)

Use this skill when building multi-modal recommendation systems (images + text + video + user behavior), reasoning-enhanced recommendation algorithms, or generative personalization models.

## Architecture

```mermaid
flowchart TD
    subgraph MultiModal ["1. Multimodal Item & User Encoding"]
        IMG["Item Images & Video Frames"] --> V["Vision Transformer (ViT / CLIP)"]
        TXT["Item Description & Reviews"] --> T["Language Model (LLM Encoder)"]
        BEH["Sequential Click/Buy Stream"] --> S["Sequential Attention (SASRec)"]
        V & T & S --> F["Unified Multimodal Fusion Space (GENIUS)"]
    end

    subgraph Reasoning ["2. ReaRec Chain-of-Thought Intent Reasoning"]
        F --> COT["User Intent & Latent Desire Inference (CoT)"]
        COT --> RR["Reasoning-Guided Multi-Candidate Re-ranking"]
    end

    subgraph Output ["3. Personalized Recommendation"]
        RR --> Feed["Personalized Feed with Transparent Reasoning Justifications"]
    end
```

## Core Capabilities
1. **Multimodal Representation Fusion**: Embeds image visual features, textual descriptions, and user behavioral graphs into a shared metric space.
2. **Reasoning-Augmented Retrieval (ReaRec)**: Uses Chain-of-Thought prompting to infer latent user motivation (e.g. why a user who bought item A and B would now need item C).
3. **Transparent Recommendation Justification**: Generates user-friendly explanations for every recommended item.

## How to Use
`Build multimodal reasoning recommendation pipeline for [domain/catalog] combining image/text embeddings and ReaRec Chain-of-Thought ranking.`
