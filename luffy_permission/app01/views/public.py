# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 18:39
# @Author  : sunny
# @File    : public.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密

from django.shortcuts import render, redirect
from app01 import models

def login(request):
    if request.method == 'POST':
        print(request.POST)
        user = request.POST.get('user')
        password = request.POST.get('password')
        user_obj = models.User.objects.filter(user=user, password=password).first()
        print(user_obj)
        if user_obj:
            # 登陆成功
            request.session['is_login'] = True
            persisson = user_obj.roles.exclude(persisson=None).values('persisson__url').distinct()
            request.session['persisson'] = list(persisson)
            return redirect('/index/')
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')
