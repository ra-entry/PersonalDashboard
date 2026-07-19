from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

from core.weather_service import WeatherService
from core.weather_codes import get_weather_description

class WeatherWidget(QLabel):

    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)

        self.weather_service = WeatherService()

        self.update_weather()


    def update_weather(self):

        weather = self.weather_service.get_weather()

        temperature = weather["temperature"]
        feels_like = weather["feels_like"]
        humidity = weather["humidity"]
        wind = weather["wind"]
        code = weather["weather_code"]

        description = get_weather_description(code)

        self.setText(
            f"Weather\n\n"
            f"{temperature:.1f}°F\n"
            f"{description}\n\n"
            f"Feels Like: {feels_like:.1f}°F\n"
            f"Humidity: {humidity}%\n"
            f"Wind: {wind} mph"
        )