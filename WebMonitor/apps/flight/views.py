from django.shortcuts import render

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from .models import Flight,TakeFlight
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FlightFilter
from rest_framework import filters
from rest_framework.parsers import MultiPartParser
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class SelfPagination(PageNumberPagination):
    page_size = 5  # 默认每页显示5条数据
    page_size_query_param = 'page_size' # 自定义每页显示条数的请求参数->  ./?page_size=10
    max_page_size = 20
    page_query_param = 'page' # 分页请求参数变量名-> ./?page_size=10&page=2

class FlightCreateListView(ListAPIView,CreateAPIView):
    queryset = Flight.objects.all().extra(select={'begin_time': "DATE_FORMAT(begin_time,'%%Y-%%m-%%d %%H:%%i:%%s')"})\
        .extra(select={'end_time': "DATE_FORMAT(end_time,'%%Y-%%m-%%d %%H:%%i:%%s')"})
    serializer_class = FlightSerializer
    # 使用自定义过滤器对数据进行时间段的搜索
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filter_class = FlightFilter
    parser_classes = [MultiPartParser]  # 重新指定解析器
    # 列表分页功能
    pagination_class = SelfPagination
    # 搜索-模糊查询like
    search_fields = ('flight_id', 'flight_company','departure','destination')  # 指定模糊查询匹配的列

class FlightRetriveUpdateDeleteView(RetrieveAPIView,DestroyAPIView,UpdateAPIView):
    queryset = Flight.objects.all().extra(select={'begin_time': "DATE_FORMAT(begin_time,'%%Y-%%m-%%d %%H:%%i:%%s')"})\
        .extra(select={'end_time': "DATE_FORMAT(end_time,'%%Y-%%m-%%d %%H:%%i:%%s')"})
    serializer_class = FlightSerializer
    lookup_url_kwarg = "pk"
    parser_classes = [MultiPartParser]  # 重新指定解析器


class TakeFlightCreateListView(ListAPIView,CreateAPIView):
    queryset = TakeFlight.objects.all()
    serializer_class = TakeFlightSerializer
    parser_classes = [MultiPartParser]  # 重新指定解析器

class TakeFlightRetriveUpdateDeleteView(RetrieveAPIView,DestroyAPIView,UpdateAPIView):
    queryset = TakeFlight.objects.all()
    serializer_class = TakeFlightSerializer
    lookup_url_kwarg = "pk"
    parser_classes = [MultiPartParser]  # 重新指定解析器
