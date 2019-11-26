# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 17:20
# @Author  : sunny
# @File    : user.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密
from django.shortcuts import render, redirect, reverse
from app01 import models
from app01.forms import RegForm
import hashlib

from django.db.models import Q


def login(request):
    """
    登陆页面
    :param request:登陆请求
    :return:
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        password = md5.hexdigest()
        user_obj = models.UserProfile.objects.filter(username=username, password=password, is_active=True).first()
        if user_obj:
            request.session['username'] = username
            request.session['pk'] = user_obj.pk
            request.session['is_login'] = True
            return redirect(reverse('app01:index'))
        else:
            return render(request, 'register_login/login.html', {'error': '用户名或密码'})
    return render(request, 'register_login/login.html')


def logout(request):
    """
    注销
    :param request:
    :return:
    """
    request.session.delete()
    return redirect(reverse('app01:login'))


def register(request):
    """
    注册
    :param request:
    :return:
    """
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            # 校验通过
            # 插入数据库
            reg_form.save()
            return redirect(reverse('app01:login'))
    reg_form = RegForm()

    return render(request, 'register_login/register.html', {'reg_form': reg_form})


def index(request):
    """
    主页
    :param request:
    :return:
    """
    if request.path_info == reverse('app01:index'):
        customer_lis = models.Customer.objects.filter(consultant__isnull=True)
    else:
        customer_lis = models.Customer.objects.filter(consultant=request.user_obj)
    if request.method == 'POST':
        lis = request.POST.getlist('optionses')
        if request.POST.get('gzs') == "1":
            for i in lis:
                customer_obj = models.Customer.objects.filter(pk=int(i)).first()
                customer_obj.consultant = models.UserProfile.objects.filter(pk=request.session.get('pk')).first()
                customer_obj.save()
            return redirect(reverse('app01:index'))
        else:
            for i in lis:
                customer_obj = models.Customer.objects.filter(pk=int(i)).first()
                customer_obj.consultant = None
                customer_obj.save()
            return redirect(reverse('app01:my_curtor'))
    return render(request, 'index.html', {'customer_lis': customer_lis})


def sousuo(request):
    sousuo_text = request.POST.get('sousuo')
    if sousuo_text:
        customer_lis = models.Customer.objects.filter(Q(qq__contains=sousuo_text) | Q(name__contains=sousuo_text),
                                                      consultant_id=request.session.get('pk'))
        return render(request, 'index.html', {'customer_lis': customer_lis, 'sousuo': sousuo_text})
    else:
        return redirect(reverse('app01:index'))
