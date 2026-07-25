from pathlib import Path
import pandas as pd

# This function returns a dataframe consisting of nrows (default all rows) from the dataset
def load_data(file_path: Path, nrows: int | None = None):

    print(f"Loading dataset from {file_path}")

    df = pd.read_csv(
        file_path,
        nrows=nrows
    )

    print(f"Loaded {len(df)} transactions")

    return df



# DATA_PATH = Path("data/raw/SAML-D.csv")
# df = load_data(DATA_PATH, 1000)

# print(df)