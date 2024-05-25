import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import os


def clean_data(df):
    df.columns = ['Category', 'Value', 'Year']
    df = df.dropna(subset=['Category']).copy()
    df.loc[:, 'Value'] = df['Value'].replace(
        '[\$,]', '', regex=True).astype(float)
    return df


# Database connection with absolute path
db_path = 'C:/Users/berli/canadian-imports-data-analysis/data/canadian_imports.db'
engine = create_engine(f'sqlite:///{db_path}')

# Connect to the database
conn = sqlite3.connect(db_path)

# Query raw data
query = "SELECT * FROM raw_imports"
df_raw = pd.read_sql_query(query, conn)

# Clean data
df_cleaned = clean_data(df_raw)

# Cleaned data directory exists
cleaned_data_dir = '../data/cleaned'

# Save cleaned data to CSV
cleaned_path = os.path.join(cleaned_data_dir, 'cleaned_imports.csv')
df_cleaned.to_csv(cleaned_path, index=False)
print(f"Cleaned data saved to {cleaned_path}")

# Load cleaned data into the database
df_cleaned.to_sql('cleaned_imports', con=engine,
                  if_exists='replace', index=False)
print("Cleaned data loaded successfully into the database.")

# Verify cleaned data insertion
query = "SELECT * FROM cleaned_imports LIMIT 10"
df_check = pd.read_sql_query(query, conn)
print("First 10 rows from the cleaned_imports table:")
print(df_check)

conn.close()
