# Weather Watcher ☁️

**Field**: Climatology\
**Tech**: multithreading + external APIs\
**Objective**: Pull weather data for multiple cities in parallel using threads, then calculate average humidity, pressure, temperature, etc.

This mimics real-world weather monitoring dashboards that collect sensor or API data simultaneously from distributed sources.

Learning
---
- Using threads to parallelize HTTP requests (I/O-bound task).
- Handling JSON APIs.
- Aggregating real-time weather metrics.
- (Bonus) Making it resilient against slow/broken APIs.

Tools
---
- `requests` – for API calls.
- `concurrent.futures.ThreadPoolExecutor` – for threading.
- `open-meteo.com` - no auth key needed!

