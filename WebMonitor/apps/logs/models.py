import datetime

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# 日志模型类
class Logs(models.Model):
    log_addtime = models.DateTimeField(default=datetime.datetime.now,verbose_name="添加时间")
    log_type = models.CharField(max_length=255, verbose_name="操作模块")
    log_ip = models.CharField(max_length=20, verbose_name="操作ip地址")
    log_content = models.CharField(max_length=255, verbose_name="操作内容")
    log_user = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="操作者",null=True)




