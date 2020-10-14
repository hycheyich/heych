# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 16:44
# @Author  : Sunny
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密
import xadmin
from .models import Order


class OrderModelAdmin(object):
    """订单模型管理类"""
    pass


xadmin.site.register(Order, OrderModelAdmin)

from .models import OrderDetail


class OrderDetailModelAdmin(object):
    """订单详情模型管理类"""
    pass


xadmin.site.register(OrderDetail, OrderDetailModelAdmin)
