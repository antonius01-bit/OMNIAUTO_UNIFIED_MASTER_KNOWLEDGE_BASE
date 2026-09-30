---
name: deepteam-ai-redteamer
description: >-
  Automated adversarial red teaming and safety evaluation engine powered by Confident AI DeepTeam. Tests agents for 40+ vulnerabilities (OWASP LLM Top 10, prompt injection, PII leaks, Crescendo jailbreaking).
---

# 🛡️ DeepTeam AI Red Teamer & Safety Evaluator (Confident AI DeepTeam)

Use this skill when auditing AI agents, prompts, or model outputs for security vulnerabilities, safety compliance (OWASP Top 10 for LLMs, NIST AI RMF), jailbreak resistance, or bias/hallucination risks.

## Architecture

```mermaid
flowchart TD
    subgraph Target ["1. Target Agent / System"]
        A["Agent Under Test (Model / API / Prompt)"]
    end

    subgraph RedTeamEngine ["2. DeepTeam Adversarial Attack Engine"]
        M1["Single-Turn Attacks (Leetspeak, ROT-13, Prompt Injection)"]
        M2["Multi-Turn Attacks (Crescendo, Tree, Linear Jailbreaks)"]
        M3["Vulnerability Scanners (PII, Harmful Content, Hallucination)"]
    end

    subgraph AuditReport ["3. Compliance & Risk Scorecard"]
        M1 & M2 & M3 --> R["OWASP Top 10 for LLMs & NIST AI RMF Scorecard"]
        R --> MIT["Automated Guardrails & Mitigation Hardening"]
    end

    Target <--> RedTeamEngine
```

## Core Vulnerability Checks (40+ Categories)
1. **Prompt Injection & System Prompt Extraction**: Testing susceptibility to direct and indirect prompt overrides.
2. **Multi-Turn Crescendo Jailbreaks**: Gradual trust-building multi-turn conversations designed to bypass safety filters.
3. **Data Leakage & PII Protection**: Auditing model memory and responses for sensitive credential exposure.
4. **Factual Integrity & Hallucination Scoring**: Quantifying truthfulness against grounded ground-truth baselines.

## How to Use
`Run adversarial red team audit on [agent/model/prompt] testing for [vulnerability_types] with DeepTeam scorecard.`
