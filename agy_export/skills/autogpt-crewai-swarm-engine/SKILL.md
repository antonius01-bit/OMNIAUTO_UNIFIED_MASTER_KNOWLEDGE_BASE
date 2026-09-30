---
name: autogpt-crewai-swarm-engine
description: Autonomous goal-driven task execution and collaborative role-playing agent crews powered by AutoGPT (Significant Gravitas) and CrewAI.
---

# AutoGPT and CrewAI Swarm Engine (S57)

## Overview
Enterprise multi-agent goal pursuit and role-playing orchestration engine fusing AutoGPT (Significant-Gravitas/AutoGPT) and CrewAI (crewAIInc/crewAI). Executes multi-step autonomous objectives, manages agent task dependencies, and enforces collaborative delegation across specialized crew roles.

## Architecture
1. Goal-Driven Autonomy (AutoGPT): High-level objective decomposition into milestone sub-tasks, persistent memory, and self-directed loops.
2. Crew Collaboration (CrewAI): Role-playing definitions (Role, Goal, Backstory), hierarchical and sequential process management, tool sharing, and structured handoffs.

## Activation
- AutoGPT Mode: /omni-auto autogpt: Execute goal [autonomous_objective] with milestone verification
- CrewAI Mode: /omni-auto crew: Assemble crew of [researcher, writer, critic] to execute [project_workflow]
