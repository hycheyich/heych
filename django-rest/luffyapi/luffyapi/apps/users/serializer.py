# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 20:07
# @Author  : Sunny
# @Site    : 
# @File    : serializer.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密
import re
from rest_framework import serializers
from django_redis import get_redis_connection
from .models import Account


class UserModelSerializer(serializers.ModelSerializer):
    """
    用户注册的序列化器
    """
    # 字段申明
    sms_code = serializers.CharField(write_only=True, max_length=6, required=True, help_text="短信验证码")
    token = serializers.CharField(read_only=True, help_text='jwt的认证token')

    # 模型相关的声明
    class Meta:
        model = Account
        fields = ["mobile", "password", "sms_code", "id", "username", "token"]
        # 给模型序列化器进行额外声明
        extra_kwargs = {
            "password": {"min_length": 6, "write_only": True, },
            "mobile": {"write_only": True},
            "username": {"read_only": True},
        }

    def validate_mobile(self, data):
        ret = re.match('1[3-9]\d{9}', data)
        if not ret:
            raise serializers.ValidationError("对不起，手机号码格式有误！")

        # 是否被注册了
        try:
            Account.objects.get(mobile=data)
            raise serializers.ValidationError("对不起，手机号码已经被使用！")
        except Account.DoesNotExist:
            pass
        return data

    def validate(self, attrs):
        """
        验证数据
        """
        # 1 从redis中取出数据
        sms_code_conn = get_redis_connection('sms_code')
        mobile = attrs.get('mobile')
        http_sms_code = attrs.get('sms_code')
        redis_sms_code = sms_code_conn.get("sms_%s" % mobile)
        if redis_sms_code is None:
            raise serializers.ValidationError("短信验证码已经失效了！")
        # 2. 把用户提交的短信验证码和redis里面的进行对比是否正确
        if http_sms_code != redis_sms_code.decode():
            raise serializers.ValidationError("短信验证码错误！")

        # 3. 如果正确了，则删除掉redis中的验证码
        sms_code_conn.delete("sms_%s" % mobile)

        return attrs

    def create(self, validated_data):
        """
        创建数据
        validated_data表示校验过后的数据
        """
        mobile = validated_data.get("mobile")
        password = validated_data.get("password")
        try:
            user = Account.objects.create_user(mobile=mobile, password=password, username=mobile)
            from rest_framework_jwt.settings import api_settings
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            user.token = jwt_encode_handler(payload)
            return user
        except:
            raise serializers.ValidationError("保存用户失败！")
