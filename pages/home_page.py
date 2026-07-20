from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel
)

from PySide6.QtCore import Qt

from widgets.system_status_widget import SystemStatusWidget

from widgets.weather_summary_widget import WeatherSummaryWidget

from widgets.clock_widget import ClockWidget
from widgets.task_widget import TaskWidget
from widgets.dashboard_card import DashboardCard


class HomePage(QWidget):

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(
            20, 20, 20, 20
        )

        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        top_layout.setSpacing(15)
        bottom_layout.setSpacing(15)

        title = QLabel("Welcome Back!")
        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #222222;
        """)

        clock = DashboardCard(
            "🕒 Clock",
            ClockWidget()
        )

        weather = DashboardCard(
            "🌤️ Weather",
            WeatherSummaryWidget()
        )

        tasks = DashboardCard(
            "📝 Tasks",
            TaskWidget()
        )

        system = DashboardCard(
            "⚙ System",
            SystemStatusWidget()
        )

        top_layout.addWidget(clock, 1)
        top_layout.addWidget(weather, 1)

        bottom_layout.addWidget(tasks, 2)
        bottom_layout.addWidget(system, 1)

        main_layout.addWidget(title)
        main_layout.addLayout(top_layout, 2)
        main_layout.addLayout(bottom_layout, 1)

        main_layout.setSpacing(15)

        self.setLayout(main_layout)