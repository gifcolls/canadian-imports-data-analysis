import pandas as pd
import os
import numpy as np

# List of csv files with direct download links
csv_files = [
    # id_2019 = 1k-fn2pPNPY8rJZea_RLrbs5tMyK0DkQ8
    'https://drive.google.com/uc?export=download&id=1k-fn2pPNPY8rJZea_RLrbs5tMyK0DkQ8',
    # id_2020 = 1HVezgDvQW1pHV-7l5FObBcIg3_1rbBpD
    'https://drive.google.com/uc?export=download&id=1HVezgDvQW1pHV-7l5FObBcIg3_1rbBpD',
    # id_2021 = 1moc-jF6AtYw-1EXEKKqlt91WgN7T-cq1
    'https://drive.google.com/uc?export=download&id=1moc-jF6AtYw-1EXEKKqlt91WgN7T-cq1',
    # id_2022 = 1JUI8nUnAy3Es2TbEczNO1hbt7j18df1V
    'https://drive.google.com/uc?export=download&id=1JUI8nUnAy3Es2TbEczNO1hbt7j18df1V',
    # id_2023 = 1kgIKquJ9KSbvmTpHJsFlpXZJnM5P-v9x
    'https://drive.google.com/uc?export=download&id=1kgIKquJ9KSbvmTpHJsFlpXZJnM5P-v9x'
]

#Combining all the CSV files into a one dataframe
df_list = []
for file in csv_files:
    df = pd.read_csv(file)
    df_list.append(df)

#Concatenate all dataframes
combined_df= pd.concat(df_list, ignore_index=True)

#Display the information
print(combined_df.info())
print(combined_df.head())

#Check for missing values
print(combined_df.isnull().sum())

#Fill missing vlues
for column in combined_df.select_dtypes(include=[np.number]).columns:
    combined_df[column].fillna(combined_df[column].mean(), inplace=True)
    

#Rmove duplicates
combined_df.drop_duplicates(inplace=True)

#Convert date column to datetime format
combined_df['Year'] = pd.to_datetime(combined_df['Year'], format='%Y')

#Save cleaned data
combined_df.to_csv('data/cleaned_data.csv', index=False)
