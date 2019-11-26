# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 17:07
# @Author  : sunny
# @File    : Customer.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密
from django.shortcuts import render, HttpResponse, redirect, reverse
from app01 import models
from app01.forms import CustorForm
from utils.pagination import Pagination
from django.db import transaction
from .base import Baseview


class Customer(Baseview):

    def get(self, request, *args, **kwargs):
        if request.path_info == reverse('app01:index'):
            customer_lis = models.Customer.objects.filter(consultant__isnull=True)
        else:
            customer_lis = models.Customer.objects.filter(consultant=request.user_obj)

        q = self.query(['name', 'phone', 'qq'])

        page_obj = Pagination(request.GET.get('page', 1), customer_lis.filter(q).count(), request.GET.copy(), 2)

        return render(request, 'index.html',
                      {
                          'customer_lis': customer_lis.filter(q)[page_obj.start:page_obj.end],
                          'url': reverse('app01:index'),
                          'page_obj': page_obj,
                      })

    def multi_apply(self):
        """
        公户转私户
        :return:
        """
        pk_list = self.request.POST.getlist('optionses')  # 客户列表
        from django.conf import settings
        self.request.user_obj.customers.add(*models.Customer.objects.filter(pk__in=pk_list))
        if self.request.user_obj.customers.all().count() + len(pk_list) > settings.MAX_CUSTOMER_NUM:
            return HttpResponse('做人留一线，事后好相见')
        try:
            with transaction.atomic():

                query_set = models.Customer.objects.filter(pk__in=pk_list, consultant=None).select_for_update()  # 行级锁
                # 判断客户是否被其他销售抢走
                if len(query_set) == len(pk_list):
                    return query_set.update(consultant=self.request.user_obj)
                else:
                    return HttpResponse('手速慢，被其他人抢走')

        except Exception:
            pass

    def multi_pul(self):
        """
        私户转公户
        :return:
        """
        pk_list = self.request.POST.getlist('optionses')

        self.request.user_obj.customers.remove(*models.Customer.objects.filter(pk__in=pk_list))


def add(request, pk=None):
    custor_obj = models.Customer.objects.filter(pk=pk).first()
    form_obj = CustorForm(instance=custor_obj)
    if request.method == 'POST':
        form_obj = CustorForm(request.POST, instance=custor_obj)
        if form_obj.is_valid():
            form_obj.save()
            if request.path_info == reverse('app01:curtoradd'):
                if request.POST.get('consultant'):
                    return redirect('app01:my_curtor')
                else:
                    return redirect('app01:index')
            else:
                path = request.GET.get('path')
                return redirect(path)
    return render(request, 'consultant/curtor_add.html', {'form_obj': form_obj})
