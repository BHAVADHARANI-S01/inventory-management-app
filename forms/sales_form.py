# forms/sales_form.py

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit,
    QDoubleSpinBox, QPushButton, QMessageBox, QHBoxLayout
)
import sqlite3

class SalesForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sales Form")
        self.setup_ui()
        self.load_products()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.product_dropdown = QComboBox()
        layout.addWidget(QLabel("Product"))
        layout.addWidget(self.product_dropdown)

        self.customer_input = QLineEdit()
        self.customer_input.setPlaceholderText("Customer Name")
        layout.addWidget(QLabel("Customer Name"))
        layout.addWidget(self.customer_input)

        self.quantity_input = QDoubleSpinBox()
        self.quantity_input.setMaximum(100000)
        layout.addWidget(QLabel("Quantity"))
        layout.addWidget(self.quantity_input)

        self.unit_input = QLineEdit()
        self.unit_input.setPlaceholderText("Unit (e.g. kg, pcs)")
        layout.addWidget(QLabel("Unit"))
        layout.addWidget(self.unit_input)

        self.rate_input = QDoubleSpinBox()
        self.rate_input.setMaximum(100000)
        layout.addWidget(QLabel("Rate Per Unit"))
        layout.addWidget(self.rate_input)

        self.tax_input = QDoubleSpinBox()
        self.tax_input.setSuffix(" %")
        self.tax_input.setMaximum(100)
        layout.addWidget(QLabel("Tax (%)"))
        layout.addWidget(self.tax_input)

        # Submit button
        self.submit_btn = QPushButton("Submit Sale")
        self.submit_btn.clicked.connect(self.save_sale)
        layout.addWidget(self.submit_btn)

        self.setLayout(layout)

    def load_products(self):
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, product_name FROM product_master")
        self.products = cursor.fetchall()
        conn.close()

        for prod_id, name in self.products:
            self.product_dropdown.addItem(name, userData=prod_id)

    def save_sale(self):
        product_index = self.product_dropdown.currentIndex()
        product_id = self.product_dropdown.itemData(product_index)
        customer_name = self.customer_input.text()
        quantity = self.quantity_input.value()
        unit = self.unit_input.text()
        rate = self.rate_input.value()
        tax_percent = self.tax_input.value()

        subtotal = quantity * rate
        tax_amount = subtotal * (tax_percent / 100)
        total = subtotal + tax_amount

        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO sales (product_id, customer_name, quantity, unit, rate_per_unit, total, tax)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (product_id, customer_name, quantity, unit, rate, total, tax_percent))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Success", "Sale recorded successfully!")

        self.customer_input.clear()
        self.quantity_input.setValue(0)
        self.unit_input.clear()
        self.rate_input.setValue(0)
        self.tax_input.setValue(0)
