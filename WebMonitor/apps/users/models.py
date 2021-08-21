# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.FileUtils import ImageStorage
# Create your models here.

# 继承AbstractUser类，实际上django的User也是继承他，我们要做的就是用自己的类代替django自己的 User
class UserInfo(AbstractUser):
    # 定义类属性：拓展User模型的字段属性-新增的用户表字段
    age = models.IntegerField(verbose_name='年龄',default=0,null=True)
    card_id = models.CharField(max_length=20,verbose_name='身份证号码',null=True)
    tel = models.CharField(max_length=20,verbose_name='手机号码',null=True)
    person_type = models.CharField(verbose_name='人员类型', max_length=10, choices=
    (('admin','机场管理员'),('passenger', '旅客'), ('airport', '机场工作人员'), ('flight', '机组人员')), default='admin')
    infect_level = models.CharField(max_length=1,verbose_name='感染风险等级',
                                    choices=(('1', '低风险'), ('2', '中风险'), ('3', '高风险')),default='1')
    isDelete = models.BooleanField(default=False,verbose_name='是否已删除')
    # ./media/avatar/2021/08/
    avatar = models.ImageField(upload_to='avatar/%Y/%m',verbose_name='用户头像',
                               default="avatar/default.jpg",storage=ImageStorage())
    # 机场工作人员专属属性
    task_type = models.CharField(verbose_name='工种', max_length=10,
                                 choices=(('security', '安保'), ('cleaning', '保洁'), ('check-in', '值机服务')),
                                 blank=True, null=True)
    # 机组人员专属属性
    flight_type = models.CharField(verbose_name='职务', max_length=8,
                                 choices=(('pilot', '飞行员'), ('service', '空勤人员')),blank=True, null=True)
