import sqlite3
import os

# path to your database
db_path = os.path.join(os.path.dirname(__file__), "SalesDB", "sales.db")

# connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# fetch all rows from sales table
cursor.execute("SELECT * FROM sales")

# fetchall() → returns all rows as a list of tuples
rows = cursor.fetchall()

# print each row
for row in rows:
    print(row)

conn.close()