# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-16 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp1', '0003_auto_20191116_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='lbalance',
        ),
        migrations.AddField(
            model_name='balance',
            name='laboratory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Balance', to='djangoapp1.laboratory'),
        ),
    ]
