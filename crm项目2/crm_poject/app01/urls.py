from django.conf.urls import url, include
from app01 import views

urlpatterns = [
    url('login/', views.login, name='login'),
    url('register/', views.register, name='register'),
    url(r'index/', views.Customer.as_view(), name='index'),
    url(r'my_curtor/', views.Customer.as_view(), name='my_curtor'),

    url(r'logout/', views.logout, name='logout'),
    url(r'curtor_add/$', views.add, name='curtoradd'),
    url(r'custoredit/(\d+)/', views.add, name='custoredit'),
    #某个销售的跟进记录
    url(r'^consult_record/$', views.ConsultRecordList.as_view(), name='consult_record'),
    #某个客户的跟进记录
    url(r'^consult_record/(?P<customer_id>\d+)/$', views.ConsultRecordList.as_view(), name='one_consult_record'),
    #跟进记录添加和编辑
    url(r'^consult_record_add/$', views.consult_record_change, name='consult_record_add'),
    url(r'^consult_record_edit/(\d+)/$', views.consult_record_change, name='consult_record_edit'),
    #显示报名表
    url(r'^enrollment_list/$', views.EnrollmentList.as_view(), name='enrollment_list'),
    url(r'^enrollment_list/(?P<customer_id>\d+)/$', views.EnrollmentList.as_view(), name='one_enrollment_list'),
    #
    url(r'^enrollment_add/(?P<customer_id>\d+)$', views.enrollment_change, name='enrollment_add'),
    url(r'^enrollment_add2/$', views.enrollment_change, name='enrollment_add2'),

    url(r'^enrollment_edit/(?P<pk>\d+)$', views.enrollment_change, name='enrollment_edit'),

    # url(r'paging/',views.paging),
]
