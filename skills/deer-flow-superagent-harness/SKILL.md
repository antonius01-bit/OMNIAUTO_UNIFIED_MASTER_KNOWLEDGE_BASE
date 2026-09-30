---
name: deer-flow-superagent-harness
description: Long-horizon autonomous SuperAgent harness by ByteDance for multi-hour research, coding, and creative tasks with sandboxed environments, subagent routing, memory gateways, and multi-lingual skill execution.
---

# S89: ByteDance Deer-Flow SuperAgent Harness (deer-flow-superagent-harness)

## ⚡ Overview & Architecture
Synthesized from ByteDance Deer-Flow and DeerFlow 2.0 Enhanced:
1. **Long-Horizon SuperAgent Harness**:
   - Designed to run complex multi-step tasks that scale from minutes to multiple hours without drift.
   - Built-in sandboxed execution environments for isolated, reproducible code and tool execution.
2. **Subagent Delegation & Message Gateway**:
   - Hierarchical subagent routing with specialized worker dispatching.
   - Durable message gateways for asynchronous agent-to-agent event passing and human interjection.
3. **Multi-Modal Memory & State Checkpointing**:
   - Long-term memory store tracking goals, context snapshots, tool artifacts, and execution histories.
   - Fault-tolerant pause, resume, and rollback capabilities across complex execution graphs.

## 🛠️ Usage in Omni-Auto
- **Command**: `/omni-auto deer-flow: Execute long-horizon task [task_description] with sandboxed execution and memory checkpointing`
- Powers long-running research synthesis, codebase migration, and multi-step artifact generation.
