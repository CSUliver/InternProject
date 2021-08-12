from django.shortcuts import render

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from .models import Task,TaskFinish
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TaskFilter
from rest_framework.parsers import MultiPartParser

# Create your views here.

class TaskCreateListView(ListAPIView,CreateAPIView):
    queryset = Task.objects.all().extra(select={'time': "DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s')"})
    serializer_class = TaskSerializer
    # 使用自定义过滤器对数据进行时间段的搜索
    filter_backends = [DjangoFilterBackend]
    filter_class = TaskFilter
    parser_classes = [MultiPartParser]  # 重新指定解析器

class TaskRetriveUpdateDeleteView(RetrieveAPIView,DestroyAPIView,UpdateAPIView):
    queryset = Task.objects.all().extra(select={'time': "DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s')"})
    serializer_class = TaskSerializer
    lookup_url_kwarg = "pk"
    parser_classes = [MultiPartParser]  # 重新指定解析器


class TaskFinishCreateListView(ListAPIView,CreateAPIView):
    queryset = TaskFinish.objects.all()
    serializer_class = TaskFinishSerializer
    parser_classes = [MultiPartParser]  # 重新指定解析器

class TaskFinishRetriveUpdateDeleteView(RetrieveAPIView,DestroyAPIView,UpdateAPIView):
    queryset = TaskFinish.objects.all()
    serializer_class = TaskFinishSerializer
    lookup_url_kwarg = "pk"
    parser_classes = [MultiPartParser]  # 重新指定解析器
