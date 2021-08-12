# Generated by Django 2.2.2 on 2021-08-12 15:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=20, verbose_name='位置')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MonitorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name='监测时间')),
                ('person_type', models.CharField(choices=[('passenger', '旅客'), ('airport', '机场工作人员'), ('flight', '机组人员')], default='passenger', max_length=10, verbose_name='监测人员类型')),
                ('person_id', models.IntegerField(verbose_name='监测人员编号')),
                ('person_name', models.CharField(max_length=10, verbose_name='监测人员姓名')),
                ('person_temperature', models.FloatField(max_length=6, verbose_name='监测人员体温')),
                ('person_infect', models.CharField(choices=[('Y', '感染'), ('NY', '无症状感染'), ('N', '未感染')], default='N', max_length=2, verbose_name='监测人员受感染状态')),
                ('monitor_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='monitor.Monitor', verbose_name='监测点编号')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='执勤人员编号')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]