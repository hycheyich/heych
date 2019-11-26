
from django.conf.urls import url
from django.contrib import admin
from djangoapp1 import views
urlpatterns = [
    url(r"^user/$",views.user,name='user'),
    url(r'^user_add/',views.useradd,name='useradd'),
    url(r'^user_del/',views.userldel,name='userldel'),
    url(r'^user_edit/(\d+)/$',views.useredit,name='useredit'),

    url(r"^laboratory/$",views.laboratory,name='laboratory'),
    url(r"^laboratoryadd/$",views.laboratoryadd,name='laboratoryadd'),
    url(r'^laboratory_del/', views.laboratorydel, name='laboratorydel'),
    url(r'^laboratory_edit/(\d+)/$', views.laboratoryedit, name='laboratoryedit'),

    url(r"^balance/$",views.balance,name='balance'),
    url(r"^balanceadd/$",views.balanceadd,name='balanceadd'),
    url(r"^balanceedit/(\d+)/$",views.balanceedit,name='balanceedit'),
    url(r'^balance_del/', views.balancedel, name='balancedel'),
]




