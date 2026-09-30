---
name: langflow-visual-rag-builder
description: >-
  Visual multi-agent RAG pipeline builder, frontend code review auditor, and AI product manager engineering engine powered by Langflow and Product Manager Skills.
---

# 🧩 Langflow Visual RAG Builder & Product Engineering Suite

Use this skill when constructing modular RAG pipelines visually, auditing frontend code architecture, drafting AI Product Requirement Documents (PRDs), or mapping agentic logic into executable Langflow JSON graphs.

## Architecture

```mermaid
flowchart TD
    subgraph PMProduct ["1. AI Product Management (deanpeters/Product-Manager-Skills)"]
        PRD["PRD & User Story Formulation"] --> SPEC["Agentic Functional Requirements & KPIs"]
    end

    subgraph LangflowEngine ["2. Langflow Visual Multi-Agent Architecture (langflow-ai/langflow)"]
        SPEC --> VEC["Vector Store & Document Chunking Nodes"]
        SPEC --> LLM["Model Routing & Prompt Template Nodes"]
        SPEC --> TOOL["Custom Tool & Python Execution Nodes"]
    end

    subgraph ReviewQuality ["3. Frontend & Architecture Review (langflow frontend-code-review)"]
        VEC & LLM & TOOL --> REV["Frontend Code Review Audit (React / TS / Accessibility)"]
        REV --> OUT["Deployable Langflow JSON Flow & Production Web Component"]
    end
```

## Key Capabilities
1. **Langflow Flow Generation**: Builds valid, deployable Langflow JSON graph definitions containing vector stores, prompt chains, and agents.
2. **Frontend Code Review Skill**: Audits React/TypeScript components for state management efficiency, accessibility (a11y), and zero UI bloat.
3. **AI Product Manager Skills**: Generates structured PRDs, user stories with Gherkin acceptance criteria, and technical milestone roadmaps.

## How to Use
`Design Langflow multi-agent RAG graph for [product_concept] with PRD specification and frontend review checklist.`
