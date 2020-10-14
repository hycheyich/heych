# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 17:11
# @Author  : Sunny
# @Site    : 
# @File    : utils.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import Account


# jwt自定义返回函数
def jwt_response_payload_handler(token, user=None, request=None):
    """
    Returns the response data for both the login and refresh views.
    Override to return a custom response such as including the
    serialized representation of the User.

    Example:

    def jwt_response_payload_handler(token, user=None, request=None):
        return {
            'token': token,
            'user': UserSerializer(user, context={'request': request}).data
        }
    自定义jwt认证成功返回数据
    :parameter token 本次响应给客户端的jwt字符串
    :parameter user  本次查询出来的用户模型对象
    :parameter request  本次客户端的请求对象

    """
    return {
        'token': token,
        'id': user.id,
        'username': user.username
    }


def get_account_by_user(username):
    """根据username获取用户信息"""
    try:
        user = Account.objects.get(Q(username=username) | Q(mobile=username))
    except Account.DoesNotExist:
        user = None
    return user


# 实现多用户登陆
class UsernameMobileAuthBackend(ModelBackend):
    """实现用户多条件登录"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = get_account_by_user(username)
        except Account.DoesNotExist:
            user = None
        if user is not None and user.check_password(password) and user.is_active:
            return user
