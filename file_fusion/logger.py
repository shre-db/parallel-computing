import random
import os
from datetime import datetime, timedelta

def log_activity():
    base_time = datetime(2023, 4, 19, 14, 0, 0)
    logs = []
    for _ in range(random.randint(50, 100)):
        offset = timedelta(seconds=random.randint(0, 3600), milliseconds=random.randint(0, 999))
        timestamp = (base_time + offset).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        level = random.choice(["INFO", "WARN", "ERROR"])
        msg = random.choice([
            "User logged in", "File accessed", "Connection failed",
            "Sensor ping", "System reboot", "Unauthorized attempt"
        ])
        logs.append(f"{timestamp} [{level}] {msg}")
    logs.sort()  # Sorted within each file
    return logs

def create_log_files(folder="logs", count=1000):
    os.makedirs(folder, exist_ok=True)
    for i in range(count):
        with open(os.path.join(folder, f"log_{i}.log"), 'w') as f:
            f.write("\n".join(log_activity()))


if __name__ == "__main__":
    create_log_files()