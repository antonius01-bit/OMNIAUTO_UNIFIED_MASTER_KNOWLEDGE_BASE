@echo off
chcp 65001 >nul
title STARK INDUSTRIES -- QUANTUM RUNTIME SUPERVISOR (PORT 5050)
color 0B
cd /d "C:\Users\antoni\Dola"

echo.
echo ================================================================================
echo      STARK INDUSTRIES -- QUANTUM NEURAL AGENT MESH v5.0
echo ================================================================================
echo [*] Memulai Stark Runtime Supervisor di Port 5050...
echo.

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Users\antoni\Dola\stark_supervisor.ps1"

if %errorlevel% neq 0 (
    echo.
    echo ================================================================================
    echo [!] Terjadi kendala saat menjalankan Stark Supervisor.
    echo ================================================================================
    pause
)
