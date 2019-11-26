from django.shortcuts import render,redirect,reverse
from djangoapp1 import models
from django import  forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.http import JsonResponse
# Create your views here.
from djangoapp1.forms import  UserForm,laboratoryForm,BalanceForm



def index(request):
    """
    主页
    :param request:
    :return:
    """
    laboratory_obj = models.laboratory.objects.all()
    user_obj = models.User.objects.all()
    balance_obj = models.Balance.objects.all()
    content={
        'laboratory_obj':laboratory_obj,
        'user_obj':user_obj,
        'balance_obj':balance_obj
    }

    return  render(request, 'index.html', content)

def  register(request):
    """
    注册
    :param request:
    :return:
    """
    content={
        'registflag':True,
        'loginflage': True,
        'error':"",
    }
    if request.method =='POST':
        post = request.POST
        username = post.get('registerUsername')
        name = post.get('name')
        phone = post.get('phone')
        pwd = post.get('registerPassword')
        if models.User.objects.filter(user_name=username) and len(pwd)<20 and len(name)<6:
            error = "用户名存在"
            return render(request,'register.html',content)
        else:
            obj = models.User.objects.create(user_name=username,uname=name,phone=phone,passwd=pwd)
            obj.save()
            return redirect(reverse('login'))
    return render(request,'register.html',content)

def login(request):
    """
    登陆
    :param request:
    :return:
    """
    content = {
        'registflag': True,
        'loginflage': True,
        'error':"",
    }
    if request.method == 'POST':
        post = request.POST
        username = post.get('loginUsername')
        pwd = post.get('loginPassword')
        repwd = post.get('loginPassword')
        if  len(pwd)<20 and pwd == repwd  and models.User.objects.filter(user_name=username,passwd=pwd) :
            return redirect(reverse('index'))
        else:
            error = '用户名或密码错误'
            return  render(request,'login.html',content)
    return render(request, 'login.html', content)

def user(request):
    """
    用户查询
    :param request:
    :return:
    """
    user_obj = models.User.objects.all()
    content = {
        'user_obj':user_obj
    }
    return render(request,'user.html',content)
def useradd(request):
    """
    用户添加
    :param request:
    :return:
    """
    if request.method == 'POST':
        form_obj = UserForm(request.POST)
        if form_obj.is_valid():  # 校验数据
            # 插入数据库
            user=  form_obj.cleaned_data.get('user')
            passwd=  form_obj.cleaned_data.get('passwd')
            uname=  form_obj.cleaned_data.get('uname')
            phone=  form_obj.cleaned_data.get('phone')
            obj = models.User.objects.create(user_name=user,passwd=passwd,uname=uname,phone=phone)
            obj.save()
            return redirect(reverse('user'))
    else:
        form_obj = UserForm()
        UserForm.pk=0
    return render(request, 'user_add.html', {'form_obj': form_obj})

def useredit(request,pk):
    user_obj = models.User.objects.filter(pk=pk).first()
    UserForm.pk = pk
    if request.method == 'POST':
        form_obj = UserForm(request.POST)
        if form_obj.is_valid():  # 校验数据
            # 插入数据库
            user_obj.user_name=  form_obj.cleaned_data.get('user')
            user_obj.passwd=  form_obj.cleaned_data.get('passwd')
            user_obj.uname=  form_obj.cleaned_data.get('uname')
            user_obj.phone=  form_obj.cleaned_data.get('phone')
            user_obj.save()
            return redirect(reverse('user'))
    else:
        form_obj = UserForm()
        dic = dict(form_obj.fields)
        dic['user'].initial = user_obj.user_name
        dic['passwd'].initial = user_obj.passwd
        dic['repasswd'].initial = user_obj.passwd
        dic['uname'].initial = user_obj.uname
        dic['phone'].initial = user_obj.phone
    # return render(request, 'user_edit.html', {'form_obj': form_obj.as_p()})
    return JsonResponse({'form':form_obj.as_p()})

def userldel(request):
    """
    用户删除
    :param request:
    :return:
    """
    user_get = request.GET
    user_id = user_get.get('pk')
    obj = models.User.objects.filter(pk=user_id).filter()
    if  obj:
        obj.delete()
        content = {'ret':True}
    else:
        content = {'ret': False}
    return JsonResponse(content)


def laboratory(request):
    """
    实验室查询
    :param request:
    :return:
    """
    laboratory_obj = models.laboratory.objects.all()
    content = {
        'laboratory_obj': laboratory_obj
    }
    return render(request, 'laboratory.html', content)


def laboratoryadd(request):
    if request.method == 'POST':
        form_obj = laboratoryForm(request.POST)
        if form_obj.is_valid():  # 校验数据
            # 插入数据库
            lname = form_obj.cleaned_data.get('lname')
            floor = form_obj.cleaned_data.get('floor')
            room_num = form_obj.cleaned_data.get('room_num')
            user = form_obj.cleaned_data.get('user')
            user_obj = models.User.objects.filter(pk=user).first()
            obj = models.laboratory.objects.create(lname=lname, floor=floor, room_num=room_num, user=user_obj)
            obj.save()
            return redirect(reverse('laboratory'))
    else:
        form_obj = laboratoryForm()
        laboratoryForm.pk = 0
    return render(request, 'laboretory_add.html', {'form_obj': form_obj})

def laboratorydel(request):
    laboratory_get = request.GET
    laboratory_id = laboratory_get.get('pk')
    obj = models.laboratory.objects.filter(pk=laboratory_id).filter()
    if obj:
        obj.delete()
        content = {'ret': True}
    else:
        content = {'ret': False}
    return JsonResponse(content)

def laboratoryedit(request,pk):
    laboratory_obj = models.laboratory.objects.filter(pk=pk).first()
    laboratoryForm.pk = pk
    if request.method == 'POST':
        form_obj = laboratoryForm(request.POST)
        if form_obj.is_valid():  # 校验数据
            # 插入数据库
            laboratory_obj.lname = form_obj.cleaned_data.get('lname')
            laboratory_obj.floor = form_obj.cleaned_data.get('floor')
            laboratory_obj.room_num = form_obj.cleaned_data.get('room_num')
            user = form_obj.cleaned_data.get('user')
            user_obj = models.User.objects.filter(pk=user).first()
            laboratory_obj.user = user_obj
            laboratory_obj.save()
            return redirect(reverse('laboratory'))
    else:
        form_obj = laboratoryForm()
        dic = dict(form_obj.fields)
        dic['lname'].initial = laboratory_obj.lname
        dic['floor'].initial = laboratory_obj.floor
        dic['room_num'].initial = laboratory_obj.room_num
        dic['user'].initial = laboratory_obj.user.pk
    return render(request, 'laboretory_edit.html', {'form_obj': form_obj})

def balance(request) :
    """
    物资查询
    :param request:
    :return:
    """
    balance_obj = models.Balance.objects.all()
    content={
        'balance_obj':balance_obj,
    }
    return  render(request, 'Balance.html', content)

def balanceadd(request):
    """
    物资添加
    :param request:
    :return:
    """
    if request.method == 'POST':
        form_obj = BalanceForm(request.POST)
        if form_obj.is_valid():  # 校验数据
            # 插入数据库
            bname =  form_obj.cleaned_data.get('bname')
            btext=  form_obj.cleaned_data.get('btext')
            buser=  form_obj.cleaned_data.get('buser')
            blaboratory = form_obj.cleaned_data.get('blaboratory')
            user_obj = models.User.objects.filter(pk=buser).first()
            blaboratory_obj = models.laboratory.objects.filter(pk=blaboratory).first()
            obj = models.Balance.objects.create(bname=bname,btext=btext,buser=user_obj,laboratory=blaboratory_obj)
            obj.save()
            return redirect(reverse('balance'))
    else:
        form_obj = BalanceForm()
        BalanceForm.pk = 0
    return render(request, 'Balance_add.html', {'form_obj': form_obj})


def balanceedit(request,pk):
    """
    编辑功能
    :param request:
    :return:
    """
    balance_obj = models.Balance.objects.filter(pk=pk).first()
    BalanceForm.pk = pk
    if request.method == 'POST':
        form_obj = BalanceForm(request.POST)
        if form_obj.is_valid():  # 校验数据
            # 插入数据库
            buser = form_obj.cleaned_data.get('buser')
            blaboratory = form_obj.cleaned_data.get('blaboratory')
            user_obj = models.User.objects.filter(pk=buser).first()
            blaboratory_obj = models.laboratory.objects.filter(pk=blaboratory).first()
            obj = models.Balance.objects.filter(pk=form_obj.pk).first()
            obj.bname = form_obj.cleaned_data.get('bname')
            obj.btext = form_obj.cleaned_data.get('btext')
            obj.buser = user_obj
            obj.laboratory =blaboratory_obj
            obj.save()
            return redirect(reverse('balance'))
    else:
        form_obj = BalanceForm()
        dic = dict(form_obj.fields)
        dic['bname'].initial = balance_obj.bname
        dic['btext'].initial =  balance_obj.btext
        dic['buser'].initial =  balance_obj.buser.pk
        dic['blaboratory'].initial =  balance_obj.laboratory.pk
    return render(request, 'Balance_edit.html', {'form_obj': form_obj})


def balancedel(request):
    balance_get = request.GET
    balance_id = balance_get.get('pk')
    obj = models.Balance.objects.filter(pk=balance_id).filter()
    if obj:
        obj.delete()
        content = {'ret': True}
    else:
        content = {'ret': False}
    return JsonResponse(content)


