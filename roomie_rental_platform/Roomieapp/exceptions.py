
from rest_framework.exceptions import APIException

class CustomAPIException(APIException):
    status_code = 400
    default_detail = 'A custom error message'
    default_code = 'custom_error'