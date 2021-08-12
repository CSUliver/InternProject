from django.shortcuts import render

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from .models import Monitor,MonitorData
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MonitorDataFilter
from rest_framework.parsers import MultiPartParser

# Create your views here.

class MonitorCreateListView(ListAPIView,CreateAPIView):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
    parser_classes = [MultiPartParser]  # 重新指定解析器

class MonitorRetriveUpdateDeleteView(RetrieveAPIView,DestroyAPIView,UpdateAPIView):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
    lookup_url_kwarg = "pk"
    parser_classes = [MultiPartParser]  # 重新指定解析器


class MonitorDataView(ListAPIView,CreateAPIView):
    # 直接对日期格式化
    queryset = MonitorData.objects.all().extra(select={'time': "DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s')"})
    serializer_class = MonitorDataSerializer
    # 使用自定义过滤器对数据进行时间段的搜索
    filter_backends = [DjangoFilterBackend]
    filter_class = MonitorDataFilter
    parser_classes = [MultiPartParser]  # 重新指定解析器