# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 17:14
# @Author  : sunny
# @File    : consultrecord.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密

from django.shortcuts import render, redirect
from app01 import models
from app01.forms import ConsultRecord
from utils.pagination import Pagination
from .base import Baseview


class ConsultRecordList(Baseview):

    def get(self, request, customer_id=None, *args, **kwargs):
        if customer_id:
            consultrecord_obj = models.ConsultRecord.objects.filter(consultant=request.user_obj, customer=customer_id)
        else:
            consultrecord_obj = models.ConsultRecord.objects.filter(consultant=request.user_obj)
        q = self.query([])

        page_obj = Pagination(request.GET.get('page', 1), consultrecord_obj.filter(q).count(), request.GET.copy(), 2)
        return render(request, 'consultant/consultRecord.html', {
            "consultrecord_obj": consultrecord_obj.filter(q).order_by("-date")[page_obj.start:page_obj.end],
            'page_obj': page_obj,
        })


def consult_record_change(request, pk=None):
    custor_obj = models.ConsultRecord.objects.filter(pk=pk).first()
    form_obj = ConsultRecord(request, instance=custor_obj)
    if request.method == 'POST':
        form_obj = ConsultRecord(request, data=request.POST, instance=custor_obj)
        if form_obj.is_valid():
            form_obj.save()
            path = request.GET.get('path')
            return redirect(path)
    title = '编辑跟进记录' if pk else '新增跟进记录'
    return render(request, 'form.html', {'form_obj': form_obj, 'title': title})
