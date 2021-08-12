# 自定义过滤器filters以传统django_filter为基础
import django_filters
from django_filters import rest_framework as filters
from . models import *

class MonitorDataFilter(filters.FilterSet):
    # filter_name：要进行过滤的数据库字段；lookup_expr：过滤条件
    start_time = django_filters.DateTimeFilter(field_name='time',lookup_expr='gte')
    end_time = django_filters.DateTimeFilter(field_name='time', lookup_expr='lte')

    class Meta:
        model = MonitorData
        fields = ['start_time','end_time']