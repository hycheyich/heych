from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from .serializers import CourseCategorySerializer, CourseModelSerializer, CourseRetrieveModelSerializer, \
    CourseChapterRetrieveModelSerializer
from .models import CourseCategory, Course, CourseChapter
from .paginations import CourseListPageination


# Create your views here.
# 模型 -》 视图-》 序列化器-》路由

class CourseCategoryModelAPIView(ListAPIView):
    """
    课程大类视图 【python】
    """
    queryset = CourseCategory.objects.filter(is_show=True, is_delete=False).order_by('orders', '-id')
    serializer_class = CourseCategorySerializer


class CourseModelAPIView(ListAPIView):
    """
    实战课程视图 【python3天入门】
    """
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by('orders', 'id')
    serializer_class = CourseModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ["course_category"]
    ordering_fields = ["id", "students", "price"]
    pagination_class = CourseListPageination


class CourseRetrieveAPIView(RetrieveAPIView):
    """
    单独为课程类视图【详情页】
    """
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by('orders', 'id')
    serializer_class = CourseRetrieveModelSerializer


class CourseChapterListAPIView(ListAPIView):
    """
    筛选出课程相关的章节和课时
    """
    queryset = CourseChapter.objects.filter(is_show=True, is_delete=False).order_by('orders', 'id')
    serializer_class = CourseChapterRetrieveModelSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['course']
