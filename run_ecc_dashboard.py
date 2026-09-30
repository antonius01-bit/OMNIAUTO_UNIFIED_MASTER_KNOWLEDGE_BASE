import os
import subprocess
import sys

ECC_DIR = r"C:\Users\antoni\Dola\clones\ECC"

def main():
    dashboard_script = os.path.join(ECC_DIR, "ecc_dashboard.py")
    if not os.path.exists(dashboard_script):
        print(f"Error: {dashboard_script} not found")
        sys.exit(1)
        
    print("="*60)
    print(" Everything Claude Code (ECC) Dashboard Launcher")
    print(f" ECC Directory: {ECC_DIR}")
    print(" Launching 68 Agents & 292 Skills Management Console...")
    print("="*60)
    
    cmd = [sys.executable, dashboard_script]
    subprocess.run(cmd, cwd=ECC_DIR)

if __name__ == "__main__":
    main()
