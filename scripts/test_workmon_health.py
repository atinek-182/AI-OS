#!/usr/bin/env python3
"""
ZORIXEL AIOS WorkMon Pre-Flight Health Script (scripts/test_workmon_health.py)
Validates that workmon_sensor.py, workmon_auto_evolver.py, and n8n master hub JSON
exist, execute cleanly, and pass zero-cost boundary checks.
"""

import os
import sys
import subprocess

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(__file__))

def check_file(rel_path):
    full_path = os.path.join(WORKSPACE_ROOT, rel_path)
    exists = os.path.exists(full_path)
    tag = "[OK]" if exists else "[ERROR]"
    print(f"{tag} File {rel_path}: {'EXISTS' if exists else 'MISSING'}")
    return exists

def main():
    print("========================================================")
    print("ZORIXEL AIOS: WorkMon Pre-Flight Health Validator")
    print("========================================================")
    
    files_ok = all([
        check_file("scripts/workmon_sensor.py"),
        check_file("scripts/workmon_auto_evolver.py"),
        check_file("n8n/workflows/workmon_master_hub.json"),
        check_file("docs/specs/SPEC-workmon-master.md")
    ])
    
    if not files_ok:
        print("[ERROR] WorkMon components missing!")
        sys.exit(1)
        
    # Run test mode on sensor
    sensor_res = subprocess.run([sys.executable, "scripts/workmon_sensor.py", "--test-run"], cwd=WORKSPACE_ROOT, capture_output=True, text=True)
    if sensor_res.returncode == 0:
        print("[OK] workmon_sensor.py test run PASSED")
    else:
        print(f"[ERROR] workmon_sensor.py failed: {sensor_res.stderr}")
        sys.exit(1)
        
    # Run test mode on auto-evolver
    evolver_res = subprocess.run([sys.executable, "scripts/workmon_auto_evolver.py", "--test-run"], cwd=WORKSPACE_ROOT, capture_output=True, text=True)
    if evolver_res.returncode == 0:
        print("[OK] workmon_auto_evolver.py test run PASSED")
    else:
        print(f"[ERROR] workmon_auto_evolver.py failed: {evolver_res.stderr}")
        sys.exit(1)

    print("========================================================")
    print("[SUCCESS] All WorkMon Pre-Flight Health Checks Passed!")
    print("========================================================")

if __name__ == "__main__":
    main()
