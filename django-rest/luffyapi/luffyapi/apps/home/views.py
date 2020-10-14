from django.shortcuts import render
from rest_framework.generics import ListAPIView
from luffyapi.settings import constants


# Create your views here.

from .models import Banner,Nav
from .serializers import BannerModelSerializer,NavModelSerializer
class BannerListAPIView(ListAPIView):
    """
    轮播图视图函数
    """
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("orders", "-id")[
               :constants.HOME_BANNER_LENGTH]
    serializer_class = BannerModelSerializer


class NavHeaderListAPIView(ListAPIView):
    """
    顶部导航栏视图函数
    """
    queryset = Nav.objects.filter(is_show=True, is_delete=False, opt=0).order_by('orders', '-id')[
               :constants.HEADER_NAV_LENGTH]
    serializer_class = NavModelSerializer


class NavFooterListAPIView(ListAPIView):
    """
    底部导航栏视图函数
    """
    queryset = Nav.objects.filter(is_show=True, is_delete=False, opt=1).order_by('orders', '-id')[
               :constants.FOOTER_NAV_LENGTH]
    serializer_class = NavModelSerializer
