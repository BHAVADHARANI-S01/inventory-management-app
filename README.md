# Inventory Management Application

A desktop-based Inventory Management System built with **PySide6** and **SQLite**, developed as part of an internship assignment for **Infoware India**.

This application allows operators to log in and manage inventory through three core modules:
- Product Master
- Goods Receiving
- Sales Form

---

##  Features

- Operator login with credentials  
- Product management with barcode, image, and categorization  
- Goods receiving from suppliers with unit-based pricing and tax  
- Sales recording with customer details  
- Local SQLite database (MySQL compatible structure)  
- Converts to `.exe` using PyInstaller  
- Clean and intuitive UI using PySide6  

---


## Demo Video

[[Watch the demo video](https://github.com/BHAVADHARANI-S01/inventory-management-app/blob/main/assets/video_thumb.png?raw=true)](https://drive.google.com/file/d/1By5xH67UTBZTw3ZkLjGZjdIVgEsrO8sY/view?usp=sharing)

> Click the thumbnail above to watch the full screen-recorded demo of the application.


## Operator Logins

| Username   | Password  |
|------------|-----------|
| operator1  | pass123   |
| operator2  | pass456   |

---

##  Database Tables

- `operators`
- `product_master`
- `goods_receiving`
- `sales`

All data is stored in `inventory.db` using SQLite.

---

##  How to Run

### 1. Clone the repo

```bash
git clone https://github.com/BHAVADHARANI-S01/inventory-management-app.git
cd inventory-management-app
