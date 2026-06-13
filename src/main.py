import sys
import os
from load.postgres_loader import load_to_postgres
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from config.config import *
from extract.blob_reader import read_blob



from transform.data_cleaner import clean_data


df = read_blob(
    CONNECTION_STRING,
    CONTAINER_NAME,
    BLOB_NAME
)
df = clean_data(df)
print(df.head())
print("\nRows:", len(df))
print(df.columns)

df = read_blob(
    CONNECTION_STRING,
    CONTAINER_NAME,
    BLOB_NAME
)

df = clean_data(df)

print(df.head())
print("\nRows:", len(df))
print(df.columns)

load_to_postgres(df)