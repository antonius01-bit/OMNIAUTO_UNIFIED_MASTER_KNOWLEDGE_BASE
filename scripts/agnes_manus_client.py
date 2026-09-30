#!/usr/bin/env python3
"""
Agnes AI & Manus AI Unified Client Engine
Provides programmatic & CLI access to Agnes AI (models, chat, multimodal) and Manus AI (autonomous tasks, agent execution).
"""

import os
import sys
import json
import urllib.request
import urllib.error
import ssl
import argparse

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

CTX = ssl.create_default_context()

# GAuth Zero-Trust Security Gate Integration
try:
    import gauth_security_gate as gauth_gate
except ImportError:
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    try:
        import gauth_security_gate as gauth_gate
    except Exception:
        gauth_gate = None

# Load keys from environment or fallbacks
AGNES_KEY = os.environ.get("AGNES_API_KEY", "sk-REDACTED_BY_SECURITY_POLICY")
AGNES_BASE_URL = os.environ.get("AGNES_BASE_URL", "https://apihub.agnes-ai.com/v1")

MANUS_KEY = os.environ.get("MANUS_API_KEY", "sk-REDACTED_BY_SECURITY_POLICY")
MANUS_BASE_URL = os.environ.get("MANUS_BASE_URL", "https://api.manus.im/v1")

# ==========================================
# AGNES AI METHODS
# ==========================================
def agnes_list_models():
    """Retrieve list of available models from Agnes AI"""
    url = f"{AGNES_BASE_URL}/models"
    headers = {"Authorization": f"Bearer {AGNES_KEY}", "User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10, context=CTX) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("data", [])
    except Exception as e:
        print(f"[!] Agnes list_models error: {e}")
        return []

def agnes_chat_stream(prompt, model="agnes-2.5-flash", system_prompt=None):
    """Send chat prompt to Agnes AI with streaming output"""
    url = f"{AGNES_BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {AGNES_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    # GAuth Zero-Trust Run Signature
    if gauth_gate:
        gauth_res = gauth_gate.authorize_workflow_run(f"Agnes AI Chat ({model})", agent="agnes", details=prompt[:40])
        headers["X-GAuth-Signature"] = gauth_res.get("signature", "")
        headers["X-GAuth-Run-Token"] = gauth_res.get("run_token", "")

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    payload = json.dumps({
        "model": model,
        "messages": messages,
        "stream": True
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    full_response = ""
    try:
        with urllib.request.urlopen(req, timeout=30, context=CTX) as resp:
            for line in resp:
                line_str = line.decode("utf-8", errors="ignore").strip()
                if line_str.startswith("data: ") and line_str != "data: [DONE]":
                    try:
                        chunk = json.loads(line_str[6:])
                        delta = chunk.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        if delta:
                            sys.stdout.write(delta)
                            sys.stdout.flush()
                            full_response += delta
                    except Exception:
                        pass
            print()
            return full_response
    except Exception as e:
        print(f"\n[!] Agnes chat error: {e}")
        return ""

# ==========================================
# MANUS AI METHODS
# ==========================================
def manus_list_tasks(limit=10):
    """Retrieve active and recent tasks from Manus AI"""
    url = f"{MANUS_BASE_URL}/tasks"
    headers = {
        "API_KEY": MANUS_KEY,
        "Authorization": f"Bearer {MANUS_KEY}",
        "User-Agent": "Mozilla/5.0"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=12, context=CTX) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("data", [])[:limit]
    except Exception as e:
        print(f"[!] Manus list_tasks error: {e}")
        return []

def manus_get_task(task_id):
    """Retrieve detailed state of a specific Manus task"""
    url = f"{MANUS_BASE_URL}/tasks/{task_id}"
    headers = {
        "API_KEY": MANUS_KEY,
        "Authorization": f"Bearer {MANUS_KEY}",
        "User-Agent": "Mozilla/5.0"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=12, context=CTX) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data
    except Exception as e:
        print(f"[!] Manus get_task error ({task_id}): {e}")
        return {}

def manus_create_task(prompt, model="manus-1.6-lite-adaptive"):
    """Submit a new autonomous agent task to Manus AI"""
    url = f"{MANUS_BASE_URL}/tasks"
    headers = {
        "API_KEY": MANUS_KEY,
        "Authorization": f"Bearer {MANUS_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    # GAuth Zero-Trust Run Signature
    if gauth_gate:
        gauth_res = gauth_gate.authorize_workflow_run(f"Manus AI Task ({model})", agent="manus", details=prompt[:40])
        headers["X-GAuth-Signature"] = gauth_res.get("signature", "")
        headers["X-GAuth-Run-Token"] = gauth_res.get("run_token", "")

    payload = json.dumps({
        "model": model,
        "prompt": prompt
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=20, context=CTX) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data
    except Exception as e:
        print(f"[!] Manus create_task error: {e}")
        return {}

# ==========================================
# CLI DISPATCHER
# ==========================================
def main():
    parser = argparse.ArgumentParser(description="Agnes AI & Manus AI Client")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Agnes commands
    agnes_p = subparsers.add_parser("agnes", help="Agnes AI operations")
    agnes_p.add_argument("--list-models", action="store_true", help="List available Agnes models")
    agnes_p.add_argument("--chat", type=str, help="Prompt to send to Agnes AI")
    agnes_p.add_argument("--model", type=str, default="agnes-2.5-flash", help="Agnes model to use")

    # Manus commands
    manus_p = subparsers.add_parser("manus", help="Manus AI operations")
    manus_p.add_argument("--list-tasks", action="store_true", help="List recent tasks")
    manus_p.add_argument("--task-id", type=str, help="Get details for a task ID")
    manus_p.add_argument("--create-task", type=str, help="Create a new autonomous Manus task")
    manus_p.add_argument("--model", type=str, default="manus-1.6-lite-adaptive", help="Manus model to use")

    args = parser.parse_args()

    if args.command == "agnes":
        if args.list_models:
            models = agnes_list_models()
            print(f"=== AGNES AI MODELS ({len(models)} Available) ===")
            for m in models:
                print(f" - {m.get('id')}")
        elif args.chat:
            print(f"[*] Agnes AI ({args.model}): Sending prompt...")
            agnes_chat_stream(args.chat, model=args.model)
        else:
            agnes_p.print_help()

    elif args.command == "manus":
        if args.list_tasks:
            tasks = manus_list_tasks()
            print(f"=== MANUS AI RECENT TASKS ({len(tasks)} Found) ===")
            for t in tasks:
                meta = t.get("metadata", {})
                title = meta.get("task_title", "Untitled")
                print(f" - ID: {t.get('id')} | Status: {t.get('status')} | Model: {t.get('model')} | Title: {title}")
        elif args.task_id:
            task = manus_get_task(args.task_id)
            print(json.dumps(task, indent=2, ensure_ascii=False))
        elif args.create_task:
            print(f"[*] Submitting task to Manus AI ({args.model})...")
            res = manus_create_task(args.create_task, model=args.model)
            print("Response:", json.dumps(res, indent=2, ensure_ascii=False))
        else:
            manus_p.print_help()
    else:
        # Default status check
        print("=== AGNES AI & MANUS AI GATEWAY STATUS ===")
        models = agnes_list_models()
        print(f"1. Agnes AI: CONNECTED ({len(models)} models)")
        tasks = manus_list_tasks()
        print(f"2. Manus AI: CONNECTED ({len(tasks)} tasks on record)")
        print("\nUse --help for CLI execution options.")

if __name__ == "__main__":
    main()
