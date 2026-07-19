import requests

from core.settings import Settings

class WeatherService:

    def __init__(self):

        self.settings = Settings()

        self.latitude = self.settings.get("latitude")
        self.longitude = self.settings.get("longitude")


    def get_weather(self):

        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={self.latitude}"
            f"&longitude={self.longitude}"
            "&current="
            "temperature_2m,"
            "apparent_temperature,"
            "relative_humidity_2m,"
            "wind_speed_10m,"
            "weather_code,"
            "&temperature_unit=fahrenheit"
        )

        response = requests.get(url)

        data = response.json()

        current = data["current"]

        return {
            "temperature": current["temperature_2m"],
            "feels_like": current["apparent_temperature"],
            "humidity": current["relative_humidity_2m"],
            "wind": current["wind_speed_10m"],
            "weather_code": current["weather_code"]
        }