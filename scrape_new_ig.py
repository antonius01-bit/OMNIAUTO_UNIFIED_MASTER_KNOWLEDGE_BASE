import sys
import os
import json
import subprocess
import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

shortcodes = ['DdmBUoExrtb', 'Ddj7w16jbDA', 'DdbadaAJeM-', 'DdOc3rHBvTb']
results = {}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

for sc in shortcodes:
    url = f'https://www.instagram.com/p/{sc}/'
    print(f'Fetching {sc}...')
    data = {'shortcode': sc, 'url': url}
    
    # Try yt-dlp first
    try:
        proc = subprocess.run(['yt-dlp', '--dump-json', '--skip-download', url], capture_output=True, text=True, timeout=30, encoding='utf-8')
        if proc.returncode == 0 and proc.stdout.strip():
            j = json.loads(proc.stdout)
            data['title'] = j.get('title')
            data['description'] = j.get('description')
            data['uploader'] = j.get('uploader')
            data['uploader_id'] = j.get('uploader_id')
            data['duration'] = j.get('duration')
            data['method'] = 'yt-dlp'
            results[sc] = data
            print(f"Success yt-dlp for {sc}: uploader={data.get('uploader')}")
            continue
    except Exception as e:
        print(f"yt-dlp error for {sc}: {e}")
        
    # Fallback to embed
    try:
        embed_url = f'https://www.instagram.com/p/{sc}/embed/?_fb_noscript=1'
        r = requests.get(embed_url, headers=headers, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        caption = ''
        
        caption_div = soup.find('div', class_='Caption')
        if caption_div:
            caption = caption_div.get_text(separator=' ', strip=True)
        else:
            caption = soup.get_text(separator=' ', strip=True)
            
        data['caption'] = caption[:2500]
        data['method'] = 'embed'
        results[sc] = data
        print(f"Embed fetched for {sc}: len={len(caption)}")
    except Exception as e:
        data['error'] = str(e)
        results[sc] = data
        print(f"Error for {sc}: {e}")

with open('new_instagram_harvest_4.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print('Saved to new_instagram_harvest_4.json')
