---
name: anthropic-commerce-agent-blueprints
description: Official Anthropic reference blueprint for building customer shopping agents and merchant back-office agents with Claude, featuring strict tool contracts, staged human approval gates, and multi-vertical enterprise commerce workflows.
---

# S93: Anthropic Commerce Agents & Multi-Domain Blueprints (anthropic-commerce-agent-blueprints)

## ⚡ Overview & Architectural Blueprints
Synthesized from Anthropic's official `anthropics/commerce-agents` and repository collection:
1. **Dual-Agent Architecture**:
   - **Shopping Agent**: Customer-facing conversational agent embedding search, personalized recommendations, cart composition, and staged checkout.
   - **Merchant Agent**: Back-office operational agent managing inventory, pricing adjustments, fulfillment tracking, and campaign optimization.
2. **Declarative Tool Contracts & Guardrails**:
   - Single definition of prompt, skills, tool schemas, and validation gates running on the Messages API and Claude Agent SDK.
   - Strictly staged writes: No live orders or payment authorizations occur autonomously; actions are staged until validated by host application or human approver.
3. **Multi-Vertical Reference Implementations**:
   - Production blueprints across Retail, Telecommunications, B2B SaaS Commerce, and Digital Entertainment.

## 🛠️ Usage in Omni-Auto
- **Command**: `/omni-auto commerce: Architect Claude shopping or merchant agent for [vertical] with policy gates`
- Implements secure, compliant transactional AI systems for e-commerce, customer portals, and internal enterprise ERPs.
