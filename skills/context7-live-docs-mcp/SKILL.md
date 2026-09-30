---
name: context7-live-docs-mcp
description: >-
  Real-time version-specific documentation and anti-hallucination MCP engine powered by Upstash Context7. Injects live, verified code examples and library APIs directly into AI coding workflows.
---

# 📚 Context7 Live Docs & Anti-Hallucination MCP Engine (Upstash Context7)

Use this skill when developing with modern frameworks (React, Next.js, Express, Prisma, Tailwind, FastMCP) to eliminate hallucinated methods, retrieve live version-specific docs, or verify API signatures.

## Architecture

```mermaid
flowchart LR
    subgraph Prompt ["1. Coding Request"]
        U["User Task: 'Build Next.js middleware with JWT auth'"] --> T["Trigger: 'use context7'"]
    end

    subgraph MCPContext7 ["2. Context7 MCP Server (upstash/context7)"]
        T --> C7["Context7 Real-Time Resolver (npx ctx7)"]
        C7 --> G["Official Upstream Repositories (50+ Supported)"]
    end

    subgraph GroundedCode ["3. Verified Execution"]
        G --> API["Exact API Signatures & Version-Specific Syntax"]
        API --> OUT["100% Working, Non-Deprecating Code"]
    end
```

## Core Capabilities
1. **Zero Hallucinated APIs**: Direct grounding in official upstream source code and documentation.
2. **Version-Specific Precision**: Supports Next.js App Router, React 19, Prisma v6, Tailwind v4, Pydantic v2.
3. **Dual Execution Modes**:
   - **MCP Native**: Operates as a background MCP server responding to AI agent tool calls.
   - **CLI Mode**: Direct lightweight lookups via `npx ctx7`.

## How to Use
`Write [feature/code] for [framework] using [version]. use context7.`
