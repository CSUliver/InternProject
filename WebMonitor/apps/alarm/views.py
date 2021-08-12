from django.shortcuts import render

from rest_framework.generics import ListAPIView,CreateAPIView
from .models import InfectRisk,InfectAlarm
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RiskDataFilter,AlarmDataFilter
from rest_framework.parsers import MultiPartParser

# Create your views here.

class RiskDataView(ListAPIView,CreateAPIView):
    queryset = InfectRisk.objects.all().extra(select={'time': "DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s')"})
    serializer_class = RiskDataSerializer
    # 使用自定义过滤器对数据进行时间段的搜索
    filter_backends = [DjangoFilterBackend]
    filter_class = RiskDataFilter
    parser_classes = [MultiPartParser]  # 重新指定解析器

class AlarmDataView(ListAPIView,CreateAPIView):
    queryset = InfectAlarm.objects.all().extra(select={'time': "DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s')"})
    serializer_class = AlarmDataSerializer
    # 使用自定义过滤器对数据进行时间段的搜索
    filter_backends = [DjangoFilterBackend]
    filter_class = AlarmDataFilter
    parser_classes = [MultiPartParser]  # 重新指定解析器