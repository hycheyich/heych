# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 17:03
# @Author  : sunny
# @File    : base.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密

from django.shortcuts import HttpResponse
from django.db.models import Q
from django.views import View


class Baseview(View):

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        if not hasattr(self, action):
            return HttpResponse('没有此方法')
        ret = getattr(self, action)()
        if ret:
            return ret

        return self.get(request, *args, **kwargs)

    def query(self, field_names):
        query = self.request.GET.get('query', '')
        q = Q()
        q.connector = 'OR'
        if not query:
            return q
        for i in field_names:
            q.children.append(Q(('{}__contains'.format(i), query)))
        return q
