# Generated by Django 2.2.2 on 2021-08-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(default='avatar/default.jpg', upload_to='avatar/%Y/%m', verbose_name='用户头像'),
        ),
    ]