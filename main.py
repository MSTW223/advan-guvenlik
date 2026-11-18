import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QPushButton
from database.db_manager import DatabaseManager
from ui.styles import DARK_QSS

class AdvanMainLayout(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ADVAN GÜVENLİK — Professional Parking & CCTV ANPR System")
        self.resize(1200, 750)
        self.db = DatabaseManager()
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)

        sidebar = QWidget()
        sidebar.setFixedWidth(240)
        sidebar.setStyleSheet("background-color: #1A1D24; border-right: 1px solid #2D3748;")
        s_layout = QVBoxLayout(sidebar)
        
        brand = QLabel("🛡️ ADVAN GÜVENLİK")
        brand.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; margin: 10px;")
        s_layout.addWidget(brand)

        btn = QPushButton("📊 لوحة القيادة (Dashboard)")
        btn.setStyleSheet("text-align: left; padding: 10px; border: none; color: #CBD5E1;")
        s_layout.addWidget(btn)
        s_layout.addStretch()

        content = QWidget()
        c_layout = QVBoxLayout(content)
        title = QLabel("أهلاً بك في نظام إدارة المواقف والكاميرات ADVAN GÜVENLİK")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #F8FAFC;")
        c_layout.addWidget(title)
        c_layout.addStretch()

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)
        self.setCentralWidget(central)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(DARK_QSS)
    window = AdvanMainLayout()
    window.show()
    sys.exit(app.exec())