import json
import logging
from utils.client_config import create_aws_local_service
from ResumeSageApp.constants import ErrorMessage

logger = logging.getLogger(__name__)

def get_db_secrets(secret_name):
    """
    This will fetch the db credentials from aws secret manager.
    :param secret_name (str)
    :return: json
    """
    secret_manager_client = create_aws_local_service("secretsmanager")
    try:
        response = secret_manager_client.get_secret_value(SecretId=secret_name)
        secret_string = response.get("SecretString", "{}")
        return json.loads(secret_string)
    except Exception as error:
        logger.error(ErrorMessage.ERROR_FETCHING_SECRETS.format(str(error)))
        return {}