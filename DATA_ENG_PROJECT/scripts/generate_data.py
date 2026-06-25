import pandas as pd
import random
from datetime import datetime, timedelta

products = ["Laptop", "Phone", "Tablet", "Chair", "Desk"]
categories = ["Electronics", "Furniture"]
regions = ["North", "South", "East", "West"]

rows = []

for i in range(50000):

    order_id = i + 1
    product = random.choice(products)
    category = random.choice(categories)
    region = random.choice(regions)
    sales_amount = random.randint(100, 2000)
    quantity = random.randint(1, 5)

    start_date = datetime(2023, 1, 1)
    order_date = start_date + timedelta(days=random.randint(0, 365))

    rows.append([
        order_id,
        product,
        category,
        region,
        sales_amount,
        quantity,
        order_date
    ])

df = pd.DataFrame(rows, columns=[
    "order_id",
    "product",
    "category",
    "region",
    "sales_amount",
    "quantity",
    "order_date"
])

df.to_csv("data/raw_sales.csv", index=False)

print("50,000 rows dataset generated")