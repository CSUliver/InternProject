from django.urls import path
from .views import *
app_name = '[alarm]'

urlpatterns = [
    # 感染风险列表get、新增post   ./alarm/riskdata/
    path('riskdata/',RiskDataView.as_view()),
    # 感染警示列表get、新增post   ./alarm/alarmdata/
    path('alarmdata/',AlarmDataView.as_view()),

]