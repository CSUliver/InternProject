from django.shortcuts import render

from rest_framework.generics import ListAPIView,CreateAPIView
from .models import InfectRisk,InfectAlarm
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RiskDataFilter,AlarmDataFilter
from rest_framework.parsers import MultiPartParser
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class SelfPagination(PageNumberPagination):
    page_size = 5  # 默认每页显示5条数据
    page_size_query_param = 'page_size' # 自定义每页显示条数的请求参数->  ./?page_size=10
    max_page_size = 20
    page_query_param = 'page' # 分页请求参数变量名-> ./?page_size=10&page=2

class RiskDataView(ListAPIView,CreateAPIView):
    queryset = InfectRisk.objects.all().extra(select={'time': "DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s')"})
    serializer_class = RiskDataSerializer
    # 使用自定义过滤器对数据进行时间段的搜索
    filter_backends = [DjangoFilterBackend]
    filter_class = RiskDataFilter
    parser_classes = [MultiPartParser]  # 重新指定解析器
    # 列表分页功能
    pagination_class = SelfPagination

class AlarmDataView(ListAPIView,CreateAPIView):
    queryset = InfectAlarm.objects.all().extra(select={'time': "DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s')"})
    serializer_class = AlarmDataSerializer
    # 使用自定义过滤器对数据进行时间段的搜索
    filter_backends = [DjangoFilterBackend]
    filter_class = AlarmDataFilter
    parser_classes = [MultiPartParser]  # 重新指定解析器
    # 列表分页功能
    pagination_class = SelfPagination