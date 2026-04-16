import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "SalesDB", "sales.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a table called 'sales'
# IF NOT EXISTS → don't throw error if table already exists


cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,  -- auto increment ID
    customer_name TEXT,                                -- customer name
    prod_name     TEXT,                                -- product name
    quantity      INTEGER,                             -- how many units sold
    price         REAL,                                -- price per unit
    total         REAL                                 -- quantity * price
)
""")

# Insert sample data
# total = quantity * price (calculated manually)
cursor.executemany(
    "INSERT INTO sales (customer_name, prod_name, quantity, price, total) VALUES (?, ?, ?, ?, ?)",
    [
        ("Vinay",   "Laptop", 2, 1200.00, 2400.00),
        ("Rahul",   "Phone",  3, 800.00,  2400.00),
        ("Priya",   "Tablet", 1, 600.00,  600.00),
        ("Amit",    "Laptop", 1, 1500.00, 1500.00),
        ("Sneha",   "Phone",  2, 900.00,  1800.00),
        ("Rohit",   "Tablet", 4, 600.00,  2400.00),
        ("Neha",    "Laptop", 1, 1200.00, 1200.00),
    ]
)

conn.commit()
conn.close()

print("✅ Table recreated with new columns at:", db_path)