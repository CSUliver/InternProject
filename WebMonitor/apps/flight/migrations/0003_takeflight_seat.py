# Generated by Django 2.2.2 on 2021-08-16 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_auto_20210816_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='takeflight',
            name='seat',
            field=models.CharField(max_length=4, null=True, verbose_name='座位号'),
        ),
    ]
