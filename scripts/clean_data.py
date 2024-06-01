import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def clean_data(df, year):
    df.columns = ['Category', 'Value']
    df['Year'] = year
    df = df.dropna(subset=['Category']).copy()

    # Filter out rows where 'Category' contains 'Total' or 'Source'
    df = df[~df['Category'].str.contains('Total|Source', case=False, na=False)]

    # Ensure 'Value' column is numeric, coercing errors to NaN
    df['Value'] = df['Value'].replace('[\$,]', '', regex=True)
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    return df


# Database connection with absolute path
db_path = 'C:/Users/berli/canadian-imports-data-analysis/data/canadian_imports.db'
engine = create_engine(f'sqlite:///{db_path}')

# Connect to the database
conn = sqlite3.connect(db_path)

# File paths and corresponding years
file_paths = [
    '../data/raw/Imports_2019.csv',
    '../data/raw/Imports_2020.csv',
    '../data/raw/Imports_2021.csv',
    '../data/raw/Imports_2022.csv',
    '../data/raw/Imports_2023.csv'
]
years = [2019, 2020, 2021, 2022, 2023]

# Initializing an empty DataFrame to store cleaned data
df_cleaned_total = pd.DataFrame()

for file_path, year in zip(file_paths, years):
    df_raw = pd.read_csv(file_path, skiprows=6, header=None)
    df_cleaned = clean_data(df_raw, year)
    df_cleaned_total = pd.concat(
        [df_cleaned_total, df_cleaned], ignore_index=True)

# Additional Data Cleaning Steps
# Check for missing values
missing_values = df_cleaned_total.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Handle missing values
df_cleaned_total['Value'] = df_cleaned_total['Value'].fillna(
    df_cleaned_total['Value'].mean())

# Check for duplicates
duplicate_rows = df_cleaned_total.duplicated().sum()
print("Number of duplicate rows:", duplicate_rows)

# Remove duplicates
df_cleaned_total = df_cleaned_total.drop_duplicates()

# Convert 'Year' column to integer
df_cleaned_total['Year'] = df_cleaned_total['Year'].astype(int)

# Convert 'Value' column to float 
df_cleaned_total['Value'] = df_cleaned_total['Value'].astype(float)

# Handling Outliers
# Calculate the Z-scores of the 'Value' column
z_scores = np.abs(
    (df_cleaned_total['Value'] - df_cleaned_total['Value'].mean()) / df_cleaned_total['Value'].std())
outliers = z_scores > 3  # Consider values with Z-score > 3 as outliers
print("Number of outliers:", np.sum(outliers))

# Display outliers
print("Outliers:")
print(df_cleaned_total[outliers])


def remove_outliers(df):
    while True:
        z_scores = np.abs(
            (df['Value'] - df['Value'].mean()) / df['Value'].std())
        outliers = z_scores > 3  # Consider values with Z-score > 3 as outliers
        if not outliers.any():
            break
        df = df[~outliers]
    return df


# Removing outliers iteratively
df_cleaned_total = remove_outliers(df_cleaned_total)

# Reseting index to ensure proper alignment
df_cleaned_total.reset_index(drop=True, inplace=True)

# Verifying the number of outliers after removal
z_scores_after = np.abs(
    (df_cleaned_total['Value'] - df_cleaned_total['Value'].mean()) / df_cleaned_total['Value'].std())
outliers_after = z_scores_after > 3
print("Number of outliers after removal:", np.sum(outliers_after))

# Display remaining outliers, if any
outliers_remaining_df = df_cleaned_total[outliers_after]
print("Remaining outliers after removal:")
print(outliers_remaining_df.head(10))

# Ensuring the cleaned data directory exists
cleaned_data_dir = '../data/cleaned'
if not os.path.exists(cleaned_data_dir):
    os.makedirs(cleaned_data_dir)

# Save cleaned data to CSV
cleaned_path = os.path.join(cleaned_data_dir, 'cleaned_imports.csv')
df_cleaned_total.to_csv(cleaned_path, index=False)
print(f"Cleaned data saved to {cleaned_path}")

# Load cleaned data into the database
df_cleaned_total.to_sql('cleaned_imports', con=engine,
                        if_exists='replace', index=False)
print("Cleaned data loaded successfully into the database.")

# Verify cleaned data insertion
query = "SELECT * FROM cleaned_imports LIMIT 10"
df_check = pd.read_sql_query(query, conn)
print("First 10 rows from the cleaned_imports table:")
print(df_check)

conn.close()
