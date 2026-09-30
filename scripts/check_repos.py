import urllib.request, json

repos = [
    'growthbook/growthbook-golang',
    'k2-fsa/OmniVoice',
    'debpalash/VoiceStudio',
    'fracabu/heygen-app',
    'DeusData/codebase-memory-mcp',
    'win4r/codebase-memory-mcp-pro',
    'msitarzewski/agency-agents',
    'jnMetaCode/agency-agents-id',
    'Panniantong/Agent-Reach',
    'EdisonChenAI/agent-reach',
    'garrytan/gstack',
    'mutagen-io/mutagen',
    'cjpais/Handy',
    'cjpais/handy-cli',
    'calesthio/OpenMontage',
    'darvis-ai/Brainless',
    'theswerd/brainless',
    'boundless-recursion/brainless',
    'alexgreensh/attention-span',
    'michalspiegel/AttentionSpan',
    'rushilsscode/Real-time-attention-span-detection-using-Machine-learning',
    'JoeRoussy/adaptive-attention-in-cv'
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
