---
name: deerflow-superagent-multimodal-harness
description: Long-horizon autonomous SuperAgent harness, multi-modal reasoning workflows, multi-tool sandbox coordination, and recursive execution pipelines.
---

# 🦌 DeerFlow SuperAgent Multimodal Harness (S142)

## 📌 Overview & Core Architecture
The `deerflow-superagent-multimodal-harness` Super-Skill implements ByteDance's groundbreaking DeerFlow 2.0 architecture and long-horizon SuperAgent execution contracts:
1. **Long-Horizon Multi-Step Task Execution**: Multi-hour autonomous problem solving capable of deep recursive tree searches, backtracking, and state checkpointing.
2. **Multimodal Agent Cognition**: Native visual DOM grounding, GUI action synthesis, document diagram comprehension, and audio/video frame analysis.
3. **Sandboxed Multi-Tool Dispatcher**: Safe terminal execution, isolated Python runtimes, browser environments, and MCP gateway orchestration.
4. **Hierarchical Subagent Swarm**: Goal decomposition into Directed Acyclic Graphs (DAGs) executed by specialized subagents with strict completion contracts.

---

## ⚡ Core Operational Modes & Commands
- `/deer-flow launch [goal]`: Decomposes complex multi-stage objectives into execution DAGs with checkpointed rollback recovery.
- `/superagent-harness sandbox`: Spins up an ephemeral, isolated execution runtime with strict resource caps and audit logging.
- `/multimodal-workflow run`: Executes end-to-end visual comprehension and GUI action pipelines.
- `/long-horizon-agent status`: Inspects task tree progression, node dependencies, and active tool budgets.

---

## ⚙️ Architectural Contracts
- **State Machine**: Explicit state transitions: `PENDING` $	o$ `PLANNING` $	o$ `DISPATCHED` $	o$ `EXECUTING` $	o$ `VERIFYING` $	o$ `COMPLETED`.
- **Fault Recovery**: Automatic timeout detection, exception catching, and alternative tool cascade fallback.
- **Artifact Governance**: Zero side-effect rule; all generated assets must be verified against predefined acceptance tests before merging.
