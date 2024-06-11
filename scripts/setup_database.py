import pandas as pd
from sqlalchemy import create_engine
import sqlite3

# Database connection with absolute path
db_path = 'C:/Users/berli/canadian-imports-data-analysis/data/canadian_imports.db'
engine = create_engine(f'sqlite:///{db_path}')

# File paths
file_paths = [
    '../data/raw/Imports_2019.csv',
    '../data/raw/Imports_2020.csv',
    '../data/raw/Imports_2021.csv',
    '../data/raw/Imports_2022.csv',
    '../data/raw/Imports_2023.csv'
]
years = range(2019, 2024)

for file_path in file_paths:
    df = pd.read_csv(file_path, skiprows=6, header=None)
print(f"First few raws of the data from {file_path}:")
print(df.head())
df.to_sql('raw_imports', con=engine, if_exists='append', index=False)
print("Data loaded successfully into the database.")

# Verify table creation and data insertion
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", tables)
conn.close()
