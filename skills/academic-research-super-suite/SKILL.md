---
name: academic-research-super-suite
description: Comprehensive academic research suite fusing Imbad0202 (Cheng-I Wu) 39-agent architecture, PRISMA systematic review, Semantic Scholar API verification, Toulmin/Bradford Hill argumentation, 22 Iron Rules, 29 Anti-Patterns, and Kimi 2M-token grounding.
---

# 🎓 S124 — Academic Research Super Suite (`academic-research-super-suite`)

## 📌 Overview & Upstream Origin
- **Upstream Repository**: [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu, 47.1k★, v3.7–v3.11), [academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex).
- **Core Methodology**: 4 core modules, 39 specialized subagents, 22 Iron Rules, 29 Anti-Patterns, PRISMA systematic literature search, Semantic Scholar API live graph verification, R&R (Revise & Resubmit) Traceability Matrix, Toulmin argumentation structure, Bradford Hill criteria for causality, VLM figure layout inspection, and Moonshot Kimi K2.6 2M-token document grounding.
- **Integration**: Direct native execution inside Dola AI `/omni-auto` Phase 1 (Methodological Grounding) & Phase 3 (Drafting & Forensic Verification).

---

## 🏛️ 4-Module Architecture & 39 Specialized Subagents

```
academic-research-super-suite/
├── 1. deep-research/ (13 Agents)
│   ├── Topic Clarification & Socratic Guide
│   ├── Literature Search Strategy (PRISMA / PICO)
│   ├── Semantic Scholar & OpenAlex API Verifier
│   ├── Citation Forward/Backward Traversal
│   ├── Methodology Gap Evaluator
│   ├── Theoretical Framework Mapper
│   ├── Devil's Advocate / Counter-Argument Hunter
│   ├── Systematic Evidence Extractor
│   ├── Quantitative Variable Normalizer
│   ├── Qualitative Thematic Coder
│   ├── SOTA Baseline Comparator
│   ├── Ethics & Institutional Compliance Auditor
│   └── Research Synthesis Synthesizer
├── 2. academic-paper/ (12 Agents)
│   ├── IMRaD Structural Architect
│   ├── Academic Style Calibrator (Passive/Active ratio)
│   ├── Claim-to-Evidence Chain Verifier
│   ├── Anti-Leakage Citation Enforcer
│   ├── Mathematical Formalization & LaTeX Hardener
│   ├── VLM Figure & Diagram Visual Auditor
│   ├── Table & Statistical Result Formatter
│   ├── Abstract & Key Takeaways Distiller
│   ├── Introduction Motivation & Hook Drafter
│   ├── Discussion & Implications Synthesizer
│   ├── Limitations & Future Scope Formalizer
│   └── Multi-Language Synchronizer (ID / EN)
├── 3. academic-paper-reviewer/ (7 Agents)
│   ├── Read-Only Manuscript Constraint Enforcer
│   ├── Desk Reject & Fast-Kill Filter
│   ├── Toulmin Argumentation Coherence Checker
│   ├── Bradford Hill Causality Assessor
│   ├── Methodological Rigor & Threats-to-Validity Auditor
│   ├── IS Basket of 8/11 Journal Criteria Evaluator
│   └── Constructive Peer-Review Report Generator
└── 4. academic-pipeline/ (7 Stages & Orchestration)
    ├── End-to-End Orchestrator (Phase 0 to Phase 5)
    ├── R&R Traceability Matrix Generator
    ├── Point-by-Point Rebuttal Drafter
    ├── Diff-Tracking & Version Control Auditor
    ├── Mendeley/Zotero RIS Sync Hook
    ├── Camera-Ready LaTeX/DOCX Packaging
    └── Submission Checklist Verifier
```

---

## ⚡ 22 Academic Iron Rules

1. **Zero Hallucinated Citations**: Every citation must correspond to an authentic DOI, PMID, arXiv ID, or verified Semantic Scholar Corpus ID.
2. **Read-Only Reviewer Constraint**: Reviewer agents must NEVER alter the manuscript text; they only produce external diagnostics and critique reports.
3. **Anti-Leakage Citation Protocol**: Citations must not reveal manuscript authorship during double-blind peer review; internal preprints must be redacted.
4. **Source-to-Claim Evidence Chain**: Every claim must follow $	ext{Claim} \to \text{Evidence} \to \text{Source} \to \text{Source Quality} \to \text{Interpretation} \to \text{Limitation}$.
5. **No Unsupported Speculation**: Speculative language ("obviously", "it is self-evident that") is strictly forbidden in Discussion sections.
6. **PRISMA 2020 Compliance**: Systematic reviews must report identification, screening, eligibility, and inclusion numbers with flowchart data.
7. **Toulmin Argumentation Standard**: Claims must have explicit Grounds, Warrants, Backing, Qualifiers, and Rebuttals.
8. **Bradford Hill Causality Audit**: Observational claims cannot claim causality without addressing temporality, strength, dose-response, and plausibility.
9. **Synchronized Citation Identifiers**: Reference IDs in manuscript text (`[1#E]`, `[2#E]`) must match `.ris` tags 1:1.
10. **Statistical Disclosure Rigor**: All regressions must report sample size $N$, degrees of freedom, $p$-values, effect sizes ($R^2$, Cohen's $d$), and confidence intervals.
11. **Threats to Validity**: Internal, external, construct, and statistical conclusion validity must each have a dedicated sub-paragraph.
12. **Balanced Baseline Comparison**: SOTA comparisons must include competing contemporary baselines under identical benchmarking setups.
13. **VLM Visual Figure Audit**: Figures must have readable font size ($\ge 8\text{pt}$), high DPI ($\ge 300$), explicit axis labels with units, and colorblind-safe palettes.
14. **LaTeX Mathematical Hardening**: All equations must be numbered, symbols formally defined in adjacent prose, and units formatted with `\mathrm{}` or `siunitx`.
15. **R&R Traceability Matrix**: Every reviewer comment must have a corresponding row with: Reviewer Comment ID, Original Text, Revised Text, Rationale, and Page/Line reference.
16. **Formal Rebuttal Tone**: Rebuttal letters must remain unfailingly polite, grateful, objective, and evidence-grounded.
17. **FK-16 Similarity Bound**: Manuscript similarity must strictly remain $\le 5\%$ against academic databases.
18. **FK-17 Cliché Ban**: Eliminate 29 AI clichés ("testament to", "delve into", "pivotal role", "landscape", "beacon of hope").
19. **Dual-Language Semantic Parity**: Indonesian and English manuscripts must maintain identical factual claims and structural sections.
20. **Reproducibility Guarantee**: Datasets, hyperparameters, random seeds, and compute hardware must be explicitly disclosed.
21. **Context Grounding Integrity**: When using 2M-token context (Kimi K2.6 / Gemini Flash), references must directly quote verifying excerpts.
22. **Clean Deliverable Packaging**: Output guaranteed `.docx`, `.pptx`, `.ris`, and compilation-ready `.tex`.

---

## 🚫 29 Anti-Patterns Detected & Eliminated

1. *The Ghost Citation*: Fabricating authors, titles, or page ranges for non-existent papers.
2. *The Circular Reference*: Citing secondary review papers for primary empirical findings.
3. *The Cherry-Picked SOTA*: Selecting outdated or weak baselines to artificially inflate proposed model gains.
4. *The Over-Promised Abstract*: Stating revolutionary discoveries in abstract not supported by Results section.
5. *The Missing Unit*: Presenting tables and charts with numerical values devoid of standard measurement units.
6. *The P-Hacking Trap*: Reporting only statistically significant models while hiding unadjusted multi-hypothesis tests.
7. *The AI Narrative Drift*: Inserting generic philosophical introductions unrelated to the specific empirical study.
8. *The Vague Methodology*: Describing workflows with generic terms ("we cleaned the data") without explicit algorithms.
9. *The Reviewer Dismissal*: Responding to reviewer critique with defensive or non-substantive dismissals ("we disagree").
10. *The Invisible Negative Result*: Omitting ablation configurations where the proposed approach performed worse.
11. *The Over-Fitting Fallacy*: Tuning hyperparameters on the test set rather than a dedicated validation fold.
12. *The Blind Assumption*: Taking survey data or self-reported metrics as objective ground truth without validation.
13. *The Passive-Voice Avalanche*: Over-using passive voice to the point where the agent or experimenter is ambiguous.
14. *The Unbounded Scope*: Claiming broad universal applicability from a hyper-narrow niche case study.
15. *The Inconsistent Notation*: Switching mathematical symbols between chapters (e.g. $w_i$ in chapter 3, $\theta_k$ in chapter 4).
16. *The Unlinked RIS File*: Delivering a manuscript with references that do not parse or match the citation manager library.
17. *The Unchecked Figure Resolution*: Embedding blurry screenshots rather than vectorized SVG or high-res PNG plots.
18. *The Hallucinated Metric*: Reporting standard deviations or error bars without computing them from experimental runs.
19. *The Disconnected Conclusion*: Introducing new literature or unanalyzed ideas in the final concluding remarks.
20. *The Incomplete Literature Sweep*: Limiting literature review to a single search query or single database.
21. *The Misused Acronym*: Using abbreviations without expanding them on first occurrence in both Abstract and Body.
22. *The Biased Sample*: Ignoring demographic or geographic skews in respondent distributions.
23. *The Broken Cross-Reference*: Referring to "Table 4" when the document only has three tables.
24. *The Phantom Appendix*: Promising extended proofs or code in "Appendix B" that does not exist in the submission package.
25. *The Misrepresented Causality*: Using verbs like "causes" or "drives" for simple correlational cross-sectional data.
26. *The Excessive Self-Citation*: Inflating reference lists with unrelated papers from the author's own laboratory.
27. *The Ignored Outliers*: Dropping inconvenient data points without reporting rejection criteria or sensitivity analyses.
28. *The Jargon Overload*: Masking conceptual vacuity behind dense, non-standard neologisms.
29. *The Unverified Pre-Print Reliance*: Basing foundational theoretical pillars entirely on non-peer-reviewed blog posts.

---

## 🛠️ Operational Workflows & Triggers

### 1. Execute Socratic Guided Deep Research
```bash
/omni-auto academic-research: Conduct Socratic literature exploration on [Topic]. Map PRISMA search strings, verify top 30 papers via Semantic Scholar API, and identify 3 key empirical gaps.
```

### 2. Full Manuscript Drafting with Anti-Leakage & IMRaD Hardening
```bash
/omni-auto academic-paper: Draft full manuscript for [Research Title]. Target Journal: [Journal Name]. Enforce Toulmin argumentation, LaTeX formulas, synchronized [N#E] citations, and dual-language ID+EN DOCX generation.
```

### 3. Read-Only Rigorous Peer Review Audit
```bash
/omni-auto academic-reviewer: Perform read-only desk-reject audit on [manuscript.docx/tex]. Apply IS Basket of 8 criteria, check Bradford Hill causality, and produce formal review report.
```

### 4. Generate R&R Traceability Matrix & Rebuttal Letter
```bash
/omni-auto academic-pipeline: Formulate R&R Traceability Matrix for reviewer comments in [comments.txt]. Generate polite point-by-point rebuttal letter with exact page/line diffs.
```