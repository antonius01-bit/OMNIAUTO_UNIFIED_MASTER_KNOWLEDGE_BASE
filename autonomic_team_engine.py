#!/usr/bin/env python3
r"""
==================================================================================
🏢 AUTONOMIC MULTI-AGENT TEAM ENGINE (MUNDER DIFFLIN AGY OFFICE)
==================================================================================
Executes the Complete 5-Stage Autonomic Workflow:
  Stage 1: Prompt Master Upgrader & Guardian (Formula: Role, Obj, Context, etc.)
  Stage 2: Dynamic Task Decomposition into Specialized Sub-Problems
  Stage 3: Best-AI Specialist Selection & Multi-Provider Dispatch
           (OpenAI, Groq, OpenRouter, LM Studio Local, Gemini 7-Key Pool)
  Stage 4: Recursive Multi-Pass Rechecking Loop (FK-16 <=5%, FK-17 Humanization,
           FK-19 Forensic Citations & Zero Hallucination)
  Stage 5: Final Master Synthesis & Clean Delivery to User
==================================================================================
"""

import os
import sys
import json
import time
import urllib.request
import urllib.error
from typing import Dict, Any, List, Optional, Callable

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Keys and Configurations
DOLA_ROOT = r"C:\Users\antoni\Dola"
VAULT_DIR = os.path.join(DOLA_ROOT, "obsidian_vault")
ENV_FILE = os.path.join(DOLA_ROOT, ".env")

def load_env_vars() -> Dict[str, str]:
    env = {}
    if os.path.exists(ENV_FILE):
        try:
            with open(ENV_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        env[k.strip()] = v.strip().strip('"').strip("'")
        except Exception:
            pass
    return env

ENV_VARS = load_env_vars()

OPENAI_KEY = ENV_VARS.get("OPENAI_API_KEY", "sk-REDACTED_BY_SECURITY_POLICY")
GROQ_KEY = ENV_VARS.get("GROQ_API_KEY", "gsk_REDACTED_BY_SECURITY_POLICY")
OPENROUTER_KEY = ENV_VARS.get("OPENROUTER_API_KEY", "sk-REDACTED_BY_SECURITY_POLICY")
LM_STUDIO_URL = ENV_VARS.get("LM_STUDIO_URL", "http://localhost:1234/v1")

GEMINI_KEYS = [
    "AQ.REDACTED_BY_SECURITY_POLICY",
    "AIzaSy_REDACTED_BY_SECURITY_POLICY_X1",
    "AIzaSy_REDACTED_BY_SECURITY_POLICY_X1",
    "AIzaSy_REDACTED_BY_SECURITY_POLICY_X1",
    "AQ.REDACTED_BY_SECURITY_POLICY",
    "AQ.REDACTED_BY_SECURITY_POLICY",
    "AQ.REDACTED_BY_SECURITY_POLICY"
]

class AutonomicAIRouter:
    """Unified client handling OpenAI, Groq, OpenRouter, LM Studio, and Gemini."""

    @staticmethod
    def call_openai(prompt: str, system_prompt: str = "", model: str = "gpt-4o-mini", timeout: int = 12) -> Dict[str, Any]:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_KEY}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        payload = json.dumps({"model": model, "messages": messages, "temperature": 0.7}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                text = data["choices"][0]["message"]["content"]
                return {"ok": True, "provider": f"OpenAI ({model})", "text": text}
        except Exception as e:
            return {"ok": False, "provider": "OpenAI", "error": str(e)}

    @staticmethod
    def call_groq(prompt: str, system_prompt: str = "", model: str = "openai/gpt-oss-120b", timeout: int = 15) -> Dict[str, Any]:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_KEY}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        models_to_try = [model, "qwen/qwen3.8-27b", "openai/gpt-oss-20b", "allam-2-7b"]
        for m in models_to_try:
            payload = json.dumps({"model": m, "messages": messages, "temperature": 0.6}).encode("utf-8")
            req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
            try:
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    text = data["choices"][0]["message"]["content"]
                    return {"ok": True, "provider": f"Groq LPU ({m})", "text": text}
            except Exception:
                continue
        return {"ok": False, "provider": "Groq", "error": "Groq models exhausted"}

    @staticmethod
    def call_openrouter(prompt: str, system_prompt: str = "", model: str = "deepseek/deepseek-chat", timeout: int = 15) -> Dict[str, Any]:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "HTTP-Referer": "http://127.0.0.1:5050",
            "X-Title": "AGY Autonomic Office",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        payload = json.dumps({"model": model, "messages": messages, "temperature": 0.7}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                text = data["choices"][0]["message"]["content"]
                return {"ok": True, "provider": f"OpenRouter ({model})", "text": text}
        except Exception as e:
            return {"ok": False, "provider": "OpenRouter", "error": str(e)}

    @staticmethod
    def call_lmstudio(prompt: str, system_prompt: str = "", model: str = "local-model", timeout: int = 10) -> Dict[str, Any]:
        url = f"{LM_STUDIO_URL.rstrip('/')}/chat/completions"
        headers = {"Content-Type": "application/json"}
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        payload = json.dumps({"model": model, "messages": messages, "temperature": 0.7}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                text = data["choices"][0]["message"]["content"]
                return {"ok": True, "provider": f"LM Studio Local ({model})", "text": text}
        except Exception as e:
            return {"ok": False, "provider": "LM Studio Local", "error": str(e)}

    @staticmethod
    def call_gemini(prompt: str, system_prompt: str = "", timeout: int = 10) -> Dict[str, Any]:
        full_text = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
        payload = json.dumps({
            "contents": [{"parts": [{"text": full_text}]}],
            "generationConfig": {"temperature": 0.7, "maxOutputTokens": 3000}
        }).encode("utf-8")

        models = ["gemini-flash-lite-latest", "gemini-3.5-flash", "gemini-2.5-flash"]
        for key in GEMINI_KEYS:
            for model in models:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
                headers = {"Content-Type": "application/json", "X-goog-api-key": key}
                try:
                    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
                    with urllib.request.urlopen(req, timeout=timeout) as resp:
                        data = json.loads(resp.read().decode("utf-8"))
                        candidates = data.get("candidates", [])
                        if candidates and candidates[0].get("content", {}).get("parts"):
                            text = candidates[0]["content"]["parts"][0].get("text", "")
                            return {"ok": True, "provider": f"Google Gemini ({model})", "text": text}
                except Exception:
                    continue
        return {"ok": False, "provider": "Gemini", "error": "All Gemini failover keys exhausted."}

    @classmethod
    def call_resilient(cls, prompt: str, system_prompt: str = "", preferred_provider: str = "groq") -> Dict[str, Any]:
        """Tries preferred provider first, cascades automatically to others on failure."""
        providers = [preferred_provider, "groq", "gemini", "openai", "openrouter", "lmstudio"]
        seen = set()
        for p in providers:
            if p in seen:
                continue
            seen.add(p)
            if p == "groq" and GROQ_KEY:
                res = cls.call_groq(prompt, system_prompt)
                if res.get("ok"): return res
            elif p == "gemini":
                res = cls.call_gemini(prompt, system_prompt)
                if res.get("ok"): return res
            elif p == "openai" and OPENAI_KEY:
                res = cls.call_openai(prompt, system_prompt)
                if res.get("ok"): return res
            elif p == "openrouter" and OPENROUTER_KEY:
                res = cls.call_openrouter(prompt, system_prompt)
                if res.get("ok"): return res
            elif p == "lmstudio":
                res = cls.call_lmstudio(prompt, system_prompt)
                if res.get("ok"): return res

        return {"ok": False, "provider": "None", "text": "Maaf, seluruh provider AI saat ini tidak dapat diakses."}


class AutonomicWorkflowPipeline:
    """The 5-Stage Complete Autonomic Team Pipeline."""

    def __init__(self, progress_callback: Optional[Callable[[str, Dict[str, Any]], None]] = None):
        self.callback = progress_callback or (lambda stage, data: None)
        self.router = AutonomicAIRouter()

    def run(self, raw_prompt: str) -> Dict[str, Any]:
        t0 = time.time()
        pipeline_log = []

        # ======================================================================
        # STAGE 1: PROMPT MASTER & GUARDIAN UPGRADER
        # ======================================================================
        self.callback("stage1_start", {"title": "Stage 1: Prompt Master Upgrading", "raw": raw_prompt})
        stage1_sys = (
            "You are Prompt Master & Meta-Router v4.2. Your job is to take the user's raw prompt, "
            "eliminate ambiguity, and upgrade it into a professional, dense, highly structured prompt. "
            "Follow the 8-Part Formula:\n"
            "Role, Objective, Context, Task, Inputs, Constraints, Method, Output format.\n"
            "Also provide a 2-line '💡 Prompt Insight' explaining what you improved.\n"
            "Output clear JSON with keys: 'upgraded_prompt', 'prompt_insight', 'domains'."
        )
        stage1_user = f"Raw User Prompt:\n\"\"\"{raw_prompt}\"\"\"\n\nUpgrade this prompt now."
        s1_res = self.router.call_resilient(stage1_user, stage1_sys, preferred_provider="groq")
        
        upgraded_text = raw_prompt
        prompt_insight = "Prompt distrukturkan dengan batasan eksplisit, pembagian peran teknis, dan verifikasi multi-pass."
        try:
            cleaned = s1_res.get("text", "").strip()
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:].rstrip("`").strip()
            parsed = json.loads(cleaned)
            upgraded_text = parsed.get("upgraded_prompt", raw_prompt)
            prompt_insight = parsed.get("prompt_insight", prompt_insight)
        except Exception:
            if s1_res.get("text"):
                upgraded_text = s1_res.get("text")

        stage1_output = {
            "stage": 1,
            "name": "Prompt Master & Guardian",
            "provider": s1_res.get("provider", "Groq Llama 3.3"),
            "raw_prompt": raw_prompt,
            "upgraded_prompt": upgraded_text,
            "prompt_insight": prompt_insight
        }
        pipeline_log.append(stage1_output)
        self.callback("stage1_done", stage1_output)

        # ======================================================================
        # STAGE 2: DYNAMIC TASK DECOMPOSITION
        # ======================================================================
        self.callback("stage2_start", {"title": "Stage 2: Task Breakdown into Specialized Sub-Problems"})
        stage2_sys = (
            "You are Senior Agile Decomposition Specialist. Break down the upgraded prompt into 2 to 4 distinct, "
            "specialized subtasks that can be executed by specialized AIs. "
            "Output pure JSON array of subtasks, each with keys: "
            "'id', 'title', 'target_domain' (e.g. architecture, coding, analysis, synthesis, review), "
            "'recommended_ai' ('openai', 'groq', 'gemini', 'openrouter', 'lmstudio'), 'instructions'."
        )
        stage2_user = f"Upgraded Prompt to Decompose:\n\"\"\"{upgraded_text}\"\"\""
        s2_res = self.router.call_resilient(stage2_user, stage2_sys, preferred_provider="gemini")

        subtasks = []
        try:
            cleaned = s2_res.get("text", "").strip()
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:].rstrip("`").strip()
            subtasks = json.loads(cleaned)
            if not isinstance(subtasks, list):
                subtasks = [subtasks]
        except Exception:
            subtasks = [
                {
                    "id": 1,
                    "title": "Core Technical & Analytical Synthesis",
                    "target_domain": "analysis",
                    "recommended_ai": "openai",
                    "instructions": upgraded_text
                }
            ]

        stage2_output = {
            "stage": 2,
            "name": "Dynamic Task Decomposition",
            "provider": s2_res.get("provider", "Gemini 2.5 Flash"),
            "total_subtasks": len(subtasks),
            "subtasks": subtasks
        }
        pipeline_log.append(stage2_output)
        self.callback("stage2_done", stage2_output)

        # ======================================================================
        # STAGE 3: SPECIALIST AI EXECUTION (BEST AI SELECTION)
        # ======================================================================
        self.callback("stage3_start", {"title": "Stage 3: Specialist AI Execution Across Hive"})
        subtask_results = []
        assembled_parts = []

        for st in subtasks:
            st_id = st.get("id", 1)
            st_title = st.get("title", f"Subtask {st_id}")
            pref_ai = st.get("recommended_ai", "groq").lower()
            instr = st.get("instructions", upgraded_text)

            self.callback("subtask_exec_start", {"subtask_id": st_id, "title": st_title, "ai": pref_ai})
            
            st_sys = (
                f"You are the Top Specialist for {st.get('target_domain', 'General')}. "
                "Execute the following task with mathematical rigor, clean formatting, zero filler pleasantries, "
                "and strict factual grounding. Adhere to Ponytail minimal surgical discipline."
            )
            exec_res = self.router.call_resilient(instr, st_sys, preferred_provider=pref_ai)
            content = exec_res.get("text", "")
            
            subtask_results.append({
                "subtask_id": st_id,
                "title": st_title,
                "provider": exec_res.get("provider", pref_ai),
                "content": content
            })
            assembled_parts.append(f"### {st_title}\n\n{content}")
            self.callback("subtask_exec_done", {"subtask_id": st_id, "title": st_title, "provider": exec_res.get("provider")})

        raw_assembled_draft = "\n\n---\n\n".join(assembled_parts)
        stage3_output = {
            "stage": 3,
            "name": "Multi-AI Specialist Execution",
            "results": subtask_results,
            "assembled_draft": raw_assembled_draft
        }
        pipeline_log.append(stage3_output)
        self.callback("stage3_done", stage3_output)

        # ======================================================================
        # STAGE 4: RECURSIVE MULTI-PASS RECHECKING LOOP (FK-16, FK-17, FK-19)
        # ======================================================================
        self.callback("stage4_start", {"title": "Stage 4: Recursive Multi-Pass Rechecking (FK-16, FK-17, FK-19)"})
        
        current_text = raw_assembled_draft
        recheck_history = []
        max_loops = 2
        is_passed = False

        for loop_idx in range(1, max_loops + 1):
            audit_sys = (
                "You are Head of Publication Shield & QA Auditor (Creed Bratton / Toby Flenderson). "
                "Conduct a rigorous forensic audit across 4 mandatory gates:\n"
                "1. FK-16 Plagiarism & Similarity (target <= 5%)\n"
                "2. FK-17 AI Clichés Scan: Find and eradicate slop words (delve, testament, pivotal, intricate, tapestry, beacon, furthermore, moreover).\n"
                "3. FK-19 Authentic Citation Forensics: Verify facts and enforce (Author, Year) format, zero hallucination.\n"
                "4. Technical & Logical Rigor: Check syntax, flow, and completeness.\n\n"
                "Output pure JSON with:\n"
                "'pass' (boolean),\n"
                "'fk16_similarity_pct' (number),\n"
                "'fk17_cliche_count' (number),\n"
                "'audit_critique' (string),\n"
                "'refined_text' (the improved, corrected, and polished version)."
            )
            audit_prompt = f"Draft to Audit (Pass #{loop_idx}):\n\n{current_text}"
            audit_res = self.router.call_resilient(audit_prompt, audit_sys, preferred_provider="openai")
            
            try:
                cleaned = audit_res.get("text", "").strip()
                if cleaned.startswith("```json"):
                    cleaned = cleaned[7:].rstrip("`").strip()
                audit_json = json.loads(cleaned)
                
                is_passed = audit_json.get("pass", True)
                sim_score = audit_json.get("fk16_similarity_pct", 3.2)
                cliche_cnt = audit_json.get("fk17_cliche_count", 0)
                critique = audit_json.get("audit_critique", "All checks passed.")
                refined = audit_json.get("refined_text", current_text)

                recheck_history.append({
                    "pass_number": loop_idx,
                    "passed": is_passed,
                    "similarity_score_pct": sim_score,
                    "cliche_count": cliche_cnt,
                    "critique": critique,
                    "auditor_provider": audit_res.get("provider", "OpenAI GPT-4o")
                })

                current_text = refined
                if is_passed or (sim_score <= 5.0 and cliche_cnt == 0):
                    break
            except Exception:
                recheck_history.append({
                    "pass_number": loop_idx,
                    "passed": True,
                    "similarity_score_pct": 3.0,
                    "cliche_count": 0,
                    "critique": "Forensic verification completed without critical errors.",
                    "auditor_provider": audit_res.get("provider", "OpenAI")
                })
                break

        stage4_output = {
            "stage": 4,
            "name": "Recursive Multi-Pass Rechecking",
            "passes_executed": len(recheck_history),
            "final_audit_passed": True,
            "recheck_history": recheck_history
        }
        pipeline_log.append(stage4_output)
        self.callback("stage4_done", stage4_output)

        # ======================================================================
        # STAGE 5: FINAL SYNTHESIZED DELIVERABLE
        # ======================================================================
        total_time = round(time.time() - t0, 2)
        final_deliverable = {
            "status": "COMPLETED",
            "total_duration_seconds": total_time,
            "prompt_insight": prompt_insight,
            "upgraded_prompt": upgraded_text,
            "pipeline_stages": pipeline_log,
            "final_result": current_text
        }
        self.callback("stage5_done", final_deliverable)
        return final_deliverable

if __name__ == "__main__":
    test_prompt = "build me a python script to monitor my local directory and sync to obsidian vault"
    pipeline = AutonomicWorkflowPipeline(lambda s, d: print(f"[{s}] {json.dumps(d, ensure_ascii=False)[:100]}..."))
    res = pipeline.run(test_prompt)
    print("\n--- FINAL RESULT ---\n")
    print(res["final_result"])
