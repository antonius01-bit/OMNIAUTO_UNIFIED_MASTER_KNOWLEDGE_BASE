---
name: swe-rex-remote-execution
description: SWE-agent Remote Execution Framework (SWE-ReX) and autonomous software engineering benchmarks for sandboxed codebase editing, Docker execution, and test evaluation.
---

# S77: SWE-ReX Remote Execution Framework (`swe-rex-remote-execution`)

## ⚡ Overview & Architecture
Developed by Princeton NLP & the SWE-bench core team (`SWE-agent/SWE-ReX`, `SWE-agent/SWE-agent`):
1. **Remote Execution Runtime (`SWE-ReX`)**:
   - Decouples agent reasoning from code execution environments (Docker containers, cloud micro-VMs, Modal, Daytona).
   - Solves the security, latency, and dependency isolation bottlenecks when running untrusted agent-generated code.
   - Streaming IO protocol for bidirectional shell execution, diff patching, and unit test evaluation.
2. **SWE-agent Core Capabilities**:
   - ACI (Agent-Computer Interface): Custom bash commands optimized for LLM readability (e.g. `open_file`, `scroll_down`, `search_dir`, `edit_lines`).
   - Trajectory recording and benchmark validation matching state-of-the-art SWE-bench Lite and Verified scores.
3. **Hypothesis-Driven Debugging**:
   - Automated git reproduction scripts, regression testing, and clean git commit generation.

## 🛠️ Operational Recipes
- Launch isolated SWE-ReX execution container:
  ```python
  from swerex.deployment import DockerDeployment
  deployment = DockerDeployment(image="swe-agent/eval:latest")
  deployment.start()
  ```
- Send interactive terminal commands and capture exit codes:
  ```python
  result = deployment.runtime.run_in_session("pytest tests/test_core.py")
  print(result.stdout, result.exit_code)
  ```
