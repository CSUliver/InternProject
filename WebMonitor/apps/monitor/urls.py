from django.urls import path
from .views import *
app_name = '[monitor]'

urlpatterns = [
    # 监测点列表get、新增post   ./monitor/monitorlist/
    path('monitorlist/',MonitorCreateListView.as_view()),
    # 监测点信息检索get、编辑put/patch、删除delete  ./monitor/monitor/<int:pk>
    path('monitor/<int:pk>',MonitorRetriveUpdateDeleteView.as_view()),
    # 监测点数据列表get、新增post   ./monitor/monitordata/
    path('monitordata/',MonitorDataView.as_view()),

]