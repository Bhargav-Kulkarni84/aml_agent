"""
    Generate transaction-level features used for AML detection.
    Parameters df : pd.DataFrame Input transaction dataframe.
    Returns pd.DataFrame : Dataframe with additional transaction features.
"""

import pandas as pd

def generate_transaction_features(df: pd.DataFrame):

    print("\nGenerating transaction features...")

    # Cross-border transaction
    df["is_cross_border"] = (
        df["sender_country"] != df["receiver_country"]
    )

    # Currency conversion
    df["currency_changed"] = (
        df["payment_currency"] != df["received_currency"]
    )

    # Self transfer
    df["is_self_transfer"] = (
        df["sender_account"] == df["receiver_account"]
    )

    # Payment type flags
    df["is_cash_deposit"] = (
        df["payment_type"] == "Cash Deposit"
    )

    df["is_cash_withdrawal"] = (
        df["payment_type"] == "Cash Withdrawal"
    )

    df["is_cheque"] = (
        df["payment_type"] == "Cheque"
    )

    df["is_ach"] = (
        df["payment_type"] == "ACH"
    )

    df["is_credit_card"] = (
        df["payment_type"] == "Credit card"
    )

    df["is_debit_card"] = (
        df["payment_type"] == "Debit card"
    )

    print("Transaction features generated.")

    return df