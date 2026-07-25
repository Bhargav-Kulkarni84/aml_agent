"""
    Creates a timestamp column and extracts
    basic time-based features.
"""

import pandas as pd

def process_timestamps(df: pd.DataFrame):

    print("\nProcessing timestamps...")

         # Rename columns (Everything Lowercase)
    df = df.rename(
        columns={
            "Time": "time",
            "Date": "date",
            "Sender_account": "sender_account",
            "Receiver_account": "receiver_account",
            "Amount": "amount",
            "Payment_currency": "payment_currency",
            "Received_currency": "received_currency",
            "Sender_bank_location": "sender_country",
            "Receiver_bank_location": "receiver_country",
            "Payment_type": "payment_type",
            "Is_laundering": "is_laundering",
            "Laundering_type": "laundering_type",
        }
    )

    # Merge Date and Time
    df["timestamp"] = pd.to_datetime(
        df["date"] + " " + df["time"],
        format="%Y-%m-%d %H:%M:%S"
    )

    # Remove old columns
    df = df.drop(columns=["date", "time"])

    # Sort chronologically
    df = df.sort_values("timestamp").reset_index(drop=True)

    print("Timestamp processing completed.")

    return df