import sys
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame.
Args:
path: Relative path to the CSV file.
Returns:
The loaded data.
"""
    return pd.read_csv(path, sep=",", encoding="utf-8-sig")

if __name__ == "__main__":
    print(load_data(sys.argv[1]).head())

def count_letters(str)
    counter = 0
    for i in str:
        counter += 1
    return counter
