import json, re, os

transcript_path = r"C:\Users\antoni\.gemini\antigravity\brain\65068e22-c3d3-4374-8597-4efb0170c7c2\.system_generated\logs\transcript_full.jsonl"
if not os.path.exists(transcript_path):
    transcript_path = r"C:\Users\antoni\.gemini\antigravity\brain\65068e22-c3d3-4374-8597-4efb0170c7c2\.system_generated\logs\transcript.jsonl"

all_links = []
if os.path.exists(transcript_path):
    with open(transcript_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            try:
                d = json.loads(line)
                if d.get("source") == "USER_EXPLICIT" and d.get("type") == "USER_INPUT":
                    content = d.get("content", "")
                    urls = re.findall(r"https?://[^\s\)]+", content)
                    all_links.extend(urls)
            except Exception:
                pass

cleaned = set()
for u in all_links:
    u = u.rstrip(".,;)'\"]>")
    cleaned.add(u)

print(f"Total unique URLs provided by user: {len(cleaned)}")
with open(r"C:\Users\antoni\Dola\ALL_USER_LINKS.txt", "w", encoding="utf-8") as out:
    for u in sorted(cleaned):
        out.write(u + "\n")
        print(u)
