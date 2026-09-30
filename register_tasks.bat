@echo off
echo [*] Registering Daily 3:00 AM /SYNC ALL Task in Windows Task Scheduler...
schtasks /create /tn "DolaSyncAll" /tr "python C:\Users\antoni\Dola\dola_sync_all.py" /sc daily /st 03:00 /f

echo [*] Registering Daily 10:00 PM Night-Shift Autonomous Learning Task...
schtasks /create /tn "DolaNightShift" /tr "python C:\Users\antoni\Dola\dola_nightshift.py" /sc daily /st 22:00 /f

echo [✓] Both automated tasks registered successfully!
