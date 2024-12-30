import io
import logging
import pdfplumber
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from utils.client_config import create_aws_local_service
from ResumeSageApp.constants import S3ErrorMessage, S3_RESUME_BUCKET
logger = logging.getLogger(__name__)

class AwsLocalS3:

    s3_client = create_aws_local_service("s3")
    bucket_name = S3_RESUME_BUCKET

    def get_object_path(self, file_name):
        """
        Creates the upstream path for the file uploaded in s3
        :param file_name: (str)
        :return: object_path (str)
        """
        object_path = f"resume/{file_name}"
        return object_path

    def generate_upload_presigned_url(self, file_name):
        """
        Generates upload presigned url for resume upload in s3 bucket.
        :param file_name: (str)
        :return: presigned_url (str)
        """
        try:
            file_extension = file_name.split(".")[1]
            if file_extension != "pdf":
                raise Exception(S3ErrorMessage.NOT_PDF_ERROR)
            object_path = self.get_object_path(file_name)
            presigned_url = self.s3_client.generate_presigned_url(
                'put_object',
                Params={'Bucket': self.bucket_name, 'Key': object_path},
                ExpiresIn=3600
            )
            return presigned_url, file_name

        except (NoCredentialsError, PartialCredentialsError) as error:
            logger.error(S3ErrorMessage.ERROR_GENERATING_PRESIGNED_URL.format(str(error)))
            return None, None

        except Exception as error:
            logger.error(S3ErrorMessage.SOMETHING_WENT_WRONG.format(error))
            return None, None

    def read_file_from_s3(self, file_name):
        """
        Reads the file content from S3 bucket.
        :param file_name: (str)
        :return: text_content (str)
        """
        try:
            s3_client = create_aws_local_service("s3")
            bucket_name = S3_RESUME_BUCKET
            file_extension = file_name.split(".")[1]
            if file_extension != "pdf":
                raise Exception(S3ErrorMessage.NOT_PDF_ERROR)
            object_path = self.get_object_path(file_name)
            response = s3_client.get_object(Bucket=bucket_name, Key=object_path)
            file_content = response['Body'].read()
            with pdfplumber.open(io.BytesIO(file_content)) as pdf:
                text_content = ""
                for page in pdf.pages:
                    text_content += page.extract_text()
            return text_content

        except (NoCredentialsError, PartialCredentialsError) as error:
            logger.error(S3ErrorMessage.ERROR_GENERATING_PRESIGNED_URL.format(str(error)))
            return None

        except Exception as error:
            logger.error(S3ErrorMessage.SOMETHING_WENT_WRONG.format(error))
            return None











