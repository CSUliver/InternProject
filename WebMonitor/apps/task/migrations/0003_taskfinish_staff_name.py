# Generated by Django 2.2.2 on 2021-08-20 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20210816_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskfinish',
            name='staff_name',
            field=models.CharField(max_length=10, null=True, verbose_name='出勤人员姓名'),
        ),
    ]
