# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-15 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=0, max_length=11, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='passwd',
            field=models.CharField(max_length=20, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uname',
            field=models.CharField(max_length=6, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='用户名'),
        ),
    ]
