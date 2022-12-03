from google.cloud import storage
from google.cloud.storage import Blob

import os
import pathlib as Path
import sys
import json
from dotenv import load_dotenv


load_dotenv("/etc/gcp.env") ## env file

BUCKET = os.getenv('BUCKET')
DEV = os.getenv('DEV')
PROD = os.getenv('PROD')
TEST = os.getenv('TEST')

projectname = os.getenv('PROJECTNAME')

try:
    if sys.argv[1] == "prod":
        print("Deploying to PROD environment.")
        environment = PROD
        en = "prod"
    elif sys.argv[1] == "ua":
        print("Deploying to UA environment.")
        environment = TEST
        en = "ua"
    else:
        print("Deploying to DEV environment.")
        environment = DEV
        en = "dev"
except:
    print("Deploying to DEV environment.")
    environment = DEV
    en = "dev"


def updateManifest(envi):
    BASE_DIR = os.path.abspath(".")
    ff = open(f"{BASE_DIR}/src/manifest.json")
    data = json.load(ff)
    ff.close()

    data["components"][0]["resource"]["js"] = f"gs://{BUCKET}/gds/{envi}/{projectname}/index.js"
    data["components"][0]["resource"]["config"] = f"gs://{BUCKET}/gds/{envi}/{projectname}/index.json"
    data["components"][0]["resource"]["css"] = f"gs://{BUCKET}/gds/{envi}/{projectname}/index.css"
    
    with open(f"{BASE_DIR}/src/manifest.json", "w") as outfile:
        json.dump(data, outfile, indent=4)

updateManifest(en)
    
###

def upload_blob(bucket_name:str, source_file_name:str, destination_blob_name:str, acl:str):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"
    # acl = "public-read, public-read-write, authenticated-read, project-private, bucket-owner-full-control, bucket-owner-read, private"


    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name, predefined_acl=acl)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

# get_files(BUCKET, DEV)


def deploy(environment):
    BASE_DIR = os.path.abspath(".")
    for file in os.listdir(f"{BASE_DIR}/src/"):
        filepath = f"{BASE_DIR}/src/{file}"
        if os.path.isdir(filepath) != True:
            destination = f"{environment}{file}"
            upload_blob(BUCKET,filepath,destination,"public-read")


if __name__ == "__main__":
    updateManifest(en)
    deploy(
        environment=environment,
    )