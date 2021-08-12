from django.db import models

# Create your models here.

class Flight(models.Model):
    flight_id = models.CharField(max_length=10, verbose_name='飞机编号')
    flight_company = models.CharField(max_length=30, verbose_name='飞机从属航空公司')
    departure = models.CharField(max_length=10, verbose_name='始发地')
    destination = models.CharField(max_length=10, verbose_name='目的地')
    begin_time = models.DateTimeField(verbose_name='起飞时间')
    end_time = models.DateTimeField(verbose_name='落地时间')

    class Meta():
        ordering = ['id']

class TakeFlight(models.Model):
    flight_id = models.ForeignKey(Flight, on_delete=models.PROTECT, verbose_name='航班编号')
    passenger_type = models.CharField(verbose_name='乘客类型', max_length=10,
                                      choices=(('passenger', '旅客'), ('flight', '机组人员')), default='passenger')
    passenger_id = models.IntegerField(verbose_name='乘客编号')
    passenger_name = models.CharField(verbose_name='乘客姓名',max_length=10)
    is_take = models.CharField(max_length=1, verbose_name='乘客是否乘机',
                                    choices=(('Y', '是'), ('N', '否')),default='N')