# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-16 07:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp1', '0002_auto_20191115_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratory',
            name='lbalance',
        ),
        migrations.AddField(
            model_name='balance',
            name='lbalance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='laboratory', to='djangoapp1.Balance'),
        ),
    ]
