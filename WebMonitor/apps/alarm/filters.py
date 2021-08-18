# 自定义过滤器filters以传统django_filter为基础
import django_filters
from django_filters import rest_framework as filters
from . models import *

class RiskDataFilter(filters.FilterSet):
    # filter_name：要进行过滤的数据库字段；lookup_expr：过滤条件
    start_time = django_filters.DateTimeFilter(field_name='time',lookup_expr='gte')
    end_time = django_filters.DateTimeFilter(field_name='time', lookup_expr='lte')
    infect_level = django_filters.ChoiceFilter(field_name='infect_level',
                                               choices=(('1', '低风险'), ('2', '中风险'), ('3', '高风险')))

    class Meta:
        model = InfectRisk
        fields = ['start_time','end_time','infect_level']

class AlarmDataFilter(filters.FilterSet):
    # filter_name：要进行过滤的数据库字段；lookup_expr：过滤条件
    start_time = django_filters.DateTimeFilter(field_name='time',lookup_expr='gte')
    end_time = django_filters.DateTimeFilter(field_name='time', lookup_expr='lte')
    alarm_level = django_filters.ChoiceFilter(field_name='alarm_level',choices=(('2', '中风险'), ('3', '高风险')))

    class Meta:
        model = InfectAlarm
        fields = ['start_time','end_time','alarm_level']