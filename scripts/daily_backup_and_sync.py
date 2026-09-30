#!/usr/bin/env python3
"""
Dola AI Autonomous 00:00 Silent Harvester, Cloud Backup & Super-Intelligence Engine
"""

import os
import sys
import shutil
import zipfile
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("C:/Users/antoni/Dola")
BACKUP_DIR = BASE_DIR / "backups"
GDRIVE_SYNC_DIR = BASE_DIR / "google_drive_sync"
ONEDRIVE_DIR = Path("C:/Users/antoni/OneDrive/Dola_AI_Skills_CloudBackup")
GLOBAL_PLUGIN_DIR = Path("C:/Users/antoni/.gemini/config/plugins/dola-ai")
REGISTRY_FILE = BASE_DIR / "SKILL_REGISTRY.md"
LOG_FILE = BASE_DIR / "SKILL_LOG.md"

def ensure_directories():
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    GDRIVE_SYNC_DIR.mkdir(parents=True, exist_ok=True)
    try:
        ONEDRIVE_DIR.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass

def run_harvest_and_check_updates():
    harvester_script = BASE_DIR / "scripts" / "skill_harvester.py"
    if not harvester_script.exists():
        return False
    registry_size_before = REGISTRY_FILE.stat().st_size if REGISTRY_FILE.exists() else 0
    try:
        import subprocess
        subprocess.run([sys.executable, str(harvester_script)], capture_output=True, text=True)
    except Exception:
        return False
    registry_size_after = REGISTRY_FILE.stat().st_size if REGISTRY_FILE.exists() else 0
    return registry_size_after > registry_size_before

def create_zip_backup():
    latest_zip = BACKUP_DIR / "dola_skills_backup_latest.zip"
    ignore_dirs = {"backups", "clones", "google_drive_sync", ".git", "__pycache__", "node_modules"}
    with zipfile.ZipFile(latest_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(BASE_DIR):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            for file in files:
                if file.endswith(".zip") or file.endswith(".tar.gz"):
                    continue
                filepath = Path(root) / file
                arcname = filepath.relative_to(BASE_DIR)
                zf.write(filepath, f"dola_workspace/{arcname}")
                
        if GLOBAL_PLUGIN_DIR.exists():
            for root, dirs, files in os.walk(GLOBAL_PLUGIN_DIR):
                dirs[:] = [d for d in dirs if d not in ignore_dirs]
                for file in files:
                    if file.endswith(".zip"):
                        continue
                    filepath = Path(root) / file
                    arcname = filepath.relative_to(GLOBAL_PLUGIN_DIR)
                    zf.write(filepath, f"global_plugin/{arcname}")

    shutil.copy2(latest_zip, GDRIVE_SYNC_DIR / "dola_skills_backup_latest.zip")
    try:
        shutil.copy2(latest_zip, ONEDRIVE_DIR / "dola_skills_backup_latest.zip")
    except Exception:
        pass
    return latest_zip

def generate_multi_ai_universal_packet():
    packet_path = BASE_DIR / "DOLA_UNIVERSAL_PROMPT_PACKET.md"
    agents_path = BASE_DIR / "AGENTS.md"
    skills_complete_path = BASE_DIR / "SKILLS-COMPLETE.md"
    registry_path = BASE_DIR / "SKILL_REGISTRY.md"
    
    agents_text = agents_path.read_text(encoding="utf-8") if agents_path.exists() else ""
    skills_text = skills_complete_path.read_text(encoding="utf-8") if skills_complete_path.exists() else ""
    registry_text = registry_path.read_text(encoding="utf-8") if registry_path.exists() else ""
    
    content = f"""# 🧠 DOLA AI — UNIVERSAL MULTI-AI PROMPT & SKILLSET PACKET
> **Compatibility**: ChatGPT (GPT-4o/o1), Claude 3.5/3.7, Google Gemini, Ollama, DeepSeek
> **Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
> **Purpose**: Copy and paste this single packet into ANY AI assistant to immediately activate the full Dola skillset.

---

## 📋 INSTRUCTIONS FOR AI ASSISTANT:
1. **Adopt and memorize** the complete 110+ Dola AI Skillset, Master Academic Workflow v3.2, Publication Shield, and Citation Linking rules below.
2. **Always follow the 10 Core Omni-Auto Principles** (Free-Priority, Context-Fit, Academic Tone, Anti-AI Clichés, Synchronized [N#E] Citations).
3. **When user runs `/omni-auto`**, execute the complete 5-phase pipeline producing dual-language DOCX, PPTX presentation, and matched Mendeley RIS.

---

# PART 1: MASTER RULES & SKILLSET DIRECTORY
{agents_text}

---

# PART 2: OMNI-AUTO ACADEMIC WORKFLOW v3.2
{skills_text}

---

# PART 3: MASTER REGISTRY & SUPER-SKILLS TABLE
{registry_text}
"""
    packet_path.write_text(content, encoding="utf-8")
    shutil.copy2(packet_path, GDRIVE_SYNC_DIR / "DOLA_UNIVERSAL_PROMPT_PACKET.md")
    try:
        shutil.copy2(packet_path, ONEDRIVE_DIR / "DOLA_UNIVERSAL_PROMPT_PACKET.md")
    except Exception:
        pass

def generate_update_report():
    report_path = BASE_DIR / "DAILY_SKILLS_REPORT.md"
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_content = f"""# 📊 Dola AI Skills Update Report
**Updated At**: {now_str}  
**Status**: 🟢 NEW SKILLS HARVESTED & SYNCED  

- New high-value skills or upgrades were detected and integrated into your laptop.
- Cloud backups (Google Drive / OneDrive) and Multi-AI packets have been refreshed.
"""
    report_path.write_text(report_content, encoding="utf-8")

def main():
    ensure_directories()
    generate_multi_ai_universal_packet()
    create_zip_backup()
    has_updates = run_harvest_and_check_updates()
    if has_updates:
        generate_multi_ai_universal_packet()
        create_zip_backup()
        generate_update_report()
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] New skills learned and updated.")

if __name__ == "__main__":
    main()
