from django.db import models
import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

# 同步到数据库中的表名：appname_modelname
class Monitor(models.Model):
    position = models.CharField(max_length=20,verbose_name='位置')

    class Meta():
        ordering = ['id']

class MonitorData(models.Model):
    time = models.DateTimeField(verbose_name='监测时间',default=datetime.datetime.now)
    monitor_id = models.ForeignKey(Monitor,on_delete=models.PROTECT,verbose_name='监测点编号',null=True)
    staff_id = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name='执勤人员编号',null=True)
    person_type = models.CharField(verbose_name='监测人员类型',max_length=10,choices=
    (('passenger','旅客'),('airport','机场工作人员'),('flight','机组人员')),default='passenger')
    person_id = models.IntegerField(verbose_name='监测人员编号')
    person_name = models.CharField(verbose_name='监测人员姓名',max_length=10)
    person_temperature = models.FloatField(verbose_name='监测人员体温',max_length=6)
    person_infect = models.CharField(verbose_name='监测人员受感染状态',max_length=2,
                                     choices=(('Y','感染'),('NY','无症状感染'),('N','未感染')),default='N')

    class Meta():
        ordering = ['-time']



