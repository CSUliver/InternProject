from django.shortcuts import render

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from .models import Flight,TakeFlight
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FlightFilter
from rest_framework.parsers import MultiPartParser

# Create your views here.

class FlightCreateListView(ListAPIView,CreateAPIView):
    queryset = Flight.objects.all().extra(select={'begin_time': "DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s')"})\
        .extra(select={'end_time': "DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s')"})
    serializer_class = FlightSerializer
    # 使用自定义过滤器对数据进行时间段的搜索
    filter_backends = [DjangoFilterBackend]
    filter_class = FlightFilter
    parser_classes = [MultiPartParser]  # 重新指定解析器

class FlightRetriveUpdateDeleteView(RetrieveAPIView,DestroyAPIView,UpdateAPIView):
    queryset = Flight.objects.all().extra(select={'begin_time': "DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s')"})\
        .extra(select={'end_time': "DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s')"})
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
