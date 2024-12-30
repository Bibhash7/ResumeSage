import json
import os
import logging
from django.shortcuts import render
from .constants import LoggedUserAttributes, ErrorMessage, SuccessMessage
from tasks.tasks import review_resume_in_background
from .models import LoggedUser
from django.http import JsonResponse
from utils import s3_file_upload_download as s3_operations
from django.views.decorators.csrf import csrf_exempt

logging.basicConfig(
    filename= os.environ.get("SERVER_LOG"),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='a'
)

logger = logging.getLogger(__name__)

def sign_up(request):
    """
    API for user sign up.
    :param request:
    :return: render template:
    """
    if request.method == 'GET':
        return render(
            request,
            template_name="ResumeSageApp/sign_up.html",
            status=200
        )
    if request.method == 'POST':
        try:
            email = request.POST.get(LoggedUserAttributes.EMAIL, LoggedUserAttributes.EMPTY_STRING)
            password = request.POST.get(LoggedUserAttributes.PASSWORD, LoggedUserAttributes.EMPTY_STRING)
            full_name = request.POST.get(LoggedUserAttributes.FULL_NAME, LoggedUserAttributes.EMPTY_STRING)

            if email == LoggedUserAttributes.EMPTY_STRING or password == LoggedUserAttributes.EMPTY_STRING:
                return render(
                    request,
                    template_name='ResumeSageApp/sign_up.html',
                    status=200
                )
            if (LoggedUser.objects.filter(email=email).exists()):
                logger.error(ErrorMessage.USER_ALREADY_EXISTS)
                return render(
                    request,
                    template_name='ResumeSageApp/sign_up.html',
                    context= ErrorMessage.USER_ALREADY_EXISTS,
                    status=400
                )
            else:
                LoggedUser.objects.create(email=email, password=password, full_name=full_name)
                return render(
                    request,
                    template_name='ResumeSageApp/sign_in.html',
                    context=SuccessMessage.USER_CREATED,
                    status=201
                )
        except Exception as error:
            logger.exception(error)
            return render(
                request,
                template_name="ResumeSageApp/internal_server_error.html",
                status=500
            )

def sign_in(request):
    """
    API for user sign in.
    :param request:
    :return render template:
    """
    if request.method == 'GET':
        return render(
            request,
            template_name='ResumeSageApp/sign_in.html',
            status=200
        )

    if request.method == 'POST':
        email = request.POST.get(LoggedUserAttributes.EMAIL, LoggedUserAttributes.EMPTY_STRING)
        password = request.POST.get(LoggedUserAttributes.PASSWORD, LoggedUserAttributes.EMPTY_STRING)
        try:
            if email == LoggedUserAttributes.EMPTY_STRING or password == LoggedUserAttributes.EMPTY_STRING:
                return render(
                    request,
                    template_name='ResumeSageApp/sign_in.html',
                    status=200
                )
            user_object = LoggedUser.objects.get(email=email)
            if user_object.validate_password(password):
                request.session[LoggedUserAttributes.EMAIL] = email
                request.session[LoggedUserAttributes.FULL_NAME] = user_object.full_name
                return render(
                    request, context=SuccessMessage.SIGN_IN_SUCCESSFUL,
                    template_name='ResumeSageApp/upload_file_to_s3.html',
                    status=200
                )
            else:
                logger.exception(ErrorMessage.INCORRECT_PASSWORD)
                return render(
                    request,
                    context=ErrorMessage.INCORRECT_PASSWORD,
                    template_name='ResumeSageApp/sign_in.html',
                    status=404
                )
        except LoggedUser.DoesNotExist:
            logger.error(LoggedUser.DoesNotExist)
            return render(
                request,
                context=ErrorMessage.USER_DOES_NOT_EXISTS,
                template_name='ResumeSageApp/sign_in.html',
                status=404
            )

        except Exception as error:
            logger.exception(error)
            return render(
                request,
                template_name="ResumeSageApp/internal_server_error.html",
                status=500
            )
    else:
        return render(
            request,
            template_name="ResumeSageApp/internal_server_error.html",
            status=500
        )

def sign_out(request):
    """
    API for sign out a session.
    :param request:
    :return render template:
    """
    try:
        request.session.flush()
        return render(
            request,
            template_name="ResumeSageApp/sign_in.html",
            context=SuccessMessage.SIGN_OUT_SUCCESSFUL,
            status=200
        )
    except Exception as error:
        logger.error(error)
        return render(
            request,
            template_name="ResumeSageApp/internal_server_error.html",
            status=500
        )

def home(request):
    """
    API for home page.
    :param request:
    :return render template:
    """
    try:
        return render(
            request,
            template_name="ResumeSageApp/index.html",
            status=200
        )
    except Exception as error:
        logger.error(error)
        return render(
            request,
            template_name="ResumeSageApp/internal_server_error.html",
            status=500
        )

def handle_unknown_routes(request):
    """
    API to handle unknown routes.
    :param request:
    :return render template:
    """
    try:
        return render(
            request,
            template_name="ResumeSageApp/unknown_routes.html",
            status=200
        )
    except Exception as error:
        logger.error(error)
        return render(
            request,
            template_name="ResumeSageApp/internal_server_error.html",
            status=500
        )
@csrf_exempt
def upload_file_to_s3(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            file_name = data.get(LoggedUserAttributes.FILE_NAME)
            s3_object = s3_operations.AwsLocalS3()
            presigned_url, file_name = s3_object.generate_upload_presigned_url(file_name)
            request.session[LoggedUserAttributes.FILE_NAME] = file_name
            if not presigned_url:
                return JsonResponse(ErrorMessage.PRESIGNED_URL_NOT_GENERATED, status=500)

            return JsonResponse({"presigned_url": presigned_url, "file_name": file_name}, status=200)

        except Exception as error:
            logger.error(error)
            return JsonResponse(ErrorMessage.PRESIGNED_URL_NOT_GENERATED, status=500)

def upload_page(request):
    try:
        return render(
            request,
            template_name="ResumeSageApp/upload_file_to_s3.html",
            status=200
        )
    except Exception as error:
        logger.error(error)
        return render(
            request,
            template_name="ResumeSageApp/internal_server_error.html",
            status=500
        )

def llm_review(request):
    try:
        email = request.session.get(LoggedUserAttributes.EMAIL)
        name = request.session.get(LoggedUserAttributes.FULL_NAME)
        file_name = request.session.get(LoggedUserAttributes.FILE_NAME)
        s3_object = s3_operations.AwsLocalS3()
        file_content = s3_object.read_file_from_s3(file_name)
        review_resume_in_background.delay(file_content, email, name)
        return render(
            request,
            template_name="ResumeSageApp/llm_review.html",
            status=200
        )
    except Exception as error:
        logger.error(error)
        print(error)
        return render(
            request,
            template_name="ResumeSageApp/internal_server_error.html",
            status=500
        )






















