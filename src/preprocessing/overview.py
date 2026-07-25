import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "SAML-D.csv"

df = pd.read_csv(DATA_PATH, nrows=2000000)

print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print(df["Is_laundering"].value_counts())
print(df["Is_laundering"].value_counts(normalize=True) * 100)

print(df["Laundering_type"].value_counts())