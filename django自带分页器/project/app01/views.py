from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
Users = [{'user': 'nihao{}'.format(i), 'password': 'hello_{}'.format(i)} for i in range(1, 478)]
def index(request):
    paginator = Paginator(Users,2)
    print(paginator.count)
    print(paginator.page_range)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数，返回第一页。
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'contacts': contacts})