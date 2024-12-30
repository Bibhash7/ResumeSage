import re
import logging
import utils.email_notification as email
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from ResumeSageApp.constants import GEMMA_2B_MODEL, ErrorMessage, SuccessMessage
from prompts.gen_ai_prompts import SYSTEM_PROMPT, USER_PROMPT
from utils.format_email_body import format_message


logger = logging.getLogger(__name__)

def review_resume(content, receiver_email, name):
    """
    Function to review a resume.
    :param content: (str)
    :param receiver_email: (str)
    :param name: (str)
    :returns None
    """
    try:
        llm = ChatOllama(model=GEMMA_2B_MODEL)
        prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    SYSTEM_PROMPT
                ),
                (
                    "human",
                    USER_PROMPT
                )
            ]
        )

        review_chain = prompt_template | llm
        response = review_chain.invoke({"context": content})
        email.send_email_notification(
            f"ResumeSage Resume Review: {name}",
            format_message(response.content),
            [receiver_email]
        )
        logger.info(SuccessMessage.REVIEWED_AND_SENT_EMAIL)

    except Exception as error:
        logger.error(ErrorMessage.REVIEW_OR_EMAIL_ERROR.format(str(error)))
