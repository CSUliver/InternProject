"""WebMonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from rest_framework_jwt.views import obtain_jwt_token
from WebMonitor import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    # media配置--配合settings中的MEDIA_ROOT的配置，就可以在浏览器的地址栏访问media文件夹及里面的文件了
    re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]

# drf_yasg ---------------------------------------
# 所有需要展示在接口交互界面中的接口url都写在此处
schema_url_patterns =[
    path('login/', obtain_jwt_token),  #jwt登录认证接口  http://127.0.0.1:8000/login/
    path('users/', include('apps.users.urls', namespace="users")),  # users/
    path('monitor/', include('apps.monitor.urls', namespace="monitor")),  # monitor/
    path('alarm/', include('apps.alarm.urls', namespace="alarm")),  # alarm/
    path('flight/', include('apps.flight.urls', namespace="flight")),  # flight/
    path('task/', include('apps.task.urls', namespace="task")),  # task/
]

urlpatterns += schema_url_patterns

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="机场人员流动监测系统 API",
      default_version='v1',
      description="机场人员流动监测系统数据接口页面 \n 用户信息管理、日志管理、数据监测、场景管理、权限管理等",
      terms_of_service="http://www.briup.com",
      contact=openapi.Contact(email="chengzy@briup.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=(permissions.AllowAny,),
   patterns= schema_url_patterns
)

# http://127.0.0.1:8000/swagger/
urlpatterns += [
   # path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
