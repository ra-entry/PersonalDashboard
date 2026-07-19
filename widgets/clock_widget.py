from datetime import datetime

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class ClockWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignCenter)

        self.date_label = QLabel()
        self.date_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            border: none;
        """)

        self.date_label.setStyleSheet("""
            font-size: 14px;
            border: none;
        """)

        layout.addWidget(self.time_label)
        layout.addWidget(self.date_label)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        self.update_time()
        self.timer.start(1000)

    def update_time(self):

        now = datetime.now()

        self.time_label.setText(
            now.strftime("%I:%M:%S %p")
        )

        self.date_label.setText(
            now.strftime("%A\n%B %d, %Y")
        )