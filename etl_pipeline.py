import pandas as pd
import logging

# Logging setup
logging.basicConfig(
    filename='etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    logging.info("ETL Job Started")

    # Extract
    df = pd.read_csv('../data/patients.csv')
    logging.info("Data extracted successfully")

    # Transform
    df = df.drop_duplicates()
    df['name'] = df['name'].fillna('Unknown')
    df['age'] = df['age'].fillna(df['age'].mean())
    df['city'] = df['city'].fillna('Unknown')

    # Data Quality Check
    if df.isnull().sum().sum() == 0:
        logging.info("No missing values found")
    else:
        logging.warning("Missing values still present")

    # Load
    df.to_csv('../output/cleaned_patients.csv', index=False)
    logging.info("Data loaded successfully")

except Exception as e:
    logging.error(f"ETL Job Failed: {e}")
