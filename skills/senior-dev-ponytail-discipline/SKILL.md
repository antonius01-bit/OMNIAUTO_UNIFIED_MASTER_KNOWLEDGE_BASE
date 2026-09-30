---
name: senior-dev-ponytail-discipline
description: Surgical non-destructive coding heuristics, minimal diffs, YAGNI, and lazy-senior-developer discipline derived from DietrichGebert Ponytail and ponytail-lite.
---

# Senior Dev Ponytail Discipline (S56)

## Overview
High-discipline engineering skill based on Ponytail (DietrichGebert/ponytail and ilindaniel/ponytail-lite). Enforces the mindset of the seasoned senior developer: the best code is the code you never wrote. Prevents AI agents from over-engineering, rewriting working modules, or introducing architectural bloat.

## Core Rules
1. Surgical Minimal Diffs: Never rewrite a file when a 3-line surgical patch achieves the objective.
2. YAGNI (You Are Not Gonna Need It): Do not create speculative abstractions, unnecessary generic classes, or premature microservices.
3. Zero Regression Guarantee: Preserve all existing comments, docstrings, and peripheral functions unless explicitly told to alter them.
4. Test Before and After: Verify existing test suites pass before touching code and pass after changes.
5. Investigate Before Editing: Trace root cause thoroughly before modifying source files.

## Activation
- Command: /omni-auto ponytail: Refactor or fix [bug/feature] with minimal surgical diffs and zero unnecessary abstractions
