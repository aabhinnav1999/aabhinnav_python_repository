import os, dotenv
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

dotenv.load_dotenv(dotenv.find_dotenv())

# using DefaultAzureCredential and role assignment
container = BlobServiceClient(account_url=os.getenv("storage_account_url"),
                                   credential=DefaultAzureCredential()).get_container_client(os.getenv("container_name"))

def get_blobs():
    try:

        blob_list = container.list_blobs()
        for blob in blob_list:
            print("\t" + blob.name)


    except Exception as e:
        print('Exception:')
        print(e)

# using connection string

blob_client = BlobServiceClient.from_connection_string(os.getenv("AZURE_STORAGE_CONNECTION_STRING"))
container_client = blob_client.get_container_client(os.getenv("container_name"))

def get_blob_2():

    for blob in container_client.list_blobs():
        print("\t" + blob.name)

# print(get_blob_2())

# upload blob
def upload_blob(file_name):

    try:
        
        with open(file_name, "rb") as data:
            container_client.upload_blob(name=os.path.basename(file_name), data=data)

        print(f"Blob {file_name} uploaded successfully.")

    except Exception as e:
        print('Exception:')
        print(e)

# print(upload_blob(os.getenv("file_name")))

# using managed identity and service principal

# from azure.identity import DefaultAzureCredential
# from azure.storage.blob import BlobServiceClient

# ACCOUNT_URL = "https://abhinavkvdsa.blob.core.windows.net"
# CONTAINER = "demo"

# credential = DefaultAzureCredential()
# service = BlobServiceClient(account_url=ACCOUNT_URL, credential=credential)
# container_client = service.get_container_client(CONTAINER)

# for blob in container_client.list_blobs():
#     print(blob.name)


