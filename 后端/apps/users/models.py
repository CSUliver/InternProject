# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.FileUtils import ImageStorage
# Create your models here.

# 继承AbstractUser类，实际上django的User也是继承他，我们要做的就是用自己的类代替django自己的 User
class UserInfo(AbstractUser):
    # 定义类属性：拓展User模型的字段属性-新增的用户表字段
    tel = models.CharField(max_length=20,verbose_name='联系方式',blank=True, null=True)
    wechat = models.CharField(verbose_name='微信', blank=True, null=True, max_length=32)
    # ./media/avatar/2021/08/
    avatar = models.ImageField(upload_to='avatar/%Y/%m',verbose_name='用户头像',
                               default="avatar/default.jpg",storage=ImageStorage())
