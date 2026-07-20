from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QWidget,
    QHBoxLayout,
)

from widgets.sidebar import Sidebar

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


        # Create sidebar
        self.sidebar = Sidebar()


        # Connect navigation buttons
        self.sidebar.home_button.clicked.connect(
            lambda: (
                self.pages.setCurrentWidget(self.home_page),
                self.sidebar.set_active_button(
                    self.sidebar.home_button
                )
            )
        )


        self.sidebar.weather_button.clicked.connect(
            lambda: (
                self.pages.setCurrentWidget(self.weather_page),
                self.sidebar.set_active_button(
                    self.sidebar.weather_button
                )
            )
        )


        self.sidebar.tasks_button.clicked.connect(
            lambda: (
                self.pages.setCurrentWidget(self.tasks_page),
                self.sidebar.set_active_button(
                    self.sidebar.tasks_button
                )
            )
        )


        self.sidebar.settings_button.clicked.connect(
            lambda: (
                self.pages.setCurrentWidget(self.settings_page),
                self.sidebar.set_active_button(
                    self.sidebar.settings_button
                )
            )
        )


        # Main layout
        container = QWidget()

        main_layout = QHBoxLayout()

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.pages)


        container.setLayout(main_layout)

        self.setCentralWidget(container)


        # Default page
        self.pages.setCurrentWidget(self.home_page)

        self.sidebar.set_active_button(
            self.sidebar.home_button
        )