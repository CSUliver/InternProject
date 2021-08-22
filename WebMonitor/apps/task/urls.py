from django.urls import path
from .views import *
app_name = '[task]'

urlpatterns = [
    # 航班列表get、新增post   ./task/tasklist/
    path('tasklist/',TaskCreateListView.as_view()),
    # 航班信息检索get、编辑put/patch、删除delete  ./task/task/<int:pk>
    path('task/<int:pk>',TaskRetriveUpdateDeleteView.as_view()),
    # 飞机搭载数据列表get、新增post   ./task/taskfinishlist/
    path('taskfinishlist/',TaskFinishCreateListView.as_view()),
    # 飞机搭载信息检索get、编辑put/patch、删除delete  ./task/taskfinish/<int:pk>
    path('taskfinish/<int:pk>',TaskFinishRetriveUpdateDeleteView.as_view()),

]