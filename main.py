from PySide6.QtWidgets import QApplication

from core.dashboard import Dashboard
from managers import initialize_managers

import sys

app = QApplication(sys.argv)

initialize_managers()

with open("themes/light.qss", "r") as file:
    app.setStyleSheet(file.read())


window = Dashboard()
window.show()

sys.exit(app.exec())