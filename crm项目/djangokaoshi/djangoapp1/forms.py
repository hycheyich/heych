from djangoapp1 import models
from django import  forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class UserForm(forms.Form):
    """
    用户form组件校验
    """
    user = forms.CharField(max_length=20,label='用户名',widget=forms.TextInput(attrs={'class': 'form-control','id':'ds_host'}))
    passwd = forms.CharField(max_length=20,min_length=6,widget=forms.PasswordInput(attrs={'class': 'form-control','id':'ds_pwd'}),label='密码')
    repasswd = forms.CharField(max_length=20,min_length=6,widget=forms.PasswordInput(attrs={'class': 'form-control','id':'ds_repwd'}),label='确认密码')
    uname = forms.CharField(max_length=6,label='姓名',widget=forms.TextInput(attrs={'class': 'form-control','id':'ds_name'}))
    phone = forms.CharField(max_length=11,validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式不正确')],label='手机号',widget=forms.TextInput(attrs={'class': 'form-control','id':'ds_phone'}))
    pk = 0
    def clean(self):
        password = self.cleaned_data.get('passwd')
        re_password = self.cleaned_data.get('repasswd')
        if password == re_password:
            return self.cleaned_data
        else:
            self.add_error('passwd', '两次密码不一致!!')
            raise ValidationError('两次密码不一致')

    def clean_user(self):
        # 局部钩子
        # 通过校验   返回当前字段的值
        # 不通过校验   抛出异常
        value = self.cleaned_data.get('user')
        if hasattr(self, 'pk') and self.pk:
            return value
        if models.User.objects.filter(user_name=value):
            raise ValidationError('用户名已存在')
        return value

class BalanceForm(forms.Form):
    """
    物资form组件校验
    """
    bname = forms.CharField(max_length=20, label='物资名称',widget=forms.TextInput(attrs={'class': 'form-control','id':'ds_bname'}))
    btext = forms.CharField(max_length=50, label='物资描述',widget=forms.TextInput(attrs={'class': 'form-control','id':'ds_btext'}))
    buser = forms.ChoiceField(initial=1,widget=forms.Select(attrs={'class': 'form-control','id':'ds_buser'}),label='购买人')
    blaboratory = forms.ChoiceField(label="所属实验室",widget=forms.Select(attrs={'class': 'form-control','id':'ds_bla'}))
    pk = 0

    def __init__(self, *args, **kwargs):
        super(BalanceForm, self).__init__(*args, **kwargs)
        self.fields['blaboratory'].choices = models.laboratory.objects.all().values_list('id', 'lname')
        self.fields['buser'].choices = models.User.objects.all().values_list('id', 'user_name')

    def clean_bname(self):
        # 局部钩子
        # 通过校验   返回当前字段的值
        # 不通过校验   抛出异常
        value = self.cleaned_data.get('bname')

        print(self.pk)
        if hasattr(self,'pk') and self.pk:
            return value
        if models.Balance.objects.filter(bname=value):
            raise ValidationError('物品已存在')
        return value

class laboratoryForm(forms.Form):
    lname = forms.CharField(max_length=20, label='实验室名称',widget=forms.TextInput(attrs={'class': 'form-control','id':'ds_lname'}))
    floor = forms.IntegerField(label='楼层',min_value=1,max_value=10,)
    room_num = forms.CharField(max_length=20, label='房间号',widget=forms.TextInput(attrs={'class': 'form-control','id':'ds_room_num'}))
    user = forms.ChoiceField(label="负责人",widget=forms.Select(attrs={'class': 'form-control','id':'ds_user'}))
    pk = 0

    def __init__(self, *args, **kwargs):
        super(laboratoryForm, self).__init__(*args, **kwargs)
        self.fields['user'].choices = models.User.objects.all().values_list('id', 'user_name')

    def clean_lname(self):
        # 局部钩子
        # 通过校验   返回当前字段的值
        # 不通过校验   抛出异常
        value = self.cleaned_data.get('lname')
        if hasattr(self, 'pk') and self.pk:
            return value
        if models.laboratory.objects.filter(lname=value):
            raise ValidationError('实验室名已存在')
        return value