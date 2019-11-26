from django import template
from django.shortcuts import reverse
from django.http.request import QueryDict

register = template.Library()

@register.simple_tag()
def reverse_url(request, name, *args, **kwargs):
    # 第一种解决方法：拼接
    # url = f'{reverse(name,*args,**kwargs)}?path={request.get_full_path()}'
    # 第二种：
    dic = QueryDict(mutable=True)
    dic['path'] = request.get_full_path()
    url = f"{reverse(name,args=args,kwargs=kwargs)}?{dic.urlencode()}"
    return url
