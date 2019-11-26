# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 17:15
# @Author  : sunny
# @File    : enrollment.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密
from django.shortcuts import render, redirect
from app01 import models
from app01.forms import Enrollment_Form
from utils.pagination import Pagination
from .base import Baseview


class EnrollmentList(Baseview):
    """
    报名表
    """

    def get(self, request, customer_id=None, *args, **kwargs):
        if customer_id:
            all_enrollments = models.Enrollment.objects.filter(customer=customer_id)
        else:
            all_enrollments = models.Enrollment.objects.filter()
        q = self.query([])
        page_obj = Pagination(request.GET.get('page', 1), all_enrollments.filter(q).count(), request.GET.copy(), 2)
        return render(request, 'consultant/enrollmentlist.html', {
            "all_enrollments": all_enrollments.filter(q).order_by("-enrolled_date")[page_obj.start:page_obj.end],
            'page_obj': page_obj,
        })


def enrollment_change(request, customer_id=None, pk=None):
    obj = models.Enrollment(customer_id=customer_id) if customer_id else models.Enrollment.objects.filter(pk=pk).first()
    form_obj = Enrollment_Form(request, instance=obj)
    if request.method == "POST":
        form_obj = Enrollment_Form(request, request.POST, instance=obj)
        if form_obj.is_valid():
            # 表示报名表验证通过
            form_obj.save()
            path = request.GET.get('path')
            return redirect(path)

    title = '编辑报名记录' if pk else '新增报名记录'
    return render(request, 'form.html', {
        "form_obj": form_obj,
        'title': title,
    })
