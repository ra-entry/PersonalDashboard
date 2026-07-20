from PySide6.QtCore import QObject, Signal, QTimer

from core.weather_service import WeatherService


class WeatherManager(QObject):

    weather_updated = Signal()


    def __init__(self):
        super().__init__()

        self.service = WeatherService()

        self.weather = None
        self.air = None

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_weather
        )

        self.timer.start(
            15 * 60 * 1000
        )

        QTimer.singleShot(
        100,
        self.update_weather
        )


    def update_weather(self):

        try:
            self.weather = self.service.get_weather()
            self.air = self.service.get_air_quality()

            self.weather_updated.emit()

        except Exception as e:
            print("Weather update failed:", e)