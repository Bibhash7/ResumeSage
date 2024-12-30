from celery import shared_task
import logging
from utils.review_resume_llm import review_resume
from ResumeSageApp.constants import ErrorMessage, SuccessMessage
logger = logging.getLogger(__name__)

@shared_task(name="LLM_Resume_Review")
def review_resume_in_background(content, email, name):
    try:
        review_resume(content, email, name)
        logger.info(SuccessMessage.TASK_EXECUTED_SUCCESSFULLY)
    except Exception as error:
        logger.error(ErrorMessage.TASK_QUEUE_ERROR.format(str(error)))


