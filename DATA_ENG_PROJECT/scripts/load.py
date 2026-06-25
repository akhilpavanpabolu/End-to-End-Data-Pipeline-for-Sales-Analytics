import pandas as pd
from sqlalchemy import create_engine

def load(df):

    engine = create_engine(
        "mysql+pymysql://root:%40Rajith%40123@localhost:3306/sales_db"
    )

    df.to_sql(
        name="sales",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded into MySQL successfully")


if __name__ == "__main__":

    df = pd.read_csv("data/raw_sales.csv")

    load(df)