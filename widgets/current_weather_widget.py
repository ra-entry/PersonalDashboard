from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

import managers

from core.weather_codes import get_weather_description


class CurrentWeatherWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.label = QLabel()

        self.layout.addWidget(self.label)

        self.setLayout(self.layout)


        managers.weather_manager.weather_updated.connect(
            self.update_weather
        )


        self.update_weather()


    def update_weather(self):

        weather = managers.weather_manager.weather


        if weather is None:
            self.label.setText(
                "Loading weather..."
            )
            return


        temperature = weather["temperature"]
        feels_like = weather["feels_like"]
        humidity = weather["humidity"]
        wind = weather["wind"]
        code = weather["weather_code"]

        description = get_weather_description(code)


        self.label.setText(
            f"{temperature:.1f}°F\n\n"
            f"{description}\n\n"
            f"Feels Like: {feels_like:.1f}°F\n"
            f"Humidity: {humidity}%\n"
            f"Wind: {wind:.1f} mph"
        )