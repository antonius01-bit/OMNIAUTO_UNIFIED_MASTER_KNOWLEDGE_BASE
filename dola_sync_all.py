import os
import sys
import shutil
import hashlib
import zipfile
import json
import datetime
import subprocess

# Paths
VAULT_DIR = r"C:\Users\antoni\Dola\obsidian_vault"
CLOUD_1_DIR = r"C:\Users\antoni\OneDrive\Dola_Vault_Backup"
CLOUD_3_DIR = r"C:\Users\antoni\Dola\cloud_backups"
STATE_FILE = r"C:\Users\antoni\Dola\cloud_backups\sync_state.json"
MARKER_FILE = r"C:\Users\antoni\Dola\cloud_backups\BACKUP_COMPLETE.json"
LOG_DIR = r"C:\Users\antoni\Dola\logs"
OMNI_SYNC_SCRIPT = r"C:\Users\antoni\Dola\dola_omni_sync.py"

os.makedirs(CLOUD_3_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

def compute_vault_hash(vault_path):
    hasher = hashlib.sha256()
    file_count = 0
    for root, dirs, files in os.walk(vault_path):
        if ".git" in dirs:
            dirs.remove(".git")
        for f in sorted(files):
            full_p = os.path.join(root, f)
            try:
                rel_p = os.path.relpath(full_p, vault_path)
                mtime = os.path.getmtime(full_p)
                size = os.path.getsize(full_p)
                hasher.update(f"{rel_p}:{mtime}:{size}".encode("utf-8"))
                file_count += 1
            except Exception:
                pass
    return hasher.hexdigest(), file_count

def run_sync(force=False):
    # Step 1: Run Omni-Directional Mesh Sync across all 4 nodes
    if os.path.exists(OMNI_SYNC_SCRIPT):
        cmd = ["python", OMNI_SYNC_SCRIPT]
        if force:
            cmd.append("--force")
        subprocess.run(cmd, capture_output=True)

    current_hash, file_count = compute_vault_hash(VAULT_DIR)
    
    previous_hash = None
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                state_data = json.load(f)
                previous_hash = state_data.get("vault_hash")
        except Exception:
            pass

    # Silent Execution Rule: If no update occurred, exit silently
    if not force and previous_hash == current_hash:
        sys.exit(0)

    timestamp_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")

    # 1. CLOUD 1: OneDrive Mirror
    os.makedirs(CLOUD_1_DIR, exist_ok=True)
    try:
        subprocess.run(
            ["robocopy", VAULT_DIR, CLOUD_1_DIR, "/MIR", "/XD", ".git", "/R:1", "/W:1", "/NFL", "/NDL", "/NJH", "/NJS"],
            capture_output=True,
            text=True
        )
        c1_status = "SUCCESS"
    except Exception as e:
        c1_status = f"ERROR: {e}"

    # 2. CLOUD 2: Git Snapshot Commit
    try:
        subprocess.run(["git", "-C", VAULT_DIR, "add", "."], capture_output=True)
        commit_res = subprocess.run(
            ["git", "-C", VAULT_DIR, "commit", "-m", f"Auto-sync /SYNC ALL 3AM snapshot: {timestamp_str}"],
            capture_output=True,
            text=True
        )
        git_hash_proc = subprocess.run(
            ["git", "-C", VAULT_DIR, "rev-parse", "HEAD"],
            capture_output=True,
            text=True
        )
        git_commit_sha = git_hash_proc.stdout.strip()
        c2_status = "SUCCESS"
    except Exception as e:
        c2_status = f"ERROR: {e}"
        git_commit_sha = "N/A"

    # 3. CLOUD 3: Compressed Archive Mesh
    archive_name = f"Dola_Vault_{date_str}.zip"
    archive_path = os.path.join(CLOUD_3_DIR, archive_name)
    try:
        with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(VAULT_DIR):
                if ".git" in dirs:
                    dirs.remove(".git")
                for file in files:
                    file_p = os.path.join(root, file)
                    arcname = os.path.relpath(file_p, VAULT_DIR)
                    zipf.write(file_p, arcname)
        
        with open(archive_path, "rb") as af:
            archive_sha = hashlib.sha256(af.read()).hexdigest()
        c3_status = "SUCCESS"
    except Exception as e:
        c3_status = f"ERROR: {e}"
        archive_sha = "N/A"

    # Verification
    all_success = (c1_status == "SUCCESS" and c2_status == "SUCCESS" and c3_status == "SUCCESS")
    
    status_record = {
        "status": "COMPLETE" if all_success else "PARTIAL",
        "timestamp": timestamp_str,
        "date": date_str,
        "vault_files_count": file_count,
        "vault_sha256": current_hash,
        "clouds": {
            "cloud_1_onedrive": {
                "destination": CLOUD_1_DIR,
                "status": c1_status
            },
            "cloud_2_git_snapshot": {
                "destination": VAULT_DIR,
                "status": c2_status,
                "commit_sha": git_commit_sha
            },
            "cloud_3_archive_mesh": {
                "destination": archive_path,
                "status": c3_status,
                "archive_sha256": archive_sha
            }
        },
        "all_identical_and_verified": all_success
    }

    with open(MARKER_FILE, "w", encoding="utf-8") as f:
        json.dump(status_record, f, indent=2)
    
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump({"vault_hash": current_hash, "last_sync": timestamp_str}, f, indent=2)

    log_file = os.path.join(LOG_DIR, "sync_all.log")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp_str}] /SYNC ALL Executed - 3 Clouds Verified: {all_success} (Files: {file_count})\n")

    print(json.dumps(status_record, indent=2))

if __name__ == "__main__":
    force_mode = "--force" in sys.argv
    run_sync(force=force_mode)
