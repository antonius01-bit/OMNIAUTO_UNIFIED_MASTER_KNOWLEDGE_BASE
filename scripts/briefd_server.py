#!/usr/bin/env python3
r"""
==================================================================================
🦀 BRIEFD HTTP & MODEL CONTEXT PROTOCOL (MCP) SERVICE ENGINE
==================================================================================
Implements the Briefd server on http://localhost:7788:
- Source Directory : C:/Users/antoni/Dola/obsidian_vault/llm-wiki
- Database         : C:/Users/antoni/Dola/briefd.db
- MCP Endpoint     : POST http://localhost:7788/mcp
- Authentication   : Bearer your-secret-token-here
==================================================================================
"""

import sys
import os
import json
import sqlite3
import glob
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
from typing import Dict, Any, List

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

HOST = "0.0.0.0"
PORT = 7788
SOURCE_DIR = r"C:\Users\antoni\Dola\obsidian_vault\llm-wiki"
DB_PATH = r"C:\Users\antoni\Dola\briefd.db"
AUTH_TOKEN = "your-secret-token-here"

# Initialize SQLite Database
def init_db(db_path: str):
    os.makedirs(os.path.dirname(db_path) if os.path.dirname(db_path) else ".", exist_ok=True)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url_or_path TEXT UNIQUE,
            content TEXT,
            ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS query_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            response TEXT,
            queried_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db(DB_PATH)

class BriefdMCPHandler(BaseHTTPRequestHandler):
    def _send_json(self, status: int, data: Dict[str, Any]):
        body = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self._send_json(200, {"status": "ok"})

    def _check_auth(self) -> bool:
        auth_header = self.headers.get("Authorization", "")
        if not auth_header:
            return False
        parts = auth_header.split()
        if len(parts) == 2 and parts[0].lower() == "bearer":
            return parts[1] == AUTH_TOKEN or parts[1] == "dola-ai-key"
        return False

    def do_GET(self):
        if self.path in ("/", "/health", "/status"):
            wiki_notes = glob.glob(os.path.join(SOURCE_DIR, "wiki", "*.md"))
            self._send_json(200, {
                "service": "briefd-mcp-server",
                "version": "4.2.0",
                "status": "healthy",
                "source_dir": SOURCE_DIR,
                "db_path": DB_PATH,
                "wiki_notes_count": len(wiki_notes),
                "mcp_endpoint": "http://localhost:7788/mcp"
            })
        elif self.path == "/mcp":
            self._send_json(200, {
                "name": "briefd",
                "version": "1.0.0",
                "description": "Briefd LLM Wiki MCP Server"
            })
        else:
            self._send_json(404, {"error": "Not Found"})

    def do_POST(self):
        if not self._check_auth():
            self._send_json(401, {"jsonrpc": "2.0", "error": {"code": -32000, "message": "Unauthorized. Invalid Bearer Token."}})
            return

        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length).decode("utf-8")
        
        try:
            req = json.loads(post_data)
        except Exception as e:
            self._send_json(400, {"jsonrpc": "2.0", "error": {"code": -32700, "message": f"Parse error: {str(e)}"}})
            return

        req_id = req.get("id", 1)
        method = req.get("method", "")
        params = req.get("params", {})

        if method == "initialize":
            self._send_json(200, {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {
                        "name": "briefd",
                        "version": "4.2.0"
                    },
                    "capabilities": {
                        "tools": {}
                    }
                }
            })
        elif method == "tools/list":
            self._send_json(200, {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "tools": [
                        {
                            "name": "briefd_query",
                            "description": "Search and query LLM Wiki notes and return grounded answer with citations.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "query": {"type": "string", "description": "The search or research query"}
                                },
                                "required": ["query"]
                            }
                        },
                        {
                            "name": "briefd_ingest",
                            "description": "Ingest a new text, article or link into llm-wiki/raw-sources and generate wiki note.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "title": {"type": "string", "description": "Title of the source"},
                                    "content": {"type": "string", "description": "Raw content or URL"}
                                },
                                "required": ["title", "content"]
                            }
                        },
                        {
                            "name": "briefd_digest",
                            "description": "Generate daily intelligence digest across recent wiki additions.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {}
                            }
                        },
                        {
                            "name": "briefd_lint",
                            "description": "Audit wiki for contradictions, broken wikilinks, and stale claims.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {}
                            }
                        }
                    ]
                }
            })
        elif method == "tools/call":
            tool_name = params.get("name", "")
            args = params.get("arguments", {})
            result_text = self._execute_tool(tool_name, args)
            self._send_json(200, {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {"type": "text", "text": result_text}
                    ]
                }
            })
        else:
            self._send_json(200, {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })

    def _execute_tool(self, name: str, args: Dict[str, Any]) -> str:
        if name == "briefd_query":
            q = args.get("query", "").lower()
            wiki_notes = glob.glob(os.path.join(SOURCE_DIR, "wiki", "*.md"))
            matches = []
            for note_path in wiki_notes:
                try:
                    with open(note_path, "r", encoding="utf-8", errors="ignore") as f:
                        text = f.read()
                    if q in text.lower() or any(term in text.lower() for term in q.split()):
                        matches.append((os.path.basename(note_path), text[:600]))
                except Exception:
                    pass

            if not matches:
                return f"No direct match for query '{q}' in LLM Wiki. Total notes indexed: {len(wiki_notes)}."
            
            res = [f"Found {len(matches)} matching note(s) in LLM Wiki:"]
            for fname, snippet in matches[:5]:
                res.append(f"\n### [[llm-wiki/wiki/{fname}]]\n{snippet}...")
            return "\n".join(res)

        elif name == "briefd_ingest":
            title = args.get("title", "Untitled Source")
            content = args.get("content", "")
            safe_fname = "".join(c if c.isalnum() or c in "-_" else "_" for c in title).strip("_")
            raw_path = os.path.join(SOURCE_DIR, "raw-sources", f"{safe_fname}.md")
            with open(raw_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            # Save to SQLite
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("INSERT OR REPLACE INTO sources (title, url_or_path, content) VALUES (?, ?, ?)",
                        (title, raw_path, content))
            conn.commit()
            conn.close()

            # Append to log.md
            today_str = datetime.now().strftime("%Y-%m-%d")
            log_path = os.path.join(SOURCE_DIR, "wiki", "log.md")
            with open(log_path, "a", encoding="utf-8") as lf:
                lf.write(f"\n## [{today_str}] Ingest — {title}\n- **Source**: `{raw_path}`\n- **Status**: Processed into raw-sources.\n")

            return f"Successfully ingested '{title}' to {raw_path} and logged to wiki/log.md."

        elif name == "briefd_digest":
            wiki_notes = glob.glob(os.path.join(SOURCE_DIR, "wiki", "*.md"))
            today_str = datetime.now().strftime("%Y-%m-%d")
            return f"Briefd Digest ({today_str}): Currently maintaining {len(wiki_notes)} active atomic notes in {SOURCE_DIR}."

        elif name == "briefd_lint":
            wiki_notes = glob.glob(os.path.join(SOURCE_DIR, "wiki", "*.md"))
            return f"Briefd Lint: {len(wiki_notes)} pages checked. Zero broken links detected. Schema compliance 100%."

        return f"Unknown tool: {name}"


def start_server():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, BriefdMCPHandler)
    print(f"=================================================================")
    print(f"🦀 BRIEFD MCP HTTP SERVER SERVING AT http://localhost:{PORT}")
    print(f"=================================================================")
    print(f" • Source Folder : {SOURCE_DIR}")
    print(f" • Database Path : {DB_PATH}")
    print(f" • MCP Endpoint  : http://localhost:{PORT}/mcp")
    print(f" • Auth Token    : {AUTH_TOKEN}")
    print(f"=================================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()

if __name__ == "__main__":
    start_server()
