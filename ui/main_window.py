# ui/main_window.py

from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QStackedWidget
from forms.product_master import ProductMasterForm
from forms.sales_form import SalesForm
from forms.goods_receiving import GoodsReceivingForm  # NEW

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Management Dashboard")
        self.resize(600, 400)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Navigation buttons
        self.product_btn = QPushButton("Product Master")
        self.sales_btn = QPushButton("Sales Form")
        self.goods_btn = QPushButton("Goods Receiving")  # NEW

        self.product_btn.clicked.connect(self.show_product_form)
        self.sales_btn.clicked.connect(self.show_sales_form)
        self.goods_btn.clicked.connect(self.show_goods_form)  # NEW

        self.layout.addWidget(QLabel("Welcome Operator!"))
        self.layout.addWidget(self.product_btn)
        self.layout.addWidget(self.sales_btn)
        self.layout.addWidget(self.goods_btn)  # NEW

        # Stack of forms
        self.stack = QStackedWidget()
        self.product_form = ProductMasterForm()
        self.sales_form = SalesForm()
        self.goods_form = GoodsReceivingForm()  # NEW

        self.stack.addWidget(self.product_form)  # index 0
        self.stack.addWidget(self.sales_form)    # index 1
        self.stack.addWidget(self.goods_form)    # index 2

        self.layout.addWidget(self.stack)

    def show_product_form(self):
        self.stack.setCurrentWidget(self.product_form)

    def show_sales_form(self):
        self.stack.setCurrentWidget(self.sales_form)

    def show_goods_form(self):  # NEW
        self.stack.setCurrentWidget(self.goods_form)
