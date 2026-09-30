---
name: ai-model-catalog-cognitive-router-40plus
description: Comprehensive taxonomy and dynamic cognitive router covering 40+ foundation models (DeepSeek R1/V3, Kimi K2.6 2M, Perplexity Pro, Gemini 2.5, Claude 3.7, GPT-4o) and OpenCode terminal agent orchestration.
---

# 🧠 S157 — 40+ AI Model Catalog, OpenCode CLI & Cognitive Router

## 📌 Executive Overview
Derived from *40+ AI Model Guide.docx*, *Perplexity AI Comprehensive Guide.docx*, *PANDUAN LENGKAP DEEPSEEK L99.docx*, *Kimi_K2.6_Optimal_Use_Guide.docx*, and *Mastering Gemini*. This Super-Skill establishes an intelligent meta-routing layer that maps complex incoming user tasks to the optimal foundation model, leveraging OpenCode as a terminal-first coding agent and managing multi-provider fallbacks.

---

## 📊 The Cognitive Routing Matrix

| Model Family | Key Strengths & Context Window | Ideal Task Routing | Special Prompt Trigger / Code |
|---|---|---|---|
| **DeepSeek R1 / V3** | Deep mathematical reasoning, algorithmic logic, ultra-low cost | Mathematical derivations, complex code architectures, zero-shot logic puzzles | `/godmode`, `/10x`, `[REASONING_CHAIN]` |
| **Kimi K2.6 (Moonshot)** | 2-Million token context window, Chinese-English bilingual synthesis | Whole-codebase analysis, massive document sets, multi-chapter manuscript proofs | `/long-context`, `/bilingual-sync`, `[2M_CACHE]` |
| **Perplexity Pro** | Real-time multi-source citation verification, live web indexing | Up-to-the-minute tech news, fact checking, academic journal searches | `/deep-search`, `/academic-mode`, `[SOURCE_AUDIT]` |
| **Google Gemini 2.5** | High-speed multimodal visual extraction, audio/video analysis | UI mockup parsing, video frame OCR, large table extractions | `/multimodal-scan`, `/vision-extract` |
| **Anthropic Claude 3.7** | Nuanced writing, strict tool contracts, surgical code refactoring | Production pull requests, architectural decision records, legal/executive briefs | `/surgical-edit`, `/anti-slop`, `[TOOL_CONTRACT]` |
| **OpenCode CLI** | Open-source terminal coding agent running directly in shell | Autonomous script execution, dependency debugging, terminal pair programming | `opencode run "..."` |

---

## ⚡ OpenCode Terminal Integration
- Direct shell installation: `curl -fsSL https://opencode.ai/install | bash` or `npm install -g opencode-ai`.
- Multi-provider configuration: Configured with free and fallback providers (Groq, Gemini, DeepSeek, OpenRouter).
- Background execution: Runs commands with sandbox isolation and automated git rollback.

---

## ⚡ CLI Triggers & Slash Commands
- `/model-router [task]`: Automatically selects and routes the prompt to the highest-efficiency model.
- `/deepseek-r1 [prompt]`: Route to DeepSeek deep chain-of-thought engine.
- `/kimi-2m [files]`: Feed up to 2 million tokens into Kimi context buffer.
- `/perplexity-search [query]`: Execute cited web research with source validation.
- `/opencode [task]`: Dispatch coding task to terminal OpenCode agent.
