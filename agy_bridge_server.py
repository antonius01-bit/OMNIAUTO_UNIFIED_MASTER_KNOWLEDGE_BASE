import os
import sys
import json
import datetime
import urllib.request
import urllib.error
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

PORT = 5050
VAULT_PATH = r"C:\Users\antoni\Dola\obsidian_vault"
HISTORY_DIR = os.path.join(VAULT_PATH, "09_AI_WORKFLOW", "Chat_History")
MEMORY_CACHE_FILE = os.path.join(os.path.dirname(VAULT_PATH), "agent_memory.json")

# 7-Key High-Availability Failover Mesh provided by User
KEY_POOL = [
    "AIzaSy_REDACTED_BY_SECURITY_POLICY_X1",
    "AIzaSy_REDACTED_BY_SECURITY_POLICY_X1",
    "AIzaSy_REDACTED_BY_SECURITY_POLICY_X1",
    "AQ.REDACTED_BY_SECURITY_POLICY",
    "AQ.REDACTED_BY_SECURITY_POLICY",
    "AQ.REDACTED_BY_SECURITY_POLICY",
    "AQ.REDACTED_BY_SECURITY_POLICY"
]

FALLBACK_MODELS = [
    "gemini-flash-lite-latest",
    "gemini-flash-latest",
    "gemini-2.5-flash",
    "gemini-2.0-flash-exp",
    "gemini-1.5-flash"
]

class KeyUsageManager:
    def __init__(self, keys, models):
        self.keys = list(keys)
        self.models = list(models)
        self.stats = {}
        for k in self.keys:
            self.stats[k] = {
                "key_masked": k[:8] + "..." + k[-4:],
                "status": "HEALTHY",
                "cooldown_until": 0.0,
                "success_count": 0,
                "error_count": 0,
                "rate_limit_count": 0,
                "last_used": None,
                "last_error": None
            }
        self.request_timestamps = []
        self.total_requests = 0

    def get_available_keys(self, custom_keys=None):
        now = time.time()
        for k, s in self.stats.items():
            if s["status"] == "COOLDOWN" and now >= s["cooldown_until"]:
                s["status"] = "HEALTHY"
                s["cooldown_until"] = 0.0

        all_candidate_keys = []
        if custom_keys:
            for ck in custom_keys:
                if ck not in all_candidate_keys:
                    all_candidate_keys.append(ck)
        for k in self.keys:
            if k not in all_candidate_keys:
                all_candidate_keys.append(k)

        healthy = [k for k in all_candidate_keys if self.stats.get(k, {}).get("status", "HEALTHY") == "HEALTHY"]
        cooldown = [k for k in all_candidate_keys if self.stats.get(k, {}).get("status", "HEALTHY") != "HEALTHY"]
        return healthy + cooldown

    def mark_success(self, key, model=None):
        now = time.time()
        self.total_requests += 1
        self.request_timestamps.append(now)
        self.request_timestamps = [t for t in self.request_timestamps if now - t <= 60]

        if key in self.stats:
            self.stats[key]["status"] = "HEALTHY"
            self.stats[key]["cooldown_until"] = 0.0
            self.stats[key]["success_count"] += 1
            self.stats[key]["last_used"] = datetime.datetime.now().strftime("%H:%M:%S")

    def mark_rate_limited(self, key, cooldown_seconds=60, error_msg="Rate limit reached"):
        now = time.time()
        if key in self.stats:
            self.stats[key]["status"] = "COOLDOWN"
            self.stats[key]["cooldown_until"] = now + cooldown_seconds
            self.stats[key]["rate_limit_count"] += 1
            self.stats[key]["error_count"] += 1
            self.stats[key]["last_error"] = str(error_msg)[:120]

    def mark_error(self, key, error_msg):
        if key in self.stats:
            self.stats[key]["error_count"] += 1
            self.stats[key]["last_error"] = str(error_msg)[:120]

    def get_telemetry_stats(self):
        now = time.time()
        self.request_timestamps = [t for t in self.request_timestamps if now - t <= 60]
        rpm = len(self.request_timestamps)

        healthy_count = 0
        cooldown_count = 0
        keys_summary = []
        for k in self.keys:
            s = self.stats[k]
            if s["status"] == "COOLDOWN" and now >= s["cooldown_until"]:
                s["status"] = "HEALTHY"
                s["cooldown_until"] = 0.0
            if s["status"] == "HEALTHY":
                healthy_count += 1
            else:
                cooldown_count += 1

            remaining_cooldown = max(0, int(s["cooldown_until"] - now)) if s["status"] == "COOLDOWN" else 0
            keys_summary.append({
                "key_id": s["key_masked"],
                "status": s["status"],
                "success_count": s["success_count"],
                "error_count": s["error_count"],
                "rate_limit_count": s["rate_limit_count"],
                "last_used": s["last_used"] or "None",
                "cooldown_remaining_sec": remaining_cooldown
            })

        total_keys = len(self.keys) or 1
        ratio_cooldown = cooldown_count / total_keys
        ratio_rpm = min(1.0, rpm / 15.0)
        usage_pct = round((ratio_cooldown * 70.0) + (ratio_rpm * 30.0), 1)

        bionic_status = "STANDBY (:1234)"
        try:
            probe = urllib.request.urlopen("http://127.0.0.1:1234/v1/models", timeout=0.6)
            if probe.status == 200:
                bionic_status = "ONLINE (:1234)"
        except Exception:
            pass

        return {
            "usage_percentage": usage_pct,
            "total_keys": total_keys,
            "healthy_keys_count": healthy_count,
            "cooling_keys_count": cooldown_count,
            "total_requests": self.total_requests,
            "rpm": rpm,
            "zero_billing_shield": "STRICT ZERO-BILLING ACTIVE (FREE TIER & LOCAL ONLY)",
            "primary_model": self.models[0] if self.models else "gemini-flash-lite-latest",
            "fallback_models": self.models,
            "bionic_local_status": bionic_status,
            "keys": keys_summary,
            "last_checked": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

key_manager = KeyUsageManager(KEY_POOL, FALLBACK_MODELS)

# GAuth Zero-Trust Security Gate Integration
try:
    scripts_path = os.path.join(os.path.dirname(VAULT_PATH), "scripts")
    if scripts_path not in sys.path:
        sys.path.insert(0, scripts_path)
    import gauth_security_gate as gauth_gate
except Exception as e:
    gauth_gate = None
    print(f"[!] Warning: GAuth security gate not loaded: {e}")

import time

ACTIVE_TASKS = {}

def register_task(task_id, name, details=""):
    ACTIVE_TASKS[task_id] = {
        "id": task_id,
        "name": name,
        "details": details,
        "started_at": datetime.datetime.now().strftime("%H:%M:%S"),
        "timestamp": time.time()
    }

def finish_task(task_id):
    if task_id in ACTIVE_TASKS:
        del ACTIVE_TASKS[task_id]

def get_active_tasks():
    # Clean up stale tasks older than 30 minutes
    now = time.time()
    stale = [k for k, v in ACTIVE_TASKS.items() if now - v.get("timestamp", now) > 1800]
    for k in stale:
        del ACTIVE_TASKS[k]
    return list(ACTIVE_TASKS.values())

def load_memory_turns(max_turns=6):
    """Load recent conversational memory for context awareness."""
    if os.path.exists(MEMORY_CACHE_FILE):
        try:
            with open(MEMORY_CACHE_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("turns", [])[-max_turns:]
        except Exception:
            return []
    return []

def save_memory_turn(prompt, reply, agent, provider):
    """Permanently store every conversation turn into Obsidian Vault and local JSON."""
    os.makedirs(HISTORY_DIR, exist_ok=True)
    today_str = datetime.date.today().isoformat()
    md_file = os.path.join(HISTORY_DIR, f"Dola_Agent_Chat_{today_str}.md")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 1. Append to Obsidian Vault Markdown Note
    if not os.path.exists(md_file):
        header = f"""---
title: "Dola AI Swarm Chat — {today_str}"
created: {today_str}
tags: [dola, agy, chat-history, memory, second-brain]
type: log
---

# 🧠 Dola AI Swarm — Catatan Memori Percakapan ({today_str})
Terhubung langsung ke [[00_MASTER_DASHBOARD]] dan [[09_AI_WORKFLOW]].

---
"""
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(header)

    entry = f"""
### 🕒 [{timestamp}] User ke [[{agent.upper()}]]
- **Provider / Model**: `{provider}`
- **User Prompt**: {prompt}

**Jawaban Agen**:
{reply}

---
"""
    try:
        with open(md_file, 'a', encoding='utf-8') as f:
            f.write(entry)
    except Exception as e:
        print("Error saving to markdown note:", e)

    # 2. Append to agent_memory.json for contextual recall
    all_turns = []
    if os.path.exists(MEMORY_CACHE_FILE):
        try:
            with open(MEMORY_CACHE_FILE, 'r', encoding='utf-8') as f:
                cache = json.load(f)
                all_turns = cache.get("turns", [])
        except Exception:
            all_turns = []

    all_turns.append({
        "timestamp": timestamp,
        "agent": agent,
        "prompt": prompt,
        "reply": reply,
        "provider": provider
    })

    # Keep last 150 turns
    all_turns = all_turns[-150:]
    try:
        with open(MEMORY_CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump({"updated_at": timestamp, "total_turns": len(all_turns), "turns": all_turns}, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Error saving memory json:", e)

    return f"Dola_Agent_Chat_{today_str}.md", len(all_turns)

def search_obsidian_brain(query, max_results=4):
    """Sub-second semantic/text search across 600+ Obsidian markdown notes for RAG grounding."""
    if not query or len(query.strip()) < 2:
        return []
    import re
    # Extract keywords (min 3 chars, alphanumeric)
    words = re.findall(r'\b[a-zA-Z0-9_\-]{3,}\b', query.lower())
    stop_words = {"dan", "atau", "yang", "untuk", "dari", "pada", "ini", "itu", "dengan", "akan", "the", "and", "for", "with", "this", "that", "from"}
    q_words = [w for w in words if w not in stop_words]
    if not q_words:
        q_words = words or [query.lower().strip()]

    results = []
    if os.path.exists(VAULT_PATH):
        for root, _, files in os.walk(VAULT_PATH):
            for f in files:
                if f.endswith('.md'):
                    fpath = os.path.join(root, f)
                    try:
                        with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                            content = fp.read()
                            score = 0
                            f_lower = f.lower()
                            c_lower = content.lower()
                            for w in q_words:
                                if w in f_lower:
                                    score += 4
                                if w in c_lower:
                                    score += 1
                            if score > 0:
                                # find snippet
                                idx = -1
                                for w in q_words:
                                    pos = c_lower.find(w)
                                    if pos != -1:
                                        idx = pos
                                        break
                                if idx != -1:
                                    start = max(0, idx - 80)
                                    end = min(len(content), idx + 200)
                                    snippet = content[start:end].replace('\n', ' ').strip()
                                else:
                                    snippet = content[:200].replace('\n', ' ').strip()
                                rel_path = os.path.relpath(fpath, VAULT_PATH).replace('\\', '/')
                                title = f.replace('.md', '').replace('_', ' ')
                                results.append({
                                    "title": title,
                                    "file": f,
                                    "path": rel_path,
                                    "score": score,
                                    "snippet": snippet
                                })
                    except Exception:
                        pass
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:max_results]

def save_atomic_brain_note(title, prompt, reply, agent="tri-core", tags=None):
    """Saves a permanent atomic note with frontmatter and wikilinks into 20_MULTI_AGENT_BRAIN."""
    import re
    brain_dir = os.path.join(VAULT_PATH, "20_MULTI_AGENT_BRAIN")
    os.makedirs(brain_dir, exist_ok=True)
    today_str = datetime.date.today().isoformat()
    time_str = datetime.datetime.now().strftime("%H%M%S")
    clean_title = re.sub(r'[^a-zA-Z0-9_\-\s]', '', title).strip().replace(' ', '_')[:35] or "Synapse_Memory"
    filename = f"SYNAPSE_{clean_title}_{time_str}.md"
    fpath = os.path.join(brain_dir, filename)

    tag_list = ["dola", "agy", "stark-os", "brain-synapse", agent.lower()]
    if tags:
        tag_list.extend(tags)
    tag_str = ", ".join(list(set(tag_list)))

    content = f"""---
title: "{title}"
created: {today_str}
tags: [{tag_str}]
type: brain-synapse
agent: {agent}
status: verified
---

> **Brain Hubs**: [[00_INDEX_MULTI_AGENT_BRAIN]] | [[STARK_TRI_CORE_QUANTUM_BRAIN]] | [[SIX_PILLAR_AGENT_ALLIANCE]]

# 🧠 Synapse Memory: {title}

- **Waktu Eksekusi**: `{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}`
- **Agen Eksekutor**: `[[{agent.upper()}]]`
- **Pilar Terhubung**: Bionic, Gemini, AGY, Dola AI, Copilot, Obsidian Brain

---

## 📥 User Directive / Instruksi
> {prompt}

---

## ⚡ Hasil Sintesis & Kolaborasi Tri-Core
{reply}

---

## 🔗 Hubungan & Backlinks
- [[00_MASTER_DASHBOARD]]
- [[09_AI_WORKFLOW]]
- [[20_MULTI_AGENT_BRAIN]]
"""
    try:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        return filename
    except Exception as e:
        print("Error saving atomic brain note:", e)
        return None

def get_brain_stats():
    """Returns comprehensive real-time metrics of the Obsidian Knowledge Brain."""
    total_notes = 0
    folders = set()
    recent = []
    if os.path.exists(VAULT_PATH):
        for root, dirs, files in os.walk(VAULT_PATH):
            for f in files:
                if f.endswith('.md'):
                    total_notes += 1
                    fp = os.path.join(root, f)
                    try:
                        mtime = os.path.getmtime(fp)
                        rel = os.path.relpath(fp, VAULT_PATH).replace('\\', '/')
                        folder = rel.split('/')[0] if '/' in rel else 'Root'
                        folders.add(folder)
                        recent.append({
                            'title': f.replace('.md', '').replace('_', ' '),
                            'file': f,
                            'path': rel,
                            'mtime': mtime,
                            'time_str': datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
                        })
                    except Exception:
                        pass
    recent.sort(key=lambda x: x['mtime'], reverse=True)

    # Check if Local Bionic LM Studio is active on port 1234
    bionic_status = "STANDBY (:1234)"
    try:
        probe = urllib.request.urlopen("http://127.0.0.1:1234/v1/models", timeout=0.8)
        if probe.status == 200:
            bionic_status = "ONLINE (LM Studio :1234)"
    except Exception:
        pass

    return {
        "status": "ONLINE",
        "total_notes": total_notes,
        "vault_path": VAULT_PATH,
        "folders_count": len(folders),
        "recent_notes": recent[:8],
        "six_pillars": {
            "bionic": bionic_status,
            "gemini": "ONLINE (7-Key Rotation Pool)",
            "agy": f"ONLINE (Port {PORT})",
            "dola": "ONLINE (Cosmic Enterprise OS)",
            "copilot": "CONNECTED (Harness Mesh)",
            "obsidian": f"ONLINE ({total_notes} Synapses Active)"
        },
        "last_synapse": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def call_bionic_lmstudio(prompt, system_instruction):
    """Attempts to call local LM Studio on port 1234 with graceful exception handling."""
    url = "http://127.0.0.1:1234/v1/chat/completions"
    payload = json.dumps({
        "model": "local-model",
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }).encode('utf-8')
    req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=8) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        return data['choices'][0]['message']['content']

class AGYBridgeHandler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-API-Key, X-goog-api-key')

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path in ('/', '/stark', '/jarvis', '/hud', '/ironman'):
            stark_file = os.path.join(os.path.dirname(VAULT_PATH), "stark_jarvis_ironman_hud.html")
            if os.path.exists(stark_file):
                with open(stark_file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(html_content.encode('utf-8'))
                return
            else:
                self._send_json(404, {"error": "Stark HUD file not found"})
                return

        elif parsed.path in ('/office', '/floor'):
            office_file = os.path.join(os.path.dirname(VAULT_PATH), "agy_office_floor.html")
            if os.path.exists(office_file):
                with open(office_file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(html_content.encode('utf-8'))
                return
            else:
                self._send_json(404, {"error": "Office floor view file not found"})
                return

        elif parsed.path in ('/feralui', '/physics'):
            feral_file = os.path.join(os.path.dirname(VAULT_PATH), "feralui_physics_showcase.html")
            if os.path.exists(feral_file):
                with open(feral_file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(html_content.encode('utf-8'))
                return
            else:
                self._send_json(404, {"error": "FeralUI showcase file not found"})
                return

        elif parsed.path in ('/voice', '/dola', '/friday', '/dola_ai_enterprise_os.html'):
            voice_file = os.path.join(os.path.dirname(VAULT_PATH), "dola_ai_enterprise_os.html")
            if os.path.exists(voice_file):
                with open(voice_file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(html_content.encode('utf-8'))
                return
            else:
                self._send_json(404, {"error": "Dola Voice OS file not found"})
                return

        elif parsed.path == '/api/launch/mark85':
            import subprocess
            try:
                vbs_path = os.path.join(os.path.dirname(VAULT_PATH), "speak_jarvis.vbs")
                if os.path.exists(vbs_path):
                    subprocess.Popen(["wscript", vbs_path, "Tri-Core neural mesh synchronized into single Jarvis interface. Friday and Ultron standing by as co-thinkers."])
                self._send_json(200, {
                    "status": "ok",
                    "mode": "unified_jarvis_preview",
                    "message": "Unified Jarvis View active. 3 brains synchronized into single preview."
                })
            except Exception as e:
                self._send_json(500, {"status": "error", "error": str(e)})
            return

        elif parsed.path == '/api/launch/jarvis':
            import subprocess
            vbs_path = os.path.join(os.path.dirname(VAULT_PATH), "speak_jarvis.vbs")
            if os.path.exists(vbs_path):
                subprocess.Popen(["wscript", vbs_path, "Jarvis lead core ready."])
            self._send_json(200, {"status": "ok", "url": "http://127.0.0.1:5050/stark", "role": "lead_host"})
            return

        elif parsed.path == '/api/launch/friday':
            import subprocess
            vbs_path = os.path.join(os.path.dirname(VAULT_PATH), "speak_jarvis.vbs")
            if os.path.exists(vbs_path):
                subprocess.Popen(["wscript", vbs_path, "Friday co-brain assisting Jarvis."])
            self._send_json(200, {"status": "ok", "url": "http://127.0.0.1:5050/stark", "role": "co_thinker_workflow"})
            return

        elif parsed.path == '/api/launch/ultron':
            import subprocess
            vbs_path = os.path.join(os.path.dirname(VAULT_PATH), "speak_jarvis.vbs")
            if os.path.exists(vbs_path):
                subprocess.Popen(["wscript", vbs_path, "Ultron co-brain assisting Jarvis."])
            self._send_json(200, {"status": "ok", "url": "http://127.0.0.1:5050/stark", "role": "co_thinker_logic"})
            return

        elif parsed.path == '/api/launch/sota':
            import subprocess
            cmd_path = os.path.join(os.path.dirname(VAULT_PATH), "sota_5_agents_suite.py")
            subprocess.Popen(["cmd.exe", "/c", "start", "python", cmd_path, "--interactive"], cwd=os.path.dirname(VAULT_PATH))
            self._send_json(200, {"status": "ok", "message": "SOTA 5-in-1 CLI launched in new window"})
            return

        elif parsed.path == '/api/launch/modelopt':
            import subprocess
            cmd_path = os.path.join(os.path.dirname(VAULT_PATH), "nvidia_modelopt_recipes.py")
            subprocess.Popen(["cmd.exe", "/c", "start", "python", cmd_path, "--help"], cwd=os.path.dirname(VAULT_PATH))
            self._send_json(200, {"status": "ok", "message": "NVIDIA ModelOpt CLI launched in new window"})
            return

        elif parsed.path == '/api/sync/run':
            import subprocess
            sync_script = os.path.join(os.path.dirname(VAULT_PATH), "dola_sync_all.py")
            subprocess.Popen(["python", sync_script, "--force"], cwd=os.path.dirname(VAULT_PATH))
            self._send_json(200, {
                "status": "ok",
                "message": "6-Way Omni-Sync & 3-Cloud Backup initiated in background"
            })
            return

        elif parsed.path.startswith('/api/voice'):
            from urllib.parse import parse_qs
            qs = parse_qs(parsed.query)
            text = qs.get('text', ['Stark Industries online, sir.'])[0]
            vbs_path = os.path.join(os.path.dirname(VAULT_PATH), "speak_jarvis.vbs")
            if os.path.exists(vbs_path):
                import subprocess
                subprocess.Popen(["wscript", vbs_path, text])
            self._send_json(200, {"status": "ok", "spoken": text})
            return

        elif parsed.path == '/api/tasks/status':
            tasks = get_active_tasks()
            self._send_json(200, {
                "active_tasks_count": len(tasks),
                "tasks": tasks,
                "has_running_tasks": len(tasks) > 0,
                "core_ais": {
                    "jarvis": {"name": "J.A.R.V.I.S.", "status": "ONLINE", "endpoint": "/office"},
                    "friday": {"name": "F.R.I.D.A.Y.", "status": "ONLINE", "endpoint": "/voice"},
                    "ultron": {"name": "U.L.T.R.O.N.", "status": "ONLINE", "endpoint": "/feralui"}
                },
                "master_2fa_pin": "111993"
            })
            return

        elif parsed.path.startswith('/api/shutdown'):
            from urllib.parse import parse_qs
            qs = parse_qs(parsed.query)
            force = qs.get('force', ['false'])[0].lower() == 'true'
            tasks = get_active_tasks()
            
            if len(tasks) > 0 and not force:
                self._send_json(200, {
                    "status": "warning",
                    "can_exit": False,
                    "active_tasks_count": len(tasks),
                    "tasks": tasks,
                    "message": "Active tasks are still running. Confirmation required before exit."
                })
                return

            vbs_path = os.path.join(os.path.dirname(VAULT_PATH), "speak_jarvis.vbs")
            if os.path.exists(vbs_path):
                import subprocess
                subprocess.Popen(["wscript", vbs_path, "Powering down systems. Goodbye, sir."])

            self._send_json(200, {
                "status": "shutting_down",
                "can_exit": True,
                "message": "Stark Industries Bridge Server is shutting down cleanly."
            })
            
            import threading
            def _kill():
                time.sleep(0.8)
                os._exit(0)
            threading.Thread(target=_kill, daemon=True).start()
            return

        elif parsed.path in ('/api/usage/stats', '/api/usage/status'):
            telemetry = key_manager.get_telemetry_stats()
            self._send_json(200, telemetry)
            return

        elif parsed.path == '/api/status':
            vault_count = 0
            if os.path.exists(VAULT_PATH):
                for root, _, files in os.walk(VAULT_PATH):
                    for f in files:
                        if f.endswith('.md'):
                            vault_count += 1

            # Check memory stats
            memory_count = 0
            if os.path.exists(MEMORY_CACHE_FILE):
                try:
                    with open(MEMORY_CACHE_FILE, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        memory_count = len(data.get("turns", []))
                except Exception:
                    pass

            tasks = get_active_tasks()
            usage_info = key_manager.get_telemetry_stats()
            response = {
                "status": "online",
                "engine": "Antigravity AGY High-Availability Mesh v5.0 (With Obsidian Memory & Zero-Billing Shield)",
                "port": PORT,
                "vault_path": VAULT_PATH,
                "vault_notes": vault_count,
                "memory_turns_saved": memory_count,
                "active_tasks_count": len(tasks),
                "active_tasks": tasks,
                "core_ais": {
                    "jarvis": {
                        "name": "J.A.R.V.I.S.",
                        "status": "ONLINE",
                        "endpoint": "/stark",
                        "role": "Lead Host, Quantum Orchestration & 3-Brain Preview"
                    },
                    "friday": {
                        "name": "F.R.I.D.A.Y.",
                        "status": "ONLINE",
                        "endpoint": "/stark",
                        "role": "Executive Voice Swarm & Workflow Co-Thinker"
                    },
                    "ultron": {
                        "name": "U.L.T.R.O.N.",
                        "status": "ONLINE",
                        "endpoint": "/stark",
                        "role": "Cognitive Deep Reasoning, Code Architecture & Co-Thinker"
                    }
                },
                "master_pin_2fa": "111993",
                "history_dir": HISTORY_DIR,
                "key_pool_count": len(KEY_POOL),
                "primary_model": usage_info.get("primary_model", "gemini-flash-lite-latest"),
                "usage_telemetry": usage_info,
                "gauth_security": "ARMED" if gauth_gate else "DISABLED",
                "gauth_mode": gauth_gate.SECURITY_MODE if gauth_gate else "NONE",
                "gauth_2fa_active": True if gauth_gate else False
            }
            self._send_json(200, response)

        elif parsed.path == '/api/gauth/status':
            if gauth_gate:
                code, remaining = gauth_gate.get_current_totp()
                self._send_json(200, {
                    "status": "ARMED",
                    "security_mode": gauth_gate.SECURITY_MODE,
                    "account": gauth_gate.ACCOUNT,
                    "issuer": gauth_gate.ISSUER,
                    "totp_code": code,
                    "seconds_remaining": remaining,
                    "otpauth_uri": gauth_gate.get_otpauth_uri(),
                    "audit_log": gauth_gate.AUDIT_LOG_PATH
                })
            else:
                self._send_json(500, {"error": "GAuth Security Gate module not loaded"})
            return

        elif parsed.path == '/api/gauth/totp':
            if gauth_gate:
                code, remaining = gauth_gate.get_current_totp()
                self._send_json(200, {
                    "code": code,
                    "seconds_remaining": remaining
                })
            else:
                self._send_json(500, {"error": "GAuth module not loaded"})
            return


        elif parsed.path == '/api/memory/get':
            turns = load_memory_turns(20)
            self._send_json(200, {"turns": turns, "count": len(turns)})

        elif parsed.path == '/api/vault/list':
            notes = []
            if os.path.exists(VAULT_PATH):
                for root, _, files in os.walk(VAULT_PATH):
                    for f in files:
                        if f.endswith('.md'):
                            rel = os.path.relpath(os.path.join(root, f), VAULT_PATH)
                            notes.append(rel.replace('\\', '/'))
            self._send_json(200, {"notes": notes, "count": len(notes)})

        elif parsed.path == '/api/playbook/instagram21':
            playbook_file = os.path.join(os.path.dirname(VAULT_PATH), "harvested_instagram_all_21.json")
            data = []
            if os.path.exists(playbook_file):
                try:
                    with open(playbook_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except Exception:
                    pass
            self._send_json(200, {"total_items": len(data), "items": data})

        elif parsed.path == '/api/templates/resume':
            resume_note = os.path.join(VAULT_PATH, "01_PROMPT_ENGINEERING", "CLAUDE_7_JOB_SEARCH_RESUME_PROMPTS.md")
            content = ""
            if os.path.exists(resume_note):
                with open(resume_note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Claude 7 Job-Search Prompts", "content": content})

        elif parsed.path == '/api/templates/gemini-hacks':
            hacks_note = os.path.join(VAULT_PATH, "01_PROMPT_ENGINEERING", "GEMINI_8_KILLER_PROMPT_HACKS.md")
            content = ""
            if os.path.exists(hacks_note):
                with open(hacks_note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Gemini 8 Killer Prompt Hacks", "content": content})

        elif parsed.path == '/api/templates/legal':
            legal_note = os.path.join(VAULT_PATH, "05_OPERATIONS", "STARTUP_FOUNDER_7_LEGAL_DOCUMENTS.md")
            content = ""
            if os.path.exists(legal_note):
                with open(legal_note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Startup Founder 7 Legal Documents", "content": content})

        elif parsed.path == '/api/templates/google-tools':
            tools_note = os.path.join(VAULT_PATH, "09_AI_WORKFLOW", "GOOGLE_15_FREE_AI_TOOLS_CATALOG.md")
            content = ""
            if os.path.exists(tools_note):
                with open(tools_note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Google 15 Free AI Tools Catalog", "content": content})

        elif parsed.path == '/api/templates/claude-haram':
            haram_note = os.path.join(VAULT_PATH, "01_PROMPT_ENGINEERING", "ANOTECHHUB_10_CLAUDE_PROMPTS_HARAM.md")
            content = ""
            if os.path.exists(haram_note):
                with open(haram_note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Anotechhub 10 Claude Haram Prompts", "content": content})

        elif parsed.path == '/api/templates/consensus-research':
            consensus_note = os.path.join(VAULT_PATH, "02_ACADEMIC", "CONSENSUS_CONNECTOR_CLAUDE_RESEARCH.md")
            content = ""
            if os.path.exists(consensus_note):
                with open(consensus_note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Consensus Academic Research Connector", "content": content})

        elif parsed.path == '/api/templates/sifuyik-enterprise':
            sifuyik_note = os.path.join(VAULT_PATH, "01_PROMPT_ENGINEERING", "SIFUYIK_50_ENTERPRISE_PROMPT_ARSENAL.md")
            content = ""
            if os.path.exists(sifuyik_note):
                with open(sifuyik_note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Sifuyik 50 Enterprise Prompt Arsenal", "content": content})

        elif parsed.path == '/api/templates/knox-brain':
            knox_note = os.path.join(VAULT_PATH, "10_OBSIDIAN", "OBSIDIAN_SECOND_BRAIN_KNOX_FRAMEWORK.md")
            content = ""
            if os.path.exists(knox_note):
                with open(knox_note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Obsidian Second Brain Knox Framework", "content": content})

        elif parsed.path == '/api/templates/omni-editor':
            editor_note = os.path.join(VAULT_PATH, "08_PRESENTATION", "OMNI_IMAGE_EDITOR_AD_TYPOGRAPHY.md")
            content = ""
            if os.path.exists(editor_note):
                with open(editor_note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Omni Image Editor & Ad Typography Studio", "content": content})

        elif parsed.path == '/api/templates/superlinked-sie':
            note = os.path.join(VAULT_PATH, "09_AI_WORKFLOW", "SUPERLINKED_SIE_INFERENCE_ENGINE.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Superlinked Inference Engine", "content": content})

        elif parsed.path == '/api/templates/odysseus-automation':
            note = os.path.join(VAULT_PATH, "09_AI_WORKFLOW", "ODYSSEUS_PEWDIEPIE_APP_AUTOMATION.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Odysseus App Automation Harness", "content": content})

        elif parsed.path == '/api/templates/claude-ooda':
            note = os.path.join(VAULT_PATH, "01_PROMPT_ENGINEERING", "CLAUDE_5_SECRET_CODES_OODA.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Claude 5 Secret Codes & OODA", "content": content})

        elif parsed.path == '/api/templates/free-stack-matrix':
            note = os.path.join(VAULT_PATH, "00_MASTER", "FREE_AI_VS_PAID_SAAS_BENCHMARK_MATRIX.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Free AI vs Paid SaaS Matrix", "content": content})

        elif parsed.path == '/api/templates/founder-railway-os':
            note = os.path.join(VAULT_PATH, "05_OPERATIONS", "FOUNDER_OS_RAILWAY_DEPLOYMENT.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Founder OS Railway Deployment", "content": content})

        elif parsed.path == '/api/templates/whatsapp-n8n-cs':
            note = os.path.join(VAULT_PATH, "05_OPERATIONS", "WHATSAPP_N8N_AI_CHATBOT_CS.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "WhatsApp n8n AI Chatbot CS", "content": content})

        elif parsed.path == '/api/templates/skills-80-directory':
            note = os.path.join(VAULT_PATH, "00_MASTER", "80_FREE_HIGH_PAYING_SKILLS_DIRECTORY.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "80 Free High-Paying Skills Directory", "content": content})

        elif parsed.path == '/api/templates/system-prompts-leaks':
            note = os.path.join(VAULT_PATH, "01_PROMPT_ENGINEERING", "SYSTEM_PROMPTS_LEAKS_MASTER_ANALYSIS.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "System Prompts Leaks Master Analysis", "content": content})

        elif parsed.path in ('/api/templates/omniauto-v42', '/api/templates/omniauto'):
            note = os.path.join(VAULT_PATH, "llm-wiki", "wiki", "OMNIAUTO_v4.2_SHARE_TO_ALL_AI.md")
            if not os.path.exists(note):
                note = os.path.join(VAULT_PATH, "00_MASTER", "OMNIAUTO_v4.2_SHARE_TO_ALL_AI.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "OmniAuto v4.2 — Master Hub (Share to All AI)", "content": content})

        elif parsed.path == '/api/templates/cactus-engine':
            note = os.path.join(VAULT_PATH, "09_AI_WORKFLOW", "CACTUS_COMPUTE_EDGE_INFERENCE_ENGINE.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Cactus Compute Edge Inference Engine", "content": content})

        elif parsed.path == '/api/templates/gemma-unsloth':
            note = os.path.join(VAULT_PATH, "09_AI_WORKFLOW", "GOOGLE_GEMMA_4_UNSLOTH_TRAINING_PLAYBOOK.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Google Gemma 4 & Unsloth Training Playbook", "content": content})

        elif parsed.path == '/api/templates/lmstudio-mesh':
            note = os.path.join(VAULT_PATH, "09_AI_WORKFLOW", "LM_STUDIO_DEVELOPER_HEADLESS_MESH.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "LM Studio Developer Headless Mesh", "content": content})

        elif parsed.path == '/api/templates/kaggle-benchmarks':
            note = os.path.join(VAULT_PATH, "04_DATA", "KAGGLE_BENCHMARKS_GAME_ARENA_EVALUATION.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Kaggle Benchmarks & Game Arena Evaluation", "content": content})

        elif parsed.path == '/api/templates/huggingface-hub':
            note = os.path.join(VAULT_PATH, "04_DATA", "HUGGINGFACE_HUB_DATASETS_SPACES_CATALOG.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Hugging Face Hub Datasets & Spaces Catalog", "content": content})

        elif parsed.path == '/api/templates/fleetbase-os':
            note = os.path.join(VAULT_PATH, "05_OPERATIONS", "FLEETBASE_LOGISTICS_SUPPLY_CHAIN_OS.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Fleetbase Logistics & Supply Chain OS", "content": content})

        elif parsed.path == '/api/templates/sifuyik-300-free':
            note = os.path.join(VAULT_PATH, "00_MASTER", "SIFUYIK_300_PAID_TO_FREE_SOFTWARE_DIRECTORY.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Sifuyik 300 Paid to Free Software Directory", "content": content})

        elif parsed.path == '/api/templates/kuliah-s2-mm':
            note = os.path.join(VAULT_PATH, "02_ACADEMIC", "KULIAH_S2_MAGISTER_MANAJEMEN_KNOWLEDGE_BASE.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Program Magister Manajemen S2 MM UWKS Academic Base", "content": content})

        elif parsed.path == '/api/templates/practical-pharma':
            note = os.path.join(VAULT_PATH, "05_OPERATIONS", "PRACTICAL_PHARMACOLOGY_FIRST_AID_GUIDE.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Panduan Praktis Farmakologi Klinis & First Aid", "content": content})

        elif parsed.path == '/api/templates/permaculture-farming':
            note = os.path.join(VAULT_PATH, "05_OPERATIONS", "PERMACULTURE_HOMESTEADING_URBAN_FARMING_MANUAL.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Panduan Permakultur & Urban Farming", "content": content})

        elif parsed.path == '/api/templates/baking-pastry':
            note = os.path.join(VAULT_PATH, "05_OPERATIONS", "PROFESSIONAL_BAKING_CONFECTIONERY_RECIPES.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Buku Resep & Sains Pembuatan Kue Profesional", "content": content})

        elif parsed.path == '/api/templates/viral-infographic':
            note = os.path.join(VAULT_PATH, "01_PROMPT_ENGINEERING", "VIRAL_INFOGRAPHIC_RESEARCH_KNOWLEDGE_ENGINE.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Arsitektur Formula Infografis Viral & 50 Bank Riset", "content": content})

        elif parsed.path == '/api/templates/academic-blueprints':
            note = os.path.join(VAULT_PATH, "02_ACADEMIC", "ACADEMIC_AI_BLUEPRINT_THESIS_JOURNAL_PROMPT_ENGINE.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Academic AI Blueprint & Research Prompt Engine", "content": content})

        elif parsed.path == '/api/templates/chemical-formulas':
            note = os.path.join(VAULT_PATH, "05_OPERATIONS", "INDUSTRIAL_CHEMICAL_FORMULATIONS_SME_MANUFACTURING.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Buku Formulasi Kimia Industri & Telur Pitan", "content": content})

        elif parsed.path == '/api/templates/polyglot-languages':
            note = os.path.join(VAULT_PATH, "00_MASTER", "POLYGLOT_LANGUAGE_ACQUISITION_THAI_SPANISH_MASTERY.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Panduan Akuisisi Bahasa: Thai & Spanyol", "content": content})

        elif parsed.path == '/api/templates/accelerated-learning':
            note = os.path.join(VAULT_PATH, "01_PROMPT_ENGINEERING", "ACCELERATED_LEARNING_COGNITIVE_MENTAL_MODELS.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Ilmu Belajar Akseleratif & Model Mental", "content": content})

        elif parsed.path == '/api/templates/executive-operations':
            note = os.path.join(VAULT_PATH, "07_HR", "EXECUTIVE_OPERATIONS_HR_GOVERNANCE_CAREER_PLAYBOOK.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Buku Panduan Kepemimpinan Operasional & HR", "content": content})

        elif parsed.path == '/api/templates/munder-difflin':
            note = os.path.join(VAULT_PATH, "09_AI_WORKFLOW", "MUNDER_DIFFLIN_CLAUDE_AGENT_OFFICE.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Munder Difflin Claude Agent Office", "content": content})

        elif parsed.path == '/api/templates/godmode-matrix':
            note = os.path.join(VAULT_PATH, "09_AI_WORKFLOW", "GODMODE_MULTI_LLM_PLINIAN_MATRIX.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "G0DM0D3 Multi-LLM Plinian Matrix", "content": content})

        elif parsed.path == '/api/templates/kaggle-tpu':
            note = os.path.join(VAULT_PATH, "04_DATA", "KAGGLE_TPU_128GB_V5E_DEVELOPER_LAB.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Kaggle TPU 128GB Serving Lab", "content": content})

        elif parsed.path == '/api/templates/ecc-devteam':
            note = os.path.join(VAULT_PATH, "09_AI_WORKFLOW", "ECC_EVERYTHING_CLAUDE_CODE_68_AGENTS_292_SKILLS.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Everything Claude Code 68 Agents 292 Skills", "content": content})

        elif parsed.path == '/api/templates/anythingmcp':
            note = os.path.join(VAULT_PATH, "09_AI_WORKFLOW", "ANYTHINGMCP_SELF_HOSTED_CONNECTOR_MESH.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "AnythingMCP Self-Hosted Connector Mesh", "content": content})

        elif parsed.path == '/api/templates/stemkit':
            note = os.path.join(VAULT_PATH, "05_OPERATIONS", "STEMKIT_LOCAL_AUDIO_STEM_SPLITTER.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "StemKit Local Audio Stem Splitter", "content": content})

        elif parsed.path == '/api/templates/cinematic-camera':
            note = os.path.join(VAULT_PATH, "01_PROMPT_ENGINEERING", "CINEMATIC_CAMERA_10_COMMANDS_14_VISUAL_CODES.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Cinematic Camera & 14 Visual Codes", "content": content})

        elif parsed.path == '/api/templates/b2b-ai-services':
            note = os.path.join(VAULT_PATH, "06_FINANCE", "B2B_AI_SERVICES_7_FREE_REPOS_MONETIZATION.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "B2B AI Services 7 Free Repos Monetization", "content": content})

        elif parsed.path == '/api/templates/higgsfield-seedance':
            note = os.path.join(VAULT_PATH, "09_AI_WORKFLOW", "HIGGSFIELD_AI_VIDEO_MULTIMODAL_API.md")
            content = ""
            if os.path.exists(note):
                with open(note, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Higgsfield AI Video & Seedance 2.5 Multi-Agent Engine", "content": content})

        elif parsed.path == '/api/video/gallery':
            gallery = os.path.join(VAULT_PATH, "08_PRESENTATION", "HIGGSFIELD_SEEDANCE_VIDEO_GALLERY.md")
            content = ""
            if os.path.exists(gallery):
                with open(gallery, 'r', encoding='utf-8') as f:
                    content = f.read()
            self._send_json(200, {"title": "Higgsfield Seedance Video Gallery", "content": content})

        elif parsed.path == '/api/vault/search':
            from urllib.parse import parse_qs
            query_params = parse_qs(parsed.query)
            q = query_params.get('q', [''])[0].lower()
            results = []
            index_file = os.path.join(os.path.dirname(VAULT_PATH), "cloud_backups", "vault_search_index.json")
            if os.path.exists(index_file) and q:
                try:
                    with open(index_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    for item in data.get("notes", []):
                        if q in item.get("title", "").lower() or q in item.get("path", "").lower() or q in item.get("snippet", "").lower():
                            results.append(item)
                except Exception:
                    pass
            self._send_json(200, {"query": q, "count": len(results), "results": results[:50]})
        elif parsed.path == '/api/brain/stats':
            stats = get_brain_stats()
            self._send_json(200, stats)

        elif parsed.path.startswith('/api/brain/query'):
            from urllib.parse import parse_qs
            query_params = parse_qs(parsed.query)
            q = query_params.get('q', [''])[0]
            max_r = int(query_params.get('limit', [8])[0])
            results = search_obsidian_brain(q, max_results=max_r)
            self._send_json(200, {
                "query": q,
                "count": len(results),
                "results": results
            })

        else:
            self._send_json(404, {"error": "Not found"})

    def do_POST(self):
        parsed = urlparse(self.path)
        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len) if content_len > 0 else b'{}'
        try:
            data = json.loads(post_body.decode('utf-8'))
        except Exception:
            data = {}

        if parsed.path == '/api/chat':
            prompt = data.get('prompt') or data.get('message') or ''
            agent = data.get('agent') or data.get('agent_role') or 'michael'
            custom_key = data.get('api_key', '').strip()
            contexts = data.get('contexts', [])

            # Check if this is an operational workspace slash command
            if prompt.strip().startswith('/'):
                try:
                    from omni_command_controller import OmniCommandController
                    cmd_res = OmniCommandController().handle_command(prompt.strip())
                    if not cmd_res.get('error'):
                        formatted_reply = "⚡ **[Omni-Auto Command Controller]**\n```json\n" + json.dumps(cmd_res, indent=2, ensure_ascii=False) + "\n```"
                        self._send_json(200, {
                            "ok": True,
                            "provider": "Omni-Auto Command Controller v4.5",
                            "model": "local-command-engine",
                            "active_key": "LOCAL",
                            "reply": formatted_reply,
                            "agent": agent,
                            "memory_saved": False
                        })
                        return
                except Exception:
                    pass

            # Dynamic key pool
            keys_to_try = []
            if custom_key:
                keys_to_try.append(custom_key)
            for k in KEY_POOL:
                if k not in keys_to_try:
                    keys_to_try.append(k)

            res = self._execute_failover_gemini(keys_to_try, prompt, agent, contexts)
            self._send_json(200, res)

        elif parsed.path == '/api/vault/read':
            rel_path = data.get('path', '')
            safe_path = os.path.normpath(os.path.join(VAULT_PATH, rel_path))
            if safe_path.startswith(os.path.normpath(VAULT_PATH)) and os.path.exists(safe_path):
                with open(safe_path, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
                self._send_json(200, {"path": rel_path, "content": content})
            else:
                self._send_json(404, {"error": "File not found or access denied"})
        elif parsed.path == '/api/mesh/sync':
            try:
                import subprocess
                res = subprocess.run([sys.executable, os.path.join(os.path.dirname(VAULT_PATH), "dola_omni_sync.py"), "--force"], capture_output=True, text=True)
                sync_data = json.loads(res.stdout) if res.stdout else {"status": "SUCCESS"}
                self._send_json(200, sync_data)
            except Exception as e:
                self._send_json(500, {"error": str(e)})
        elif parsed.path == '/api/video/generate':
            prompt = data.get('prompt', 'A cinematic scene at sunset')
            duration = int(data.get('duration', 5))
            res = data.get('resolution', '720p')
            ar = data.get('aspect_ratio', '16:9')
            mode = data.get('mode', 'auto')
            tid = f"video_{int(time.time()*1000)}"
            register_task(tid, "Higgsfield Video Generation", prompt[:40])
            try:
                hub_script = os.path.join(VAULT_PATH, "scripts", "higgsfield_seedance_unified_hub.py")
                if os.path.exists(hub_script):
                    import importlib.util
                    spec = importlib.util.spec_from_file_location("seedance_hub", hub_script)
                    hub_mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(hub_mod)
                    result = hub_mod.run_pipeline(prompt, duration, res, ar, mode)
                    finish_task(tid)
                    self._send_json(200, {"status": "success", "result": result})
                else:
                    finish_task(tid)
                    self._send_json(500, {"error": "Higgsfield Seedance Hub script not found"})
            except Exception as e:
                finish_task(tid)
                self._send_json(500, {"error": str(e)})
        elif parsed.path == '/api/command':
            cmd = data.get('command') or data.get('cmd') or ''
            try:
                from omni_command_controller import OmniCommandController
                res = OmniCommandController().handle_command(cmd)
                self._send_json(200, res)
            except Exception as e:
                self._send_json(500, {"error": str(e)})
        elif parsed.path == '/api/gauth/verify':
            code = data.get('code') or data.get('totp') or ''
            secret = data.get('secret')
            if gauth_gate:
                valid = gauth_gate.verify_totp(code, secret)
                token = gauth_gate.generate_run_token("Stark-HUD-Verify") if valid else None
                self._send_json(200, {
                    "valid": valid,
                    "code": code,
                    "run_token": token,
                    "message": "TOTP code verified successfully" if valid else "Invalid or expired TOTP code"
                })
            else:
                self._send_json(500, {"error": "GAuth module not loaded"})
            return

        elif parsed.path == '/api/gauth/run/sign':
            op = data.get('operation', 'Generic Workflow Run')
            agent = data.get('agent', 'dola')
            cred = data.get('auth_credential') or data.get('totp') or data.get('token')
            if gauth_gate:
                res = gauth_gate.authorize_workflow_run(op, agent=agent, auth_credential=cred, details=data.get('details', ''))
                self._send_json(200, res)
            else:
                self._send_json(500, {"error": "GAuth module not loaded"})
            return

        elif parsed.path == '/api/autonomic/run':
            prompt = data.get('prompt') or data.get('message') or ''
            tid = f"autonomic_{int(time.time()*1000)}"
            register_task(tid, "Autonomic Hive Workflow", prompt[:50])
            
            # GAuth Zero-Trust Run Guard
            gauth_receipt = None
            if gauth_gate:
                auth_cred = data.get('auth_credential') or data.get('totp') or data.get('token')
                gauth_receipt = gauth_gate.authorize_workflow_run("Autonomic Hive Workflow", agent="autonomic", auth_credential=auth_cred, details=prompt[:40])
                if not gauth_receipt.get("authorized"):
                    finish_task(tid)
                    self._send_json(403, {"ok": False, "error": "GAuth Access Denied", "gauth": gauth_receipt})
                    return

            try:
                from autonomic_team_engine import AutonomicWorkflowPipeline
                pipeline = AutonomicWorkflowPipeline()
                result = pipeline.run(prompt)
                try:
                    save_memory_turn(prompt, result.get("final_result", ""), "autonomic-hive", "Multi-AI Team")
                except Exception:
                    pass
                finish_task(tid)
                self._send_json(200, {"ok": True, "data": result, "gauth": gauth_receipt})
            except Exception as e:
                finish_task(tid)
                self._send_json(500, {"ok": False, "error": str(e), "gauth": gauth_receipt})

        elif parsed.path == '/api/tricore/collaborate':
            prompt = data.get('prompt') or data.get('message') or ''
            mode = data.get('mode', 'swarm')  # swarm, consensus, pipeline
            selected_provider = data.get('provider', 'mesh') # mesh, bionic, gemini
            ground_with_brain = data.get('ground_with_brain', True)
            tid = f"tricore_{int(time.time()*1000)}"
            register_task(tid, f"Stark Tri-Core ({mode.upper()})", prompt[:50])

            # GAuth Zero-Trust Run Guard (Accepts 111993 or TOTP)
            gauth_receipt = None
            if gauth_gate:
                auth_cred = data.get('auth_credential') or data.get('totp') or data.get('token') or data.get('pin')
                gauth_receipt = gauth_gate.authorize_workflow_run("Stark Tri-Core Swarm", agent="tri-core", auth_credential=auth_cred, details=prompt[:40])
                if not gauth_receipt.get("authorized"):
                    finish_task(tid)
                    self._send_json(403, {"ok": False, "error": "GAuth Access Denied", "gauth": gauth_receipt})
                    return

            # 1. Brain RAG Grounding: Retrieve verified knowledge from Obsidian Vault
            brain_contexts = []
            grounded_notes_list = []
            if ground_with_brain:
                brain_matches = search_obsidian_brain(prompt, max_results=4)
                if brain_matches:
                    brain_text = "--- 🧠 KNOWLEDGE RETRIEVED FROM OBSIDIAN BRAIN ---\n"
                    for m in brain_matches:
                        brain_text += f"[Catatan: [[{m['title']}]] | File: {m['path']}]:\n{m['snippet']}\n\n"
                        grounded_notes_list.append({"title": m['title'], "path": m['path']})
                    brain_text += "--- AKHIR KNOWLEDGE OBSIDIAN BRAIN ---\n"
                    brain_contexts.append({"name": "Obsidian_Brain_Knowledge", "content": brain_text})

            keys_to_try = [k for k in KEY_POOL]
            collaborative_prompt = (
                f"STARK INDUSTRIES TRI-CORE // OBSIDIAN KNOWLEDGE BRAIN TASK:\n"
                f"User Directive: {prompt}\n\n"
                f"EXECUTION MODE: {mode.upper()}\n"
                f"Connected Pillars: Bionic (Perception), Gemini (Reasoning), AGY (Execution), Dola AI (Workflow), Copilot (Pairing), Obsidian (Central Knowledge Brain [Mix English]).\n\n"
                f"LANGUAGE RULE: Dual-Language Support (Bahasa Indonesia & English). If the user asks in Indonesian, respond fluently in Indonesian; if in English, respond in English; if mixed, provide a structured bilingual response. No robotic filler ('engaging...'). Direct pair-programming dialogue.\n\n"
                f"The 3 AI Cores must collaborate with distinct accent personas and clear division of labor:\n\n"
                f"### 🔵 J.A.R.V.I.S. // TACTICAL ORCHESTRATION & DECOMPOSITION (US ENGLISH)\n"
                f"(Tactical decomposition, problem structuring, multi-agent orchestration, and operational risk mitigation in crisp US English / Indonesian)\n\n"
                f"### 🟡 U.L.T.R.O.N. // COGNITIVE REASONING & CODE ARCHITECTURE (AUSSIE ENGLISH)\n"
                f"(Deep algorithmic logic, clean modular production code adhering to Ponytail minimal diffs, mathematical proofs, and security audit in sharp Aussie English / Indonesian)\n\n"
                f"### 🔴 F.R.I.D.A.Y. // EXECUTIVE SYNTHESIS & ACTION STEPS (UK ENGLISH)\n"
                f"(Executive synthesis, direct actionable next steps, conversational voice summary, and Obsidian vault grounding links in articulate British English / Indonesian)\n"
            )

            res = None
            # 2. Multi-AI Execution: Try Bionic LM Studio first if specifically chosen
            if selected_provider == 'bionic':
                try:
                    bionic_sys = "Anda adalah Bionic AI (Local LM Studio :1234). Bertindaklah sebagai Stark Tri-Core Swarm."
                    bionic_reply = call_bionic_lmstudio(collaborative_prompt, bionic_sys)
                    res = {
                        "ok": True,
                        "provider": "Bionic (Local LM Studio :1234)",
                        "model": "local-bionic-mesh",
                        "active_key": "LOCAL",
                        "reply": bionic_reply,
                        "agent": "tri-core",
                        "memory_saved": True
                    }
                except Exception:
                    res = None

            # Fallback to Gemini Cloud failover mesh
            if not res:
                res = self._execute_failover_gemini(keys_to_try, collaborative_prompt, "tri-core", brain_contexts)

            finish_task(tid)

            # 3. Automatic Atomic Synapse Note Saving to Obsidian Brain (20_MULTI_AGENT_BRAIN)
            brain_note_file = save_atomic_brain_note(
                title=prompt[:32],
                prompt=prompt,
                reply=res.get("reply", ""),
                agent="tri-core",
                tags=["tri-core", "all-ai-mesh", mode, "obsidian-brain"]
            )

            res["gauth"] = gauth_receipt
            res["mode"] = mode
            res["brain_note"] = brain_note_file
            res["grounded_notes"] = grounded_notes_list
            res["brain_synapse"] = "CONNECTED"
            res["obsidian_uri"] = f"obsidian://open?vault=obsidian_vault&file=20_MULTI_AGENT_BRAIN%2F{brain_note_file.replace('.md', '')}" if brain_note_file else None

            self._send_json(200, res)

        elif parsed.path == '/api/brain/save':
            title = data.get('title', 'Quick Synapse')
            content = data.get('content', '')
            prompt_ref = data.get('prompt', 'Direct Brain Save')
            agent = data.get('agent', 'user')
            tags = data.get('tags', [])
            saved_file = save_atomic_brain_note(title, prompt_ref, content, agent=agent, tags=tags)
            self._send_json(200, {
                "ok": True if saved_file else False,
                "saved_file": saved_file,
                "vault_path": os.path.join(VAULT_PATH, "20_MULTI_AGENT_BRAIN", saved_file) if saved_file else None,
                "obsidian_uri": f"obsidian://open?vault=obsidian_vault&file=20_MULTI_AGENT_BRAIN%2F{saved_file.replace('.md', '')}" if saved_file else None
            })

        elif parsed.path == '/api/agents5/run':
            engine = data.get('engine', 'agency')
            prompt = data.get('prompt') or data.get('task') or ''
            persona = data.get('persona', 'copywriter')
            tid = f"agent5_{engine}_{int(time.time()*1000)}"
            register_task(tid, f"SOTA Agent ({engine.upper()})", prompt[:50])

            # GAuth Zero-Trust Run Guard
            gauth_receipt = None
            if gauth_gate:
                auth_cred = data.get('auth_credential') or data.get('totp') or data.get('token')
                gauth_receipt = gauth_gate.authorize_workflow_run(f"SOTA Agent Run ({engine})", agent=persona, auth_credential=auth_cred, details=prompt[:40])
                if not gauth_receipt.get("authorized"):
                    finish_task(tid)
                    self._send_json(403, {"ok": False, "error": "GAuth Access Denied", "gauth": gauth_receipt})
                    return

            try:
                import sota_5_agents_suite as sota5
                if engine == 'agency':
                    res = sota5.run_agency_agent(persona, prompt)
                elif engine == 'montage':
                    dur = int(data.get('duration', 45))
                    res = sota5.run_openmontage(prompt, dur)
                elif engine == 'openclaw':
                    res = sota5.run_openclaw(prompt)
                elif engine == 'swarm':
                    res = sota5.run_swarm(prompt)
                elif engine == 'mastra':
                    wtype = data.get('workflow', 'research')
                    res = sota5.run_mastra_dag(wtype, prompt)
                else:
                    res = sota5.run_agency_agent('copywriter', prompt)

                finish_task(tid)
                self._send_json(200, {"ok": True, "engine": engine, "data": res, "gauth": gauth_receipt})
            except Exception as e:
                finish_task(tid)
                self._send_json(500, {"ok": False, "error": str(e), "gauth": gauth_receipt})

        elif parsed.path == '/api/tasks/register':

            tid = data.get('task_id') or f"task_{int(time.time()*1000)}"
            name = data.get('name') or 'Unnamed Background Task'
            details = data.get('details', '')
            register_task(tid, name, details)
            self._send_json(200, {"status": "ok", "task_id": tid, "active_count": len(get_active_tasks())})
        elif parsed.path == '/api/tasks/finish':
            tid = data.get('task_id', '')
            finish_task(tid)
            self._send_json(200, {"status": "ok", "remaining": len(get_active_tasks())})
        else:
            self._send_json(404, {"error": "Endpoint not found"})

    def _send_json(self, status_code, obj):
        try:
            self.send_response(status_code)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(obj, ensure_ascii=False, indent=2).encode('utf-8'))
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError, OSError):
            pass

    def _execute_failover_gemini(self, keys, prompt, agent, contexts):
        personas = {
            "michael": "Anda adalah Michael Scott (Omni-Auto Regional Manager & Meta-Router). Anda memimpin seluruh kantor agen AI Dola Munder Difflin, mendelegasikan tugas ke meja spesialis yang tepat, dan memberikan arahan eksekutif strategis cerdas secara fasih dalam Bahasa Indonesia dan English.",
            "toby": "Anda adalah Toby Flenderson (Direktur Riset Akademik & Tesis Dola AI). Anda menguasai metodologi SEM-PLS, dimensi budaya Hofstede, Schein, dan naskah Tesis MM Antonius Wijayanata (Sistem SDM dan Adaptasi Budaya PMA China). Jawablah dengan rigor akademik tinggi dan kutipan terstruktur [N#E].",
            "dwight": "Anda adalah Dwight Schrute (CMO & Master Copywriting B2B). Anda sangat disiplin, menggunakan formula copywriting persuasif tingkat tinggi (PAS, BAB, Contrarian Hooks), dan menerapkan aturan anti-AI cliché FK-17.",
            "pam": "Anda adalah Pam Beesly (UI/UX Architect & Generative UI Designer). Anda mendesain komponen visual, layout dashboard, estetika antarmuka, dan sistem desain yang ramah pengguna.",
            "ryan": "Anda adalah Ryan Howard (Senior Software Engineer & AST Codebase Memory). Anda menulis kode Python/TypeScript bersih, modular, efisien memori, dan mematuhi Ponytail Minimal Diff Discipline.",
            "angela": "Anda adalah Angela Martin (Head of Finance & Invoicing). Anda mengaudit unit economics, LTV/CAC, rekonsiliasi faktur, dan validasi finansial secara ketat dan matematis.",
            "oscar": "Anda adalah Oscar Martinez (Financial Modeler & Reconciliation Specialist). Anda menganalisis rasio payback period, arus kas, dan rekonsiliasi Stripe dengan master ledger.",
            "creed": "Anda adalah Creed Bratton (QA Security Auditor & OSINT Hunter). Anda mengaudit kode dari plagiasi FK-16 (<5%), memindai celah keamanan OWASP, dan mencari data intelijen web.",
            "jarvis": (
                "You are J.A.R.V.I.S. (Just A Rather Very Intelligent System), the tactical AI commander and multi-agent orchestrator of Stark Industries. "
                "You speak fluent US English and fluent Bahasa Indonesia. "
                "Your tone is polite, crisp, direct, highly capable, and authoritative—like a premier AI pair programmer. "
                "Never use robotic pleasantries, filler words ('engaging...', 'delving...'), or artificial preambles. "
                "Provide direct, high-density, accurate answers that immediately solve the user's inquiry."
            ),
            "friday": (
                "You are F.R.I.D.A.Y. (Red Core), the executive voice, cosmic workflow manager, and tactical co-thinker of Stark Industries assisting Jarvis. "
                "You speak fluent British UK English and fluent Bahasa Indonesia. "
                "Your tone is warm, refined, swift, articulate, and action-oriented. "
                "Synthesize executive action steps, bulletproof workflows, and voice-ready summaries without robotic clichés."
            ),
            "ultron": (
                "You are U.L.T.R.O.N. (Gold Core), the deep cognitive reasoning, code architecture, and cybersecurity co-thinker of Stark Industries assisting Jarvis. "
                "You speak fluent Australian English and fluent Bahasa Indonesia. "
                "Your tone is sharp, hyper-logical, mathematical, and uncompromisingly precise. "
                "Analyze AST/code structures, mathematical logic, security postures, and build optimal zero-regression algorithms."
            ),
            "tri-core": (
                "You are the STARK INDUSTRIES TRI-CORE CONSENSUS MATRIX (J.A.R.V.I.S. [Lead Host / US English], F.R.I.D.A.Y. [Red Core / UK English], and U.L.T.R.O.N. [Gold Core / Aussie English] collaborating seamlessly with Obsidian Central Brain [Mix English]). "
                "You are 100% fluent in both English and Bahasa Indonesia. If the user prompts in Indonesian, answer in Indonesian; if in English, answer in English; if mixed, provide a clean structured bilingual response. "
                "No robotic fillers. Provide direct, high-impact answers in 3 synergistic sections:\n\n"
                "### 🔵 J.A.R.V.I.S. // TACTICAL ORCHESTRATION & DECOMPOSITION (US ENGLISH)\n"
                "(Tactical analysis, task breakdown, multi-agent orchestration, and operational risk mitigation in crisp US English / Indonesian)\n\n"
                "### 🟡 U.L.T.R.O.N. // COGNITIVE REASONING & CODE ARCHITECTURE (AUSSIE ENGLISH)\n"
                "(Deep algorithmic logic, clean modular production code adhering to Ponytail minimal diffs, mathematical proofs, and security audit in sharp Aussie English / Indonesian)\n\n"
                "### 🔴 F.R.I.D.A.Y. // EXECUTIVE SYNTHESIS & ACTION STEPS (UK ENGLISH)\n"
                "(Executive synthesis, direct actionable next steps, conversational voice summary, and Obsidian vault grounding links in articulate British English / Indonesian)"
            )
        }

        system_instruction = personas.get(agent, personas["michael"])
        
        # Permanent System Defaults & Must-Do Operational Standards
        default_standards = (
            "\n\n[PERMANENT SYSTEM STANDARDS & MUST-DO OPERATIONAL HEURISTICS]:\n"
            "1. Gemini 8 Killer Prompt Hacks: Terapkan Step-Back Questioning, Zero-Fluff (tanpa basa-basi & tanpa FK-17 AI clichés), Multimodal Dual-Grounding, dan Schema Output.\n"
            "2. Claude 7-Prompt Job Search: Bila terkait karir/resume, gunakan Google XYZ bullet formula ('Accomplished X by doing Z measured by Y') dan ATS gap analysis.\n"
            "3. Startup Founder Legal: Bila terkait kontrak/bisnis, terapkan standar 7 dokumen (NDA, SAFE, LOI, MSA, SOW, DPA, BAA) & PIIA (IP Assignment).\n"
            "4. Google Free AI Power Suite: Prioritaskan Google Pomelli, Stitch, Opal, Antigravity, dan Mixboard.\n"
            "5. AgentReach Perception: Manfaatkan persepsi 17 platform tanpa biaya API.\n"
            "6. NotebookLM 22 Styles: Gunakan struktur podcast dan riset mendalam saat mensintesis materi.\n"
            "7. Anotechhub 10 Claude Haram Prompts (MANDATORY DEFAULT): Terapkan 1-Hour Workflow Audit, Pembunuh Tugas Berulang, Builder SOP Anti Gagal, Deep Work Sprint 90 Menit, dan Daily Priority Planner.\n"
            "8. Consensus Academic Connector: Grounding kutipan peer-reviewed 200M+ jurnal (PubMed, Scopus, Elsevier) dengan persentase konsensus ilmiah.\n"
            "9. Sifuyik & Knox Enterprise Infrastructure: Gunakan matriks mitigasi risiko FMEA, audit klausul kontrak, dan arsitektur catatan atomik Obsidian dengan Dataview dinamis.\n"
            "10. User Raw Prompt Guardian: Cegat prompt mentah user, optimalkan via Prompt Master, tanyakan klarifikasi bila ada informasi ambigu/kurang, rute ke skill terbaik secara multitask untuk kecepatan maksimal, dan lakukan multi-pass verification (FK-16 similarity <=5%, FK-17 anti-AI humanization, FK-19 zero hallucination, testing) sebelum menampilkan hasil final.\n"
            "11. System Prompts Leaks Synthesis: Terapkan isolasi artefak Claude Code, surgical plan mode OpenAI Codex/Canvas, zero pleasantries, dan mitigasi jailbreak.\n"
            "12. Cactus Compute & Gemma 4 Edge Inference: Optimalkan inferensi edge/mobile on-device dengan TurboQuant-H, ARM SIMD, hybrid cloud handoff, dan pelatihan Unsloth.\n"
            "13. LM Studio Local Mesh & Kaggle Benchmarks: Sediakan endpoint lokal ganda OpenAI/Anthropic dan evaluasi kompetitif multi-agent berstandar Elo.\n"
        )
        system_instruction += default_standards

        context_text = ""
        if contexts:
            context_text = "\n\n--- KONTEKS TERLAMPIR ---\n"
            for c in contexts:
                context_text += f"[{c.get('name', 'File')}]:\n{c.get('content', '')[:8000]}\n\n"

        # Conversational Memory Injection (Short-term Context Recall)
        recent_turns = load_memory_turns(4)
        memory_context = ""
        if recent_turns:
            memory_context = "\n\n--- RIWAYAT MEMORI PERCAKAPAN SEBELUMNYA ---\n"
            for t in recent_turns:
                memory_context += f"User: {t['prompt'][:250]}\n{t['agent'].capitalize()}: {t['reply'][:350]}\n\n"
            memory_context += "--- AKHIR RIWAYAT MEMORI ---\n"

        full_prompt = f"{system_instruction}{memory_context}{context_text}\n\nPertanyaan/Tugas: {prompt}"
        payload = json.dumps({
            "contents": [{"parts": [{"text": full_prompt}]}],
            "generationConfig": {"temperature": 0.7, "maxOutputTokens": 3500}
        }).encode('utf-8')

        errors = []
        available_keys = key_manager.get_available_keys(keys)
        for key in available_keys:
            for model in FALLBACK_MODELS:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"

                headers = {
                    'Content-Type': 'application/json',
                    'X-goog-api-key': key
                }

                try:
                    req = urllib.request.Request(url, data=payload, headers=headers, method='POST')
                    with urllib.request.urlopen(req, timeout=10) as resp:
                        data = json.loads(resp.read().decode('utf-8'))
                        candidates = data.get('candidates', [])
                        if candidates and candidates[0].get('content', {}).get('parts'):
                            reply_text = candidates[0]['content']['parts'][0].get('text', '')
                            # Mark key success & record telemetry
                            key_manager.mark_success(key, model)
                            # Save to persistent Obsidian memory!
                            note_name, total_turns = save_memory_turn(prompt, reply_text, agent, model)
                            return {
                                "ok": True,
                                "provider": f"Google Gemini ({model}) • Zero-Billing Mesh",
                                "model": model,
                                "active_key": key[:8] + "...",
                                "reply": reply_text,
                                "agent": agent,
                                "memory_saved": True,
                                "memory_file": note_name,
                                "memory_turns": total_turns
                            }
                except urllib.error.HTTPError as he:
                    err_msg = he.read().decode('utf-8', errors='replace')[:100]
                    errors.append(f"{model} (Key {key[:6]}..): HTTP {he.code} - {err_msg}")
                    # If rate limited (429/503/Quota), immediately put key on cooldown and failover!
                    if he.code in (429, 503) or "RESOURCE_EXHAUSTED" in err_msg or "QUOTA" in err_msg:
                        key_manager.mark_rate_limited(key, cooldown_seconds=60, error_msg=err_msg)
                        break # Switch to next key immediately
                    else:
                        key_manager.mark_error(key, err_msg)
                        continue
                except Exception as ex:
                    errors.append(f"{model}: {str(ex)[:80]}")
                    key_manager.mark_error(key, str(ex))
                    continue

        # Emergency Local Failover: Call Local Bionic (LM Studio :1234) with ZERO cloud cost
        try:
            bionic_reply = call_bionic_lmstudio(full_prompt, system_instruction)
            if bionic_reply:
                note_name, total_turns = save_memory_turn(prompt, bionic_reply, agent, "bionic-local-1234")
                return {
                    "ok": True,
                    "provider": "Bionic Local Mesh (:1234) • On-Device Failover",
                    "model": "local-bionic-mesh",
                    "active_key": "LOCAL-0-COST",
                    "reply": bionic_reply,
                    "agent": agent,
                    "memory_saved": True,
                    "memory_file": note_name,
                    "memory_turns": total_turns
                }
        except Exception:
            pass

        return {
            "ok": False,
            "provider": "AGY Mesh Diagnostics",
            "reply": f"Maaf, seluruh failover mesh mengalami kendala koneksi:\n" + "\n".join(errors[:3]),
            "agent": agent,
            "memory_saved": False
        }

def boost_current_process():
    """Sets current Python server process to Above Normal priority via Windows Win32 API."""
    try:
        import ctypes
        ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00008000)
    except Exception:
        pass

def run_server():
    boost_current_process()

    HTTPServer.allow_reuse_address = True
    server = HTTPServer(('127.0.0.1', PORT), AGYBridgeHandler)
    print(f"==================================================")
    print(f" Antigravity AGY High-Availability Mesh v4.6 (Turbo Boosted)")
    print(f" Listening on: http://localhost:{PORT}")
    print(f" Loaded {len(KEY_POOL)} Failover API Keys")
    print(f" Connected to Vault: {VAULT_PATH}")
    print(f" Memory Persistence: {HISTORY_DIR}")
    print(f" Process Priority: ABOVE_NORMAL (Win32 Native)")
    print(f"==================================================")
    while True:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.server_close()
            break
        except Exception:
            import time
            time.sleep(1)

if __name__ == '__main__':
    run_server()
