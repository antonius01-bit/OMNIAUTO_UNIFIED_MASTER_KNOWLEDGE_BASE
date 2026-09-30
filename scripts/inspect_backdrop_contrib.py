import urllib.request
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

url = 'https://api.github.com/orgs/backdrop-contrib/repos?per_page=50&sort=pushed'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as r:
        repos = json.loads(r.read().decode('utf-8'))
        print(f"Total Backdrop Contrib repos fetched: {len(repos)}")
        repos.sort(key=lambda x: x.get('stargazers_count', 0), reverse=True)
        for repo in repos[:20]:
            name = repo['name']
            stars = repo.get('stargazers_count', 0)
            desc = (repo.get('description') or '')[:80]
            print(f" * {name:25} | Stars: {stars:2} | {desc}")
except Exception as e:
    print('Error:', e)
