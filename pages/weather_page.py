from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel
)

from PySide6.QtCore import Qt

from widgets.dashboard_card import DashboardCard

from widgets.current_weather_widget import CurrentWeatherWidget
from widgets.air_quality_widget import AirQualityWidget
from widgets.forecast_widget import ForecastWidget

class WeatherPage(QWidget):

    def __init__(self):
        super().__init__()


        main_layout = QVBoxLayout()


        title = QLabel("🌤 Weather")

        title.setAlignment(
            Qt.AlignCenter
        )

        title.setStyleSheet(
            """
            font-size:28px;
            font-weight:bold;
            """
        )


        top_layout = QHBoxLayout()


        current = DashboardCard(
            "Current Conditions",
            CurrentWeatherWidget()
        )


        air = DashboardCard(
            "Air Quality",
            AirQualityWidget()
        )

        forecast = DashboardCard(
            "Forecast",
            ForecastWidget()
        )

        main_layout.addWidget(forecast)

        top_layout.addWidget(
            current,
            1
        )

        top_layout.addWidget(
            air,
            1
        )


        main_layout.addWidget(title)

        main_layout.addLayout(
            top_layout
        )


        self.setLayout(main_layout)