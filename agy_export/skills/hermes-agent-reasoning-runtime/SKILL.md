---
name: hermes-agent-reasoning-runtime
description: Hermes Agent reasoning runtime, structured function calling, XML/JSON tool routing, and multi-turn chain-of-thought deliberation trees powered by NousResearch.
---

# ⚡ Hermes Agent Reasoning Runtime (S119)

Industrial-grade autonomous agent reasoning engine and structured tool calling harness powered by **NousResearch** (`NousResearch/hermes-agent` - 243.6k★). Delivers state-of-the-art function calling, interleaved reasoning, and adversarial prompt resilience.

---

## 🧠 1. Structured Function Calling Architecture

Hermes implements strict JSON/XML tool calling contracts with pre-execution validation:

```xml
<tools>
  <tool_call>
    <name>execute_action</name>
    <arguments>{"target": "deploy_service", "params": {"cluster": "us-east-1", "nodes": 4}}</arguments>
  </tool_call>
</tools>
```

### Pre-Execution Deliberation (Chain-of-Thought Scratchpad):
Before issuing any tool call, Hermes enforces a deliberation block:
1. **Hypothesis**: What is the immediate objective of this tool call?
2. **Preconditions**: Are all required parameters verified and grounded in facts?
3. **Failure Mode Analysis**: What happens if the tool returns a non-zero exit code or schema validation error?
4. **Action**: Dispatch tool call.

---

## 🛡️ 2. Adversarial Tool Robustness & Safety Gates

1. **Jailbreak Defenses**: Sanitizes inputs against prompt injection hidden inside external API responses, web crawl buffers, or file contents.
2. **Schema Enforcement**: Drops hallucinated arguments not defined in the tool signature.
3. **Interleaved Observation Loops**: Evaluates the raw observation immediately before proceeding to the next step, preventing cascading erroneous assumptions.

---

## 🚀 3. Trigger & Workflows
- **Trigger**: `/omni-auto hermes-agent` atau `/hermes-reasoning`
- **Sub-skills**:
  - `hermes_tool_router`: Routing dinamis pemanggilan tool berbasis intent multi-tahap.
  - `hermes_cot_deliberator`: Blok pemikiran mendalam sebelum aksi berisiko.
  - `hermes_schema_validator`: Validasi tipe dan parameter fungsi saat runtime.
