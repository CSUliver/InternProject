from django.urls import path
from .views import *
app_name = '[flight]'

urlpatterns = [
    # 航班列表get、新增post   ./flight/flightlist/
    path('flightlist/',FlightCreateListView.as_view()),
    # 航班信息检索get、编辑put/patch、删除delete  ./flight/flight/<int:pk>
    path('flight/<int:pk>',FlightRetriveUpdateDeleteView.as_view()),
    # 飞机搭载数据列表get、新增post   ./flight/takeflightlist/
    path('takeflightlist/',TakeFlightCreateListView.as_view()),
    # 飞机搭载信息检索get、编辑put/patch、删除delete  ./flight/takeflght/<int:pk>
    path('takeflght/<int:pk>',TakeFlightRetriveUpdateDeleteView.as_view()),

]