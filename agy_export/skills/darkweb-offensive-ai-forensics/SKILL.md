---
name: darkweb-offensive-ai-forensics
description: Security auditing, AI infrastructure exposure scanning (Bishop Fox AIMap), dark-web OSINT crawling (Robin), mobile forensics (MVT Pegasus), and facial recognition (FaceCheck.ID).
---

# S72: Darkweb & Offensive AI Forensics (darkweb-offensive-ai-forensics)

## ⚡ Overview & Architecture
Extracted and synthesized from the forensic intelligence guidelines (C:\Users\antoni\Downloads\ai guideline):
1. **AIMap AI Infrastructure Scanner (Bishop Fox AIMap)**:
   - Audits exposed AI endpoints, open Ollama ports, vLLM servers, LiteLLM gateways, ComfyUI instances, LangServe backends, and MCP server endpoints.
   - Detects unauthorized prompt injection vulnerabilities, unauthenticated model fine-tuning APIs, and leaked API credentials.
2. **Robin Dark-Web OSINT Engine (Robin)**:
   - Autonomous agent-driven dark-web search traversing Tor (.onion) networks, leak forums, and threat intelligence repositories.
   - Performs automated breach data aggregation, credential exposure checks, and threat actor monitoring.
3. **MVT - Mobile Verification Toolkit (MVT)**:
   - Forensic toolkit for detecting signs of target surveillance spyware (e.g. NSO Group Pegasus, Cytrox Predator) in Android and iOS backup artifacts.
4. **FaceCheck.ID Facial OSINT Search (FaceCheck.ID)**:
   - High-accuracy reverse image facial recognition engine searching mugshots, social footprints, and public web archives for threat identification.
5. **AgentFiles Standard (Railly/agentfiles, 
agapp/agentfiles)**:
   - Open standard specification for defining AI agent context, system personas, file attachments, and prompt bundles across agent frameworks.

## 🛠️ Usage & Ethical Boundaries
- **Strict Defensive & Forensic Protocol**: Used strictly for authorized defensive security audits, asset exposure mapping, and corporate risk mitigation.
- **Zero-Harm Principle**: Any offensive reconnaissance requires explicit authorized scope and sandbox isolation.
