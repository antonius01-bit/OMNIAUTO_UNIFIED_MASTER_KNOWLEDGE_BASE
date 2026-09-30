---
name: openviking-filesystem-agent-memory
description: Virtual filesystem context database and multi-asset memory hub for AI agents powered by Volcengine OpenViking (viking:// protocol), rohitg00 agentmemory, TencentDB Agent Memory, and Neo4j agent graph memory. Replaces flat vector stores with hierarchical directory recursive retrieval, local-first REST/MCP memory servers, and 4 enterprise memory assets.
---

# 🗄️ S129 — OpenViking Filesystem Agent Memory (`openviking-filesystem-agent-memory`)

## 📌 Overview & Upstream Origin
- **Upstream Repositories**:
  - [volcengine/OpenViking](https://github.com/volcengine/OpenViking) (ByteDance/Volcengine context database for AI agents using the `viking://` virtual filesystem protocol).
  - [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) (Local-first persistent memory server for AI coding agents with REST API and MCP surface).
  - [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) (Enterprise memory hub converting interactions into 4 reusable assets: Chat Memory, Skill, LLM-Wiki, Code-Graph).
  - [neo4j-labs/agent-memory](https://github.com/neo4j-labs/agent-memory) (Graph-native memory system with skill distillation and entity-relationship tracking).
  - [GitHub Copilot Agent Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) (Repository-level memory scratchpads and persistent cross-session preferences).
- **Core Methodology**: Traditional vector databases act as opaque "black boxes" where agents retrieve isolated chunks without spatial or ontological context. This super-skill structures agent memory into an inspectable **Virtual Filesystem Hierarchy** (`viking://`) with **Directory Recursive Retrieval**, combined with a local-first memory daemon (port 3111) and enterprise knowledge governance.

---

## 🏛️ Virtual Filesystem Protocol (`viking://`)

```
viking://
├── user/                  # User profile, coding habits, stylistic preferences
│   ├── preferences.json   # E.g. "prefers TypeScript strict, forbids any"
│   └── persona.md         # Working role, language preferences (ID/EN)
├── resources/             # Static reference documentation & private knowledge
│   ├── docs/              # Ingested API references, library cheatsheets
│   └── architecture/      # ADRs (Architectural Decision Records), system specs
├── sessions/              # Multi-turn conversational episodic memory
│   ├── 2026-09-10/        # Chronological session logs with token budgets
│   └── checkpoints/       # Intermediate task checkpoints and diff snapshots
└── skills/                # Distilled, reusable procedural routines
    ├── testing/           # Verified test-generation patterns
    └── refactoring/       # Surgical diff templates and lint fixes
```

### Directory Recursive Retrieval
Rather than scanning millions of embeddings globally, the retrieval engine operates in two stages:
1. **Directory Selection**: Discovers the relevant top-level folder (e.g. `viking://resources/architecture/` vs `viking://skills/refactoring/`).
2. **Drill-Down Search**: Recursively filters files and sections within the targeted directory path, minimizing semantic drift and hallucinations.

---

## 🧩 The 4 Enterprise Memory Assets (TencentDB Architecture)

1. **Chat Memory (Episodic Context)**:
   - Stores raw interactions, user directives, constraints, and chronological milestone logs.
2. **Skill Assets (Procedural Workflows)**:
   - Successfully executed multi-step tasks are automatically distilled into repeatable procedural playbooks.
3. **LLM-Wiki (Structured Semantic Knowledge)**:
   - Continuous project documentation curated collaboratively by agents and developers.
4. **Code-Graph (Structural Relationships)**:
   - AST-level dependency graph mapping call chains, import hierarchies, and blast-radius impact analysis.

---

## 💻 Local Memory Server & MCP Integration (rohitg00 Architecture)

The local memory server runs on `http://127.0.0.1:3111` or as a standard MCP server:
```json
{
  "mcpServers": {
    "agent-memory": {
      "command": "python",
      "args": ["-m", "openviking.mcp_server"],
      "env": {
        "VIKING_STORAGE_PATH": "C:/Users/antoni/Dola/agent_memory"
      }
    }
  }
}
```

### Core Memory Operations
- `viking_ls(path: str)`: List files and sub-directories within the virtual filesystem.
- `viking_read(path: str)`: Fetch exact memory or resource document.
- `viking_write(path: str, content: str)`: Persist new knowledge, session milestone, or preference.
- `viking_search(query: str, root_dir: str = "viking://")`: Hierarchical semantic search bounded by directory scope.
- `viking_distill_skill(session_id: str)`: Turn a verified task trajectory into a permanent skill.

---

## 🚀 Triggers & Operational Commands
- `/omni-auto memory ls: Browse virtual filesystem memory tree under [path].`
- `/omni-auto memory store: Save [fact/rule/decision] to viking://resources/architecture/ADR-[name].md.`
- `/omni-auto memory query: Perform directory recursive retrieval for [query] scoped to viking://skills/.`
- `/omni-auto memory distill: Extract reusable skill from current conversation and persist permanently.`