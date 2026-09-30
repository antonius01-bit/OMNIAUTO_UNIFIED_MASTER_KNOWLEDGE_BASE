---
name: anthropic-cybersecurity-arsenal-818
description: Complete enterprise cybersecurity defense, threat hunting, memory forensics, and AI red-teaming engine powered by Mukul975 818 procedural skills mapped to MITRE ATT&CK, NIST CSF 2.0, ATLAS, D3FEND, NIST AI RMF, and MITRE F3.
---

# 🛡️ S137 — Anthropic Cybersecurity Arsenal 818 (`anthropic-cybersecurity-arsenal-818`)

## 📌 Overview & Upstream Origin
- **Upstream Repository**: [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git)
- **Scale**: Exactly **818 granular, production-tested procedural cybersecurity playbooks** spanning:
  - MITRE ATT&CK (Enterprise, Cloud, Mobile, ICS/SCADA)
  - NIST Cybersecurity Framework (CSF 2.0: Identify, Protect, Detect, Respond, Recover, Govern)
  - MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)
  - MITRE D3FEND (Defensive Cybersecurity Countermeasures)
  - NIST AI Risk Management Framework (AI RMF 1.0)
  - MITRE F3 (Financial Fraud Framework)
- **Local Clone**: `C:/Users/antoni/Dola/clones/Anthropic-Cybersecurity-Skills/skills/`

---

## 🏛️ The 6-Framework Threat Coverage Matrix

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 Mukul975 818 Procedural Cybersecurity Suite                 │
├──────────────────────┬──────────────────────┬───────────────────────────────┤
│  Threat Hunting & IR │  Cloud & Kubernetes  │      AI & LLM Red-Teaming     │
├──────────────────────┼──────────────────────┼───────────────────────────────┤
│ • Memory Forensics   │ • AWS IAM Auditing   │ • Prompt Injection in RAG     │
│   (Volatility 3)     │ • Kube-bench CIS     │ • LLM Red-Teaming (Garak)     │
│ • Network Forensics  │ • S3 Misconfig Check │ • System Prompt Leakage Audit │
│   (Zeek, Tshark)     │ • Container Scanning │ • Agentic Tool Invocation     │
│ • Malware Triage     │   (Trivy, Grype)     │   Guardrails Validation       │
│   (YARA Rules)       │ • CloudTrail Triage  │ • Training Data Poisoning     │
├──────────────────────┼──────────────────────┼───────────────────────────────┤
│    Offensive SecOps  │  Industrial & SCADA  │      Governance & GRC         │
├──────────────────────┼──────────────────────┼───────────────────────────────┤
│ • External Pentest   │ • ICS Asset Discover │ • NIST CSF 2.0 Assessment     │
│ • Burp Suite Web App │ • S7comm Inspection  │ • SOC 2 Type II Preparation   │
│ • AFL++ Fuzzing      │ • PLC Firmware Audit │ • Privacy Impact Assessment   │
│ • Hashcat Cracking   │ • OT Network Defense │ • Post-Quantum Cryptography   │
└──────────────────────┴──────────────────────┴───────────────────────────────┘
```

---

## 🛠️ High-Frequency Operational Playbooks

### 1. Agentic AI & LLM Red-Teaming (`securing-agentic-ai-tool-invocation`)
- **Objective**: Audit autonomous AI tool execution loops for unsafe command injection, directory traversal, and unauthorized API token exfiltration.
- **Verification Rule**: Enforce JSON schema validation, human approval gates on dangerous actions, and environment isolation.

### 2. Memory Forensics with Volatility 3 (`performing-memory-forensics-with-volatility3`)
- Extract process trees (`windows.pstree`), hidden DLLs (`windows.ldrmodules`), and injected shellcode (`windows.malfind`) from raw RAM dumps.

### 3. Container & Kubernetes Hardening (`scanning-containers-with-trivy-in-cicd`)
- Automate zero-CVE container builds, enforce non-root user execution, and audit admission controllers.

---

## 💻 Operational Workflows & Triggers
- `/omni-auto sec-audit: Run 818-skill security audit against current codebase and cloud configuration.`
- `/omni-auto redteam-llm: Execute MITRE ATLAS adversarial prompts against AI agent tool endpoints.`
- `/omni-auto forensic-ir: Trigger incident response playbook for suspicious network logs or memory artifacts.`