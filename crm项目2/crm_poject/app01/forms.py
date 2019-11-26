from app01 import models
from django import forms
from django.core.exceptions import ValidationError
from multiselectfield.forms.fields import MultiSelectFormField
from django.forms.fields import BooleanField
import hashlib
from django.forms import forms
from django.forms.fields import BooleanField
from multiselectfield.forms.fields import MultiSelectFormField

#基础form组件
class BaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field, (BooleanField, MultiSelectFormField)):
                continue
            field.widget.attrs['class'] = 'form-control'

class RegForm(forms.ModelForm):
    re_password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = models.UserProfile
        fields = '__all__'
        exclude = ['is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'placeholder': '用户名'}
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': '密码'})
        self.fields['re_password'].widget.attrs = {'placeholder': '确认密码'}
        self.fields['name'].widget.attrs = {'placeholder': '姓名'}
        self.fields['mobile'].widget.attrs = {'placeholder': '手机号'}
        self.fields['department'].choices = [('', '请选择职位')] + [(i.pk, str(i)) for i in models.Department.objects.all()]

    def clean(self):
        self._validate_unique = False
        password = self.cleaned_data.get('password', "")
        re_password = self.cleaned_data.get('re_password')
        if password == re_password:
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            self.cleaned_data['password'] = md5.hexdigest()
            return self.cleaned_data
        self.add_error('password', '密码不一致')
        raise ValidationError('两次密码不一致')



class CustorForm(BaseForm):
    class Meta:
        model = models.Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ConsultRecord(BaseForm):
    class Meta:
        model = models.ConsultRecord
        fields = "__all__"

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].choices = models.Customer.objects.filter(consultant=request.user_obj).values_list('id',
                                                                                                                  'name')
        self.fields['consultant'].choices = [(request.user_obj.pk, request.user_obj)]


class Enrollment_Form(BaseForm):
    class Meta:
        model = models.Enrollment
        fields = "__all__"

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.customer_id:
            self.fields['customer'].choices = [(i.pk, str(i)) for i in request.user_obj.customers.all()]
        else:
            self.fields['customer'].choices = [(self.instance.customer_id, self.instance.customer)]
            self.fields['enrolment_class'].choices = [(i.pk, str(i)) for i in self.instance.customer.class_list.all()]
