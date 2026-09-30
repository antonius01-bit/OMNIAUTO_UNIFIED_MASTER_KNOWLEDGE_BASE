---
name: mcp-ecosystem-integrator
description: >-
  Connects, manages, and executes Model Context Protocol (MCP) servers and clients, bridging AI agents with local databases, cloud APIs, filesystem tools, and developer utilities.
---

# 🔌 MCP Ecosystem Integrator (Model Context Protocol)

Use this skill when integrating external MCP servers, discovering MCP tools, managing `mcp_config.json`, or communicating with MCP backends.

## Core Workflows
1. **Server Discovery**: Search and select MCP servers from `modelcontextprotocol/servers` or verified community packages (PostgreSQL, SQLite, GitHub, Brave Search, Puppeteer, Filesystem, Slack, Google Drive).
2. **Configuration Management**: Safely register servers into `~/.gemini/config/mcp_config.json` with appropriate environment variables and flags.
3. **Tool Invocation & Error Handling**: Call exposed MCP tools cleanly and format output into structured markdown tables and JSON for downstream processing.
