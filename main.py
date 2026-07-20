import sys

from PySide6.QtWidgets import QApplication

from core.dashboard import Dashboard

app = QApplication(sys.argv)

with open("themes/light.qss", "r") as file:
    app.setStyleSheet(file.read())


window = Dashboard()
window.show()

sys.exit(app.exec())