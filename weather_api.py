import requests
from config import get_secret
def get_weather(location):
    key = get_secret("OPENWEATHER_API_KEY")
    if not key:
        return {"ok": False, "message": "Weather API key is not configured yet."}
    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": location, "appid": key, "units": "metric"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        return {
            "ok": True,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"].title(),
            "source": "OpenWeather",
        }
    except Exception as exc:
        return {"ok": False, "message": f"Weather service unavailable: {exc}"}
