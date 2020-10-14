# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 20:14
# @Author  : Sunny
# @Site    : 
# @File    : paginations.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密

from rest_framework.pagination import PageNumberPagination


class CourseListPageination(PageNumberPagination):
    page_size = 5  # 默认的单页数据量
    page_query_param = 'page'  # 页码在地址栏中的参数名称
    page_size_query_param = 'size' # 单页数据量在地址栏上的参数名称
    max_page_size = 100 # 允许客户端用过参数调整的最大的单页数据量

