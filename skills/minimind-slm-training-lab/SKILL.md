---
name: minimind-slm-training-lab
description: >-
  Small Language Model (SLM) end-to-end training and alignment lab based on MiniMind. Automates tokenizer creation, pretraining, SFT, DPO, and lightweight on-device model deployment.
---

# 🔬 MiniMind SLM Training & Alignment Lab (From-Scratch Small LLMs)

Use this skill when training custom lightweight language models (26M–100M parameters) from scratch, designing domain-specific tokenizers, running Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), or deploying ultra-fast edge AI models.

## Pipeline Architecture

```mermaid
flowchart LR
    subgraph Tokenization ["1. Tokenizer & Corpus"]
        RAW["Domain Text Corpus"] --> BPE["Custom BPE / SentencePiece Tokenizer Training"]
    end

    subgraph Pretraining ["2. Architecture & Pretraining (MiniMind)"]
        BPE --> ARCH["Transformer / MoE Architecture Setup (26M-100M Params)"]
        ARCH --> PRE["Pretraining on Minimal Consumer GPU (Single RTX 3090/4090)"]
    end

    subgraph Alignment ["3. Alignment & Post-Training"]
        PRE --> SFT["Instruction Tuning (Supervised Fine-Tuning)"]
        SFT --> DPO["Preference Optimization (DPO / RLHF)"]
    end

    subgraph Export ["4. Quantization & Edge Deployment"]
        DPO --> EXP["GGUF / ONNX Export for Mobile & Edge Devices"]
    end
```

## Key Capabilities
1. **Low-Compute Model Training**: Complete training scripts capable of training capable 26M–100M parameter LLMs in hours on a single consumer GPU.
2. **End-to-End Alignment Loop**: Covers pretraining $\to$ SFT instruction following $\to$ DPO human preference alignment.
3. **Edge Quantization & Export**: Compiles trained weights directly to GGUF format for instant execution via Ollama and Koboldcpp.

## How to Use
`Configure MiniMind SLM training pipeline for [domain/corpus] with [param_size: 26M/100M] covering pretraining, SFT, and GGUF export.`
