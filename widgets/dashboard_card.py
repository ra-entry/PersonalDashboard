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

        self.layout.setContentsMargins(15, 10, 15, 15)
        self.layout.setSpacing(10)

        title_label = QLabel(title)
        title_label.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: #222222;
        """)
        title_label.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(title_label)
        self.layout.addWidget(content)
        self.layout.addStretch()

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        self.setMinimumHeight(150)

        self.setStyleSheet("""
            DashboardCard {
                background-color: white;
                color: #222222;
                border: 1px solid #bbbbbb;
                border-radius: 10px;
             }

            QLabel {
                color: #222222;
                border: none;
                background: transparent;
            }
        """)
    def add_widget(self, widget):
        self.layout.addWidget(widget)