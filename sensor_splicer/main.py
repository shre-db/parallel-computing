from sensor import sensor_thread
from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import threading


def main():
    sensor_data = []
    lock = threading.Lock()
    simulation_duration = 10
    num_sensors = 10

    with ThreadPoolExecutor(max_workers=num_sensors) as executor:
        futures = [executor.submit(sensor_thread, sensor_id, lock, sensor_data, simulation_duration) for sensor_id in range(10)]
        wait(futures)
        
    print(f"\n✅ Collected {len(sensor_data)} total readings.")
    print("🗃️ Saving to database (simulated)...")

     # Simulated write to disk or DB
    with open("sensor_data_log.json", "w") as f:
        import json
        json.dump(sensor_data, f, indent=2)

    print("💾 Data saved to 'sensor_data_log.json'.")


if __name__ == "__main__":
    main()