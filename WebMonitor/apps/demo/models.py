import datetime

from django.db import models

# Create your models here.

# 同步到数据库中的表名：appname_modelname   eg:demo_deptinfo
class DeptInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name="部门名称")
    decription = models.CharField(max_length=255)
    isDelete = models.BooleanField(default=False)

    class Meta():
        ordering = ['-id']
        db_table = "deptinfo"  #重新指定表名


class UserInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name='姓名')
    gender = models.CharField(verbose_name='性别',max_length=7,choices=(('male','男'),('female','女')),default='male')
    birthday = models.DateTimeField(verbose_name='生日',default=datetime.datetime.now)
    salary = models.FloatField(verbose_name='工资')
    isDelete = models.BooleanField(default=False)
    dept = models.ForeignKey('DeptInfo',on_delete=models.PROTECT)