from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
)

from pages.home_page import HomePage
from pages.weather_page import WeatherPage
from pages.tasks_page import TasksPage


class Dashboard(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Dashboard")
        self.resize(900, 800)

        self.pages = QStackedWidget()

        self.home_page = HomePage()
        self.weather_page = WeatherPage()
        self.tasks_page = TasksPage()

        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.weather_page)
        self.pages.addWidget(self.tasks_page)

        self.setCentralWidget(self.pages)