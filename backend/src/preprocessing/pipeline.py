from pathlib import Path
from loader import load_data
from cleaner import clean_data
from timestamp import process_timestamps

DATA_PATH = Path("data/raw/SAML-D.csv")
DEV_ROWS = 2_000_000

def main():

    df = load_data(DATA_PATH, nrows=DEV_ROWS)
    df = clean_data(df)
    df = process_timestamps(df)

    print(df.head())
    print(df.dtypes)

main()