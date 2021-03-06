# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-27 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, verbose_name='链接地址')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
            ],
            options={
                'verbose_name': '权限表',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='角色')),
                ('persisson', models.ManyToManyField(related_name='role', to='app01.Permission', verbose_name='权限')),
            ],
            options={
                'verbose_name': '角色表',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('roles', models.ManyToManyField(related_name='user', to='app01.Role', verbose_name='角色')),
            ],
            options={
                'verbose_name': '用户表',
            },
        ),
    ]
