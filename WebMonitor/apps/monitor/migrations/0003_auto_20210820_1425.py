# Generated by Django 2.2.2 on 2021-08-20 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20210816_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitordata',
            name='person_infect',
            field=models.CharField(choices=[('感染', '感染'), ('无症状感染', '无症状感染'), ('未感染', '未感染')], default='N', max_length=5, verbose_name='监测人员受感染状态'),
        ),
    ]
