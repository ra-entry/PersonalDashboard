from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from core.recommendations import get_outdoor_recommendation

import managers


class DailyStatusWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.status_label = QLabel()

        self.layout.addWidget(self.status_label)


        managers.weather_manager.weather_updated.connect(
            self.update_status
        )


        self.setLayout(self.layout)

        self.update_status()


    def update_status(self):

        weather = managers.weather_manager.weather
        air = managers.weather_manager.air

        if weather is None or air is None:
            self.status_label.setText(
                "Loading status..."
            )
            return


        recommendation = get_outdoor_recommendation(
            weather,
            air
        )

        temperature = weather["temperature"]
        outdoor = recommendation["recommendation"]


        self.status_label.setText(
            f"🌡 Temperature\n"
            f"{temperature:.1f}°F\n\n"

            f"🌲 Outdoor Activity\n"
            f"{outdoor}\n\n"

            f"⚙ System\n"
            f"Running"
        )