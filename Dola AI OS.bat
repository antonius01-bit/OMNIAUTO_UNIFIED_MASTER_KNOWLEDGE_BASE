@echo off
chcp 65001 >nul
title "DOLA AI - Cosmic Workflow and Interactive Omni-Auto OS v4.0"
color 0D

echo.
echo     ╔════════════════════════════════════════════════════════════════╗
echo     ║                                                                ║
echo     ║        ◈  DOLA AI — COSMIC WORKFLOW SYSTEM v4.0  ◈            ║
echo     ║                                                                ║
echo     ║        Multi-AI Integration · Omni-Auto Interactive OS         ║
echo     ║        158 Super-Skills · 352 Providers · 204 Vault Notes      ║
echo     ║                                                                ║
echo     ╚════════════════════════════════════════════════════════════════╝
echo.
echo     [AI NODES] Gemini ◆ GPT ◆ Claude ◆ Obsidian ◆ AGY ◆ Kimi ◆ DeepSeek
echo     [INTELLIGENCE] Interactive Omni-Auto Chat · Automated Agent Routing
echo     [ACADEMIC] Antonius Wijayanata MM Thesis Hub · SEM-PLS · Mendeley RIS
echo.
echo     ────────────────────────────────────────────────────────────────
echo.
echo     Membuka DOLA AI Interactive Cosmic Cockpit di browser default...
echo.

set "TARGET_HTML="

REM 1. Check OneDrive Desktop
if exist "%USERPROFILE%\OneDrive\Desktop\DolaAI-Cosmic-Workflow.html" (
    set "TARGET_HTML=%USERPROFILE%\OneDrive\Desktop\DolaAI-Cosmic-Workflow.html"
)

REM 2. Check Local Desktop
if "%TARGET_HTML%"=="" if exist "%USERPROFILE%\Desktop\DolaAI-Cosmic-Workflow.html" (
    set "TARGET_HTML=%USERPROFILE%\Desktop\DolaAI-Cosmic-Workflow.html"
)

REM 3. Check Current Directory
if "%TARGET_HTML%"=="" if exist "%~dp0DolaAI-Cosmic-Workflow.html" (
    set "TARGET_HTML=%~dp0DolaAI-Cosmic-Workflow.html"
)

REM 4. Check Dola Workspace
if "%TARGET_HTML%"=="" if exist "C:\Users\antoni\Dola\dola_ai_enterprise_os.html" (
    set "TARGET_HTML=C:\Users\antoni\Dola\dola_ai_enterprise_os.html"
)

if not "%TARGET_HTML%"=="" (
    echo     [✓] Ditemukan: %TARGET_HTML%
    start "" "%TARGET_HTML%"
    echo.
    echo     [✓] DOLA AI System berhasil dibuka!
    ping 127.0.0.1 -n 2 >nul
    exit /b 0
) else (
    echo     [ERROR] Tidak dapat menemukan file HTML Dola AI.
    echo     Mencari di C:\Users\antoni\OneDrive\Desktop\DolaAI-Cosmic-Workflow.html
    pause
    exit /b 1
)
