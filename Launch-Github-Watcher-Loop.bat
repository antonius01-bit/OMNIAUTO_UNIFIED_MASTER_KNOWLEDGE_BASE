@echo off
title GITHUB PROFILE WATCHER ^& SELF-IMPROVEMENT LOOP
color 0B
echo ===============================================================================
echo        🛰️ GITHUB PROFILE WATCHER ^& RECURSIVE RE-LEARNER (173 AUTHORS)
echo ===============================================================================
echo Target Profile Format: https://github.com/{username}?tab=repositories
echo Tracked Profiles: 173 Users/Orgs in C:\Users\antoni\Dola\tracked_github_profiles.json
echo Vault Nodes: 14_AUTONOMOUS_LOOPS, 15_HARVESTED_PROFILES, 16_META_LEARNING
echo ===============================================================================
echo [1] Quick Scan (Top 20 Repositories)
echo [2] Full Check (All 173 Profiles - Remote Commit Audit)
echo [3] Dry-Run Scan (Check without pulling)
echo [4] Check Specific User (Enter username)
echo [5] Exit
echo ===============================================================================
set /p opt="Pilih opsi [1-5]: "

if "%opt%"=="1" (
    python C:\Users\antoni\Dola\scripts\github_profile_watcher_loop.py --quick-scan 20
    goto end
)
if "%opt%"=="2" (
    python C:\Users\antoni\Dola\scripts\github_profile_watcher_loop.py --check-all
    goto end
)
if "%opt%"=="3" (
    python C:\Users\antoni\Dola\scripts\github_profile_watcher_loop.py --quick-scan 20 --dry-run
    goto end
)
if "%opt%"=="4" (
    set /p usr="Masukkan GitHub username: "
    python C:\Users\antoni\Dola\scripts\github_profile_watcher_loop.py --user %usr%
    goto end
)
if "%opt%"=="5" (
    exit /b 0
)

:end
echo.
echo [✓] Watcher task completed. Cek hasil di C:\Users\antoni\Dola\obsidian_vault\16_META_LEARNING\SELF_IMPROVEMENT_RUNLOG.md
pause
