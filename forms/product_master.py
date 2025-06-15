from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit, QTextEdit, QComboBox,
    QPushButton, QLabel, QFileDialog, QMessageBox
)
from PySide6.QtGui import QPixmap
import os
import shutil
import sqlite3

PRODUCT_IMAGE_DIR = "assets/product_images"

class ProductMasterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Master Form")
        self.image_path = None
        self.setup_ui()
        self.setup_db()

    def setup_ui(self):
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.barcode_input = QLineEdit()
        self.sku_input = QLineEdit()
        self.category_input = QLineEdit()
        self.subcategory_input = QLineEdit()
        self.name_input = QLineEdit()
        self.description_input = QTextEdit()
        self.tax_input = QLineEdit()
        self.price_input = QLineEdit()
        self.unit_input = QComboBox()
        self.unit_input.addItems(["pcs", "kg", "litre", "pack"])

        self.image_label = QLabel("No image selected")
        self.image_label.setFixedHeight(100)
        self.image_label.setStyleSheet("border: 1px solid gray;")

        self.upload_button = QPushButton("Upload Image")
        self.upload_button.clicked.connect(self.upload_image)

        self.submit_button = QPushButton("Save Product")
        self.submit_button.clicked.connect(self.save_product)

        form_layout.addRow("Barcode:", self.barcode_input)
        form_layout.addRow("SKU ID:", self.sku_input)
        form_layout.addRow("Category:", self.category_input)
        form_layout.addRow("Subcategory:", self.subcategory_input)
        form_layout.addRow("Product Name:", self.name_input)
        form_layout.addRow("Description:", self.description_input)
        form_layout.addRow("Tax (%):", self.tax_input)
        form_layout.addRow("Price:", self.price_input)
        form_layout.addRow("Unit:", self.unit_input)
        form_layout.addRow("Product Image:", self.upload_button)
        form_layout.addRow("", self.image_label)
        form_layout.addRow("", self.submit_button)

        layout.addLayout(form_layout)
        self.setLayout(layout)

    def upload_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(
            self, "Select Product Image", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if image_path:
            self.image_path = image_path
            pixmap = QPixmap(image_path).scaledToHeight(100)
            self.image_label.setPixmap(pixmap)

    def setup_db(self):
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS product_master (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                barcode TEXT,
                sku TEXT,
                category TEXT,
                subcategory TEXT,
                name TEXT,
                description TEXT,
                tax REAL,
                price REAL,
                unit TEXT,
                image TEXT
            )
        """)
        conn.commit()
        conn.close()

    def save_product(self):
        if not self.image_path:
            QMessageBox.warning(self, "Missing Image", "Please upload an image.")
            return

        # Copy image to assets folder
        filename = os.path.basename(self.image_path)
        save_path = os.path.join(PRODUCT_IMAGE_DIR, filename)
        os.makedirs(PRODUCT_IMAGE_DIR, exist_ok=True)
        shutil.copy(self.image_path, save_path)

        data = (
            self.barcode_input.text(),
            self.sku_input.text(),
            self.category_input.text(),
            self.subcategory_input.text(),
            self.name_input.text(),
            self.description_input.toPlainText(),
            float(self.tax_input.text() or 0),
            float(self.price_input.text() or 0),
            self.unit_input.currentText(),
            filename
        )

        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO product_master
            (barcode, sku, category, subcategory, name, description, tax, price, unit, image)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Saved", "Product saved successfully!")
        self.clear_form()

    def clear_form(self):
        self.barcode_input.clear()
        self.sku_input.clear()
        self.category_input.clear()
        self.subcategory_input.clear()
        self.name_input.clear()
        self.description_input.clear()
        self.tax_input.clear()
        self.price_input.clear()
        self.unit_input.setCurrentIndex(0)
        self.image_label.clear()
        self.image_path = None
