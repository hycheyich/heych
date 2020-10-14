# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 17:11
# @Author  : Sunny
# @Site    : 
# @File    : main.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密
import os
import django
from celery import Celery

# 初始化celery应用对象
app = Celery('luffy')
# 1 如果celery需要在任务调用其它框架的内部对象，则需要进行相应的框架初始化
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffyapi.settings.dev')
django.setup()
# 加载初始化配置
app.config_from_object('my_cerely.config')
# 注册异步任务
app.autodiscover_tasks(['my_cerely.sms'])

# 在终端启动Celery
# celery -A mycerely.main worker -l info -P eventlet
