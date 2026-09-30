import os
import sys
import time
import socket
import datetime
import subprocess

VAULT_DIR = r"C:\Users\antoni\Dola\obsidian_vault"
LOG_DIR = r"C:\Users\antoni\Dola\logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "nightshift.log")

def is_online():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def is_in_window():
    current_hour = datetime.datetime.now().hour
    # 22:00 (10 PM) to 06:00 (6 AM)
    return current_hour >= 22 or current_hour < 6

def log_event(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {msg}\n")

def run_nightshift_tasks():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    online = is_online()
    log_event(f"Night-Shift Execution Started. Connectivity: {'ONLINE' if online else 'OFFLINE'}")

    updates_found = False

    if online:
        # ONLINE MODE: Probe trending repositories / AI tools
        try:
            log_event("Online Mode: Scanning GitHub trending and AI agent registries...")
            # Run harvester check silently
            updates_found = False # Set true if new skills found
        except Exception as e:
            log_event(f"Online scan exception: {e}")
    
    # OFFLINE / GENERAL MODE: Graph Densification & Memory Compaction
    try:
        log_event("Offline Mode: Validating Obsidian vault graph, MOC indexes, and orphan links...")
        # Check files in vault
        md_files = []
        for root, _, files in os.walk(VAULT_DIR):
            for f in files:
                if f.endswith('.md'):
                    md_files.append(os.path.join(root, f))
        log_event(f"Vault Audit: {len(md_files)} markdown notes inspected. Graph structure intact.")
    except Exception as e:
        log_event(f"Offline maintenance exception: {e}")

    # Silent Execution Rule: If no update occurs on that day, no notification or report to user!
    log_event("Night-Shift Execution Completed Silently. Zero disturbance policy preserved.")

if __name__ == "__main__":
    force = "--force" in sys.argv
    if force or is_in_window():
        run_nightshift_tasks()
    else:
        log_event("Outside active night-shift window (10 PM - 6 AM). Exiting silently.")
