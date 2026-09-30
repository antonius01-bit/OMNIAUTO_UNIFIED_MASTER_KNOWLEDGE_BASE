---
name: open-notebook-gemini-mcp
description: Open-source local-first NotebookLM implementation and Gemini Notebook CLI/MCP server. Features multi-provider LLM grounding (esperanto), SurrealDB graph memory checkpointer, citation check validation layer, and multi-model consensus deliberation (the-ai-counsel).
---

# S115: Open Notebook & Gemini MCP Engine (open-notebook-gemini-mcp)

## ⚡ Overview & Local Knowledge Architecture
Synthesized from `lfnovo/open-notebook` (38,400+ Stars) and `jacob-bd/gemini-notebook-mcp-cli` (6,000+ Stars):
1. **Open-Source Local-First NotebookLM (`lfnovo/open-notebook`)**:
   - Complete open-source alternative to Google NotebookLM with zero cloud lock-in.
   - Multi-provider model abstraction via `esperanto` (Gemini, Claude, DeepSeek, local Ollama).
   - SurrealDB graph database checkpointer for persistent document embeddings and cross-session knowledge graphs.
2. **Gemini Notebook CLI & Model Context Protocol Server (`jacob-bd/gemini-notebook-mcp-cli`)**:
   - Direct CLI and MCP server bridging AI coding agents to Google Gemini NotebookLM notebooks.
   - Grounded Q&A with authentic citation extraction and real-time document synchronization.
3. **Citation Check & AI Counsel Consensus Layer**:
   - `citation-check-skill` validates source-to-claim evidence chains.
   - `the-ai-counsel` multi-model deliberation compares conclusions across 3 independent models.

## 🛠️ Usage in Omni-Auto
- **Command**: `/omni-auto open-notebook: Ingest sources and query local grounded notebook with SurrealDB checkpointer for [query]`
- Enforced during Phase 2 (Evidence Forensics) and private local RAG synthesis.
