from django.db import models
import datetime
from django.contrib.auth import get_user_model
User = get_user_model()
from apps.monitor.models import Monitor

# Create your models here.

class Task(models.Model):
    monitor_id = models.ForeignKey(Monitor, on_delete=models.PROTECT, verbose_name='监测点编号',null=True)
    time = models.DateTimeField(verbose_name='出勤时间', default=datetime.datetime.now)

    class Meta():
        ordering = ['-time']

class TaskFinish(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.PROTECT, verbose_name='出勤任务编号',null=True)
    staff_id = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='出勤人员编号',null=True)
    staff_name = models.CharField(verbose_name='出勤人员姓名',max_length=10,null=True)
    is_finish = models.CharField(max_length=1, verbose_name='出勤人员是否到勤',
                                    choices=(('Y', '是'), ('N', '否')),default='N')