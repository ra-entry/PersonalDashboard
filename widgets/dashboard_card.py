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

        self.layout = QVBoxLayout(self)

        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(10)

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(title_label)

        self.layout.addWidget(content)

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        self.setStyleSheet("""
            DashboardCard {
                background-color: white;
                border: 1px solid #bbbbbb;
                border-radius: 10px;
            }

            QLabel {
                border: none;
                background: transparent;
            }
        """)
    def add_widget(self, widget):
        self.layout.addWidget(widget)