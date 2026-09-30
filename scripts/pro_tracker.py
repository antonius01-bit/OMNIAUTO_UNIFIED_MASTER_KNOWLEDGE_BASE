import os
import sys
from datetime import datetime

# Enforce UTF-8 output on Windows terminal
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

VAULT_PATH = r"C:\Users\antoni\Dola\obsidian_vault"
LOG_FOLDER = os.path.join(VAULT_PATH, "05_OPERATIONS")
LOG_PATH = os.path.join(LOG_FOLDER, "PRO_MODE_USAGE_LOG.md")

def buat_folder_jika_tidak_ada():
    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)
        print(f"✅ Folder dibuat: {LOG_FOLDER}")

def buat_log_awal():
    buat_folder_jika_tidak_ada()
    konten_awal = """---
tanggal_mulai: 2026-09-30
total_pemakaian: 0
batas_harian: tak_ditetapkan
---

# 📊 PRO Mode — Catatan Pemakaian

| Waktu | Mode | Tugas | Token Dipakai | Sisa Kredit | Catatan |
|---|---|---|---|---|---|
"""
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write(konten_awal)
    print(f"✅ File log dibuat: {LOG_PATH}")

def catat_pemakaian(mode, tugas, token_dipakai=0, sisa_kredit="dipantau", catatan=""):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists(LOG_PATH):
        buat_log_awal()
    baris = f"| {waktu} | {mode} | {tugas} | {token_dipakai} | {sisa_kredit} | {catatan} |\n"
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(baris)
    print(f"✅ Tercatat: [{mode}] {tugas}")

def tampil_status():
    if not os.path.exists(LOG_PATH):
        print("📋 Belum ada catatan pemakaian PRO Mode")
        print("Jalankan tugas /PRO MAX pertama untuk memulai")
        return
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        print(f.read())

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        mode = sys.argv[1]
        tugas = sys.argv[2]
        token = sys.argv[3] if len(sys.argv) > 3 else 0
        sisa = sys.argv[4] if len(sys.argv) > 4 else "dipantau"
        catat_pemakaian(mode, tugas, token, sisa)
    elif len(sys.argv) == 2 and sys.argv[1] == "status":
        tampil_status()
    else:
        print("Penggunaan:")
        print("  python scripts\\pro_tracker.py status          → Cek catatan")
        print("  python scripts\\pro_tracker.py PRO 'Tugas'     → Catat PRO")
        print("  python scripts\\pro_tracker.py FAST 'Tugas'   → Catat FAST")