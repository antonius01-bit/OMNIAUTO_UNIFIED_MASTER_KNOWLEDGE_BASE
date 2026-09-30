---
name: harness-engineering-super-scaffolding
description: Enterprise agentic harness engineering and runtime scaffolding framework based on WalkingLabs (learn-harness-engineering), awesome-harness-engineering, and Andrew Ng's 4 Agentic Design Patterns. Governs execution sandboxing, automated feedback self-correction loops, deterministic state machines, and AGENTS.md system constraints.
---

# 🏗️ S130 — Harness Engineering Super Scaffolding (`harness-engineering-super-scaffolding`)

## 📌 Overview & Upstream Origin
- **Upstream Repositories**:
  - [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) (Project-based guide on moving from 0 to 1 in building production-grade AI coding agent harnesses).
  - [walkinglabs/awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering) (Curated catalog of harness tools, sandboxes, and supervisor architectures).
  - [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) & [Jiaaqiliu/Awesome-Harness-Engineering](https://github.com/Jiaaqiliu/Awesome-Harness-Engineering).
  - [Picrew/awesome-agent-harness](https://github.com/Picrew/awesome-agent-harness) (Agent harness evaluation and runtime benchmarks).
  - [Andrew Ng Agentic Design Patterns](https://github.com/andrewyng/translation-agent) (Reflection, Planning, Tool Use, Multi-Agent Collaboration).
- **Core Philosophy**: **"Agent = Model + Harness"**. While LLMs provide reasoning and intelligence, the **Harness** supplies the operational boundaries, tool contracts, execution sandboxes, test-driven feedback loops, and memory checkpoints necessary to transform stochastic completions into reliable, zero-regression production software.

---

## 🏛️ The 5 Pillars of Harness Engineering

```
┌────────────────────────────────────────────────────────────────────────┐
│                        AGENT RUNTIME HARNESS                           │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Context Governance & Constraints:                                  │
│    • AGENTS.md / CLAUDE.md declarative rule enforcement                │
│    • Surgical diff bounds (YAGNI, minimal line edits)                 │
├────────────────────────────────────────────────────────────────────────┤
│ 2. Control Loops & State Machine:                                      │
│    • Staged lifecycle: Research -> Planning -> Approval -> Execution  │
│    • Checkpointing & rollback state graph                              │
├────────────────────────────────────────────────────────────────────────┤
│ 3. Sandboxed Tool Execution:                                           │
│    • Safe containerized shell / microVM isolation                      │
│    • Strict argument typing & timeout watchdogs                        │
├────────────────────────────────────────────────────────────────────────┤
│ 4. Automated Feedback & Self-Correction:                               │
│    • Test-Driven Loop: Run pytest/jest -> Catch stderr -> Auto-Reprompt│
│    • Linter & AST static analysis gatekeepers                          │
├────────────────────────────────────────────────────────────────────────┤
│ 5. Memory & Context Budgeting:                                         │
│    • Dynamic context window trimming & token eviction                  │
│    • Cross-session persistent scratchpad persistence                   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## ⚡ Andrew Ng's 4 Core Agentic Patterns Integrated

1. **Reflection Pattern**:
   - The agent critiques its own intermediate generation (code, manuscript, or architectural plan) against explicit rubrics before finalizing output.
   - Example: Translation / code refinement loop ($Draft \to Critique \to Polish$).
2. **Tool Use Pattern**:
   - Strict typed schema contracts. Every tool call must return structured JSON or plain text with explicit error handling.
3. **Planning Pattern**:
   - Mandatory decomposition into sub-goals before tool execution. Prevents unguided rambling and premature code modifications.
4. **Multi-Agent Collaboration Pattern**:
   - Distinct role personas (Architect, Coder, Critic, Security Auditor) with explicit communication protocols and handover contracts.

---

## 🛡️ The Feedback Self-Correction Loop Contract

When an agent executes an action (e.g. code modification), the harness enforces an automated feedback loop:
```
[Agent Action] ──> [Harness Execution] ──> [Automated Test / Lint]
                           │                           │
                           │ Passed                    │ Failed (stderr)
                           ▼                           ▼
                   [Commit & Proceed]        [Harness Injects Error]
                                                       │
                                                       ▼
                                             [Agent Reflexion & Fix]
```
- **Rule**: If a test fails, the agent must NOT ask the human for help. The harness re-injects the exact traceback and diff into the agent's prompt until tests pass or the max retry budget ($K=3$) is reached.

---

## 🛠️ Operational Workflows & Triggers

### 1. Initialize Harness Scaffolding for Codebase
```bash
/omni-auto harness-init: Scaffold AGENTS.md, test harness, pre-commit linter gates, and reflection loop for [repo_path].
```

### 2. Run Test-Driven Self-Correction Sprint
```bash
/omni-auto harness-tdd: Implement [feature] with strict TDD harness. Generate failing test, code implementation, auto-run pytest, and iterate until green.
```

### 3. Audit Agent Tool Boundaries & Safety
```bash
/omni-auto harness-audit: Inspect tool schemas, sandbox timeouts, and permission boundaries for [agent_config.json].
```