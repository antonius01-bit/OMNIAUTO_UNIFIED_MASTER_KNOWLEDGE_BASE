import urllib.request
import urllib.error
import json
import ssl
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()

agnes_key = "sk-REDACTED_BY_SECURITY_POLICY"
manus_key = "sk-REDACTED_BY_SECURITY_POLICY"

print("--- TESTING AGNES ---")
agnes_urls = [
    "https://apihub.agnes-ai.com/v1/models",
    "https://api.agnes-ai.com/v1/models",
    "https://platform.agnes-ai.com/v1/models",
    "https://api.agnes.ai/v1/models",
    "https://api.agnes.com/v1/models",
    "https://api.agnesai.com/v1/models"
]

for u in agnes_urls:
    req = urllib.request.Request(u, headers={"Authorization": f"Bearer {agnes_key}", "User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=5, context=ctx) as resp:
            data = resp.read().decode("utf-8")
            print(f"Agnes Success at {u}: {data[:200]}")
            break
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="ignore")
        print(f"Agnes HTTPError at {u}: {e.code} - {err[:150]}")
    except Exception as e:
        print(f"Agnes Error at {u}: {e}")

print("\n--- TESTING MANUS ---")
manus_urls = [
    "https://api.manus.im/v1/models",
    "https://api.manus.im/models",
    "https://api.manus.im/v1/tasks",
    "https://api.manus.ai/v1/models",
    "https://api.manus.im/apiproxy.v1.ApiProxyService/CallApi",
    "https://api.manus.im/v1/agent/tasks"
]

for u in manus_urls:
    req = urllib.request.Request(u, headers={"Authorization": f"Bearer {manus_key}", "API_KEY": manus_key, "User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=5, context=ctx) as resp:
            data = resp.read().decode("utf-8")
            print(f"Manus Success at {u}: {data[:200]}")
            break
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="ignore")
        print(f"Manus HTTPError at {u}: {e.code} - {err[:150]}")
    except Exception as e:
        print(f"Manus Error at {u}: {e}")
