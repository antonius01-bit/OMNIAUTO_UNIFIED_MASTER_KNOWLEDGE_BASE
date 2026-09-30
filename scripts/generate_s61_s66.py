import os

base_plugin = r"C:\Users\antoni\.gemini\config\plugins\dola-ai\skills"
base_dola = r"C:\Users\antoni\Dola\skills"

skills = {}

skills["scrapegraph-scrapling-stealth-scraper"] = """---
name: scrapegraph-scrapling-stealth-scraper
description: AI-driven autonomous scraping graphs (ScrapeGraphAI), undetectable anti-bot Cloudflare bypass (Scrapling), and resilient element tracking.
---

# ScrapeGraphAI & Scrapling Stealth Scraper (S61)

## Overview
Next-generation web scraping and data extraction engine combining ScrapeGraphAI (prompt-driven graph scraping pipelines without CSS/XPath selectors) and Scrapling (undetectable scraping framework with automated Cloudflare bypass and adaptive element locating).

## Key Capabilities
1. Prompt-Driven Extraction (ScrapeGraphAI): Define natural language schemas; LLM automatically navigates the DOM and extracts structured JSON.
2. Undetectable Anti-Bot Bypass (Scrapling): Stealth HTTP headers, browser fingerprint masking, automated Cloudflare challenge resolution.
3. Resilient Element Locating: Adapts automatically when web pages change their class names, IDs, or layout hierarchies.
4. MCP Server & Claude Integration: Direct scrapling-mcp and scrapegraph-mcp tool calling for autonomous coding agents.

## Activation
- Command: /omni-auto scrapegraph: Extract [data_schema] from [url] using prompt-driven graph pipeline
- Stealth Command: /omni-auto scrapling: Bypass anti-bot and stealthily scrape [url] with adaptive element tracking
"""

skills["supabase-cloud-postgres-architect"] = """---
name: supabase-cloud-postgres-architect
description: Enterprise Postgres backend architecture, database branching with GitHub, pgvector embeddings, and RLS security policies via Supabase.
---

# Supabase Cloud Postgres Architect (S62)

## Overview
Comprehensive cloud database and backend platform engineering powered by Supabase (supabase/supabase). Automates relational database design, database branching with GitHub PR integration, pgvector vector search, Edge Functions, and enterprise Row-Level Security (RLS).

## Key Capabilities
1. Database Branching & CI/CD: Automated preview databases for GitHub pull requests, migration verification, and schema diffing.
2. Vector Embeddings (pgvector): Native semantic search, hybrid keyword-vector indexing, and AI document chunk retrieval.
3. Row-Level Security (RLS) Engine: Mathematical access-control policies guaranteeing multi-tenant data isolation.
4. Realtime & Edge Functions: WebSocket change data capture (CDC) and low-latency Deno/TypeScript serverless functions.

## Activation
- Command: /omni-auto supabase: Architect schema and RLS policies for [domain_model] with pgvector embeddings
- Branching Command: /omni-auto supabase-branch: Set up database branching pipeline for GitHub repository [repo]
"""

skills["nocodb-smart-database-spreadsheet"] = """---
name: nocodb-smart-database-spreadsheet
description: Open-source Airtable alternative transforming SQL databases into smart collaborative spreadsheets and instant REST/GraphQL APIs via NocoDB.
---

# NocoDB Smart Database Spreadsheet (S63)

## Overview
Smart database management and automated API gateway powered by NocoDB (nocodb/nocodb). Connects to existing PostgreSQL, MySQL, SQL Server, or SQLite instances and transforms them into collaborative Airtable-like spreadsheet interfaces with instant REST and GraphQL endpoints.

## Key Capabilities
1. SQL-to-Spreadsheet Bridge: Connects directly to production databases without schema migrations; renders rich views (Grid, Gallery, Kanban, Form).
2. Instant API Generation: Automatically generates Swagger/OpenAPI-compliant REST and GraphQL endpoints with pagination and filtering.
3. Formula & Virtual Columns: Computes complex business formulas, rollup aggregations, and multi-table relationships.
4. Webhooks & Automations: Dispatches event-driven webhooks on record creation, updates, and deletes to n8n or internal microservices.

## Activation
- Command: /omni-auto nocodb: Connect [database_url] and generate collaborative spreadsheet views with REST APIs
"""

skills["posthog-product-analytics-os"] = """---
name: posthog-product-analytics-os
description: Full-stack Product OS covering event funnels, session replay, feature flags, A/B experiments, and AI agent observability via PostHog.
---

# PostHog Product Analytics OS (S64)

## Overview
Complete product analytics, session recording, and feature experiment platform powered by PostHog (PostHog/posthog). Provides end-to-end telemetry for modern web/mobile applications and AI agents, enabling data-driven growth, root-cause debugging, and safe feature rollouts.

## Key Capabilities
1. Product Telemetry & Funnels: Tracks user actions, conversion funnels, retention cohorts, and drop-off points.
2. Session Replay & Console Logs: High-fidelity DOM session recordings synchronized with network waterfalls and error logs.
3. Feature Flags & Multivariate A/B Testing: Statistical significance calculation, gradual rollouts, and kill-switches.
4. AI Observability & PostHog MCP: Native LLM tracing (tokens, latency, cost) and direct MCP server integration for autonomous diagnosis.

## Activation
- Command: /omni-auto posthog: Configure analytics tracking, session replay, and feature flag for [feature/app]
- Experiment Command: /omni-auto posthog-experiment: Design A/B testing experiment for [metric_goal] with significance threshold
"""

skills["calcom-enterprise-scheduling-engine"] = """---
name: calcom-enterprise-scheduling-engine
description: Enterprise appointment scheduling infrastructure, multi-calendar synchronization, booking API webhooks, and self-hosted Cal.com deployments.
---

# Cal.com Enterprise Scheduling Engine (S65)

## Overview
Self-hosted and enterprise scheduling infrastructure engine powered by Cal.com (calcom/cal.com). Automates calendar booking, multi-calendar conflict checking, dynamic availability rules, round-robin team scheduling, and booking API integrations.

## Key Capabilities
1. Multi-Calendar Sync: Two-way synchronization across Google Calendar, Office 365, Apple Calendar, and CalDAV.
2. Dynamic Routing & Round-Robin: Routes prospects to the optimal team member based on criteria, time zones, and availability.
3. Webhook & Payment Workflows: Dispatches booking webhooks to CRM/Zapier/n8n and accepts deposits via Stripe.
4. White-Label Self-Hosting: Docker and Kubernetes deployment templates with custom branding (cal.diy).

## Activation
- Command: /omni-auto calcom: Configure event booking type [meeting_name] with availability rules and webhook notifications
"""

skills["firecrawl-terax-agent-plugins"] = """---
name: firecrawl-terax-agent-plugins
description: Native Claude Code & Codex Firecrawl plugins combined with Terax AI lightweight terminal-first developer workspace.
---

# Firecrawl & Terax Agent Plugins (S66)

## Overview
Specialized agent integration and terminal-native developer environment combining Firecrawl Plugins for Claude Code and Codex (firecrawl/firecrawl-claude-plugin) with Terax AI (crynta/terax-ai), a 7MB terminal-first AI development workspace.

## Key Capabilities
1. Claude Code & Codex Firecrawl Plugins: Injects clean markdown crawling and search directly into agent CLI toolkits.
2. Terax Terminal Workspace: Ultra-lightweight (7MB), instant-launch terminal workspace with AI-native execution and session persistence.
3. Multi-Turn Command Memory: Preserves bash execution contexts, terminal outputs, and intermediate states across developer sessions.

## Activation
- Command: /omni-auto firecrawl-plugin: Enable Firecrawl tool calling within Claude Code or Codex runtime
- Terminal Command: /omni-auto terax: Launch lightweight terminal AI session for [development_task]
"""

for name, content in skills.items():
    p1 = os.path.join(base_plugin, name, "SKILL.md")
    p2 = os.path.join(base_dola, name, "SKILL.md")
    os.makedirs(os.path.dirname(p1), exist_ok=True)
    os.makedirs(os.path.dirname(p2), exist_ok=True)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print("Installed:", name)
