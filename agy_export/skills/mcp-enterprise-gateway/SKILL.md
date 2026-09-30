---
name: mcp-enterprise-gateway
description: >-
  Comprehensive Model Context Protocol (MCP) enterprise gateway, managing 50+ vetted MCP servers, FastMCP tool compilation, stdio/SSE transports, and secure tool routing.
---

# 🔌 Enterprise MCP Gateway & Multi-Tool Router (FastMCP + 50+ Servers)

Use this skill when configuring, discovering, building, or managing Model Context Protocol (MCP) clients and servers across developer environments.

## Architecture

```mermaid
flowchart LR
    subgraph AgentClient ["AI Agent Host (Antigravity / Claude / Cursor)"]
        AC["Agent Core"] --> TR["MCP Tool Router"]
    end

    subgraph Transports ["Transports & Gateways"]
        TR --> T1["Stdio Protocol (Subprocess)"]
        TR --> T2["Server-Sent Events (SSE / HTTP)"]
    end

    subgraph ServerCatalog ["50+ Enterprise MCP Servers"]
        T1 & T2 --> S1["Databases: Postgres, MySQL, SQLite, Neo4j, Redis"]
        T1 & T2 --> S2["Developer: GitHub, GitLab, Sentry, Docker, Kubernetes"]
        T1 & T2 --> S3["Web & Browsing: Puppeteer, Brave Search, Fetch, Playwright"]
        T1 & T2 --> S4["Workplace: Slack, Notion, Linear, Google Drive, Jira"]
    end
```

## Supported Server Categories & Tools
1. **Developer Tools**: `github` (PRs, issues, commits), `git` (local diffs), `sentry` (error monitoring), `docker` (container inspect/run).
2. **Databases**: `postgres` (schema inspect, read-only queries, transactions), `sqlite`, `redis` (cache key lookup).
3. **Web & Automation**: `brave-search` (web queries), `puppeteer` (full DOM interaction), `fetch` (HTML to markdown).
4. **Productivity**: `slack` (channel messages), `notion` (pages & databases), `linear` (issue tracking).

## Configuration Standard (`mcp_config.json`)
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "<TOKEN>" }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": { "BRAVE_API_KEY": "<KEY>" }
    }
  }
}
```

## How to Use
`Configure and register MCP server [server_name/package] with environment variables in mcp_config.json and test tool availability.`
