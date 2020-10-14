# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 20:45
# @Author  : Sunny
# @Site    : 
# @File    : xadminx.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密


import xadmin

from .models import CourseCategory

from .models import Teacher
from .models import Course
from .models import CourseLesson
from .models import CourseChapter, CourseExpire, CourseActivity, PriceDiscountType, PriceDiscount, Activity


class CourseCategoryModelxadmin(object):
    """课程分类模型管理类"""
    pass


xadmin.site.register(CourseCategory, CourseCategoryModelxadmin)
class CourseModelxadmin(object):
    """课程模型管理类"""
    pass


xadmin.site.register(Course, CourseModelxadmin)


class TeacherModelxadmin(object):
    """老师模型管理类"""
    pass


xadmin.site.register(Teacher, TeacherModelxadmin)


class CourseChapterModelxadmin(object):
    """课程章节模型管理类"""
    pass


xadmin.site.register(CourseChapter, CourseChapterModelxadmin)


class CourseLessonModelxadmin(object):
    """课程课时模型管理类"""
    pass


xadmin.site.register(CourseLesson, CourseLessonModelxadmin)


class CourseExpireModelxadmin(object):
    """
    课程有效期表
    """
    list_display = ["course", "expire", "price"]


xadmin.site.register(CourseExpire, CourseExpireModelxadmin)

"""优惠策略"""


class CourseDiscountTypeModelxadmin(object):
    """课程优惠类型"""
    pass


xadmin.site.register(PriceDiscountType, CourseDiscountTypeModelxadmin)


class CourseDiscountModelxadmin(object):
    """课程优惠策略模型"""
    pass


xadmin.site.register(PriceDiscount, CourseDiscountModelxadmin)


class ActivityModelxadmin(object):
    """优惠活动模型"""
    pass


xadmin.site.register(Activity, ActivityModelxadmin)


class CourseActivityModelxadmin(object):
    """课程与活动的关系模型"""
    pass


xadmin.site.register(CourseActivity, CourseActivityModelxadmin)
