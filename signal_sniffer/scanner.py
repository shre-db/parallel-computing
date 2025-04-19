import time
import random
from radio_systems import telescope


def scan_stream(telescope_id, results, lock):
    time.sleep(random.uniform(0.5, 2.0))
    stream = telescope(with_pattern=random.choice([True, False, False]))

    print(f"📡 [Telescope - {telescope_id}] Scanning Stream...")
    if "... --- ..." in stream:
        with lock:
            results.append((telescope_id, "Signal Detected 📶"))
    else:
        with lock:
            results.append((telescope_id, "No Signal"))