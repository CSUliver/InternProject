from django.db import models
import datetime
from django.contrib.auth import get_user_model
User = get_user_model()
from apps.monitor.models import Monitor

# Create your models here.

class InfectRisk(models.Model):
    monitor_id = models.ForeignKey(Monitor, on_delete=models.PROTECT,verbose_name='监测点编号',null=True)
    infect_level = models.CharField(max_length=1, verbose_name='感染风险等级',
                                    choices=(('1', '低风险'), ('2', '中风险'), ('3', '高风险')),default='1')
    time = models.DateTimeField(verbose_name='时间', default=datetime.datetime.now)

    class Meta():
        ordering = ['-time']

class InfectAlarm(models.Model):
    alarm_level = models.CharField(max_length=1, verbose_name='感染警示等级',
                                    choices=(('2', '中风险'), ('3', '高风险')))
    risk_id = models.ForeignKey(InfectRisk, on_delete=models.PROTECT,verbose_name='感染风险预警编号',null=True)
    staff_id = models.ForeignKey(User, on_delete=models.PROTECT,verbose_name='机场管理人员编号',null=True)
    time = models.DateTimeField(verbose_name='警示时间', default=datetime.datetime.now)

    class Meta():
        ordering = ['-time']
