---
name: codebase-memory-mcp-engine
description: Ultra-high-performance pure-C codebase knowledge graph MCP server, sub-millisecond AST indexing across 158 languages, and persistent agent memory based on DeusData & win4r Codebase Memory MCP Pro.
---

# 🧠 Codebase Memory MCP Engine (S50)

## Overview
Ultra-high-performance codebase knowledge graph engine powered by **DeusData Codebase Memory MCP** and **win4r Codebase Memory MCP Pro**. Indexes entire codebases into persistent AST symbol graphs in milliseconds, enabling sub-millisecond symbol queries, call-graph tracking, and reducing agent token consumption by up to 99%.

## Key Capabilities
1. **Persistent Code Knowledge Graph**: Builds symbol nodes (functions, classes, interfaces, traits) and edge relationships (CALLS, DEFINES, REFERENCES, IMPORTS) across 158 programming languages.
2. **Sub-ms Symbol Retrieval**: Instant lookup of function signatures, usages, and call hierarchies without full-file reading.
3. **99% Token Reduction**: AI agents query only relevant symbol subgraphs instead of feeding raw multi-thousand-line files into LLM context.
4. **Incremental Hot Reindexing**: Sub-second re-indexing on file edits with CALLS-edge preservation and git diff awareness.

## Standard MCP Tools Exposed
- index_codebase(path, depth): Build or refresh persistent AST graph database.
- search_symbols(query, kind): Fast lookup of functions, methods, classes by name or pattern.
- get_callers(symbol_name) / get_callees(symbol_name): Traverse the directional invocation graph.
- get_architecture_summary(): High-level module hierarchy and dependency matrix.

## Activation
- Command: /omni-auto memory: Index codebase [path] and trace call graph for symbol [function_name]
