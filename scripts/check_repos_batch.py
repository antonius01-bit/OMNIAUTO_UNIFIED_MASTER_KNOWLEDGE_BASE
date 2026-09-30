import urllib.request, json

repos = [
    'Nutlope/hallmark',
    'DietrichGebert/ponytail',
    'ilindaniel/ponytail-lite',
    'Significant-Gravitas/AutoGPT',
    'RimaBuilds/AutoGPT-handbook',
    'N3rdmade/TBCPL',
    'Wan-Video/Wan2.1',
    'Wan-Video/Wan2.2',
    'Wan-Video/Wan-skills',
    'pipecat-ai/pipecat',
    'pipecat-ai/pipecat-flows',
    'cline/cline',
    'gitroomhq/postiz-app',
    'Mintplex-Labs/anything-llm',
    'crewAIInc/crewAI',
    'browser-use/browser-use',
    'firecrawl/firecrawl',
    'firecrawl/firecrawl-mcp-server'
]

headers = {'User-Agent': 'Mozilla/5.0'}
for r in repos:
    url = f'https://api.github.com/repos/{r}'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            desc = data.get('description', '')
            stars = data.get('stargazers_count', 0)
            lang = data.get('language', '')
            print(f'[{r}] ({lang}, Stars: {stars}): {desc}')
    except Exception as e:
        print(f'[{r}]: {e}')
