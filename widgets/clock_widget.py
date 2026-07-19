from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QTimer, QDateTime, Qt


class ClockWidget(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QDateTime.currentDateTime()

        text = current_time.toString(
            "hh:mm:ss\ndddd, MMMM d, yyyy"
        )

        self.setText(text)