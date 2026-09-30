---
name: tdd-guard-karpathy-runtime-discipline
description: Strict Test-Driven Development (TDD) enforcement guardrails and 10 Karpathy runtime discipline rules (4 edit-time, 6 runtime budget/safety caps) powered by nizos/tdd-guard, draftcat v2, and Andrej Karpathy autoresearch.
---

# 🛡️ TDD-Guard & Karpathy Runtime Discipline (S121)

Industrial-grade coding rigor combining **TDD-Guard** (`nizos/tdd-guard` - 2.3k★, SkillsLLM) and **Andrej Karpathy's 10 Production Rules** (from `draftcat` v2 & `karpathy/autoresearch` - 95.4k★). Blocks AI code slop by enforcing red-green-refactor cycles and strict runtime safety budgets.

---

## 🚦 1. TDD-Guard Ironclad Execution Contract

AI agents are strictly forbidden from writing production code before an automated test exists and fails:

```
[Phase 1: RED]
  Write a minimal unit test that asserts the desired behavior.
  Execute test suite -> CONFIRM FAILURE (assert test fails for the expected reason).

[Phase 2: GREEN]
  Make the absolute minimal, surgical code edit required to make the test pass.
  Execute test suite -> CONFIRM PASS (all tests green).

[Phase 3: REFACTOR & VERIFY]
  Refactor for clean code, YAGNI, and readability without adding unrequested features.
  Execute full regression test suite.
```

---

## ⚡ 2. Karpathy's 10 Production Rules (Draftcat v2)

### Edit-Time Rules (When Writing Code):
1. **Surgical Diffs**: Modify only lines directly tied to the prompt. Never touch unrelated formatting or imports.
2. **Zero Inventions**: Do not invent utility functions or abstractions unless required by $\ge 3$ callers.
3. **Strict Typings**: Every function parameter and return must be explicitly typed.
4. **YAGNI Compliance**: You Aren't Gonna Need It. Delete dead code immediately.

### Runtime Rules (When Agent is Executing):
5. **Silent Budget Caps**: Terminate agent loops immediately if iteration count $> 10$ or token budget exceeds thresholds.
6. **Zero Silent Swallowing**: Never use bare `except: pass`. Log or re-raise every exception.
7. **Read-Before-Write**: Always read existing file contents before proposing modifications.
8. **Idempotent Operations**: File operations and database migrations must be safely re-runnable without corruption.
9. **Defense-in-Depth Assertions**: Place runtime sanity assertions on critical business logic boundaries.
10. **Evidence-Based Success**: An agent may only declare a task complete when automated test output or verified logs confirm success.

---

## 🚀 3. Trigger & Workflows
- **Trigger**: `/omni-auto tdd-guard` atau `/karpathy-discipline`
- **Sub-skills**:
  - `tdd_red_green_enforcer`: Blok eksekusi kode produksi sebelum tes unit merah gagal terverifikasi.
  - `karpathy_surgical_diff_auditor`: Audit diff kode untuk memastikan zero-regression dan YAGNI.
  - `runtime_budget_governor`: Pemantau ambang batas token dan batas iterasi loop agen.
