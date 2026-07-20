from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

import managers

from core.air_quality import get_aqi_description


class AirQualityWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.label = QLabel()

        self.layout.addWidget(self.label)

        self.setLayout(self.layout)


        managers.weather_manager.weather_updated.connect(
            self.update_air_quality
        )


        self.update_air_quality()


    def update_air_quality(self):

        air = managers.weather_manager.air


        if air is None:
            self.label.setText(
                "Loading air quality..."
            )
            return


        aqi = air["aqi"]
        pm25 = air["pm25"]
        pm10 = air["pm10"]

        description = get_aqi_description(aqi)


        self.label.setText(
            f"AQI: {aqi}\n"
            f"{description}\n\n"
            f"PM2.5: {pm25:.1f}\n"
            f"PM10: {pm10:.1f}"
        )