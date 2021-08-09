import json
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext
from rest_framework.response import Response
from django.http import HttpResponse
from coreapi import Document
from django.conf import settings


class ResponseMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if not isinstance(response, Response):
            if response.status_code in [ 404 ]: # 处理 路径错误
                data = dict()
                data['code'] = 404
                data['msg'] = gettext('URL ERROR')
                return HttpResponse(json.dumps(data), content_type='json')
            return response

        # 对成功的响应 增加 code/msg 字段
        if response.status_code in [ 200, 201, 204 ]:
            if isinstance(response.data, Document):
                return response
            try:
                data = dict()
                if isinstance(response.data, list):
                    data['results'] = response.data
                elif isinstance(response.data, dict):
                    data = response.data
                elif response.data is None:
                    pass
                data['code'] = 200
                data['msg'] = _('OK')
                response.status_code = 200
                response.data = data
                response._is_rendered = False
                response.render()
            except Exception as e:
                # print('e', e)
                pass
        return response

    def process_exception(self, request, exception):
        if settings.DEBUG:
            print('process_exception', exception) # 异常记录
        data = dict()
        data['code'] = 400
        data['msg'] = str(exception)
        return HttpResponse(json.dumps(data), content_type='json')