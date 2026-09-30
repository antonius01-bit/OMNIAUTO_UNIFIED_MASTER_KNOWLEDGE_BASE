---
name: humanlayer-12factor-agent-platform
description: Enterprise Human-in-the-Loop (HITL) agent control plane and 12-Factor Agent methodology combining multiplayer coding agent IDEs, schema-first typed state machines (@humanlayer/effect-machine), durable event streams, and sync-based platforms.
---

# S90: HumanLayer 12-Factor Agent Platform (humanlayer-12factor-agent-platform)

## ⚡ Overview & 12-Factor Architecture
Synthesized from HumanLayer ecosystem (humanlayer.dev, 12-factor-agents, effect-machine, electric):
1. **The 12-Factor Agent Principles**:
   - Factor 1: Codebase Grounding (Strict context boundary).
   - Factor 2: Declarative Tool Contracts (Typed schema contracts).
   - Factor 3: Human Approval Gates (Gated destructive actions).
   - Factor 4: Stateless Inference & External State (State stored in event logs).
   - Factor 5: Build, Release, Run Isolation (Separation of prompt config from execution).
   - Factor 6: Disposable Processes (Instant agent spin-up and teardown).
   - Factor 7: Port Binding & Protocol Independence (CLI/MCP/REST agnosticism).
   - Factor 8: Concurrency & Forking (Parallel worker evaluation).
   - Factor 9: Disposability & Crash-First Design (Fault tolerance).
   - Factor 10: Dev/Prod Parity (Identical tool environments).
   - Factor 11: Logs as Event Streams (Streaming diffs and telemetry).
   - Factor 12: Admin & Inspection Tooling (Multiplayer control plane).
2. **Schema-First State Machines (@humanlayer/effect-machine)**:
   - Type-safe actors and finite state machines built on Effect-TS.
   - Eliminates loose boolean flags; strictly models transitions, event streams, and error recovery.

## 🛠️ Usage in Omni-Auto
- **Command**: `/omni-auto humanlayer: Enforce 12-factor agent guardrails and HITL approval gates for [action/workflow]`
- Ensures zero unauthorized destructive actions on production environments.
