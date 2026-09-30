# 🌐 Master MCP Server Registry & Technical Documentation Index

> **Compiled Sources**:
> - [mcpservers.org](https://mcpservers.org/)
> - [mcp.so](https://mcp.so/servers) (18,000+ servers cataloged across 15 categories)
> - [mcpplaygroundonline.com](https://mcpplaygroundonline.com/mcp-registry) (10,000+ servers)
> - [mcpmarket.com](https://mcpmarket.com/)
> - Official Model Context Protocol Registry (`registry.modelcontextprotocol.io`)

---

## 📊 1. Top MCP Categories Taxonomy

| Category | Global Count (mcp.so) | Core Use Case | Representative Servers |
|---|:---:|---|---|
| **Developer Tools** | 2,361 servers | Code editing, compilation, terminals, AST analysis | Termany, LocalCan, AST-Grep, Docker |
| **AI & Agents** | 1,153 servers | Multi-agent swarms, agent toolkits, prompt routers | Hostinger AI, LangChain, CrewAI, AutoGen |
| **Cloud & Infrastructure** | 752 servers | Cloud deployment, AWS, GCP, Cloudflare Workers | AWS MCP, Cloudflare, Kubernetes, Terraform |
| **Memory & Knowledge** | 648 servers | Long-term episodic memory, graph storage, vector caches | OpenViking VFS, PLUR, OpenLore, Mem0 |
| **Media & Design** | 626 servers | Image editing, Figma integration, video pipelines | Canva MCP, StableDiffusion, Figma API |
| **Databases** | 563 servers | Relational & vector databases, SQL execution | Supabase, PostgreSQL, SQLite, Neo4j |
| **Version Control** | 505 servers | Git workflow, commit analysis, PR automation | GitHub MCP, GitLab, Gitlawb, Bitbucket |
| **Data & Analytics** | 492 servers | BigQuery, ClickHouse, PostHog, BI reporting | BigQuery MCP, PostHog, Pandas AI |
| **Finance & Commerce** | 325 servers | Payment webhooks, stock market APIs, crypto | Stripe MCP, AlphaVantage, CoinGecko |
| **Productivity** | 309 servers | Notion, Linear, Jira, Todoist, Obsidian PKM | Obsidian MCP, Linear, Notion, Todoist |
| **Communication** | 284 servers | ChatOps, Email agents, Slack, Discord | Slack MCP, Atomic Mail, Discord Bot |
| **Search & Research** | 283 servers | Web search, academic paper scraping, citations | Brave Search, Exa Search, Semantic Scholar |
| **Browser Automation** | 238 servers | Headless scraping, DOM evaluation, session replay | Puppeteer, Playwright, Browser-Use |
| **Files & Storage** | 194 servers | Sandboxed file I/O, Google Drive, S3, Dropbox | Filesystem MCP, Google Drive, S3 |
| **Reasoning** | 124 servers | Deliberation trees, multi-step math, reflection | Sequential Thinking, Tree of Thoughts |

---

## 🛠️ 2. High-Impact Enterprise MCP Servers Specification

| Server Name | Upstream Package | Transport | Auth Required | Core Tools & API Endpoints |
|---|---|:---:|:---:|---|
| **GitHub MCP Server** | `modelcontextprotocol/server-github` | `stdio` | `GITHUB_PERSONAL_ACCESS_TOKEN` | Repository management, issues, pull requests, file contents, commit inspection. (CLI: `npx -y @modelcontextprotocol/server-github`) |
| **Fetch MCP Server** | `modelcontextprotocol/server-fetch` | `stdio` | `None` | Fetches web page content, converts HTML to clean markdown, strips ads/scripts. (CLI: `npx -y @modelcontextprotocol/server-fetch`) |
| **Puppeteer MCP Server** | `modelcontextprotocol/server-puppeteer` | `stdio` | `None` | Headless Chrome automation, screenshot capture, DOM interaction, SPA rendering. (CLI: `npx -y @modelcontextprotocol/server-puppeteer`) |
| **Brave Search MCP** | `modelcontextprotocol/server-brave-search` | `stdio` | `BRAVE_API_KEY` | Real-time web search and localized query results with high privacy. (CLI: `npx -y @modelcontextprotocol/server-brave-search`) |
| **SQLite MCP Server** | `modelcontextprotocol/server-sqlite` | `stdio` | `None` | Direct SQL querying, schema introspection, tables and rows modification. (CLI: `npx -y @modelcontextprotocol/server-sqlite --file <db_path>`) |
| **PostgreSQL MCP Server** | `modelcontextprotocol/server-postgres` | `stdio` | `POSTGRES_URL` | Enterprise PostgreSQL database querying, transaction execution, schema inspection. (CLI: `npx -y @modelcontextprotocol/server-postgres <connection_string>`) |
| **OpenViking Memory VFS** | `volcengine/OpenViking` | `stdio / port 3111` | `None` | Virtual filesystem context DB (viking:// protocol) with directory recursive retrieval. (CLI: `python -m openviking.mcp_server`) |
| **Sequential Thinking MCP** | `modelcontextprotocol/server-sequential-thinking` | `stdio` | `None` | Structured dynamic thinking loop with hypothesis testing, revisions, and branching. (CLI: `npx -y @modelcontextprotocol/server-sequential-thinking`) |
| **Upstash Context7** | `upstash/context7-mcp` | `stdio` | `None` | Real-time version-specific library documentation and anti-hallucination code injection. (CLI: `npx -y @upstash/context7-mcp`) |
| **Obsidian MCP Server** | `obsidian-mcp` | `stdio` | `None` | Search, read, create, tag, and modify markdown notes inside Obsidian vaults. (CLI: `npx -y obsidian-mcp serve --vault <path>`) |
| **Seekstone Obsidian** | `seekstone` | `stdio` | `SEEKSTONE_VAULT` | Context-packing, outline extraction, backlinks, frontmatter patching for Obsidian. (CLI: `npx -y seekstone`) |
| **Docker MCP Server** | `modelcontextprotocol/server-docker` | `stdio` | `Docker Socket` | Container lifecycle management, image building, logs inspection, sandboxed execution. (CLI: `npx -y @modelcontextprotocol/server-docker`) |
| **Filesystem MCP Server** | `modelcontextprotocol/server-filesystem` | `stdio` | `None` | Sandboxed filesystem access: read, write, edit, search, and directory tree. (CLI: `npx -y @modelcontextprotocol/server-filesystem <allowed_dir>`) |
| **Slack MCP Server** | `modelcontextprotocol/server-slack` | `stdio` | `SLACK_BOT_TOKEN` | Channel messaging, thread reading, user mentions, team notification automation. (CLI: `npx -y @modelcontextprotocol/server-slack`) |
| **Exa AI Search MCP** | `exa-labs/exa-mcp-server` | `stdio` | `EXA_API_KEY` | Neural search engine built for LLMs with link semantic similarity and full text filtering. (CLI: `npx -y exa-mcp-server`) |

---

## ⚙️ 3. Client Configuration Snippets

### A. Antigravity Global Config (`~/.gemini/config/mcp_config.json`)
```json
{
  "mcpServers": {
    "github": {
      "command": "cmd.exe",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_TOKEN" }
    },
    "fetch": {
      "command": "cmd.exe",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-fetch"]
    },
    "brave-search": {
      "command": "cmd.exe",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-brave-search"],
      "env": { "BRAVE_API_KEY": "YOUR_KEY" }
    }
  }
}
```

### B. Cursor IDE (`~/.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    }
  }
}
```

### C. Claude Desktop (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "openviking-memory": {
      "command": "python",
      "args": ["-m", "openviking.mcp_server"],
      "env": { "VIKING_STORAGE_PATH": "C:/Users/antoni/Dola/agent_memory" }
    }
  }
}
```