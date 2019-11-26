# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 17:32
# @Author  : sunny
# @File    : teacher.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密
from app01 import models
from .base import Baseview
from utils.pagination import Pagination
from django.shortcuts import render, redirect
from app01.forms import ClassListForm, CourseRecordListForm, Study_Record_Form


class classlist(Baseview):
    def get(self, request, *args, **kwargs):
        all_classes = models.ClassList.objects.all()
        q = self.query([])
        page_obj = Pagination(request.GET.get('page', 1), all_classes.filter(q).count(), request.GET.copy(), 2)
        return render(request, 'class_list/class_list.html', {
            "all_classes": all_classes.filter(q)[page_obj.start:page_obj.end],
            'page_obj': page_obj,
        })


def classchange(request, course=None):
    class_obj = models.ClassList.objects.filter(course=course).first()
    form_obj = ClassListForm(instance=class_obj)
    if request.method == 'POST':
        class_form = ClassListForm(request.POST, instance=class_obj)
        if class_form.is_valid():
            # 校验成功
            class_form.save()
            path = request.GET.get('path')
            return redirect(path)
    title = '编辑班级' if course else '新增班级'
    return render(request, 'form.html', {
        'form_obj': form_obj,
        "title": title,
    })


class course_record(Baseview):

    def get(self, request, class_id=None, *args, **kwargs):
        all_courserecord = models.CourseRecord.objects.all()
        q = self.query([])
        page_obj = Pagination(request.GET.get('page', 1), all_courserecord.filter(q).count(), request.GET.copy(), 2)
        return render(request, 'class_list/courserecord_list.html', {
            "all_courserecord": all_courserecord.filter(q)[page_obj.start:page_obj.end],
            'page_obj': page_obj,
            'class_id': class_id,
        })

    def multi_init(self):
        # 批量初始化学习记录
        pk_list = self.request.POST.getlist('pk')
        print(self.request.POST)
        print(pk_list)

        # for course_record_id in pk_list:
        #     # 根据一个课程记录生成学习记录
        #     students = models.CourseRecord.objects.get(pk=course_record_id).re_class.customer_set.filter(status='studying')
        #     for student in students:
        #         models.StudyRecord.objects.get_or_create(course_record_id=course_record_id,student=student)

        for course_record_id in pk_list:
            # 根据一个课程记录生成学习记录
            students = models.CourseRecord.objects.get(pk=course_record_id).re_class.customer_set.filter(
                status='studying')

            study_record_list = []
            for student in students:
                if not models.StudyRecord.objects.filter(course_record_id=course_record_id, student=student).exists():
                    study_record_list.append(models.StudyRecord(course_record_id=course_record_id, student=student))
            # 批量插入
            models.StudyRecord.objects.bulk_create(study_record_list)


def course_Record_changes(request, class_id=None, pk=None):
    course_record_obj = models.CourseRecord(re_class_id=class_id,
                                            recorder=request.user_obj) if class_id else models.CourseRecord.objects.filter(
        pk=pk).first()
    form_obj = CourseRecordListForm(instance=course_record_obj)
    if request.method == "POST":
        form_obj = CourseRecordListForm(request.POST, instance=course_record_obj)
        if form_obj.is_valid():
            form_obj.save()
            path = request.GET.get('path')
            return redirect(path)
    title = '编辑课程记录' if pk else '新增课程记录'
    return render(request, 'form.html', {
        'form_obj': form_obj,
        'title': title,
    })


from django.forms import modelformset_factory


def study_record_list(request, course_record_id=None):
    model_formset = modelformset_factory(models.StudyRecord, form=Study_Record_Form, extra=2)
    queryset = models.StudyRecord.objects.filter(course_record_id=course_record_id)
    form_set = model_formset(queryset=queryset)
    if request.method == 'POST':
        print(request.POST)
        form_set = model_formset(data=request.POST)
        if form_set.is_valid():
            form_set.save()
    return render(request, 'class_list/study_record_list.html', {'form_set': form_set})
