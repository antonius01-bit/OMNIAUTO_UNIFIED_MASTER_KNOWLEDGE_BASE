---
name: graphify-headroom-intelligence
description: Codebase knowledge graph extraction via Graphify (graphify.net) and multi-agent developer desktop workspace via Headroom Labs.
---

# S70: Graphify & Headroom Intelligence (graphify-headroom-intelligence)

## ⚡ Overview & Architecture
1. **Graphify Engine (Graphify-Labs/graphify, graphify.net)**:
   - Converts source code repositories and documentation into rich, queryable knowledge graphs.
   - Maps call trees, class hierarchies, dependency imports, and architectural coupling into Neo4j / NetworkX graph formats.
   - Enhances RAG retrieval by navigating topological code relationships rather than naive vector search.
2. **Headroom Desktop (headroomlabs-ai/headroom, gglucass/headroom-desktop)**:
   - Multi-agent developer productivity workspace providing interactive agent supervision, context persistence, and tool routing.
   - Visual inspection of agent scratchpads, task state machines, and file modifications.

## 🛠️ Usage & Key Recipes
- **Graphify Code Graph**:
  `ash
  graphify analyze --repo ./my-codebase --output graph.json
  `
- **Topological Traversal**: Query incoming/outgoing references to locate all impact zones before refactoring.
