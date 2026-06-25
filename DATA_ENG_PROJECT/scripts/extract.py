import pandas as pd

def extract(file_path):

    df = pd.read_csv(file_path)

    print("Data extracted successfully")
    print(df.head())

    return df


if __name__ == "__main__":
    extract("data/raw_sales.csv")