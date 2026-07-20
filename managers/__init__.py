from managers.weather_manager import WeatherManager
from managers.task_manager import TaskManager


weather_manager = None
task_manager = None


def initialize_managers():

    global weather_manager
    global task_manager

    weather_manager = WeatherManager()
    task_manager = TaskManager()