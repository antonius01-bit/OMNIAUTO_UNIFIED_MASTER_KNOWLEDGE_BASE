import os
import re

PATTERNS = [
    (re.compile(r'AQ\.[A-Za-z0-9_-]{20,}'), 'AQ.REDACTED_BY_SECURITY_POLICY'),
    (re.compile(r'AIzaSy[A-Za-z0-9_-]{33}'), 'AIzaSy_REDACTED_BY_SECURITY_POLICY_X1'),
    (re.compile(r'sk-proj-[A-Za-z0-9_-]{20,}'), 'sk-REDACTED_BY_SECURITY_POLICY'),
    (re.compile(r'sk-or-v1-[A-Za-z0-9_-]{20,}'), 'sk-REDACTED_BY_SECURITY_POLICY'),
    (re.compile(r'sk-[A-Za-z0-9_-]{20,}'), 'sk-REDACTED_BY_SECURITY_POLICY'),
    (re.compile(r'gsk_[A-Za-z0-9_-]{20,}'), 'gsk_REDACTED_BY_SECURITY_POLICY'),
    (re.compile(r'seed_[A-Za-z0-9_-]{20,}'), 'seed_REDACTED_BY_SECURITY_POLICY'),
]

IGNORE_DIRS = {
    '.git', 'harvested_repos', 'cloud_backups', 'backups', 
    'clones', 'repos', 'DolaAI-Complete-Cloud-Backup', 'node_modules', '__pycache__'
}

def sanitize():
    sanitized_files = 0
    total_matches = 0
    
    for root, dirs, files in os.walk('C:/Users/antoni/Dola'):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for f in files:
            if f == '.env':
                continue
            
            fp = os.path.join(root, f)
            try:
                with open(fp, 'r', encoding='utf-8', errors='ignore') as fl:
                    content = fl.read()
                
                new_content = content
                file_matches = 0
                for pattern, replacement in PATTERNS:
                    matches = pattern.findall(new_content)
                    if matches:
                        file_matches += len(matches)
                        new_content = pattern.sub(replacement, new_content)
                
                if file_matches > 0:
                    with open(fp, 'w', encoding='utf-8') as fl:
                        fl.write(new_content)
                    print(f"[SANITIZED] {fp} ({file_matches} secrets replaced)", flush=True)
                    sanitized_files += 1
                    total_matches += file_matches
            except Exception as e:
                print(f"[SKIP] {fp}: {e}", flush=True)
                
    print(f"\n[SUMMARY] Successfully sanitized {total_matches} secrets across {sanitized_files} files.", flush=True)

if __name__ == '__main__':
    sanitize()
