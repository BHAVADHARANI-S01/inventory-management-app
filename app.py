# app.py

from PySide6.QtWidgets import QApplication
import sys
from ui.login_window import LoginWindow
from database import db_setup  # ensure db is ready

if __name__ == "__main__":
    db_setup  # runs setup (just imports to ensure tables exist)

    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())
