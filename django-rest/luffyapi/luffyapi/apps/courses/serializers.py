# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 21:20
# @Author  : Sunny
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密
from rest_framework import serializers
from .models import CourseCategory, Course, Teacher, CourseChapter, CourseLesson


class CourseCategorySerializer(serializers.ModelSerializer):
    """
    课程序列化器
    """

    class Meta:
        model = CourseCategory
        fields = ['id', 'name']


# 解决课程基本信息中只返回老师的ID的问题
# 有两种方法：
# 1 在模型类中通过给模型增加自定义字段方法来返回多个字段数据
# 2 在序列化器中重写外键字段，通过序列化器嵌套的方式来重新声明返回的外检子弹

class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'role', 'title', 'signature', "brief", "image"]


class CourseLessonModelSerializer(serializers.ModelSerializer):
    """
    课时序列化器
    """

    class Meta:
        model = CourseLesson
        fields = ["id", "name", "free_trail", "duration"]


# class CourseChapterModelSerializer(serializers.ModelSerializer):
#     """
#     课程章节序列器
#     """
#     lessons = CourseLessonModelSerializer(many=True)
#
#     class Meta:
#         model = CourseChapter
#         fields = ["id", "name", "lessons"]


class CourseModelSerializer(serializers.ModelSerializer):
    """
    课程列表的课程基本信息
    # 序列化器嵌套[被嵌套的序列化器必须声明对应的字段为模型原有的外键字段，同时这个被嵌套的序列化器必须先声明才能进行调用！]
    # 如果嵌套的序列化器数据有多条，则需要在调用序列化器时需要声明 many=True
    """
    teacher = TeacherModelSerializer()

    class Meta:
        model = Course
        fields = ["id", "name", "course_img", "students", "lessons", "pub_lessons", "price", "teacher",
                  "free_lesson_list", "discount_price", 'discount_name']


class CourseRetrieveModelSerializer(serializers.ModelSerializer):
    """
    课程单一序列化器
    """
    teacher = TeacherModelSerializer()

    class Meta:
        model = Course
        fields = ["id", "name", "course_img", "students", "lessons", "pub_lessons", "price", "teacher", "brief",
                  "level_name", "discount_name", "discount_price", "has_time"]


class CourseChapterRetrieveModelSerializer(serializers.ModelSerializer):
    """
    章节序列化器
    """

    lessons = CourseLessonModelSerializer(many=True)

    class Meta:
        model = CourseChapter
        fields = ["chapter", "name", "summary", "lessons"]
