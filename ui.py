from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QProgressBar
from PyQt5.QtGui import QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt5.QtCore import Qt

class DashboardUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard UI")
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet("background-color: #1E1E2E;")

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Header Section
        header = QLabel("Hello, Jenny")
        header.setFont(QFont("Arial", 24, QFont.Bold))
        header.setStyleSheet("color: white;")
        header.setAlignment(Qt.AlignLeft)
        layout.addWidget(header)

        # Icon Section
        icon_layout = QHBoxLayout()
        for _ in range(4):
            icon = QLabel()
            icon.setFixedSize(60, 60)
            icon.setStyleSheet("border-radius: 10px; background-color: #4E4E6C;")
            icon_layout.addWidget(icon)

        layout.addLayout(icon_layout)

        # Balance Card
        balance_card = QWidget()
        balance_card.setFixedSize(360, 150)
        balance_card.setStyleSheet("""
            background: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:1, 
                stop:0 rgba(98, 0, 234, 255), stop:1 rgba(123, 31, 162, 255));
            border-radius: 20px;
        """)

        balance_layout = QVBoxLayout()
        balance_layout.setContentsMargins(20, 20, 20, 20)
        
        balance_label = QLabel("My balance")
        balance_label.setFont(QFont("Arial", 14))
        balance_label.setStyleSheet("color: white;")
        
        balance_value = QLabel("$26,129")
        balance_value.setFont(QFont("Arial", 28, QFont.Bold))
        balance_value.setStyleSheet("color: white;")

        balance_stats = QLabel("Spend: +$2,800    Profit: -$687")
        balance_stats.setFont(QFont("Arial", 12))
        balance_stats.setStyleSheet("color: white;")

        balance_layout.addWidget(balance_label)
        balance_layout.addWidget(balance_value)
        balance_layout.addWidget(balance_stats)
        balance_card.setLayout(balance_layout)

        layout.addWidget(balance_card)

        # Goals Section
        goals_layout = QVBoxLayout()
        goals_header = QLabel("Goal")
        goals_header.setFont(QFont("Arial", 18, QFont.Bold))
        goals_header.setStyleSheet("color: white;")

        goals_layout.addWidget(goals_header)

        goal_items = [
            ("Travel", "$915", 94),
            ("Apartment", "$315,000", 7),
        ]

        for goal_name, goal_amount, goal_progress in goal_items:
            goal_widget = QHBoxLayout()

            goal_label = QLabel(f"{goal_name} (Goal: {goal_amount})")
            goal_label.setFont(QFont("Arial", 12))
            goal_label.setStyleSheet("color: white;")
            goal_bar = QProgressBar()
            goal_bar.setValue(goal_progress)
            goal_bar.setStyleSheet(
                """
                QProgressBar {
                    background-color: #4E4E6C;
                    border-radius: 5px;
                }
                QProgressBar::chunk {
                    background-color: #62E2F5;
                    border-radius: 5px;
                }
                """
            )
            goal_widget.addWidget(goal_label)
            goal_widget.addWidget(goal_bar)

            goals_layout.addLayout(goal_widget)

        layout.addLayout(goals_layout)

        self.setLayout(layout)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dashboard = DashboardUI()
    dashboard.show()
    sys.exit(app.exec_())
