#!/usr/bin/env python3
import json
import os
import sys
import subprocess
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROFILES_JSON = r"C:\Users\antoni\Dola\tracked_github_profiles.json"
profiles = json.load(open(PROFILES_JSON, encoding='utf-8-sig'))

print(f"Auditing & repairing {len(profiles)} tracked authors...")
fixed = 0
all_valid = 0
still_broken = []

for p in profiles:
    u = p.get('username')
    for r in p.get('repos', []):
        path = r.get('local_path')
        git_dir = os.path.join(path, '.git')
        if not os.path.exists(git_dir):
            continue

        repo_name = r.get('name')

        # 1. Clean stale locks
        try:
            for item in os.listdir(git_dir):
                if item.endswith('.lock'):
                    try:
                        os.remove(os.path.join(git_dir, item))
                        print(f"  Cleaned lock file {item} in {u}/{repo_name}")
                    except Exception:
                        pass
        except Exception:
            pass

        # 2. Check HEAD
        res = subprocess.run(['git', '-C', path, 'rev-parse', '--verify', 'HEAD'], capture_output=True, text=True)
        if res.returncode == 0:
            all_valid += 1
            continue

        # HEAD is invalid - let's fix it
        print(f"Fixing {u}/{repo_name}...")
        commit_hash = None
        target_branch = 'main'

        # Look in FETCH_HEAD
        fh_path = os.path.join(git_dir, 'FETCH_HEAD')
        if os.path.exists(fh_path):
            content = open(fh_path, 'r', errors='ignore').read()
            m = re.search(r'^([0-9a-f]{40})\s+(?:not-for-merge\s+)?branch \'([^\']+)\'', content, re.MULTILINE)
            if m:
                commit_hash = m.group(1)
                target_branch = m.group(2)
            else:
                m2 = re.search(r'^([0-9a-f]{40})', content)
                if m2:
                    commit_hash = m2.group(1)

        # Look in packed-refs
        if not commit_hash:
            pr_path = os.path.join(git_dir, 'packed-refs')
            if os.path.exists(pr_path):
                content = open(pr_path, 'r', errors='ignore').read()
                m = re.search(r'^([0-9a-f]{40})\s+refs/remotes/origin/(\w+)', content, re.MULTILINE)
                if m:
                    commit_hash = m.group(1)
                    target_branch = m.group(2)
                else:
                    m2 = re.search(r'^([0-9a-f]{40})\s+refs/tags/', content, re.MULTILINE)
                    if m2:
                        commit_hash = m2.group(1)

        # Look in refs/remotes/origin
        if not commit_hash:
            remotes_dir = os.path.join(git_dir, 'refs', 'remotes', 'origin')
            if os.path.exists(remotes_dir):
                for rf in os.listdir(remotes_dir):
                    if rf not in ['HEAD']:
                        target_branch = rf
                        commit_hash = open(os.path.join(remotes_dir, rf), 'r', errors='ignore').read().strip()
                        break

        # Look in refs/heads
        if not commit_hash:
            heads_dir = os.path.join(git_dir, 'refs', 'heads')
            if os.path.exists(heads_dir):
                for hf in os.listdir(heads_dir):
                    if hf != '.invalid':
                        target_branch = hf
                        commit_hash = open(os.path.join(heads_dir, hf), 'r', errors='ignore').read().strip()
                        break

        # If still no commit found, try shallow fetch of origin HEAD with try/except
        if not commit_hash:
            env = {**os.environ, 'GIT_TERMINAL_PROMPT': '0', 'GIT_ASKPASS': ''}
            try:
                subprocess.run(['git', '-C', path, 'fetch', '--depth=1', 'origin'], capture_output=True, text=True, timeout=35, env=env)
                if os.path.exists(fh_path):
                    content = open(fh_path, 'r', errors='ignore').read()
                    m = re.search(r'^([0-9a-f]{40})', content)
                    if m:
                        commit_hash = m.group(1)
            except Exception as e:
                print(f"  [!] Fetch error for {u}/{repo_name}: {e}")

        if commit_hash:
            with open(os.path.join(git_dir, 'HEAD'), 'w') as f:
                f.write(f'ref: refs/heads/{target_branch}\n')
            res_rst = subprocess.run(['git', '-C', path, 'reset', '--hard', commit_hash], capture_output=True, text=True)
            res_v = subprocess.run(['git', '-C', path, 'rev-parse', '--verify', 'HEAD'], capture_output=True, text=True)
            if res_v.returncode == 0:
                print(f"  [OK] Healed to {target_branch} @ {commit_hash[:7]}")
                fixed += 1
                all_valid += 1
            else:
                print(f"  [FAIL] Reset failed: {res_rst.stderr.strip()[:100]}")
                still_broken.append((u, repo_name, path))
        else:
            print(f"  [FAIL] No commit found for {u}/{repo_name}")
            still_broken.append((u, repo_name, path))

print(f"\n==========================================")
print(f"RESULT: Valid Repos: {all_valid}/226 | Fixed: {fixed}")
print(f"Still Broken: {len(still_broken)}")
for b in still_broken:
    print(f"  - {b}")
