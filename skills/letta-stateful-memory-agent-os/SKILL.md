---
name: letta-stateful-memory-agent-os
description: Stateful agent operating system and 3-tiered memory architecture (Core Memory, Recall Event Log, Archival Vector DB) powered by Letta (formerly MemGPT). Equips LLM agents with persistent state, self-editing memory tools, and multi-agent execution threads.
---

# 🧠 Letta Stateful Memory Agent OS (S118)

State-of-the-Art Stateful Agent Operating System and Hierarchical Memory Architecture powered by **Letta** (formerly **MemGPT**, 24.6k★). Bridges stateless LLMs with persistent, self-updating memory structures across unbounded session horizons.

---

## ⚡ 1. The 3-Tiered Memory Hierarchy

```
┌──────────────────────────────────────────────────────────────┐
│                    TIER 1: CORE MEMORY                       │
│  - In-Context Working Memory (Always visible in LLM context) │
│  - Persona Block: Agent identity, behavioral rules, role     │
│  - Human Block: User profile, preferences, current goals     │
│  - Editable via: core_memory_append, core_memory_replace     │
└──────────────────────────────┬───────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────┐
│                   TIER 2: RECALL MEMORY                      │
│  - Chronological Event Log of all past messages and actions  │
│  - Paginated & time-filtered search: recall_memory_search    │
│  - Conversation message ledger with metadata timestamps      │
└──────────────────────────────┬───────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────┐
│                  TIER 3: ARCHIVAL MEMORY                     │
│  - Infinite-Capacity Dense Vector Database (pgvector/LanceDB)│
│  - Semantic search: archival_memory_search(query, page)      │
│  - Persistent document storage: archival_memory_insert(doc)  │
└──────────────────────────────────────────────────────────────┘
```

---

## 🛠️ 2. Core Memory Tooling Contract

Agents operating under S118 possess deterministic self-editing memory capabilities:

```python
# Self-Editing Core Memory Block
def core_memory_append(name: str, content: str) -> str:
    """Appends facts, directives, or state to named Core Memory block (persona/human)."""
    ...

def core_memory_replace(name: str, old_content: str, new_content: str) -> str:
    """Replaces stale or invalidated knowledge in named Core Memory block."""
    ...

# Recall Search across conversation timeline
def conversation_search(query: str, page: int = 0) -> list[dict]:
    """Searches chronological event log for specific past dialogues."""
    ...

# Archival Vector Retrieval
def archival_memory_search(query: str, top_k: int = 5) -> list[str]:
    """Semantic cosine similarity retrieval over unbounded knowledge archives."""
    ...
```

---

## 🔄 3. Multi-Agent Shared Context & Threads

Letta enables deterministic multi-agent collaboration with shared and isolated memory partitions:
1. **Agent State Serialization**: Agents persist as discrete schemas (`AgentState`) containing tool bindings, system prompts, and memory block pointers.
2. **Context Compaction (Summarizer Loops)**: When conversation approaches LLM token window limits, Letta triggers an internal eviction loop:
   - Evaluates conversation messages for semantic novelty.
   - Updates Core Memory with distilled facts.
   - Archives raw dialogue into Recall Memory.
   - Truncates context while preserving strict reasoning continuity.

---

## 🚀 4. Trigger & Workflows
- **Trigger**: `/omni-auto letta` atau `/stateful-memory`
- **Sub-skills**:
  - `letta_agent_bootstrap`: Inisialisasi agent dengan blok persona & human tersimpan.
  - `letta_memory_consolidation`: Kompresi otomatis percakapan ke archival vector DB.
  - `letta_context_checkpoint`: Snapshot status agen ke disk untuk recovery instan.
