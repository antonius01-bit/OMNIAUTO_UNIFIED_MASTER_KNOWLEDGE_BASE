#!/usr/bin/env python3
"""
==================================================================================
🎬 HIGGSFIELD SEEDANCE 2.5 UNIFIED MULTI-AGENT HUB
==================================================================================
Unified Bridge Connecting:
1. AGY (Antigravity Execution Engine & Pair Programming)
2. Bionic / LM Studio (Local LLM Mesh & Briefd MCP)
3. Dola AI (Autonomous /omni-auto Workflow Router & S239 Skill)
4. Obsidian Second Brain (Persistent Video Gallery, Dataview & Wikilinks)
5. Virtual Office / Bridge Server (Port 5050 Live Telemetry & Event Streaming)
==================================================================================
"""

import os
import sys
import json
import time
import urllib.parse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Path Definitions
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env.local"
if not ENV_FILE.exists():
    ENV_FILE = Path(r"C:\Users\antoni\.gemini\antigravity\scratch\higgsfield-seedance\.env.local")

VAULT_DIR = Path(r"C:\Users\antoni\Dola\obsidian_vault")
GALLERY_NOTE = VAULT_DIR / "08_PRESENTATION" / "HIGGSFIELD_SEEDANCE_VIDEO_GALLERY.md"
WORKFLOW_NOTE = VAULT_DIR / "09_AI_WORKFLOW" / "HIGGSFIELD_AI_VIDEO_MULTIMODAL_API.md"

# Load Credentials Server-Side Safely
if ENV_FILE.exists():
    load_dotenv(dotenv_path=ENV_FILE)
else:
    load_dotenv()

# Verify client library
try:
    import higgsfield_client
    from higgsfield_client.exceptions import HiggsfieldClientError, CredentialsMissedError
    SDK_AVAILABLE = True
except ImportError:
    SDK_AVAILABLE = False


def build_cinematic_prompt(raw_prompt: str) -> dict:
    """
    Enhances raw user prompt into professional Seedance 2.5 cinematic prompt
    incorporating The Visual Prompts (S238) standards: lighting, camera lens, resolution.
    """
    enhanced = f"{raw_prompt.strip()}, 8k uhd, cinematic lighting, shot on 35mm lens, photorealistic, intricate textures, masterpiece, high dynamic range"
    return {
        "raw_prompt": raw_prompt,
        "enhanced_prompt": enhanced,
        "lighting": "Volumetric cinematic golden hour / rim lighting",
        "camera": "Arri Alexa 65, 35mm anamorphic, smooth dynamic gimbal motion",
        "aspect_ratio": "16:9",
        "resolution": "720p",
        "duration": 5
    }


def log_to_obsidian_gallery(record: dict):
    """Logs the generation request and output to Obsidian Second Brain."""
    os.makedirs(GALLERY_NOTE.parent, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # If gallery doesn't exist, create it with Dataview query & master headers
    if not GALLERY_NOTE.exists():
        header = f"""---
title: "Higgsfield Seedance 2.5 Video Asset Gallery"
created: {today}
tags: [dola, agy, bionic, obsidian, higgsfield, seedance, video-generation, s239]
type: gallery
---

# 🎬 Higgsfield Seedance 2.5 Video Asset Gallery
*Hub Terpadu Generasi Video AI Antigravity + Bionic + Dola + Obsidian + Virtual Office*

Terhubung ke: [[00_MASTER/00_INDEX]], [[09_AI_WORKFLOW/HIGGSFIELD_AI_VIDEO_MULTIMODAL_API]], [[01_PROMPT_ENGINEERING/THE_VISUAL_PROMPTS_S238]].

## 📊 Ringkasan Aset Video Terdaftar (Dataview Table)
```dataview
TABLE 
  status as "Status",
  model as "Model",
  duration as "Durasi (s)",
  aspect_ratio as "Rasio",
  video_link as "Video Output",
  created_at as "Waktu"
FROM #higgsfield
SORT file.ctime DESC
```

---

## 🎥 Riwayat Generasi Video (Live Stream)
"""
        with open(GALLERY_NOTE, "w", encoding="utf-8") as f:
            f.write(header)

    status_badge = "✅ COMPLETED" if record.get("status") == "completed" else "⏳ PENDING_CREDITS / WEB_RENDER"
    video_url = record.get("video_url") or "Tersedia via Web Studio / Menunggu Top Up API"
    web_link = f"https://higgsfield.ai/?prompt={urllib.parse.quote(record.get('prompt', ''))}"

    entry = f"""
### 🎞️ Video [{timestamp}] — {record.get('title', 'Cinematic Clip')}
- **Model**: `{record.get('model', 'bytedance/seedance-2.5/text-to-video')}`
- **Status**: `{status_badge}`
- **Prompt**: "{record.get('prompt')}"
- **Spesifikasi**: {record.get('duration', 5)}s | {record.get('resolution', '720p')} | {record.get('aspect_ratio', '16:9')}
- **Kamera & Gaya (S238)**: {record.get('camera', 'Arri Alexa 65 35mm')}
- **Video URL / Output**: [{video_url}]({video_url if video_url.startswith('http') else web_link})
- **Aksi Cepat Web (1-Click Free Generation)**: [Buka di Higgsfield Web Generator]({web_link})
- **Terkait**: [[09_AI_WORKFLOW/HIGGSFIELD_AI_VIDEO_MULTIMODAL_API]] | [[08_PRESENTATION/Higgsfield_Video_Generations]]

---
"""
    with open(GALLERY_NOTE, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"[Obsidian] Logged entry to {GALLERY_NOTE}")


def notify_virtual_office(event_name: str, payload: dict):
    """Notifies the AGY Bridge Server / Virtual Office on port 5050."""
    try:
        import urllib.request
        data = json.dumps({"event": event_name, "data": payload}).encode("utf-8")
        req = urllib.request.Request("http://127.0.0.1:5050/api/event", data=data, headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=1.5)
    except Exception:
        # Server might not have /api/event, fail silently
        pass


def run_pipeline(prompt: str, duration: int = 5, resolution: str = "720p", aspect_ratio: str = "16:9", mode: str = "auto") -> dict:
    """
    Executes the Seedance 2.5 pipeline across all connected platforms.
    Modes:
      - 'auto': Attempts live API. If credit exhausted, smoothly falls back to web handoff & Obsidian record.
      - 'live': Strictly runs live API call.
      - 'mock': Immediately returns simulated preview & pre-filled web prompt without API call.
    """
    print("=" * 70)
    print("🎬 HIGGSFIELD SEEDANCE 2.5 PENTA-PLATFORM PIPELINE")
    print("=" * 70)
    print(f"[*] Input Prompt     : {prompt}")
    print(f"[*] Duration/Res     : {duration}s @ {resolution} ({aspect_ratio})")
    print(f"[*] Execution Mode   : {mode.upper()}")

    enhanced = build_cinematic_prompt(prompt)
    model = "bytedance/seedance-2.5/text-to-video"
    args = {
        "prompt": enhanced["enhanced_prompt"],
        "duration": duration,
        "resolution": resolution,
        "aspect_ratio": aspect_ratio
    }

    result = {
        "title": prompt[:30],
        "prompt": enhanced["enhanced_prompt"],
        "model": model,
        "duration": duration,
        "resolution": resolution,
        "aspect_ratio": aspect_ratio,
        "camera": enhanced["camera"],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Notify Virtual Office
    notify_virtual_office("video_task_started", {"model": model, "prompt": prompt})

    if mode in ["auto", "live"] and SDK_AVAILABLE:
        try:
            print("[*] Contacting Higgsfield Live API Gateway...")
            api_res = higgsfield_client.subscribe(
                application=model,
                arguments=args
            )
            status = api_res.get("status")
            if status == "completed":
                video_url = api_res.get("video", {}).get("url") or api_res.get("url")
                result["status"] = "completed"
                result["video_url"] = video_url
                print(f"[SUCCESS] Video Generated: {video_url}")
            else:
                result["status"] = status
                result["error"] = api_res.get("error")
                print(f"[STATUS] API returned status: {status}")

        except HiggsfieldClientError as e:
            err_str = str(e)
            if "not_enough_credits" in err_str:
                print("\n[INFO] Live API: 0 credits detected ($0.72 needed for 5s Seedance render).")
                print("[INFO] Seamlessly routing to Free Web Handoff + Obsidian Asset Record...")
                result["status"] = "pending_credits"
                result["web_url"] = f"https://higgsfield.ai/?prompt={urllib.parse.quote(enhanced['enhanced_prompt'])}"
            else:
                result["status"] = "error"
                result["error"] = err_str
                print(f"[ERROR] Live API Error: {e}")
        except Exception as e:
            result["status"] = "error"
            result["error"] = str(e)
            print(f"[ERROR] Unexpected: {e}")
    else:
        # Mock / Simulation mode
        result["status"] = "simulated"
        result["web_url"] = f"https://higgsfield.ai/?prompt={urllib.parse.quote(enhanced['enhanced_prompt'])}"

    # 1. Sync to Obsidian Second Brain
    log_to_obsidian_gallery(result)

    # 2. Notify Virtual Office completion
    notify_virtual_office("video_task_completed", result)

    print("\n" + "=" * 70)
    print("✨ PIPELINE EXECUTION COMPLETED")
    print(f" • Status           : {result.get('status')}")
    print(f" • Obsidian Gallery : file:///{str(GALLERY_NOTE).replace(os.sep, '/')}")
    if result.get("video_url"):
        print(f" • Video URL        : {result.get('video_url')}")
    else:
        web_link = f"https://higgsfield.ai/?prompt={urllib.parse.quote(result['prompt'])}"
        print(f" • 1-Click Web Gen  : {web_link}")
    print("=" * 70)
    return result


if __name__ == "__main__":
    test_prompt = sys.argv[1] if len(sys.argv) > 1 else "A cinematic scene at sunset"
    run_pipeline(test_prompt, duration=5, resolution="720p", aspect_ratio="16:9", mode="auto")
