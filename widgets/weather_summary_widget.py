from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

import managers

from core.weather_codes import get_weather_description
from core.recommendations import get_outdoor_recommendation


class WeatherSummaryWidget(QLabel):

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


        description = get_weather_description(
            weather["weather_code"]
        )

        recommendation = get_outdoor_recommendation(
            weather,
            air
        )


        self.setText(
            f"{weather['temperature']:.1f}°F\n"
            f"{description}\n"
            f"Feels Like: "
            f"{weather['feels_like']:.1f}°F\n\n"
            f"Outdoor:\n"
            f"{recommendation['recommendation']}"
        )