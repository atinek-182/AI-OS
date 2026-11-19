import shutil
import os

print("Python Playwright import test...")
try:
    import playwright
    print("[SUCCESS] Python playwright module is available!")
except ImportError:
    print("[INFO] Python playwright module not installed.")

print("Checking global npm node_modules...")
global_npm = r"C:\Users\HP\AppData\Roaming\npm\node_modules"
if os.path.exists(global_npm):
    print("Found global npm packages:", os.listdir(global_npm))

print("Checking root AI-OS node_modules...")
aios_npm = r"d:\AI-OS\node_modules"
if os.path.exists(aios_npm):
    print("Found aios node_modules:", os.listdir(aios_npm)[:10])
