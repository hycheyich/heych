# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 9:50
# @Author  : sunny
# @File    : exceptions.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密

# 自定义的异常处理
from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.db import DatabaseError
from rest_framework import status
from redis import RedisError
import logging

logger = logging.getLogger('django')


def custom_exception_handler(exc, context):
    """
    自定义异常处理
    :param exc: 异常类
    :param context: 抛出异常的上下文
    :return: Response相应对象
    """
    response = exception_handler(exc, context)

    if response is None:
        # 表示成功或者就是异常不在所定义的范围内
        view = context['view']
        if isinstance(exc, DatabaseError) or isinstance(exc, RedisError):
            # 数据库异常
            logger.error('[%s] %s' % (view, exc))
            response = Response({'message': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response
