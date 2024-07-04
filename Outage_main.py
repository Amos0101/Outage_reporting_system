import sys
from user_login_main import login
from PyQt6.QtWidgets import QApplication

app = QApplication([])
window = login()
window.show()
sys.exit(app.exec())