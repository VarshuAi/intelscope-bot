import os
import sys
import subprocess
import shutil

def run_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end="")
        process.wait()
        return process.returncode == 0
    except Exception as e:
        print(f"Error running command: {e}")
        return False

def setup_and_build():
    print("=" * 60)
    print("      IntelScope OSINT Bot - Code Obfuscation Tool       ")
    print("=" * 60)
    
    # 1. Ask user which tool they want to use
    print("\nSelect compilation mode:")
    print(" [1] PyArmor Obfuscation (Generates encrypted scripts - runs with Python)")
    print(" [2] PyInstaller Compilation (Generates a standalone executable binary)")
    
    choice = input("\nEnter choice (1 or 2, default is 1): ").strip()
    if choice not in ["1", "2"]:
        choice = "1"
        
    # Clean previous builds
    for dir_name in ["dist", "build"]:
        if os.path.exists(dir_name):
            print(f"Cleaning existing {dir_name} directory...")
            shutil.rmtree(dir_name)

    if choice == "1":
        print("\n[+] Setting up PyArmor...")
        if not run_command("pip install pyarmor"):
            print("[-] Failed to install PyArmor. Make sure pip is available.")
            return
            
        print("\n[+] Obfuscating bot codebase recursively...")
        # Obfuscates bot.py and recursively processes submodules under recon/
        success = run_command("pyarmor gen -O dist -r bot.py recon/")
        
        if success:
            print("\n" + "=" * 60)
            print("Success! Obfuscation complete.")
            print("Output files are in: dist/")
            print("To run the obfuscated bot: python dist/bot.py")
            print("Note: Keep the 'dist/pyarmor_runtime_xxxxxx' folder with 'bot.py'")
            print("=" * 60)
        else:
            print("\n[-] Obfuscation failed. Check PyArmor console logs above.")
            
    else:
        print("\n[+] Setting up PyInstaller...")
        if not run_command("pip install pyinstaller"):
            print("[-] Failed to install PyInstaller.")
            return
            
        print("\n[+] Compiling bot into a single executable binary...")
        # Compiles bot.py into a single executable, importing modules and assets
        success = run_command("pyinstaller --onefile bot.py")
        
        if success:
            print("\n" + "=" * 60)
            print("Success! Compilation complete.")
            print("Output binary is at: dist/bot.exe")
            print("Simply share 'dist/bot.exe' with users.")
            print("=" * 60)
        else:
            print("\n[-] PyInstaller build failed. Check logs above.")

if __name__ == "__main__":
    setup_and_build()
