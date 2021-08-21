from django.shortcuts import render

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from .models import Monitor,MonitorData
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MonitorDataFilter
from rest_framework import filters
from rest_framework.parsers import MultiPartParser
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class SelfPagination(PageNumberPagination):
    page_size = 5  # 默认每页显示5条数据
    page_size_query_param = 'page_size' # 自定义每页显示条数的请求参数->  ./?page_size=10
    max_page_size = 20
    page_query_param = 'page' # 分页请求参数变量名-> ./?page_size=10&page=2

class MonitorCreateListView(ListAPIView,CreateAPIView):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
    parser_classes = [MultiPartParser]  # 重新指定解析器
    # 列表分页功能
    pagination_class = SelfPagination

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
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filter_class = MonitorDataFilter
    parser_classes = [MultiPartParser]  # 重新指定解析器
    # 列表分页功能
    pagination_class = SelfPagination
    # 搜索
    search_fields = ('person_name',)  # 指定模糊查询匹配的列