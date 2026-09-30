import requests
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get('https://console.higgsfield.ai/models/bytedance/seedance-2.5/text-to-video/api-reference', headers=headers)

# Find parameters and code examples
print("Searching for code examples in page...")
for match in re.finditer(r'(bytedance/seedance-2\.5/text-to-video.*?)(?="slug"|function|$)', r.text, re.DOTALL):
    text = match.group(1)[:2000]
    print("Found snippet:", repr(text[:300]))

# Search for python example
py_matches = re.findall(r'(subscribe\(.*?\))', r.text)
print("Subscribe matches:", len(py_matches))
for pm in py_matches:
    print("Subscribe call:", pm)

# Search for argument keys
for kw in ['aspect_ratio', 'resolution', 'duration', 'camera_motion', 'generate_audio']:
    m = re.findall(rf'"{kw}"\s*:\s*([^,\}}]+)', r.text)
    if m:
        print(f"Key {kw}:", m[:5])
