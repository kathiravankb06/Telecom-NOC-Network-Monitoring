"""
Telecom NOC Network Monitoring & Backhaul Link Failure Analysis

This script simulates real-time telecom NOC monitoring by checking
reachability of Core, Aggregation, and Backhaul network links.

Features:
- Real-time monitoring loop
- Threshold-based failure detection
- UP/DOWN state change logging
- Timestamp recording
- Link flapping prevention
"""

import time
from datetime import datetime
from ping3 import ping


# ============================================================
# DEVICE CONFIGURATION (Modify IPs as needed)
# ============================================================

devices = [
    ("8.8.8.8", "Core"),             # Represents upstream core connectivity
    ("1.1.1.1", "Backhaul"),         # Represents transport/backhaul path
    ("10.100.152.21", "Aggregation")  # Represents local aggregation/gateway
]


# ============================================================
# MONITORING PARAMETERS
# ============================================================

CHECK_INTERVAL = 5     # Seconds between checks
THRESHOLD = 3          # Consecutive checks required for state change
LOG_FILE = "log.txt"  # Log output file


# ============================================================
# STATUS TRACKING STRUCTURES
# ============================================================

last_status = {name: "UNKNOWN" for _, name in devices}
failure_count = {name: 0 for _, name in devices}
success_count = {name: 0 for _, name in devices}


# ============================================================
# LOGGING FUNCTION
# ============================================================

def log_event(device_name, status, timestamp):
    """Writes monitoring events to log file."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{device_name},{status},{timestamp}\n")


# ============================================================
# MONITORING FUNCTION
# ============================================================

def monitor_devices():
    """Continuously monitors configured telecom network devices."""

    print("Telecom NOC Monitoring Started\n")

    while True:

        for ip, name in devices:

            # ------------------------------------------------
            # ICMP Reachability Check
            # ------------------------------------------------
            try:
                response = ping(ip, timeout=2)
                is_up = response is not None
            except Exception:
                is_up = False

            # ------------------------------------------------
            # Update Success / Failure Counters
            # ------------------------------------------------
            if is_up:
                success_count[name] += 1
                failure_count[name] = 0
            else:
                failure_count[name] += 1
                success_count[name] = 0

            # ------------------------------------------------
            # DOWN Detection Logic
            # ------------------------------------------------
            if failure_count[name] >= THRESHOLD and last_status[name] != "DOWN":

                last_status[name] = "DOWN"
                now = datetime.now().strftime("%H:%M:%S")
                message = f"{name} changed to DOWN at {now}"

                print(message)
                log_event(name, "DOWN", now)

            # ------------------------------------------------
            # UP Detection Logic
            # ------------------------------------------------
            if success_count[name] >= THRESHOLD and last_status[name] != "UP":

                last_status[name] = "UP"
                now = datetime.now().strftime("%H:%M:%S")
                message = f"{name} changed to UP at {now}"

                print(message)
                log_event(name, "UP", now)

        # ----------------------------------------------------
        # Wait before next monitoring cycle
        # ----------------------------------------------------
        time.sleep(CHECK_INTERVAL)


# ============================================================
# MAIN ENTRY POINT
# ============================================================

if __name__ == "__main__":
    monitor_devices()
