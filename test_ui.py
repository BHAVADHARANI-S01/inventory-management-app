from PySide6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Test Window")
window.resize(300, 200)
window.show()
sys.exit(app.exec())
