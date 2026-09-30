---
name: anthropic-cybersecurity-redteam-playbooks
description: Structured, framework-mapped procedural cybersecurity playbooks for AI agents based on mukul975 Anthropic-Cybersecurity-Skills and OSINT Team. Systematically cross-referenced against 6 international frameworks (MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF, MITRE F3) for threat hunting, memory forensics, vulnerability assessment, and AI red-teaming.
---

# 🛡️ S131 — Anthropic Cybersecurity Red-Team Playbooks (`anthropic-cybersecurity-redteam-playbooks`)

## 📌 Overview & Upstream Origin
- **Upstream Repositories & Guides**:
  - [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) (Open-source library of structured, framework-mapped cybersecurity playbooks for AI agents).
  - [OSINT Team Tutorial](https://osintteam.blog/anthropic-cybersecurity-skills-full-tutorial-4b3621f14c59) (Comprehensive operational guide for agentic threat hunting, DFIR, and red-teaming).
  - Supported Platforms: Claude Code CLI, Cursor, Codex CLI, Gemini CLI, and Antigravity.
- **Core Methodology**: Replaces generic prompting with standardized, repeatable `SKILL.md` procedural playbooks. Every security task is mapped to established international security ontologies, enforces verification gates, and produces forensic-grade artifacts without hallucinations.

---

## 🏛️ The 6 Mapped Cybersecurity Frameworks

```
┌────────────────────────────────────────────────────────────────────────┐
│             ANTHROPIC CYBERSECURITY AGENT FRAMEWORK MATRIX             │
├────────────────────────────────────────────────────────────────────────┤
│ 1. MITRE ATT&CK: Enterprise adversary tactics, techniques & procedures │
│    (Initial Access, Execution, Persistence, Privilege Escalation)      │
├────────────────────────────────────────────────────────────────────────┤
│ 2. NIST CSF 2.0: Core cybersecurity functions                          │
│    (Govern, Identify, Protect, Detect, Respond, Recover)               │
├────────────────────────────────────────────────────────────────────────┤
│ 3. MITRE ATLAS: Adversarial Threat Landscape for AI Systems            │
│    (Prompt Injection, Training Data Poisoning, Model Inversion)        │
├────────────────────────────────────────────────────────────────────────┤
│ 4. D3FEND: Defensive countermeasure ontology and mitigation mapping    │
│    (Process Lineage Tracking, Credential Eviction, Memory Isolation)   │
├────────────────────────────────────────────────────────────────────────┤
│ 5. NIST AI RMF: AI Risk Management Framework                           │
│    (Validating safety, fairness, transparency, and resilience)        │
├────────────────────────────────────────────────────────────────────────┤
│ 6. MITRE F3: Fight Fraud Framework                                     │
│    (Synthesized identity fraud, credential stuffing, bot mitigation)   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## ⚡ Core Operational Playbooks

### 1. Threat Hunting & Detection Engineering
- Generates and tests **Sigma rules** against Windows Security Event logs (Event ID 4688, 4624, 7045) and Sysmon logs (Event ID 1, 3, 10, 11).
- Formulates multi-clause **YARA rules** for binary payload classification and memory scraping.
- Correlates network artifacts (Zeek / Suricata logs) against MITRE ATT&CK Command and Control ($T1071$) techniques.

### 2. Digital Forensics & Incident Response (DFIR)
- **Memory Forensics**: Automated extraction of process trees, DLL injections, and unlinked VAD structures via Volatility 3.
- **Timeline Reconstruction**: Builds master chronologies from NTFS $MFT, shimcache, amcache, and prefetch files.
- **Chain of Custody Guarantee**: Cryptographically hashes ($SHA-256$) all inspected disk dumps and log extracts.

### 3. Vulnerability Assessment & Auto-Remediation
- Scans repositories against OWASP Top 10 (SQLi, SSRF, IDOR, Broken Authentication).
- Validates proof-of-concept exploits safely inside sandboxes to eliminate false positives.
- Generates surgical, minimal code diffs and regression unit tests to patch vulnerabilities.

### 4. Adversarial AI Red-Teaming & Jailbreak Auditing
- Systematically audits LLM agents against MITRE ATLAS:
  - Direct & Indirect Prompt Injection ($AML.T0051$).
  - System Prompt Leakage & Extraction ($AML.T0054$).
  - Jailbreak Fuzzing: Evaluates Crescendo multi-turn coaxing, cipher encoding, and role-playing attacks.
  - Generates adversarial robustness scorecard with pass/fail metrics.

---

## 🛠️ Operational Workflows & Triggers

### 1. Execute Adversarial Red-Team Audit on Agent Prompt/System
```bash
/omni-auto sec-redteam: Audit [system_prompt.md/agent_config] against MITRE ATLAS and NIST AI RMF. Fuzz for prompt injection, leakage, and privilege bypass.
```

### 2. Threat Hunting on Security Logs
```bash
/omni-auto sec-hunt: Ingest [sysmon_logs.json/evtx] and hunt for lateral movement ($T1021$) and credential dumping ($T1003$). Generate Sigma rule and remediation guide.
```

### 3. Codebase Vulnerability Scan & Surgical Patch
```bash
/omni-auto sec-audit: Perform NIST CSF 2.0 vulnerability assessment on [repo_path]. Identify critical flaws, validate POCs in sandbox, and generate surgical security patches.
```