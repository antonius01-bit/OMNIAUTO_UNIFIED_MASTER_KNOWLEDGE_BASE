#!/usr/bin/env python3
import sys
import json
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def test_groq():
    key = "gsk_REDACTED_BY_SECURITY_POLICY"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}
    payload = json.dumps({"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 10}).encode("utf-8")
    try:
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print("Groq: OK -", data["choices"][0]["message"]["content"].strip(), flush=True)
            return True
    except Exception as e:
        print("Groq Error:", e, flush=True)
        return False

def test_openai():
    key = "sk-REDACTED_BY_SECURITY_POLICY"
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}
    payload = json.dumps({"model": "gpt-4o-mini", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 10}).encode("utf-8")
    try:
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print("OpenAI: OK -", data["choices"][0]["message"]["content"].strip(), flush=True)
            return True
    except Exception as e:
        print("OpenAI Error:", e, flush=True)
        return False

def test_openrouter():
    key = "sk-REDACTED_BY_SECURITY_POLICY"
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}
    payload = json.dumps({"model": "deepseek/deepseek-chat", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 10}).encode("utf-8")
    try:
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print("OpenRouter: OK -", data["choices"][0]["message"]["content"].strip(), flush=True)
            return True
    except Exception as e:
        print("OpenRouter Error:", e, flush=True)
        return False

def test_gemini():
    key = "AQ.REDACTED_BY_SECURITY_POLICY"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent?key={key}"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"contents": [{"parts": [{"text": "ping"}]}], "generationConfig": {"maxOutputTokens": 10}}).encode("utf-8")
    try:
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print("Gemini: OK -", data["candidates"][0]["content"]["parts"][0]["text"].strip(), flush=True)
            return True
    except Exception as e:
        print("Gemini Error:", e, flush=True)
        return False

def test_agnes():
    key = "sk-REDACTED_BY_SECURITY_POLICY"
    url = "https://apihub.agnes-ai.com/v1/models"
    headers = {"Authorization": f"Bearer {key}", "User-Agent": "Mozilla/5.0"}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            models = [m.get("id") for m in data.get("data", [])]
            print("Agnes AI: OK -", f"{len(models)} models available (e.g. {models[0]})", flush=True)
            return True
    except Exception as e:
        print("Agnes AI Error:", e, flush=True)
        return False

def test_manus():
    key = "sk-REDACTED_BY_SECURITY_POLICY"
    url = "https://api.manus.im/v1/tasks"
    headers = {
        "API_KEY": key,
        "Authorization": f"Bearer {key}",
        "User-Agent": "Mozilla/5.0"
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            tasks = data.get("data", [])
            print("Manus AI: OK -", f"Connected ({len(tasks)} agent tasks on file)", flush=True)
            return True
    except Exception as e:
        print("Manus AI Error:", e, flush=True)
        return False

if __name__ == "__main__":
    print("Testing Provider Connections...", flush=True)
    test_groq()
    test_openai()
    test_openrouter()
    test_gemini()
    test_agnes()
    test_manus()
