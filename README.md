# 🏪 Inventory Management System (Python + MySQL)

A console-based Inventory Management System developed using Python and MySQL.  
This project allows users to manage products, track stock, record sales, and generate reports securely using a login system.

---

## 📌 Features

- 🔐 User Login Authentication
- ➕ Add New Products
- 🛒 Sell Products (Auto Stock Update)
- ⚠️ Low Stock Alerts
- 📊 Sales Report Generation
- ❌ Exception Handling
- 🗄️ MySQL Database Integration

---

## 🛠️ Technologies Used

- Python 3
- MySQL
- mysql-connector-python

---

## 🗂️ Database Structure

### PRODUCT Table
| Column | Description |
|------|------------|
| P_ID | Product ID |
| P_NAME | Product Name |
| PRICE | Product Price |
| STOCK | Available Stock |

### SALES Table
| Column | Description |
|------|------------|
| SALES_ID | Sale ID |
| P_ID | Product ID |
| QUANTITY | Quantity Sold |
| TOTAL_PRICE | Total Amount |
| SALES_DATE | Date of Sale |

### USERS Table
| Column | Description |
|------|------------|
| USER_ID | User ID |
| USER_NAME | Username |
| PASSWORD | Password |

---

## ⚙️ Installation Steps

1. Install MySQL and Python  
2. Install MySQL connector:
   ```bash
   pip install mysql-connector-python
