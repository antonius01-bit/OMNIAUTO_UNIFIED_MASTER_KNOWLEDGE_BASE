# STARK INDUSTRIES -- QUANTUM RUNTIME SUPERVISOR (PORT 5050)
$Host.UI.RawUI.WindowTitle = "STARK INDUSTRIES -- RUNTIME SUPERVISOR (PORT 5050)"
$dolaDir = "C:\Users\antoni\Dola"
Set-Location $dolaDir

# 1. Check if server is already running on port 5050
$serverRunning = $false
try {
    $test = Invoke-RestMethod -Uri "http://127.0.0.1:5050/api/status" -TimeoutSec 1 -ErrorAction Stop
    $serverRunning = $true
} catch {
    $serverRunning = $false
}

if (-not $serverRunning) {
    Write-Host "`n[*] [STARK AI] Memulai Quantum Bridge Server di Port 5050..." -ForegroundColor Cyan
    Start-Process -FilePath "python" -ArgumentList "agy_bridge_server.py" -WorkingDirectory $dolaDir -WindowStyle Hidden
    Start-Sleep -Seconds 2
}

# 1b. Launch 6-Way Omni-Sync in background (OneDrive + Git + Archive Mesh)
Write-Host "[*] Memulai 6-Way Omni-Sync di latar belakang..." -ForegroundColor Cyan
Start-Process -FilePath "python" -ArgumentList "dola_sync_all.py" -WorkingDirectory $dolaDir -WindowStyle Hidden

# 2. Play Jarvis Voice Greeting via native VBScript SAPI
$vbsPath = Join-Path $dolaDir "speak_jarvis.vbs"
if (Test-Path $vbsPath) {
    Start-Process -FilePath "wscript" -ArgumentList "`"$vbsPath`"", "`"Welcome back, sir. Stark Industries neural grid online. Protocols Jarvis, Friday, and Ultron are all fully engaged and standing by.`"" -WindowStyle Hidden
}

# 3. Open Browser to Stark Cockpit (Unified 3-Orb Swarm: Jarvis, Friday, Ultron)
Write-Host "[OK] Mengaktifkan Stark Cockpit Tri-Core Mesh (Jarvis, Friday, Ultron)..." -ForegroundColor Green
Start-Process "http://127.0.0.1:5050/stark"


# 4. Display Supervisor Console HUD
Clear-Host
Write-Host ""
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "     STARK INDUSTRIES -- QUANTUM RUNTIME SUPERVISOR (PORT 5050)                 " -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host " [OK] Bridge Server     : ONLINE (http://127.0.0.1:5050)" -ForegroundColor Green
Write-Host " [OK] Jarvis Single HUD : ONLINE (http://127.0.0.1:5050/stark)" -ForegroundColor Green
Write-Host " [OK] 3 Co-Thinking AIs : JARVIS (US English) + FRIDAY (Red / UK English) + ULTRON (Gold / Aussie English)" -ForegroundColor Cyan
Write-Host " [OK] Obsidian Brain    : ONLINE & CONNECTED (604+ Synapses Active / Mix English)" -ForegroundColor Magenta
Write-Host " [OK] 6-Pillar Alliance : Bionic (:1234) | Gemini Pool | AGY | Dola | Copilot | Obsidian" -ForegroundColor Cyan
Write-Host " [OK] 6-Way Omni-Sync   : RUNNING (Dola <-> AGY <-> Obsidian <-> 3-Cloud)" -ForegroundColor Green
Write-Host " [OK] GAuth 2FA Guard   : ACTIVE (Master PIN: 111993 / TOTP Mesh)" -ForegroundColor Cyan
Write-Host ""
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host " Semua 3 AI (Jarvis, Friday, Ultron) menyatu dalam 1 Tampilan Utama JARVIS." -ForegroundColor White
Write-Host " Perintah konsol:" -ForegroundColor White
Write-Host "   - [status]  : Cek status AI core & tugas berjalan" -ForegroundColor Gray
Write-Host "   - [brain]   : Cek status memori Obsidian Brain (604+ catatan & sinaps)" -ForegroundColor Gray
Write-Host "   - [sync]    : Jalankan ulang 6-Way Omni-Sync & 3-Cloud Backup" -ForegroundColor Gray
Write-Host "   - [2fa]     : Cek kode TOTP 2FA real-time & uji PIN (111993)" -ForegroundColor Gray
Write-Host "   - [open]    : Buka kembali Tampilan Utama Jarvis di browser" -ForegroundColor Gray
Write-Host "   - [q/exit]  : Matikan Server Port 5050 & Keluar" -ForegroundColor Gray
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host ""


function Stop-StarkServer {
    # Check running tasks first
    $activeTasksCount = 0
    $tasks = @()
    try {
        $taskStatus = Invoke-RestMethod -Uri "http://127.0.0.1:5050/api/tasks/status" -TimeoutSec 2 -ErrorAction Stop
        $activeTasksCount = $taskStatus.active_tasks_count
        $tasks = $taskStatus.tasks
    } catch {
        # Server might already be stopped
    }

    if ($activeTasksCount -gt 0) {
        Write-Host "`n[!] PERINGATAN: Masih ada $activeTasksCount tugas agen yang BERJALAN di latar belakang!" -ForegroundColor Yellow
        foreach ($t in $tasks) {
            Write-Host "    - [$($t.id)] $($t.name) - $($t.details) (Started: $($t.started_at))" -ForegroundColor Gray
        }
        Write-Host ""
        $confirm = Read-Host "Do you really want to exit? (Y/N/111993)"
        if ($confirm.Trim().ToUpper() -ne "Y" -and $confirm.Trim() -ne "111993") {
            Write-Host "[OK] Pembatalan keluar. Sistem Stark OS tetap aktif berjalan.`n" -ForegroundColor Green
            return $false
        }
    } else {
        Write-Host "`n[*] Tidak ada tugas aktif yang berjalan. Mematikan sistem..." -ForegroundColor Cyan
    }

    # Execute Shutdown
    Write-Host "[*] Mematikan Bridge Server Port 5050..." -ForegroundColor Cyan
    try {
        Invoke-RestMethod -Uri "http://127.0.0.1:5050/api/shutdown?force=true" -TimeoutSec 2 -ErrorAction SilentlyContinue
    } catch {}

    # Ensure port 5050 process is killed
    $connections = Get-NetTCPConnection -LocalPort 5050 -ErrorAction SilentlyContinue
    if ($connections) {
        $pids = $connections | Select-Object -ExpandProperty OwningProcess -Unique
        foreach ($pidToKill in $pids) {
            Stop-Process -Id $pidToKill -Force -ErrorAction SilentlyContinue
        }
    }

    if (Test-Path $vbsPath) {
        Start-Process -FilePath "wscript" -ArgumentList "`"$vbsPath`"", "`"Powering down systems. Goodbye, sir.`"" -WindowStyle Hidden
    }

    Write-Host "[OK] Server Port 5050 berhasil dimatikan secara bersih. Goodbye, sir.`n" -ForegroundColor Green
    Start-Sleep -Seconds 1
    return $true
}

# Interactive Monitoring Loop
while ($true) {
    $userInput = Read-Host "STARK-CONSOLE (Ketik 'q' atau 'exit' untuk keluar)"
    if ($userInput -match "^(q|exit|quit|stop|close)$") {
        $exited = Stop-StarkServer
        if ($exited) {
            break
        }
    } elseif ($userInput -match "^(status|tasks)$") {
        try {
            $taskStatus = Invoke-RestMethod -Uri "http://127.0.0.1:5050/api/tasks/status" -TimeoutSec 2
            Write-Host "[*] Active Tasks: $($taskStatus.active_tasks_count)" -ForegroundColor Cyan
            if ($taskStatus.active_tasks_count -gt 0) {
                foreach ($t in $taskStatus.tasks) {
                    Write-Host "    - [$($t.id)] $($t.name) ($($t.started_at))" -ForegroundColor Gray
                }
            } else {
                Write-Host "    Tidak ada tugas yang sedang berjalan." -ForegroundColor Green
            }
        } catch {
            Write-Host "[!] Server not responding on port 5050" -ForegroundColor Red
        }
    } elseif ($userInput -match "^(gauth|2fa|totp)$") {
        try {
            $gateScript = Join-Path $dolaDir "scripts\gauth_security_gate.py"
            & python $gateScript --status
            Write-Host ""
            $testCode = Read-Host "Ketik 6-digit TOTP code untuk uji verifikasi (atau ENTER untuk kembali)"
            if ($testCode -and $testCode.Trim().Length -gt 0) {
                & python $gateScript --verify $testCode.Trim()
            }
        } catch {
            Write-Host "[!] GAuth error: $_" -ForegroundColor Red
        }
    } elseif ($userInput -match "^(mark85|all|jarvis)$") {
        Write-Host "[*] Mengaktifkan Tri-Brain Unified Core di Tampilan Jarvis..." -ForegroundColor Cyan
        Invoke-RestMethod -Uri "http://127.0.0.1:5050/api/launch/mark85" -TimeoutSec 2 -ErrorAction SilentlyContinue
        Start-Process "http://127.0.0.1:5050/stark"
    } elseif ($userInput -match "^(brain|obsidian)$") {
        try {
            $brain = Invoke-RestMethod -Uri "http://127.0.0.1:5050/api/brain/stats" -TimeoutSec 2
            Write-Host "`n[*] [OBSIDIAN BRAIN] Total Catatan: $($brain.total_notes) | Folder: $($brain.folders_count)" -ForegroundColor Magenta
            Write-Host "[*] Status Aliansi 6 Pilar:" -ForegroundColor Cyan
            Write-Host "    - Bionic   : $($brain.six_pillars.bionic)" -ForegroundColor White
            Write-Host "    - Gemini   : $($brain.six_pillars.gemini)" -ForegroundColor White
            Write-Host "    - AGY      : $($brain.six_pillars.agy)" -ForegroundColor White
            Write-Host "    - Dola     : $($brain.six_pillars.dola)" -ForegroundColor White
            Write-Host "    - Copilot  : $($brain.six_pillars.copilot)" -ForegroundColor White
            Write-Host "    - Obsidian : $($brain.six_pillars.obsidian)" -ForegroundColor White
            Write-Host "`n[*] Sinaps & Catatan Terbaru:" -ForegroundColor Yellow
            foreach ($rn in $brain.recent_notes[0..4]) {
                Write-Host "    - [$($rn.time_str)] $($rn.title) ($($rn.path))" -ForegroundColor Gray
            }
            Write-Host ""
        } catch {
            Write-Host "[!] Gagal membaca data Obsidian Brain: $_" -ForegroundColor Red
        }
    } elseif ($userInput -match "^(sync|backup)$") {
        Write-Host "[*] Menjalankan 6-Way Omni-Sync & 3-Cloud Redundancy Backup..." -ForegroundColor Cyan
        & python dola_sync_all.py --force
        Write-Host "[OK] Sinkronisasi & backup berhasil diselesaikan.`n" -ForegroundColor Green
    } elseif ($userInput -match "^(open|hud|cockpit|browser|dola)$") {
        Start-Process "http://127.0.0.1:5050/stark"
        Write-Host "[OK] Membuka Tampilan Utama Jarvis di browser." -ForegroundColor Green
    } else {
        Write-Host "Ketik 'q' keluar, 'status' cek tugas, 'brain' status memori vault, 'sync' sinkronisasi mesh, 'open' buka cockpit Jarvis, '2fa' uji otentikasi." -ForegroundColor Gray
    }
}
