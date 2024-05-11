# Canadian Imports Data Analysis Project

## Objective
The objective of this project is to discover patterns and trends from the top 25 industries (based on 5-digit NAICS codes) in Canadian imports over the last 5 years. Additionally, we aim to predict import trends for the current year using statistical models.

## Project Structure

- `clean_data.py`: Python script for cleaning the data and making predictions. This script performs the following tasks:
  - Loads the raw data directly from Google Drive.
  - Cleans the data by handling missing values, removing duplicates, and converting data types.
  - Saves the cleaned data.
  - Implements a simple linear regression model to predict import values for the current year.

- `data/`: Directory that will contain the cleaned data file.
  - The cleaned data will be saved in this directory as `cleaned_data.csv`.

- `README.md`: Project documentation, including the objective, structure, setup instructions, and usage.

- `requirements.txt`: List of dependencies required for the project. The dependencies include:
  - `pandas`: For data manipulation and analysis.
  - `numpy`: For numerical operations.
  - `scikit-learn`: For implementing the linear regression model.

## Data Source
The data for this project comes from Trade Data Online, managed by Innovation, Science and Economic Development Canada. The dataset includes import values for various industries in Canada over the past five years.

You can access the raw data directly from this link:
- [Raw Data on Google Drive](https://drive.google.com/drive/u/1/folders/1UnMtmHZlEciara7YOu3LJOBTwmWyhpE2)

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gifcolls/canadian-imports-data-analysis.git
   cd canadian-imports-data-analysis

