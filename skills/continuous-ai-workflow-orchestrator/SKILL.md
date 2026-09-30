---
name: continuous-ai-workflow-orchestrator
description: >-
  Event-driven workflow orchestration and Continuous AI automation engine based on GitHub Next Continuous AI, n8n templates, Temporal, and Prefect. Automates self-healing pipelines, scheduled jobs, webhook routing, and multi-service workflows.
---

# ⚡ Continuous AI & Workflow Orchestrator (GitHub Next + n8n + Temporal Fusion)

Use this skill when designing, implementing, and deploying event-driven automation pipelines, background workers, scheduled cron jobs, webhook handlers, and self-healing multi-service integrations.

## Architecture & Flow

```mermaid
flowchart LR
    subgraph Triggers ["1. Event Ingestion"]
        E1["Webhook / HTTP Request"] --> D["Event Dispatcher"]
        E2["Cron Schedule (00:00)"] --> D
        E3["Git Commit / PR Event"] --> D
    end

    subgraph Orchestrator ["2. Fault-Tolerant Execution"]
        D --> W["Workflow DAG Engine (Temporal / n8n / Airflow)"]
        W --> T1["Task 1: Data Ingestion & Sanitization"]
        T1 --> T2["Task 2: AI Processing / LLM Step"]
        T2 --> T3["Task 3: Downstream Sync / Database Commit"]
    end

    subgraph SelfHealing ["3. Resilience & Self-Healing"]
        T2 -. Fail .-> SH["Auto-Retry with Exponential Backoff + Key Rotation"]
        SH --> T2
    end
```

## Core Capabilities
1. **Self-Healing Automation**: Automatic error interception, exponential backoff, dead-letter queuing, and provider rotation.
2. **Visual & Declarative Workflows**: Generates structured n8n workflow JSON, Temporal activity definitions, and Airflow DAGs.
3. **Continuous AI Feedback Loops**: Automatically tests new code commits against benchmarks and logs telemetry.

## How to Use
`Design and deploy automated workflow for [integration/event] with scheduled triggers, error handling, and notification webhooks.`
