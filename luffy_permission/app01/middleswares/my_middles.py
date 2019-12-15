# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 20:34
# @Author  : sunny
# @File    : my_middles.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse, HttpResponse
from django.conf import settings
import re


class MD(MiddlewareMixin):

    def process_request(self, request, *args, **kwargs):
        url = request.path_info

        for i in settings.WHITE_PATH:
            if re.match(r"{}".format(i), url):
                return

        login_flage = request.session.get('is_login')
        if not login_flage:
            return redirect('/login/')

        # 登陆成功
        for i in request.session.get('persisson'):
            if re.match(r'{}'.format(i['persisson__url']), request.path_info):
                return
        else:
            return HttpResponse('你的权限不够')
