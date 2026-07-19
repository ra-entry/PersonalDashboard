from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)

from PySide6.QtCore import Qt

from widgets.clock_widget import ClockWidget
from widgets.weather_widget import WeatherWidget
from widgets.task_widget import TaskWidget
from widgets.dashboard_card import DashboardCard


class Dashboard(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Dashboard")
        self.resize(900, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        top_layout.setSpacing(15)
        bottom_layout.setSpacing(15)

        central_widget.setLayout(main_layout)

        title = QLabel("Personal Dashboard")
        title.setAlignment(Qt.AlignCenter)

        clock = DashboardCard("🕒 Clock", ClockWidget())
        weather = DashboardCard("🌤️ Weather", WeatherWidget())
        tasks = DashboardCard("📝 Tasks", TaskWidget())
        
        ##clock = ClockWidget()
        ##weather = WeatherWidget()
        ##tasks = TaskWidget()

        main_layout.addWidget(title)

        top_layout.addWidget(clock)
        top_layout.addWidget(weather)

        bottom_layout.addWidget(tasks)

        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        main_layout.setSpacing(15)