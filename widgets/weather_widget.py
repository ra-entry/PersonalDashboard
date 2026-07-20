from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

from core.air_quality import get_aqi_description
from core.weather_codes import get_weather_description
from core.recommendations import get_outdoor_recommendation

import managers


class WeatherWidget(QLabel):

    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)

        managers.weather_manager.weather_updated.connect(
            self.update_weather
        )

        self.update_weather()


    def update_weather(self):

        weather = managers.weather_manager.weather
        air = managers.weather_manager.air

        if weather is None or air is None:
            self.setText(
                "Loading weather..."
            )
            return


        recommendation = get_outdoor_recommendation(
            weather,
            air
        )

        temperature = weather["temperature"]
        feels_like = weather["feels_like"]
        humidity = weather["humidity"]
        wind = weather["wind"]
        code = weather["weather_code"]

        aqi = air["aqi"]
        pm25 = air["pm25"]

        description = get_weather_description(code)
        aqi_description = get_aqi_description(aqi)

        outdoor = recommendation["recommendation"]

        positive = recommendation["positive"]
        negative = recommendation["negative"]

        reason_text = ""

        for item in positive:
            reason_text += f"✓ {item}\n"

        for item in negative:
            reason_text += f"⚠ {item}\n"


        self.setText(
            f"{temperature:.1f}°F\n"
            f"{description}\n\n"

            f"Feels Like: {feels_like:.1f}°F\n"
            f"Humidity: {humidity}%\n"
            f"Wind: {wind:.1f} mph\n\n"

            f"Air Quality: {aqi_description}\n"
            f"AQI: {aqi}\n"
            f"PM2.5: {pm25:.1f}\n\n"

            f"Outdoor Activity:\n"
            f"{outdoor}\n\n"

            f"{reason_text}"
        )