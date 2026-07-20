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
    def get_air_quality(self):

        url = (
            "https://air-quality-api.open-meteo.com/v1/air-quality"
            f"?latitude={self.latitude}"
            f"&longitude={self.longitude}"
            "&current="
            "us_aqi,"
            "pm2_5,"
            "pm10"
        )

        response = requests.get(url)

        data = response.json()

        current = data["current"]

        return {
            "aqi": current["us_aqi"],
            "pm25": current["pm2_5"],
            "pm10": current["pm10"]
        }
if __name__ == "__main__":

    service = WeatherService()

    print(service.get_air_quality())