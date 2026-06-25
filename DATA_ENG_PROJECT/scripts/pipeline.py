# from extract import extract
# from transform import transform
# from load import load

# FILE_PATH = "data/raw_sales.csv"

# def run_pipeline():

#     print("Starting ETL pipeline...")

#     raw_data = extract(FILE_PATH)

#     clean_data = transform(raw_data)

#     load(clean_data)

#     print("ETL Pipeline completed successfully!")

# if __name__ == "__main__":
#     run_pipeline()

import logging
from extract import extract
from transform import transform
from load import load

FILE_PATH = "data/raw_sales.csv"

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():

    logging.info("Starting ETL pipeline")

    raw_data = extract(FILE_PATH)
    logging.info("Data extracted")

    clean_data = transform(raw_data)
    logging.info("Data transformed")

    load(clean_data)
    logging.info("Data loaded into database")

    logging.info("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()