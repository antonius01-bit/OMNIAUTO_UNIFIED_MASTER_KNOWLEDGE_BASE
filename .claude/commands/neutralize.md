# /neutralize — AI Footprint & Cliché Neutralizer

Execute the Python AI Detection Neutralizer on the specified target file or active note:
1. Scan for the 29 FK-17 AI clichés (`delve`, `testament`, `pivotal`, `tapestry`, `realm`, etc.).
2. Calculate sentence length standard deviation (target burstiness > 10.0 words).
3. Rewrite uniform sentences to introduce natural human syntactic rhythm.
4. Verify APA 7th Edition citations `(Author, Year)`.

Command execution:
```powershell
python C:\Users\antoni\Dola\obsidian_vault\scripts\ai_detection_neutralizer.py --file "$ARGUMENTS"
# For dry-run audit only:
# python C:\Users\antoni\Dola\obsidian_vault\scripts\ai_detection_neutralizer.py --file "$ARGUMENTS" --audit
# For test diagnostic:
# python C:\Users\antoni\Dola\obsidian_vault\scripts\ai_detection_neutralizer.py --test
```

