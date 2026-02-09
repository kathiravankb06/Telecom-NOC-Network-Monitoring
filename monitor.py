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

# ==========================================
# DEVICE LIST
# ==========================================
devices = [
    ("8.8.8.8", "Core"),
    ("1.1.1.1", "Backhaul"),
    ("10.100.152.21", "Aggregation")
]

# ==========================================
# STATUS + COUNTERS
# ==========================================
last_status = {name: "UNKNOWN" for _, name in devices}
failure_count = {name: 0 for _, name in devices}
success_count = {name: 0 for _, name in devices}

THRESHOLD = 2        # Faster detection
POLL_INTERVAL = 2   # Seconds

print("Telecom NOC Monitoring Started")

# ==========================================
# MONITOR LOOP
# ==========================================
while True:
    for ip, name in devices:

        try:
            response = ping(ip, timeout=1)
            is_up = response is not None
        except Exception:
            is_up = False

        # Update counters
        if is_up:
            success_count[name] += 1
            failure_count[name] = 0
        else:
            failure_count[name] += 1
            success_count[name] = 0

        # DOWN detection
        if failure_count[name] >= THRESHOLD and last_status[name] != "DOWN":

            last_status[name] = "DOWN"
            now = datetime.now().strftime("%H:%M:%S")
            message = f"{name} changed to DOWN at {now}"

            print(message)

            with open("log.txt", "a") as log:
                log.write(f"{name},DOWN,{now}\n")

        # UP detection
        if success_count[name] >= THRESHOLD and last_status[name] != "UP":

            last_status[name] = "UP"
            now = datetime.now().strftime("%H:%M:%S")
            message = f"{name} changed to UP at {now}"

            print(message)

            with open("log.txt", "a") as log:
                log.write(f"{name},UP,{now}\n")

    time.sleep(POLL_INTERVAL)
