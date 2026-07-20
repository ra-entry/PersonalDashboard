from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
)

from pages.home_page import HomePage
from pages.weather_page import WeatherPage
from pages.tasks_page import TasksPage
from pages.settings_page import SettingsPage

class Dashboard(QMainWindow):

    def set_active_button(self, active_button):

        buttons = [
            self.home_button,
            self.weather_button,
            self.tasks_button,
            self.settings_button,
        ]

        for button in buttons:
            button.setProperty("active", False)

        active_button.setProperty("active", True)

        for button in buttons:
            button.style().unpolish(button)
            button.style().polish(button)
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Dashboard")
        self.resize(900, 800)

        # Create page container
        self.pages = QStackedWidget()

        # Create pages
        self.home_page = HomePage()
        self.weather_page = WeatherPage()
        self.tasks_page = TasksPage()
        self.settings_page = SettingsPage()

        # Create buttons
        self.home_button = QPushButton("🏠 Home")
        self.weather_button = QPushButton("🌤 Weather")
        self.tasks_button = QPushButton("📝 Tasks")
        self.settings_button = QPushButton("⚙ Settings")
        
        # Add pages to stack
        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.weather_page)
        self.pages.addWidget(self.tasks_page)
        self.pages.addWidget(self.settings_page)

        # Connect buttons  <-- Step 5 goes here
        self.home_button.clicked.connect(
            lambda: (
                self.pages.setCurrentWidget(self.home_page),
                self.set_active_button(self.home_button)
    )
        )

        self.weather_button.clicked.connect(
            lambda: (
                self.pages.setCurrentWidget(self.weather_page),
                self.set_active_button(self.weather_button)
            )
        )

        self.tasks_button.clicked.connect(
            lambda: (
                self.pages.setCurrentWidget(self.tasks_page),
                self.set_active_button(self.tasks_button)
            )
        )

        self.settings_button.clicked.connect(
            lambda: (
                self.pages.setCurrentWidget(self.settings_page),
                self.set_active_button(self.settings_button)
            )
        )

        # Build layout
        container = QWidget()

        main_layout = QHBoxLayout()
        sidebar = QVBoxLayout()
        sidebar.setSpacing(10)

        for button in [
            self.home_button,
            self.weather_button,
            self.tasks_button,
            self.settings_button
        ]:
            button.setFixedWidth(160)
            button.setStyleSheet(
                """
                QPushButton {
                    text-align: left;
                    padding-left: 15px;
                }
                """
            )

        sidebar.addWidget(self.home_button)
        sidebar.addWidget(self.weather_button)
        sidebar.addWidget(self.tasks_button)
        sidebar.addWidget(self.settings_button)

        sidebar.addStretch()

        main_layout.addLayout(sidebar)
        main_layout.addWidget(self.pages)

        container.setLayout(main_layout)

        self.setCentralWidget(container)
        self.set_active_button(self.home_button)