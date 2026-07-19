import json
import os


class Settings:

    def __init__(self):

        self.file_path = "data/settings.json"

        self.defaults = {
            "location": "Sandwich, Ontario",
            "units": "Fahrenheit",
            "theme": "Light",
            "weather_refresh_minutes": 30
        }

        self.data = self.load()


    def load(self):

        if os.path.exists(self.file_path):

            with open(self.file_path, "r") as file:
                return json.load(file)

        else:
            self.save(self.defaults)
            return self.defaults


    def save(self, settings=None):

        if settings:
            self.data = settings

        os.makedirs("data", exist_ok=True)

        with open(self.file_path, "w") as file:
            json.dump(
                self.data,
                file,
                indent=4
            )


    def get(self, key):

        return self.data.get(key)


    def set(self, key, value):

        self.data[key] = value
        self.save()