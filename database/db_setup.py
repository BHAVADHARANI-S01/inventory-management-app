# database/db_setup.py

import sqlite3
import os

def setup_database():
    # Create or connect to the SQLite database
    db_path = os.path.join(os.path.dirname(__file__), "..", "inventory.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create operator login table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS operators (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Create product master table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS product_master (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        barcode TEXT,
        sku_id TEXT,
        category TEXT,
        subcategory TEXT,
        product_name TEXT,
        description TEXT,
        tax REAL,
        price REAL,
        unit TEXT,
        image_path TEXT
    )
    """)

    # Create goods receiving table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goods_receiving (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        supplier_name TEXT,
        quantity INTEGER,
        unit TEXT,
        rate_per_unit REAL,
        total REAL,
        tax REAL,
        FOREIGN KEY (product_id) REFERENCES product_master(id)
    )
    """)

    # Create sales table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        customer_name TEXT,
        quantity INTEGER,
        unit TEXT,
        rate_per_unit REAL,
        total REAL,
        tax REAL,
        FOREIGN KEY (product_id) REFERENCES product_master(id)
    )
    """)

    # Insert two default operators
    cursor.execute("INSERT OR IGNORE INTO operators (username, password) VALUES (?, ?)", ("operator1", "pass123"))
    cursor.execute("INSERT OR IGNORE INTO operators (username, password) VALUES (?, ?)", ("operator2", "pass456"))

    conn.commit()
    conn.close()

# Optional: run directly for manual DB setup
if __name__ == "__main__":
    setup_database()
    print("Database and tables created successfully.")
