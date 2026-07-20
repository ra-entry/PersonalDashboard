from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy


class DashboardCard(QWidget):

    def __init__(self, title: str, content: QWidget):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(title_label)

        layout.addWidget(content)

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        self.setStyleSheet("""
            QWidget {
                background-color: white;
                border: 1px solid #bbbbbb;
                border-radius: 10px;
            }

            QLabel {
                border: none;
                background: transparent;
            }
        """)