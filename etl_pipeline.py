import pandas as pd

# Extract
df = pd.read_csv('../data/patients.csv')

print("Original Data:")
print(df)

# Transform (Data Cleaning)
df = df.drop_duplicates()

df['name'] = df['name'].fillna('Unknown')
df['age'] = df['age'].fillna(df['age'].mean())
df['city'] = df['city'].fillna('Unknown')

# Data Quality Check
if df.isnull().sum().sum() == 0:
    print("No missing values ✅")
else:
    print("Data still has missing values ❌")

# Load
df.to_csv('../output/cleaned_patients.csv', index=False)

print("Cleaned data saved successfully!")