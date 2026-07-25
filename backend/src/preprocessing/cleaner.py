'''
    This file will 
    Remove duplicates
    Handle missing values
    Validate Amount
    Validate Sender/Receiver
    Reset index
'''

import pandas as pd

def clean_data(df: pd.DataFrame):

    print("\nCleaning dataset...")

    # Remove duplicate rows
    before = len(df)
    df = df.drop_duplicates()

    print(f"Removed {before - len(df)} duplicate rows.")

    # Remove rows with missing values
    before = len(df)
    df = df.dropna()

    print(f"Removed {before - len(df)} rows with missing values.")

    # Remove invalid transaction amounts
    before = len(df)
    df = df[df["Amount"] > 0]

    print(f"Removed {before - len(df)} rows with invalid amounts.")

    # Reset index
    df = df.reset_index(drop=True)

    print(f"Final dataset size: {len(df)};,")

    return df