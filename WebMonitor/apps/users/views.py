# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.shortcuts import render
from apps.logs.views import addLog

# Create your views here.
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from apps.users.serializers import *
from rest_framework_jwt.utils import jwt_decode_handler

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,mixins

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser

Header_token = openapi.Parameter('Authorization', openapi.IN_HEADER, description="Token（ Format: JWT {Token Value}）", type=openapi.TYPE_STRING)
Accept_Language = openapi.Parameter('Accept-Language', openapi.IN_HEADER, description="Language: en or zh-CN", type=openapi.TYPE_STRING)

base_swagger = {
    'manual_parameters': [ Header_token, Accept_Language],
}

# 读取文件的方法
def get_swagger_docs(filename):
    DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs')
    with open(os.path.join(DIR, filename),'r',encoding='utf-8') as f:
        return f.read()

# 用户列表接口说明配置
user_list_swagger = dict({
    'tags': ['用户管理模块'],
    'operation_summary':'获得用户列表信息',
    'operation_description': get_swagger_docs('user_list.md')
}, **base_swagger)


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    @swagger_auto_schema(**user_list_swagger)   # 装饰器
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# 根据token获取用户信息
class GetInfo(ListAPIView):
    # queryset = User.objects.all()
    serializer_class = UserInfoSerializer

    @swagger_auto_schema(**base_swagger)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        # token: header Authorization: JWT xxxxx
        token = self.request.META.get("HTTP_AUTHORIZATION") # JWT xxxxx
        token = token.split(" ")[1]
        userinfo = jwt_decode_handler(token)
        user_id = userinfo.get("user_id")
        return User.objects.filter(id=user_id)

# 返回当前登陆者的用户信息
class GetInfo2(ListAPIView):
    serializer_class = UserInfoSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return User.objects.filter(id=user_id)

# 用户的新增和列表-APIView
class UserCreateListView1(APIView):
    def get(self, request, *args, **kwargs):
        # 用户列表：从User中去获取全部用户信息
        users = User.objects.all()  # 返回查询结果集-queryset对象
        print(users)
        # <QuerySet [<UserInfo: admin>, <UserInfo: add>]>
        # 数据处理：处理为符合要求的json格式([],{})
        # [{id:1,username:'admin'},{},{}]
        users_list = []
        for user in users:
            userinfo = {
                'id':user.id,
                'username':user.username,
                'email':user.email,
                # 'avatar':user.avatar,  # 序列化过程中文件以及日期要进行特殊处理
                'is_superuser':user.is_superuser
            }
            users_list.append(userinfo)
        return Response(status=200,data=users_list)

    def post(self, request, *args, **kwargs):
        # 新增用户：接受用户提交的数据->验证数据的合法性->存入数据库
        username = request.data.get("username","")  # 获取"username"，获取不到则获取""默认值
        email = request.data.get("email","")
        user = User()
        user.username = username
        user.email = email
        user.save()
        data = {
            "code":200,
            "msg":"Created Successfully",
            "username":username,
        }
        return Response(status=200,data=data)

# 用户的新增和列表-GenericAPIView
class UserCreateListView2(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateListSerializer

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()  # 获取所有的实例对象
        # 构造序列化器：多条数据的序列化many=True
        s = self.get_serializer(instance = users, many = True)
        userlist = s.data
        data = {
            "code": 200,
            "msg": "Successfully",
            "username": userlist,
        }
        return Response(status=200, data=data)

    def post(self, request, *args, **kwargs):
        # 构造序列化器
        s = self.get_serializer(data = request.data)
        # 数据的合法性校验
        if s.is_valid():
            user = s.save()
            data = {
                "code": 200,
                "msg": "Successfully",
                "username": s.data,
            }
            return Response(status=200, data=data)
        else:
            return Response(status=400,data={"code": 400,"msg": str(s.errors)})

# 用户的新增和列表-GenericAPIView,mixins
class UserCreateListView3(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserCreateListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# 用户的新增和列表-generics（知识点学习）
class UserCreateListView4(ListAPIView,CreateAPIView):
    # queryset = User.objects.all() # 获取所有的用户信息
    # queryset = User.objects.filter(is_superuser=1)  # 获取所有的超级管理员
    # queryset = User.objects.exclude(is_superuser=0).order_by('-id')  # 获取所有的超级管理员，并倒序排序
    queryset = User.objects.filter(is_superuser=1).filter(is_active=1)  # 获取所有的活跃的超级管理员
    # user = User.objects.get(id=1)
    # count = User.objects.count()
    # print(count)
    # is_exists = User.objects.filter(username="admin").exists()
    # print(is_exists)

    serializer_class = UserCreateListSerializer

# 自定义分页类
class SelfPagination(PageNumberPagination):
    page_size = 5  # 默认每页显示5条数据
    page_size_query_param = 'page_size' # 自定义每页显示条数的请求参数->  users/users/?page_size=10
    max_page_size = 20
    page_query_param = 'page' # 分页请求参数变量名-> users/users/?page_size=10&page=2

# 用户的新增和列表-generics
class UserCreateListView(ListAPIView,CreateAPIView):
    permission_classes = []
    queryset = User.objects.all() # 获取所有的用户信息
    serializer_class = UserCreateListSerializer
    # 由于用户新增涉及到图片上传（二进制流）1.将图片转为字符串(base64) 2.更改接口解析器
    parser_classes = [MultiPartParser] # 重新指定解析器
    # 列表分页功能
    pagination_class = SelfPagination
    # 排序
    filter_backends = (filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend)
    ordering_fields = ('id','date_joined','username') # 指定可以自定义排序的列选项
    ordering = ('-id',) # 指定默认的排序方式
    # 搜索-模糊查询like
    search_fields = ('username','email','tel') # 指定模糊查询匹配的列
    # 过滤筛选django_filter  终端执行：pip install django_filter==2.2
    filter_fields = ('is_superuser', 'is_active','person_type') # 指定可以支持过滤的列


# 用户查看人信息get、编辑put/patch、删除delete
class UserRetriveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateListSerializer
    lookup_url_kwarg = "pk"
    # 由于用户编辑涉及到图片上传（二进制流）1.将图片转为字符串(base64) 2.更改接口解析器
    parser_classes = [MultiPartParser]  # 重新指定解析器

    def delete(self, request, *args, **kwargs):
        # 调用函数新增日志
        addLog(*args, **kwargs)
        return self.destroy(request, *args, **kwargs)


# 用户查看人信息get、编辑put/patch、删除delete
class UserRetriveUpdateDeleteView1(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateListSerializer
    lookup_url_kwarg = "pk"
    def get(self, request, *args, **kwargs):
        # 查看个人信息
        user = self.get_object()
        s = self.get_serializer(instance = user)
        data = s.data
        data['code'] = 200
        data['msg'] = 'ok'
        return Response(status=200, data=data)




