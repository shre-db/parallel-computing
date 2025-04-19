from weather import fetch_weather
import requests
import threading

CITIES = {
    "Berlin": (52.52, 13.41),
    "New York": (40.71, -74.01),
    "Tokyo": (35.68, 139.69),
    "Delhi": (28.61, 77.21),
    "Sydney": (-33.87, 151.21),
    "Rio": (-22.91, -43.17),
    "Cape Town": (-33.93, 18.42),
    "London": (51.51, -0.13),
    "Toronto": (43.65, -79.38),
    "Moscow": (55.75, 37.61)
}


def main():
    # num_workers = len(CITIES)
    results = []
    threads = []
    lock = threading.Lock()

    for city, coords in CITIES.items():
        thread = threading.Thread(target=fetch_weather, args=(city, *coords, results, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    # Filter successful responses
    successful = [r for r in results if 'temperature' in r]
    
    # Compute averages
    if successful:
        avg_temp = sum(r['temperature'] for r in successful) / len(successful)
        avg_wind = sum(r['windspeed'] for r in successful) / len(successful)

        
        print(f"\n --- Weather Watcher Report ☁️ ---")
        for r in successful:
            print(f"{r['city']}: {r['temperature']}°C, wind {r['windspeed']} kmph")
        print(f"Average Temperature: {avg_temp:.2f}°C")
        print(f"Average Windspeed: {avg_wind:.2f} kmph")
    else:
        print("No weather data retrieved.")


if __name__ == "__main__":
    main()