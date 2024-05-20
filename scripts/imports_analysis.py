import pandas as pd
import numpy as np
import os

os.makedirs ('data', exist_ok=True)

#Loading the data
csv_files = ['https://drive.google.com/uc?export=download&id=1k-fn2pPNPY8rJZea_RLrbs5tMyK0DkQ8',
    'https://drive.google.com/uc?export=download&id=1HVezgDvQW1pHV-7l5FObBcIg3_1rbBpD',
    'https://drive.google.com/uc?export=download&id=1moc-jF6AtYw-1EXEKKqlt91WgN7T-cq1',
    'https://drive.google.com/uc?export=download&id=1JUI8nUnAy3Es2TbEczNO1hbt7j18df1V',
    'https://drive.google.com/uc?export=download&id=1kgIKquJ9KSbvmTpHJsFlpXZJnM5P-v9x']

#Reading the data
df_list = []
for file in csv_files:
    df = pd.read_csv(file)
    df_list.append(df)
    
#Concatenate all DataFrames
df_conbined = pd.concat(df_list, ignore_index=True)

#Display information
print(df_conbined.info())
print(df_conbined.head(25))
