#!/usr/bin/env python3
"""
OpenViking Virtual Filesystem CLI (viking:// protocol)
Powers hierarchical memory browsing, directory recursive retrieval, and asset persistence.
"""
import os
import sys
import json
import argparse

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(r"C:\Users\antoni\Dola\agent_memory")

def resolve_viking_path(vpath: str) -> str:
    if vpath.startswith("viking://"):
        rel = vpath[len("viking://"):].lstrip("/")
    elif vpath.startswith("viking:"):
        rel = vpath[len("viking:"):].lstrip("/")
    else:
        rel = vpath.lstrip("/")
    return os.path.normpath(os.path.join(BASE_DIR, rel))

def viking_ls(vpath: str = "viking://") -> None:
    target = resolve_viking_path(vpath)
    if not os.path.exists(target):
        print(f"[!] Path does not exist: {vpath} ({target})")
        return
    
    print(f"\n📂 OpenViking Virtual Filesystem Explorer: {vpath}")
    print("=" * 65)
    for root, dirs, files in os.walk(target):
        rel_root = os.path.relpath(root, BASE_DIR)
        v_folder = "viking://" if rel_root == "." else f"viking://{rel_root.replace(os.sep, '/')}"
        depth = rel_root.count(os.sep) if rel_root != "." else 0
        indent = "  " * depth
        folder_name = os.path.basename(root) if rel_root != "." else "viking:// (root)"
        print(f"{indent}📁 {folder_name}/  [{v_folder}]")
        for f in sorted(files):
            fpath = os.path.join(root, f)
            size = os.path.getsize(fpath)
            print(f"{indent}  📄 {f} ({size:,} bytes)")
    print("=" * 65 + "\n")

def viking_read(vpath: str) -> str:
    target = resolve_viking_path(vpath)
    if not os.path.isfile(target):
        print(f"[!] File not found: {vpath} ({target})")
        return ""
    with open(target, "r", encoding="utf-8") as f:
        content = f.read()
    rel = os.path.relpath(target, BASE_DIR).replace(os.sep, "/")
    print(f"\n📄 === [viking://{rel}] ===\n")
    print(content)
    return content

def viking_write(vpath: str, content: str) -> None:
    target = resolve_viking_path(vpath)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[✓] Successfully stored {len(content)} characters to {vpath}")

def viking_search(query: str, root_vpath: str = "viking://") -> None:
    target = resolve_viking_path(root_vpath)
    print(f"\n🔍 Directory Recursive Retrieval for '{query}' scoped to {root_vpath}...")
    print("=" * 65)
    matches = 0
    for root, dirs, files in os.walk(target):
        for f in sorted(files):
            fpath = os.path.join(root, f)
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
                    lines = fp.readlines()
                for idx, line in enumerate(lines, 1):
                    if query.lower() in line.lower():
                        rel = os.path.relpath(fpath, BASE_DIR).replace(os.sep, "/")
                        print(f"  [viking://{rel}:{idx}] {line.strip()[:100]}")
                        matches += 1
            except Exception:
                pass
    print("=" * 65)
    print(f"[✓] Search completed: {matches} match(es) located.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OpenViking Virtual Filesystem CLI")
    subparsers = parser.add_subparsers(dest="command")

    ls_parser = subparsers.add_parser("ls", help="List virtual filesystem hierarchy")
    ls_parser.add_argument("path", nargs="?", default="viking://", help="Target path (default: viking://)")

    read_parser = subparsers.add_parser("read", help="Read a file from VFS")
    read_parser.add_argument("path", help="Target path, e.g. viking://resources/architecture/ADR-001.md")

    search_parser = subparsers.add_parser("search", help="Directory recursive search")
    search_parser.add_argument("query", help="Search term")
    search_parser.add_argument("--scope", default="viking://", help="Scope path")

    store_parser = subparsers.add_parser("store", help="Store content to VFS")
    store_parser.add_argument("path", help="Target path")
    store_parser.add_argument("content", help="Content string")

    args = parser.parse_args()
    if args.command == "ls":
        viking_ls(args.path)
    elif args.command == "read":
        viking_read(args.path)
    elif args.command == "search":
        viking_search(args.query, args.scope)
    elif args.command == "store":
        viking_write(args.path, args.content)
    else:
        viking_ls("viking://")
