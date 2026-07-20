from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class WeatherPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel(
            "Detailed Weather Page Coming Soon"
        )

        layout.addWidget(label)

        self.setLayout(layout)