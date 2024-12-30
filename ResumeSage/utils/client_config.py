import boto3
from botocore.config import Config
import os
from dotenv import load_dotenv
def create_aws_local_service(service_name):
    """
    This function creates s3 service based on passed service name.
    PS: Although the secrets should be read from a env file, keeping it for future reference.
    :param service_name:
    :return: aws_service
    """
    load_dotenv()
    client = boto3.client(
        service_name,
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        endpoint_url=os.environ.get("LOCALSTACK_ENDPOINT_URL"),
        config=Config(signature_version="s3v4"),
        region_name=os.environ.get("AWS_REGION")
    )
    return client