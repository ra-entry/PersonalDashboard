from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from core.weather_codes import get_weather_description

import managers


class ForecastWidget(QWidget):

    def __init__(self):
        super().__init__()

        managers.weather_manager.weather_updated.connect(
            self.update_forecast
        )

        self.layout = QVBoxLayout()

        self.label = QLabel()

        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

        self.update_forecast()


    def update_forecast(self):

        weather = managers.weather_manager.weather

        if weather is None:
            self.label.setText(
                "Loading ..."
            )
            return


        daily = weather["daily"]

        high = daily["temperature_2m_max"][0]
        low = daily["temperature_2m_min"][0]

        code = daily["weather_code"][0]

        description = get_weather_description(code)


        self.label.setText(
            f"Today\n\n"
            f"{description}\n\n"
            f"High: {high:.1f}°F\n"
            f"Low: {low:.1f}°F"
        )