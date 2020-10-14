# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 16:18
# @Author  : Sunny
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密
from django.urls import path, re_path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('geetest/', views.GeetestCapchaAPIView.as_view()),
    path('verify/',views.VerifyAPIView.as_view()),
    path('', views.UserAPIView.as_view()),
    re_path("sms/(?P<mobile>1[3-9]\d{9})/", views.SmsCodeAPIView.as_view()),

]
