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
    flight_id = models.ForeignKey(Flight, on_delete=models.PROTECT, verbose_name='航班编号',null=True)
    passenger_type = models.CharField(verbose_name='乘客类型', max_length=10,
                                      choices=(('passenger', '旅客'), ('flight', '机组人员')), default='passenger')
    passenger_id = models.IntegerField(verbose_name='乘客编号')
    passenger_name = models.CharField(verbose_name='乘客姓名',max_length=10)
    seat = models.CharField(verbose_name='座位号',max_length=4,null=True)
    is_take = models.CharField(max_length=1, verbose_name='乘客是否乘机',
                                    choices=(('Y', '是'), ('N', '否')),default='N')

class AreaInfect(models.Model):
    name = models.CharField(max_length=10, verbose_name='地区名称')
    infect_level = models.CharField(max_length=1, verbose_name='感染风险等级',
                                    choices=(('1', '低风险'), ('2', '中风险'), ('3', '高风险')), default='1')