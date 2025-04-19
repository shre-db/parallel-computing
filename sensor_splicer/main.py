from sensor import sensor_thread
import threading

def main():
    threads = []
    sensor_data = []
    simulation_duration = 10
    lock = threading.Lock()
    num_sensors = 10

    for sensor_id in range(num_sensors):
        thread = threading.Thread(target=sensor_thread, args=(sensor_id, lock, sensor_data, simulation_duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"\n✅ Collected {len(sensor_data)} total readings.")
    print("🗃️ Saving to database (simulated)...")

     # Simulated write to disk or DB
    with open("sensor_data_log.json", "w") as f:
        import json
        json.dump(sensor_data, f, indent=2)

    print("💾 Data saved to 'sensor_data_log.json'.")
    

if __name__ == "__main__":
    main()