# 🌡️Sensor Splicer

**Field**: IoT & Robotics\
**Objective**:
Simulate 10 sensor threads, each emitting readings every second (e.g. temperature, motion, pressure). These sensors should write to a shared database (a simple in-memory list or dict) using locks to prevent data collisions.

Learning
---
- Real-time thread simulation.
- Periodic sensor "heartbeat".
- Locking shared resources with `threading.Lock`
- Organizing structured sensor data.

Setup
---
1. 10 threads.
2. Each thread acts as a different type of sensor.
3. Every second, each sensor emits a reading: a (timestamp, sensor_id, value) tuple.
4. Shared list collects all readings.
5. After 10 seconds, stop the simulation.

Sensor Types
---
Sensor ID | Type | Range
|:-|:-|:-
0 | Temperature | 20°C to 40°C
1 | Pressure | 900 to 1100 hPa
2 | Humidity | 30% to 80%
3 | Motion | 0 or 1 (boolean)
4–9 | Custom (Light, Sound, Gas, etc.) | 