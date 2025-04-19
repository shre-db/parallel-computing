import random
import time
from datetime import datetime, timezone


SENSORS = {
    0: ("Temperature", lambda: round(random.uniform(20, 40), 1)),
    1: ("Pressure", lambda: round(random.uniform(900, 1100), 2)),
    2: ("Humidity", lambda: round(random.uniform(30, 80), 1)),
    3: ("Motion", lambda: random.choice([0, 1])),
    4: ("Light", lambda: round(random.uniform(100, 1000), 1)),
    5: ("Sound", lambda: round(random.uniform(30, 120), 1)),
    6: ("Gas", lambda: round(random.uniform(0, 10), 2)),
    7: ("Vibration", lambda: round(random.uniform(0.0, 5.0), 2)),
    8: ("CO2", lambda: round(random.uniform(300, 800), 1)),
    9: ("Proximity", lambda: random.randint(0, 5))
}


def sensor_thread(sensor_id, lock, sensor_data, sim_duration):
    sensor_type, generator = SENSORS[sensor_id]
    start_time = time.time()

    while time.time() - start_time < sim_duration:
        reading = generator()
        timestamp = datetime.now(timezone.utc).isoformat()

        print(f"[{sensor_type}] {timestamp}: {reading}")
        time.sleep(1)    

        record = {
            'timestamp': timestamp,
            'sensor_id': sensor_id,
            'type': sensor_type,
            'value': reading
        }

        with lock:
            sensor_data.append(record)

        print(f"[{sensor_type}] {timestamp}: {reading}")
        time.sleep(1)
