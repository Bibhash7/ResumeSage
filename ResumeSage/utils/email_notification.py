from django.core.mail import EmailMessage
import logging

def send_email_notification(subject,body,recipients):
    """
    Send the review result to the recipient via email.
    :param subject: (Str)
    :param body: (Str)
    :param recipients: (List)
    :return: None
    """
    try:
        email = EmailMessage(subject, body, to=recipients)
        email.send()
    except Exception as error:
        logging.error(error)