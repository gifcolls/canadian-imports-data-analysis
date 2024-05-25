import sqlite3

# Path to your SQLite database
db_path = 'C:/Users/berli/canadian-imports-data-analysis/data/canadian_imports.db'

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Verify tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", tables)

# Close the connection
conn.close()
