import os
import sys
import json
from dotenv import load_dotenv

import pandas as pd
import pymongo
import certifi

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

if MONGO_DB_URL is None:
    raise ValueError("MONGO_DB_URL not found in .env file")


# --------------------------------------------------
# Data Extraction Class
# --------------------------------------------------
class NetworkDataExtract:

    def __init__(self):
        try:
            self.ca_file = certifi.where()
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_converter(self, file_path: str):
        try:
            logging.info("Reading CSV file")

            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)

            records = list(json.loads(data.T.to_json()).values())

            logging.info(f"Converted {len(records)} records to JSON")
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, database: str, collection: str, records: list):
        try:
            logging.info("Connecting to MongoDB Atlas")

            mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tls=True,
                tlsCAFile=self.ca_file,
                serverSelectionTimeoutMS=30000
            )

            db = mongo_client[database]
            col = db[collection]

            result = col.insert_many(records)

            logging.info("Data inserted successfully")
            return len(result.inserted_ids)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


# --------------------------------------------------
# Main Execution
# --------------------------------------------------
if __name__ == "__main__":
    try:
        FILE_PATH = r"Network_Data/phisingData.csv"
        DATABASE = "OPQP"
        COLLECTION = "NetworkData"

        network_obj = NetworkDataExtract()

        records = network_obj.csv_to_json_converter(FILE_PATH)
        print(records[:2])  # preview first 2 records

        no_of_records = network_obj.insert_data_mongodb(
            DATABASE,
            COLLECTION,
            records
        )

        print(f"Inserted {no_of_records} records successfully")

    except Exception as e:
        raise NetworkSecurityException(e, sys)
