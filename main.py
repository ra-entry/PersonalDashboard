import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout
)

app = QApplication(sys.argv)

with open("themes/light.qss", "r") as file:
    app.setStyleSheet(file.read())

from PySide6.QtCore import Qt

from widgets.clock_widget import ClockWidget

from widgets.weather_widget import WeatherWidget

from widgets.task_widget import TaskWidget

from core.settings import Settings

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Dashboard")
        self.resize(900, 600)

        # Main container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        main_layout = QVBoxLayout()

        top_layout = QHBoxLayout()

        bottom_layout = QHBoxLayout()

        central_widget.setLayout(main_layout)

        # Title
        title = QLabel("Personal Dashboard")
        title.setAlignment(Qt.AlignCenter)

        # Placeholder widgets
        clock = ClockWidget()
        weather = WeatherWidget()
        tasks = TaskWidget()

        # Add widgets to layout
        main_layout.addWidget(title)

        top_layout.addWidget(clock)
        top_layout.addWidget(weather)

        bottom_layout.addWidget(tasks)

        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

window = Dashboard()
window.show()

sys.exit(app.exec())