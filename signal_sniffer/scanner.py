import time
import random
from radio_systems import telescope


def scan_stream(telescope_id):
    time.sleep(random.uniform(0.5, 2.0))
    stream = telescope(with_pattern=random.choice([True, False, False]))
    print(f"📡 [Telescope - {telescope_id}] Scanning Stream...")

    if "... --- ..." in stream:
        return telescope_id, "Signal Detected 📶"
    else:
        return telescope_id, "No Signal"
    