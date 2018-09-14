from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status

def custom_exception_handler(exc,context):
    response = exception_handler(exc,context) #获取本来应该返回的exception的response
    # if response is not None:
    #     #response.data['status_code'] = response.status_code  #可添加status_code
    #     try:
    #         response.data['message'] = response.data['detail']    #增加message这个key
    #         del response.data['detail']
    #     except:pass
    return response


class myException(APIException):
    # from apps.User.utils.exceptions import exception
    status_code = status.HTTP_401_UNAUTHORIZED

class myException401(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
class myException500(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
