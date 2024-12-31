

S3_RESUME_BUCKET = "resumesagebucket"

GEMMA_2B_MODEL = "gemma:2b"

class S3ErrorMessage:
    ERROR_GENERATING_PRESIGNED_URL = "Error generating pre-signed URL: {}"
    SOMETHING_WENT_WRONG = "Something went wrong {}"
    NOT_PDF_ERROR = "Accepted file format is .pdf"

class LoggedUserAttributes:
    EMAIL = 'email'
    PASSWORD = 'password'
    EMPTY_STRING = ""
    DATA = "data"
    COUNT = "count"
    ERROR = "error"
    INTERNAL_SERVER_ERROR = "internal server error."
    FILE_NAME = "file_name"
    FULL_NAME = "full_name"

class ErrorMessage:
    USER_ALREADY_EXISTS = {"success": False, "message": "User already exists in DB."}
    INCORRECT_PASSWORD = {"success": False, "message": "Invalid username or password."}
    USER_DOES_NOT_EXISTS = {"success": False, "message": "User does not exists, please sign up."}
    INVALID_FORMAT = {"success": False, "message": "Provide a string of alphabetic characters only, allowing underscores; comma, space or newline-separated."}
    PRESIGNED_URL_NOT_GENERATED = {"error": "Could not generate presigned URL."}
    REVIEW_OR_EMAIL_ERROR = "An error occurred while reviewing resume: {}"
    TASK_QUEUE_ERROR = "An error occurred in Celery Task Queue. {}"
    ERROR_FETCHING_SECRETS = "An error occurred while fetching secrets: {}"
class SuccessMessage:
    USER_CREATED = {"success": True, "message": "User Created."}
    CONSTANT_CLASS_GENERATED ={"success": True,"message": "Constant class generated."}
    SIGN_IN_SUCCESSFUL = {"success": True, "message": "Successfully signed in."}
    SIGN_OUT_SUCCESSFUL = {"success": True, "message": "Successfully signed out."}
    REVIEWED_AND_SENT_EMAIL = "Resume reviewed successfully, please check email."
    TASK_EXECUTED_SUCCESSFULLY = "The Celery task executed successfully."
