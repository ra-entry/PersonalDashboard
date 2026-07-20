from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel
)

from PySide6.QtCore import Qt

from widgets.clock_widget import ClockWidget
from widgets.weather_widget import WeatherWidget
from widgets.task_widget import TaskWidget
from widgets.dashboard_card import DashboardCard


class HomePage(QWidget):

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        top_layout.setSpacing(15)
        bottom_layout.setSpacing(15)

        title = QLabel("Personal Dashboard")
        title.setAlignment(Qt.AlignCenter)

        clock = DashboardCard(
            "🕒 Clock",
            ClockWidget()
        )

        weather = DashboardCard(
            "🌤️ Weather",
            WeatherWidget()
        )

        tasks = DashboardCard(
            "📝 Tasks",
            TaskWidget()
        )


        top_layout.addWidget(clock, 1)
        top_layout.addWidget(weather, 2)

        bottom_layout.addWidget(tasks)


        main_layout.addWidget(title)
        main_layout.addLayout(top_layout, 3)
        main_layout.addLayout(bottom_layout, 1)

        main_layout.setSpacing(15)

        self.setLayout(main_layout)