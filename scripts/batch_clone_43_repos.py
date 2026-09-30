#!/usr/bin/env python3
"""
Batch Shallow Clone 43 Repositories into C:\\Users\\antoni\\Dola\\clones
Runs with ThreadPoolExecutor for high-speed parallel cloning.
"""

import os
import sys
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

TARGET_DIR = Path(r"C:\Users\antoni\Dola\clones")
TARGET_DIR.mkdir(parents=True, exist_ok=True)

REPOS = [
    "https://github.com/exa-labs/websets-mcp-server.git",
    "https://github.com/exa-labs/websets-news-monitor.git",
    "https://github.com/jegly/Box.git",
    "https://github.com/CodeAbra/iai-personal-memory-engine.git",
    "https://github.com/eigent-ai/eigent.git",
    "https://github.com/TryGhost/Ghost.git",
    "https://github.com/getmaxun/maxun.git",
    "https://github.com/0xK3vin/MegaMemory.git",
    "https://github.com/dyamin/MEGA.git",
    "https://github.com/Haehnchen/my-mega-memory.git",
    "https://github.com/netease-youdao/QAnything.git",
    "https://github.com/yanliudesign/offer-toolkit-skill.git",
    "https://github.com/Mxtiv/BlueJammer.git",
    "https://github.com/EmenstaNougat/ESP32-BlueJammer.git",
    "https://github.com/stanfordnlp/dspy.git",
    "https://github.com/WyattBlue/auto-editor.git",
    "https://github.com/Openpanel-dev/openpanel.git",
    "https://github.com/markdoc/markdoc.git",
    "https://github.com/wilsonfreitas/awesome-quant.git",
    "https://github.com/apache/cloudberry.git",
    "https://github.com/coder/code-server.git",
    "https://github.com/wasp-lang/open-saas.git",
    "https://github.com/stablyai/orca.git",
    "https://github.com/arcboxlabs/arcbox.git",
    "https://github.com/Vincentwei1021/video-shotcraft.git",
    "https://github.com/kestra-io/kestra.git",
    "https://github.com/aidongise-cell/prism-scanner.git",
    "https://github.com/jftuga/transcript-critic.git",
    "https://github.com/nicobailon/visual-explainer.git",
    "https://github.com/hardikpandya/stop-slop.git",
    "https://github.com/unisone/self-improving-skills.git",
    "https://github.com/haddock-development/claude-reflect-system.git",
    "https://github.com/microsoft/SkillOpt.git",
    "https://github.com/austindixson/mulch.git",
    "https://github.com/BerriAI/self-improving-agent.git",
    "https://github.com/BerriAI/terraform-google-litellm.git",
    "https://github.com/unisone/ai-prompts.git",
    "https://github.com/jzOcb/self-improving-skill.git",
    "https://github.com/jzOcb/writing-style-skill.git",
    "https://github.com/jzOcb/baoyu-skills.git",
    "https://github.com/jzOcb/ristretto.git",
    "https://github.com/Kulaxyz/self-learning-skills.git",
    "https://github.com/Kulaxyz/token-diet.git"
]

def get_repo_name(url):
    raw = url.rstrip("/").split("/")[-1]
    if raw.endswith(".git"):
        raw = raw[:-4]
    elif raw.endswith(".github"):
        raw = raw[:-7]
    return raw

def clone_repo(url):
    name = get_repo_name(url)
    dest = TARGET_DIR / name
    if dest.exists() and any(dest.iterdir()):
        return (name, True, "Already exists")

    # Try primary URL, with fallback if .github was specified
    urls_to_try = [url]
    if url.endswith(".github"):
        urls_to_try.append(url[:-7] + ".git")
        urls_to_try.append(url[:-7])
    elif not url.endswith(".git"):
        urls_to_try.append(url + ".git")

    for u in urls_to_try:
        cmd = ["git", "clone", "--depth", "1", u, str(dest)]
        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=120)
            if res.returncode == 0:
                return (name, True, f"Cloned successfully from {u}")
        except Exception as e:
            pass

    return (name, False, "Clone failed across all URL variations")

def main():
    print(f"[*] Starting batch cloning of {len(REPOS)} repositories into: {TARGET_DIR}")
    successful = 0
    failed = 0
    failed_repos = []

    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {executor.submit(clone_repo, repo): repo for repo in REPOS}
        for future in as_completed(futures):
            name, ok, msg = future.result()
            if ok:
                successful += 1
                print(f"  [+] {name}: {msg}")
            else:
                failed += 1
                failed_repos.append(name)
                print(f"  [-] {name}: {msg}")

    print("\n==========================================")
    print(f"Batch Cloning Summary: {successful} Successful | {failed} Failed")
    if failed_repos:
        print(f"Failed repos: {', '.join(failed_repos)}")
    print("==========================================")

if __name__ == "__main__":
    main()
