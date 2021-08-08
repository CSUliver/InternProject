from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    """
    自定义异常处理函数（需要在setting中配置）
    :param exc :异常对象
    :param context:长下文
    :return:返回response对象
    """
    response = exception_handler(exc, context)
    # print('type exec:',type(exc))
    if response is not None:
        data = {
            'code': response.status_code,
            'msg': str(exc),
        }
        return Response(data=data, status=response.status_code)
    else:
        data = {
            'code': 400,
            'msg': str(exc)
        }
        return Response(data=data, status=400)