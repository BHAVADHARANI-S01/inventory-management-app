# 🧾 Inventory Management Application

A desktop-based Inventory Management System built with **PySide6** and **SQLite**, developed as part of an internship assignment for **Infoware India**.

This application allows operators to log in and manage inventory through three core modules:
- 📦 Product Master
- 🚚 Goods Receiving
- 🛒 Sales Form

---

## 🔧 Features

✅ Operator login with credentials  
✅ Product management with barcode, image, and categorization  
✅ Goods receiving from suppliers with unit-based pricing and tax  
✅ Sales recording with customer details  
✅ Local SQLite database (MySQL compatible structure)  
✅ Converts to `.exe` using PyInstaller  
✅ Clean and intuitive UI using PySide6  

---

## 🧑‍💼 Operator Logins

| Username   | Password  |
|------------|-----------|
| operator1  | pass123   |
| operator2  | pass456   |

---
## 🖼️ Application Screenshots

### 🔐 Login Window  
[![Login](https://github.com/BHAVADHARANI-S01/inventory-management-app/blob/main/assets/screenshot_login.png?raw=true)](https://github.com/BHAVADHARANI-S01/inventory-management-app/blob/main/assets/screenshot_login.png?raw=true)

### 🧾 Product Master Form  
[![Product Master](https://github.com/BHAVADHARANI-S01/inventory-management-app/blob/main/assets/screenshot_product.png?raw=true)](https://github.com/BHAVADHARANI-S01/inventory-management-app/blob/main/assets/screenshot_product.png?raw=true)

### 📦 Goods Receiving  
[![Goods Receiving](https://github.com/BHAVADHARANI-S01/inventory-management-app/blob/main/assets/screenshot_goods.png?raw=true)](https://github.com/BHAVADHARANI-S01/inventory-management-app/blob/main/assets/screenshot_goods.png?raw=true)

### 🛒 Sales Form  
[![Sales Form](https://github.com/BHAVADHARANI-S01/inventory-management-app/blob/main/assets/screenshot_sales.png?raw=true)](https://github.com/BHAVADHARANI-S01/inventory-management-app/blob/main/assets/screenshot_sales.png?raw=true)

---

## 🗃️ Database Tables

- `operators`
- `product_master`
- `goods_receiving`
- `sales`

All data is stored in `inventory.db` using SQLite.

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/BHAVADHARANI-S01/inventory-management-app.git
cd inventory-management-app
