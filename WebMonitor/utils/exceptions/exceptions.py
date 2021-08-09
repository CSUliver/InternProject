from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _

class AuthenticationFailed(APIException):
    """
    认证失败
    """
    status_code = 401
    default_detail = _('Authentication Failed.')
    default_code = "401"