from django.urls import path
from .views import *
app_name = '[users]'

urlpatterns = [
    # ./users/getinfo/
    path('getinfo/',GetInfo.as_view(),name="getinfo"),
    # 用户列表get、用户新增post   ./users/users/
    path('users/',UserCreateListView.as_view()),
    #用户查看个人信息get、编辑put/patch、删除delete
    path('users/<int:pk>',UserRetriveUpdateDeleteView.as_view()),
]