@echo off
set "OBSIDIAN_EXE=C:\Program Files\Obsidian\Obsidian.exe"
if not exist "%OBSIDIAN_EXE%" (
    if exist "%LOCALAPPDATA%\Obsidian\Obsidian.exe" (
        set "OBSIDIAN_EXE=%LOCALAPPDATA%\Obsidian\Obsidian.exe"
    )
)

if not exist "%OBSIDIAN_EXE%" (
    echo [!] Error: Obsidian.exe not found at %OBSIDIAN_EXE%
    pause
    exit
)

start /high "" "%OBSIDIAN_EXE%" --js-flags="--max-old-space-size=4096" --disable-features=CalculateNativeWinOcclusion,IntensiveWakeUpThrottling
exit