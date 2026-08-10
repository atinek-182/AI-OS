#!/usr/bin/env python3
"""
ZORIXEL AIOS WorkMon Sensor Daemon (scripts/workmon_sensor.py)
Non-intrusive monitoring sensor for WorkMon Workflows 1 & 2.
Polls system PIDs, tracks log file modification timestamps (mtime velocity),
scans for critical error keywords, executes smart auto-mitigation,
and transmits telemetry payloads to n8n main hub with local JSON fallback.

Features:
- ANSI Colorized Terminal Reporting
- Defensive Windows File Lock Retries (PermissionError handling)
- Webhook Alert Cooldown Rate-Limiter (60s suppression window per task)
- Automatic Log Retention Cleanup (> 7 days)
"""

import os
import sys
import time
import json
import re
import subprocess
import urllib.request
import urllib.error
from datetime import datetime

# UTF-8 Encoding Safeguard for Windows OS
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ANSI Color Codes for Scannable Console Output
CLR_RESET = "\033[0m"
CLR_GREEN = "\033[92m"
CLR_RED = "\033[91m"
CLR_YELLOW = "\033[93m"
CLR_CYAN = "\033[96m"

N8N_WEBHOOK_URL = os.environ.get("N8N_WORKMON_WEBHOOK", "http://localhost:5678/webhook/workmon-telemetry")
FALLBACK_LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "scratch", "workmon_fallback.json")
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".system_generated", "tasks")

ERROR_KEYWORDS = [
    r"Traceback \(most recent call last\):",
    r"Fatal error",
    r"WinError \d+",
    r"TimeoutError",
    r"403 Forbidden",
    r"invalid_grant",
    r"RateLimitError",
    r"UnhandledPromiseRejectionWarning",
    r"ERR_FAILED"
]

# Webhook Cooldown Tracker {task_id: timestamp}
_LAST_ALERT_TIME = {}
COOLDOWN_SECONDS = 60

def check_pid_active(pid):
    """Check if process ID is running on Windows/Unix."""
    if not pid:
        return False
    try:
        if os.name == 'nt':
            output = subprocess.check_output(f"tasklist /FI \"PID eq {pid}\"", shell=True, text=True)
            return str(pid) in output
        else:
            os.kill(pid, 0)
            return True
    except Exception:
        return False

def scan_log_for_errors(file_path, retries=3, delay=0.1):
    """Scans log file for critical error regex signatures with defensive Windows file-lock retry."""
    if not os.path.exists(file_path):
        return []
    
    found_errors = []
    content = ""
    
    # Defensive File Lock Retry Loop
    for attempt in range(retries):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            break
        except PermissionError:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                return [f"File Lock Timeout (PermissionError): {os.path.basename(file_path)}"]
        except Exception as e:
            return [f"Log Read Error: {str(e)}"]

    if content:
        for pattern in ERROR_KEYWORDS:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                found_errors.append(matches[0])
                
    return found_errors

def is_alert_rate_limited(task_id):
    """Suppresses duplicate webhooks for the same task ID within COOLDOWN_SECONDS window."""
    now = time.time()
    last_time = _LAST_ALERT_TIME.get(task_id, 0)
    if now - last_time < COOLDOWN_SECONDS:
        return True
    _LAST_ALERT_TIME[task_id] = now
    return False

def send_telemetry_to_n8n(payload):
    """Posts telemetry payload to n8n webhook with rate-limiting and local JSON fallback."""
    task_id = payload.get("task_id", "default")
    
    # Rate limit check for warning/error alerts
    if payload.get("status") in ["FAILED", "STALLED", "CRASHED"] and is_alert_rate_limited(task_id):
        print(f"{CLR_YELLOW}[COOLDOWN]{CLR_RESET} Alert suppressed for task {task_id} (within {COOLDOWN_SECONDS}s window)")
        return False

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        N8N_WEBHOOK_URL,
        data=data,
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status == 200:
                print(f"{CLR_GREEN}[OK]{CLR_RESET} Telemetry posted to n8n hub: Task {task_id}")
                return True
    except Exception as e:
        print(f"{CLR_YELLOW}[WARN]{CLR_RESET} n8n Webhook offline ({e}). Saving to local fallback log.")
    
    # Local Fallback Log
    os.makedirs(os.path.dirname(FALLBACK_LOG_PATH), exist_ok=True)
    try:
        fallback_data = []
        if os.path.exists(FALLBACK_LOG_PATH):
            with open(FALLBACK_LOG_PATH, 'r', encoding='utf-8') as f:
                fallback_data = json.load(f)
        fallback_data.append(payload)
        with open(FALLBACK_LOG_PATH, 'w', encoding='utf-8') as f:
            json.dump(fallback_data, f, indent=2)
        print(f"{CLR_CYAN}[INFO]{CLR_RESET} Saved fallback event to {FALLBACK_LOG_PATH}")
    except Exception as err:
        print(f"{CLR_RED}[ERROR]{CLR_RESET} Failed writing fallback log: {err}")
    return False

def run_auth_recovery():
    """Runs aios_gws_health_check.py script to handle OAuth token refreshes."""
    script_path = os.path.join(os.path.dirname(__file__), "aios_gws_health_check.py")
    if os.path.exists(script_path):
        print(f"{CLR_CYAN}[INFO]{CLR_RESET} Launching automated GWS auth recovery check...")
        subprocess.run([sys.executable, script_path], check=False)

def cleanup_old_task_logs(retention_days=7):
    """Prunes task log files older than retention_days to prevent disk bloat."""
    if not os.path.exists(LOG_DIR):
        return
    now = time.time()
    max_age = retention_days * 86400
    pruned_count = 0
    
    for f in os.listdir(LOG_DIR):
        if f.endswith(".log"):
            file_path = os.path.join(LOG_DIR, f)
            try:
                if now - os.path.getmtime(file_path) > max_age:
                    os.remove(file_path)
                    pruned_count += 1
            except Exception:
                pass
    if pruned_count > 0:
        print(f"{CLR_CYAN}[CLEANUP]{CLR_RESET} Pruned {pruned_count} log files older than {retention_days} days.")

def inspect_task(task_id, pid=None, log_file=None, max_idle_seconds=180):
    """Inspects a single task for health, stalls, and error signatures."""
    timestamp = datetime.now().isoformat()
    status = "RUNNING"
    error_list = []
    
    # 1. PID Check
    pid_active = check_pid_active(pid) if pid else None
    
    # 2. Log File Telemetry & Idle Check
    idle_seconds = 0
    if log_file and os.path.exists(log_file):
        mtime = os.path.getmtime(log_file)
        idle_seconds = time.time() - mtime
        error_list = scan_log_for_errors(log_file)
    
    # 3. Status Decision Matrix
    if error_list:
        status = "FAILED"
        if any("invalid_grant" in err.lower() or "403" in err for err in error_list):
            run_auth_recovery()
    elif pid and not pid_active:
        status = "CRASHED"
    elif idle_seconds > max_idle_seconds:
        status = "STALLED"
    else:
        status = "HEALTHY"
    
    payload = {
        "task_id": task_id,
        "workflow_source": "WorkMon Workflow 2",
        "status": status,
        "pid": pid,
        "pid_active": pid_active,
        "idle_seconds": round(idle_seconds, 1),
        "errors": error_list,
        "timestamp": timestamp,
        "host": os.environ.get("COMPUTERNAME", "AIOS-Host")
    }
    
    send_telemetry_to_n8n(payload)
    return payload

def main():
    cleanup_old_task_logs(retention_days=7)
    
    if "--test-run" in sys.argv:
        print("=== WorkMon Sensor Test Run ===")
        res = inspect_task("test_task_001", pid=os.getpid(), log_file=None)
        status_color = CLR_GREEN if res['status'] == "HEALTHY" else CLR_RED
        print(f"{status_color}[OK] Inspection Test Result: {res['status']}{CLR_RESET}")
        return 0

    print("Starting WorkMon Sensor Daemon...")
    if os.path.exists(LOG_DIR):
        for f in os.listdir(LOG_DIR):
            if f.endswith(".log"):
                task_id = f.replace(".log", "")
                log_path = os.path.join(LOG_DIR, f)
                inspect_task(task_id, log_file=log_path)
    else:
        print(f"{CLR_CYAN}[INFO]{CLR_RESET} Task log directory {LOG_DIR} not present yet.")

if __name__ == "__main__":
    main()
