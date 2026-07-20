from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

import managers


class SystemStatusWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.label = QLabel()

        self.label.setAlignment(
            Qt.AlignCenter
        )

        self.layout.addWidget(
            self.label
        )

        self.setLayout(
            self.layout
        )

        managers.weather_manager.weather_updated.connect(
            self.update_status
        )

        self.update_status()


    def update_status(self):

        weather_manager = managers.weather_manager

        if weather_manager.error:

            weather_status = (
                "❌ Weather unavailable"
            )

        else:

            weather_status = (
                "✓ Weather connected"
            )


        if weather_manager.last_updated:

            updated = (
                weather_manager.last_updated
                .strftime("%I:%M %p")
            )

        else:

            updated = "Never"


        self.label.setText(
            f"{weather_status}\n\n"
            f"Last Update:\n"
            f"{updated}"
        )