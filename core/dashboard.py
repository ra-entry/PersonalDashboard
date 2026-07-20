from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
)

from pages.home_page import HomePage
from pages.weather_page import WeatherPage
from pages.tasks_page import TasksPage
from pages.settings_page import SettingsPage

class Dashboard(QMainWindow):

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

        # Add pages to stack
        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.weather_page)
        self.pages.addWidget(self.tasks_page)
        self.pages.addWidget(self.settings_page)


        # Create navigation buttons
        home_button = QPushButton("Home")
        weather_button = QPushButton("Weather")
        tasks_button = QPushButton("Tasks")
        settings_button = QPushButton("Settings")


        # Connect buttons  <-- Step 5 goes here
        home_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.home_page)
        )

        weather_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.weather_page)
        )

        tasks_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.tasks_page)
        )

        settings_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.settings_page)
        )


        # Build layout
        container = QWidget()

        main_layout = QVBoxLayout()
        nav_layout = QHBoxLayout()

        nav_layout.addWidget(home_button)
        nav_layout.addWidget(weather_button)
        nav_layout.addWidget(tasks_button)
        nav_layout.addWidget(settings_button)

        main_layout.addLayout(nav_layout)
        main_layout.addWidget(self.pages)

        container.setLayout(main_layout)

        self.setCentralWidget(container)