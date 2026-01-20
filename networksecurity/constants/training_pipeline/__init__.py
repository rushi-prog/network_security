import os
import sys
import pandas as pd
import numpy as np 
"""defining common constants for training pipeline"""
TARGET_COLUMN:str = "Result"
PIPELINE_NAME:str = "NetworkSecurity"
ARTIFACTS_DIR:str = "Artifacts"
FILE_NAME:str = "phising_data.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

""" DATA ingestion related constant start with DATA_INGESTION VAR name """

DATA_INGESTION_COLLECTION_NAME:str = "NetworkData"
DATA_INGESTION_DATABASE_NAME:str = "OPQP"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested_data"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float = 0.2