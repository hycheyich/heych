from django.conf.urls import url, include
from app01 import views
from app01.views import base, consultrecord, Customer, enrollment, user,teacher

urlpatterns = [
    # 登陆
    url('login/', user.login, name='login'),
    # 注册
    url('register/', user.register, name='register'),
    # 注册
    url(r'logout/', user.logout, name='logout'),
    # 客户展示
    url(r'index/', Customer.Customer.as_view(), name='index'),
    url(r'my_curtor/', Customer.Customer.as_view(), name='my_curtor'),
    # 客户添加和编辑
    url(r'curtor_add/$', Customer.add, name='curtoradd'),
    url(r'custoredit/(\d+)/', Customer.add, name='custoredit'),
    # 某个销售的跟进记录
    url(r'^consult_record/$', consultrecord.ConsultRecordList.as_view(), name='consult_record'),
    # 某个客户的跟进记录
    url(r'^consult_record/(?P<customer_id>\d+)/$', consultrecord.ConsultRecordList.as_view(),
        name='one_consult_record'),
    # 跟进记录添加和编辑
    url(r'^consult_record_add/$', consultrecord.consult_record_change, name='consult_record_add'),
    url(r'^consult_record_edit/(\d+)/$', consultrecord.consult_record_change, name='consult_record_edit'),
    # 显示报名表
    url(r'^enrollment_list/$', enrollment.EnrollmentList.as_view(), name='enrollment_list'),
    url(r'^enrollment_list/(?P<customer_id>\d+)/$', enrollment.EnrollmentList.as_view(), name='one_enrollment_list'),
    # 报名表添加和编辑
    url(r'^enrollment_add/(?P<customer_id>\d+)$', enrollment.enrollment_change, name='enrollment_add'),
    url(r'^enrollment_add2/$', enrollment.enrollment_change, name='enrollment_add2'),  # 单一添加
    url(r'^enrollment_edit/(?P<pk>\d+)$', enrollment.enrollment_change, name='enrollment_edit'),

    #学习记录


    #班级
    url(r'class/$',teacher.classlist.as_view(),name = 'class_list'),
    url(r'class_edit/(?P<course>\d+)/$',teacher.classchange,name = 'class_edit'),
    url(r'class_add/$',teacher.classchange,name = 'class_add'),


    url(r'course_record/(?P<class_id>\d+)/$',teacher.course_record.as_view(),name = 'course_Record_list'),
    url(r'course_record_add/(?P<class_id>\d+)/$',teacher.course_Record_changes,name = 'course_record_add'),
    url(r'course_record_edit/(\d+)/$',teacher.course_Record_changes,name = 'course_record_edit'),

    url(r'^study_record_list/(?P<course_record_id>\d+)/$', teacher.study_record_list, name='study_record_list'),






    # url(r'paging/',views.paging),
]
