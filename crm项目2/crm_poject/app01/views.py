from django.shortcuts import render, HttpResponse, redirect, reverse
from app01 import models
from app01.forms import RegForm, CustorForm, ConsultRecord, Enrollment_Form
import hashlib
from utils.pagination import Pagination
from django.db.models import Q
from django.db import transaction

from django.views import View
# Create your views here.

def login(request):
    """
    登陆页面
    :param request:登陆请求
    :return:
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        password = md5.hexdigest()
        user_obj = models.UserProfile.objects.filter(username=username, password=password, is_active=True).first()
        if user_obj:
            request.session['username'] = username
            request.session['pk'] = user_obj.pk
            request.session['is_login'] = True
            return redirect(reverse('app01:index'))
        else:
            return render(request, 'register_login/login.html', {'error': '用户名或密码'})
    return render(request, 'register_login/login.html')


def logout(request):
    """
    注销
    :param request:
    :return:
    """
    request.session.delete()
    return redirect(reverse('app01:login'))


def register(request):
    """
    注册
    :param request:
    :return:
    """
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            # 校验通过
            # 插入数据库
            reg_form.save()
            return redirect(reverse('app01:login'))
    reg_form = RegForm()

    return render(request, 'register_login/register.html', {'reg_form': reg_form})


def index(request):
    """
    主页
    :param request:
    :return:
    """
    if request.path_info == reverse('app01:index'):
        customer_lis = models.Customer.objects.filter(consultant__isnull=True)
    else:
        customer_lis = models.Customer.objects.filter(consultant=request.user_obj)
    if request.method == 'POST':
        lis = request.POST.getlist('optionses')
        if request.POST.get('gzs') == "1":
            for i in lis:
                customer_obj = models.Customer.objects.filter(pk=int(i)).first()
                customer_obj.consultant = models.UserProfile.objects.filter(pk=request.session.get('pk')).first()
                customer_obj.save()
            return redirect(reverse('app01:index'))
        else:
            for i in lis:
                customer_obj = models.Customer.objects.filter(pk=int(i)).first()
                customer_obj.consultant = None
                customer_obj.save()
            return redirect(reverse('app01:my_curtor'))
    return render(request, 'index.html', {'customer_lis': customer_lis})


def sousuo(request):
    sousuo_text = request.POST.get('sousuo')
    if sousuo_text:
        customer_lis = models.Customer.objects.filter(Q(qq__contains=sousuo_text) | Q(name__contains=sousuo_text),
                                                      consultant_id=request.session.get('pk'))
        return render(request, 'index.html', {'customer_lis': customer_lis, 'sousuo': sousuo_text})
    else:
        return redirect(reverse('app01:index'))





class Baseview(View):

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        if not hasattr(self, action):
            return HttpResponse('没有此方法')
        ret = getattr(self, action)()
        if ret:
            return ret

        return self.get(request, *args, **kwargs)

    def query(self, field_names):
        query = self.request.GET.get('query', '')
        q = Q()
        q.connector = 'OR'
        if not query:
            return q
        for i in field_names:
            q.children.append(Q(('{}__contains'.format(i), query)))
        return q


class Customer(Baseview):

    def get(self, request, *args, **kwargs):
        if request.path_info == reverse('app01:index'):
            customer_lis = models.Customer.objects.filter(consultant__isnull=True)
        else:
            customer_lis = models.Customer.objects.filter(consultant=request.user_obj)

        q = self.query(['name', 'phone', 'qq'])

        page_obj = Pagination(request.GET.get('page', 1), customer_lis.filter(q).count(), request.GET.copy(), 2)

        return render(request, 'index.html',
                      {
                          'customer_lis': customer_lis.filter(q)[page_obj.start:page_obj.end],
                          'url': reverse('app01:index'),
                          'page_obj': page_obj,
                      })

    def multi_apply(self):
        """
        公户转私户
        :return:
        """
        pk_list = self.request.POST.getlist('optionses')  # 客户列表
        from django.conf import settings
        self.request.user_obj.customers.add(*models.Customer.objects.filter(pk__in=pk_list))
        if self.request.user_obj.customers.all().count() + len(pk_list) > settings.MAX_CUSTOMER_NUM:
            return HttpResponse('做人留一线，事后好相见')
        try:
            with transaction.atomic():

                query_set = models.Customer.objects.filter(pk__in=pk_list, consultant=None).select_for_update()  # 行级锁
                # 判断客户是否被其他销售抢走
                if len(query_set) == len(pk_list):
                    return query_set.update(consultant=self.request.user_obj)
                else:
                    return HttpResponse('手速慢，被其他人抢走')

        except Exception:
            pass

    def multi_pul(self):
        """
        私户转公户
        :return:
        """
        pk_list = self.request.POST.getlist('optionses')

        self.request.user_obj.customers.remove(*models.Customer.objects.filter(pk__in=pk_list))


def add(request, pk=None):
    custor_obj = models.Customer.objects.filter(pk=pk).first()
    form_obj = CustorForm(instance=custor_obj)
    if request.method == 'POST':
        form_obj = CustorForm(request.POST, instance=custor_obj)
        if form_obj.is_valid():
            form_obj.save()
            if request.path_info == reverse('app01:curtoradd'):
                if request.POST.get('consultant'):
                    return redirect('app01:my_curtor')
                else:
                    return redirect('app01:index')
            else:
                path = request.GET.get('path')
                return redirect(path)
    return render(request, 'consultant/curtor_add.html', {'form_obj': form_obj})


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
    form_obj = Enrollment_Form(request,instance=obj)
    if request.method == "POST":
        form_obj = Enrollment_Form(request,request.POST, instance=obj)
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

# def custoradd(request):
#     form_obj = CustorForm()
#     if request.method == 'POST':
#         form_obj = CustorForm(request.POST)
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect(reverse('app01:index'))
#     return render(request, 'curtor_add.html', {'form_obj': form_obj})
#
#
# def custoredit(request, pk):
#     custor_obj = models.Customer.objects.filter(pk=pk).first()
#     form_obj = CustorForm(instance=custor_obj)
#     if request.method == 'POST':
#         form_obj = CustorForm(request.POST, instance=custor_obj)
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect(reverse('app01:index'))
#     return render(request, 'curtor_edit.html', {'form_obj': form_obj})

# from django.http import QueryDict
# q = QueryDict()
# q.copy()


# Users = [{'user': 'alex{}'.format(i), 'password': 'alexdsb{}'.format(i)} for i in range(1, 478)]


# def paging(request):
#     page_obj = Pagination(request.GET.get('page'), len(Users))
#     return render(request, 'paging.html', {'User': Users[page_obj.start:page_obj.end], 'page_obj': page_obj})
