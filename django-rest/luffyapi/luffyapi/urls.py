"""luffyapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve
import xadmin
from xadmin.plugins import xversion
from rest_framework.documentation import include_docs_urls  # 设置接口 文档访问路径

xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model


xversion.register_models()

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('docs/',include_docs_urls(title='站点页面标题')),
    path(r'xadmin/', xadmin.site.urls),
    re_path(r'media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('', include("home.urls")),
    path('cart/', include("cart.urls")),
    path('orders/', include("orders.urls")),

]
