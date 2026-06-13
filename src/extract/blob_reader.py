from azure.storage.blob import BlobServiceClient
from io import StringIO
import pandas as pd

def read_blob(connection_string, container, blob):

    client = BlobServiceClient.from_connection_string(
        connection_string
    )

    blob_client = client.get_blob_client(
        container=container,
        blob=blob
    )

    data = blob_client.download_blob().readall()

    df = pd.read_csv(
        StringIO(data.decode("utf-8"))
    )

    return df