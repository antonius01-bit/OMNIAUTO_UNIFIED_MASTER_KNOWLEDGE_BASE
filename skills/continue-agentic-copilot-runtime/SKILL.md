---
name: continue-agentic-copilot-runtime
description: Open-source IDE coding agent integration powered by Continue.dev, local LLM autocomplete, codebase indexing, and tab-autocomplete prompts.
---

# 🤖 Continue Agentic Copilot Runtime (S148)

## 📌 Overview & Core Architecture
The `continue-agentic-copilot-runtime` Super-Skill operationalizes Continue (the leading open-source AI code assistant in VS Code and JetBrains), eliminating dependency on GitHub Copilot:
1. **Modular LLM Provider Integration**: Drop-in configuration for local models (Ollama, vLLM, LM Studio) and cloud APIs (Gemini, Claude, DeepSeek).
2. **Codebase Semantic Indexing (LanceDB / BM25)**: Full local codebase understanding via hybrid dense vector retrieval and lexical keyword search.
3. **Custom Slash Commands & Context Providers**: Modular context gathering (`@code`, `@docs`, `@terminal`, `@diff`, `@git`).
4. **Tab-Autocomplete Engineering**: Ultra-low-latency fill-in-the-middle (FIM) prompt formatting for local SLM models (MiniMind, StarCoder, Qwen2.5-Coder).

---

## ⚡ Core Operational Modes & Commands
- `/continue-code config`: Generates production-ready `config.json` for Continue with multi-model fallbacks.
- `/ide-copilot index`: Builds or refreshes local semantic vector indexing across workspace directories.
- `/local-autocomplete tune`: Optimizes FIM prompt templates and temperature for sub-50ms code completion.
- `/continue-agent run [prompt]`: Dispatches an autonomous multi-file editing workflow inside the IDE.

---

## ⚙️ Production `config.json` Reference
```json
{
  "models": [
    {
      "title": "Claude 3.7 Sonnet",
      "provider": "anthropic",
      "model": "claude-3-7-sonnet-20250219"
    },
    {
      "title": "DeepSeek R1 (Local)",
      "provider": "ollama",
      "model": "deepseek-r1:14b"
    }
  ],
  "tabAutocompleteModel": {
    "title": "Qwen2.5-Coder 1.5B",
    "provider": "ollama",
    "model": "qwen2.5-coder:1.5b-base"
  }
}
```
