# Generated by Django 2.2.2 on 2021-08-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210805_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='tel',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='联系方式'),
        ),
    ]
