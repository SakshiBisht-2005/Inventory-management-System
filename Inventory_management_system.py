import mysql.connector as c
from datetime import date

# CONNECTION
conn = c.connect(
    host="localhost",
    user="root",
    passwd="Sakshi@2005",
    database="INVENTORY_DB"
)
cursor = conn.cursor()

# DATABASE 
cursor.execute("CREATE DATABASE IF NOT EXISTS INVENTORY_DB")
cursor.execute("USE INVENTORY_DB")

# PRODUCT TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS PRODUCT (
    P_ID INT PRIMARY KEY,
    P_NAME VARCHAR(50),
    PRICE FLOAT,
    STOCK INT
)
""")

# SALES TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS SALES (
    SALES_ID INT AUTO_INCREMENT PRIMARY KEY,
    P_ID INT,
    QUANTITY INT,
    TOTAL_PRICE FLOAT,
    SALES_DATE DATE,
    FOREIGN KEY(P_ID) REFERENCES PRODUCT(P_ID)
)
""")

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS USERS (
    USER_ID INT AUTO_INCREMENT PRIMARY KEY,
    USER_NAME VARCHAR(30),
    PASSWORD VARCHAR(20)
)
""")

# Insert admin only once
cursor.execute("""
INSERT IGNORE INTO USERS (USER_NAME, PASSWORD)
VALUES ('admin', 'admin@123')
""")
conn.commit()

# LOGIN FUNCTION
def login():
    try:
        user_name = input("Enter Username: ")
        passwd = input("Enter Password: ")

        cursor.execute(
            "SELECT * FROM USERS WHERE USER_NAME=%s AND PASSWORD=%s",
            (user_name, passwd)
        )
        if cursor.fetchone():
            print("Login Successful")
            return True
        else:
            print("Invalid Login")
            return False
    except c.Error as e:
        print("Login Error:", e)
        return False

# ADD PRODUCT
def add_items():
    try:
        p_id = int(input("Enter Product ID: "))
        p_name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        stock = int(input("Enter Stock: "))

        cursor.execute(
            "INSERT INTO PRODUCT VALUES (%s,%s,%s,%s)",
            (p_id, p_name, price, stock)
        )
        conn.commit()
        print("Product Added Successfully")
    except ValueError:
        print("Invalid Input")
    except c.Error as e:
        print("Database Error:", e)

# SELL PRODUCT
def sell_items():
    try:
        p_id = int(input("Enter Product ID: "))
        qnty = int(input("Enter Quantity: "))

        cursor.execute(
            "SELECT PRICE, STOCK FROM PRODUCT WHERE P_ID=%s",
            (p_id,)
        )
        result = cursor.fetchone()

        if not result:
            print("Product Not Found")
            return

        price, stock = result

        if qnty > stock:
            print("Insufficient Stock")
            return

        total_price = price * qnty

        cursor.execute(
            "UPDATE PRODUCT SET STOCK = STOCK - %s WHERE P_ID=%s",
            (qnty, p_id)
        )

        cursor.execute(
            "INSERT INTO SALES (P_ID, QUANTITY, TOTAL_PRICE, SALES_DATE) VALUES (%s,%s,%s,%s)",
            (p_id, qnty, total_price, date.today())
        )

        conn.commit()
        print("Sale Successful")

    except ValueError:
        print("Enter valid numbers")
    except c.Error as e:
        print("Database Error:", e)

# LOW STOCK
def low_stock():
    cursor.execute("SELECT * FROM PRODUCT WHERE STOCK < 5")
    for row in cursor.fetchall():
        print(row)

# SALES REPORT
def sale_report():
    cursor.execute("SELECT * FROM SALES")
    for row in cursor.fetchall():
        print(row)

# MAIN PROGRAM
if login():
    while True:
        print("""
        1. Add Product
        2. Sell Product
        3. Low Stock Alert
        4. Sales Report
        5. Exit
        """)

        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_items()
        elif choice == 2:
            sell_items()
        elif choice == 3:
            low_stock()
        elif choice == 4:
            sale_report()
        else:
            break
