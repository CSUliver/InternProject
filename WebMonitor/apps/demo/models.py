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
