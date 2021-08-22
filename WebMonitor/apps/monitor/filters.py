# 自定义过滤器filters以传统django_filter为基础
import django_filters
from django_filters import rest_framework as filters
from . models import *

class MonitorDataFilter(filters.FilterSet):
    # filter_name：要进行过滤的数据库字段；lookup_expr：过滤条件
    start_time = django_filters.DateTimeFilter(field_name='time',lookup_expr='gte')
    end_time = django_filters.DateTimeFilter(field_name='time', lookup_expr='lte')
    monitor_id = django_filters.NumberFilter(field_name='monitor_id')
    staff_id = django_filters.NumberFilter(field_name='staff_id')
    person_type = django_filters.ChoiceFilter(field_name='person_type',choices =
    (('passenger','旅客'),('airport','机场工作人员'),('flight','机组人员')))
    person_id = django_filters.NumberFilter(field_name='person_id')
    person_infect = django_filters.ChoiceFilter(field_name='person_infect',
                                                choices =(('感染','感染'),('无症状感染','无症状感染'),('未感染','未感染')))

    class Meta:
        model = MonitorData
        fields = ['start_time','end_time','monitor_id', 'staff_id','person_type','person_id','person_infect']