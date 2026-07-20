from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.home_button = QPushButton("🏠 Home")
        self.weather_button = QPushButton("🌤 Weather")
        self.tasks_button = QPushButton("📝 Tasks")
        self.settings_button = QPushButton("⚙ Settings")


        self.buttons = [
            self.home_button,
            self.weather_button,
            self.tasks_button,
            self.settings_button,
        ]


        for button in self.buttons:
            button.setFixedWidth(160)

            button.setStyleSheet(
                """
                QPushButton {
                    text-align: left;
                    padding-left: 15px;
                    padding-top: 8px;
                    padding-bottom: 8px;
                    border: none;
                }

                QPushButton:hover {
                    background-color: #eeeeee;
                }

                QPushButton[active="true"] {
                    background-color: #cccccc;
                    font-weight: bold;
                }
                """
            )

            self.layout.addWidget(button)


        self.layout.addStretch()

        self.setLayout(self.layout)


    def set_active_button(self, active_button):

        for button in self.buttons:
            button.setProperty("active", False)

        active_button.setProperty("active", True)

        for button in self.buttons:
            button.style().unpolish(button)
            button.style().polish(button)