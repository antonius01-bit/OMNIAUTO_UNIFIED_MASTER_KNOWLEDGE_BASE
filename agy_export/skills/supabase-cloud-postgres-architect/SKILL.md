---
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
