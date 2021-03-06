# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-27 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permission',
            options={'verbose_name': '权限表', 'verbose_name_plural': '权限表'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': '角色表', 'verbose_name_plural': '角色表'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户表', 'verbose_name_plural': '用户表'},
        ),
        migrations.AlterField(
            model_name='role',
            name='persisson',
            field=models.ManyToManyField(blank=True, related_name='role', to='app01.Permission', verbose_name='权限'),
        ),
    ]
