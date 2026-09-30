import urllib.request, json

repos = [
    "firecrawl/firecrawl-claude-plugin",
    "crynta/terax-ai",
    "ScrapeGraphAI/Scrapegraph-ai",
    "ScrapeGraphAI/scrapegraph-mcp",
    "D4Vinci/Scrapling",
    "Cedriccmh/claude-code-skill-scrapling",
    "seszele64/scrapling-mcp",
    "supabase/supabase",
    "nocodb/nocodb",
    "calcom/cal.com",
    "PostHog/posthog"
]

headers = {"User-Agent": "Mozilla/5.0"}
for r in repos:
    url = f"https://api.github.com/repos/{r}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            desc = data.get("description", "")
            stars = data.get("stargazers_count", 0)
            lang = data.get("language", "")
            print(f"[{r}] ({lang}, Stars: {stars}): {desc}")
    except Exception as e:
        print(f"[{r}]: {e}")
