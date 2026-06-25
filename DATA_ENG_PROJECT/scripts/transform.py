import pandas as pd

def transform(df):

    # remove duplicate rows
    df = df.drop_duplicates()

    # convert order_date to datetime
    df["order_date"] = pd.to_datetime(df["order_date"])

    # handle missing values
    df["sales_amount"] = df["sales_amount"].fillna(0)

    # clean product names
    df["product"] = df["product"].str.strip()

    # create new column (total revenue)
    df["total_revenue"] = df["sales_amount"] * df["quantity"]

    print("Data transformed successfully")
    print(df.head())

    return df


if __name__ == "__main__":

    df = pd.read_csv("data/raw_sales.csv")

    transform(df)