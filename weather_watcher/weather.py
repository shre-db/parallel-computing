import requests

def fetch_weather(city, lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        weather = data['current_weather']
        print(f"[{city}] Temp: {weather['temperature']}°C, Wind: {weather['windspeed']} km/h")
        return {
            'city': city,
            'temperature': weather['temperature'],
            'windspeed': weather['windspeed'],
            'time': weather['time']
        }
    except Exception as e:
        print(f"[{city}] Error: {e}")
        return {
            'city': city,
            'error': str(e)
        }
