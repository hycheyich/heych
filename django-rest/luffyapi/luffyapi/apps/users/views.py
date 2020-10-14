import json
import random
from luffyapi.libs.geetest import GeetestLib
from rest_framework.response import Response
from django_redis import get_redis_connection
from rest_framework import status
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import Account
from .serializer import UserModelSerializer
import requests
from my_cerely.sms.tasks import send_sms_code


# Create your views here.


# 极验验证
# 第一步前端获取流水号
# 第二步前端提交后进行校验

class GeetestCapchaAPIView(APIView):
    def get(self, request, *args, **kwargs):
        """
          电脑端获取流水号
          """
        user_id = 'test'
        gt = GeetestLib(settings.GEETEST['pc_geetest_id'], settings.GEETEST['pc_geetest_key'])
        status = gt.pre_process(user_id)
        response_str = gt.get_response_str()
        print(response_str)
        return Response(json.loads(response_str))

    def post(self, request, *args, **kwargs):
        """
        电脑端获取ajax请求验证
        """
        gt = GeetestLib(settings.GEETEST['pc_geetest_id'], settings.GEETEST['pc_geetest_key'])
        challenge = request.data.get(gt.FN_CHALLENGE, '')
        validate = request.data.get(gt.FN_VALIDATE, '')
        seccode = request.data.get(gt.FN_SECCODE, '')
        print(challenge, validate, seccode)
        result = gt.failback_validate(challenge, validate, seccode)
        result = {"status": "success"} if result else {"status": "fail"}
        return Response(result)


# 腾讯注册验证
aid = '2010971413'
AppSecretKey = '0VMjGN4hdKbHf2bmFk4BMEg**'


class VerifyAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(aid, status=status.HTTP_200_OK)

    def post(self, request):
        Ticket = request.data.get('ticket')
        Randstr = request.data.get('randstr')
        # 上线后这里要进行修改,改为动态获取请求的ip
        UserIP = '127.0.0.1'
        ret = requests.get('https://ssl.captcha.qq.com/ticket/verify', params={
            'aid': aid,
            'AppSecretKey': AppSecretKey,
            'Ticket': Ticket,
            'Randstr': Randstr,
            'UserIP': UserIP
        })
        dic = ret.json()
        if dic and dic.get('response') == '1':
            return Response('校验成功!', status=status.HTTP_200_OK)
        return Response(dic.get('err_msg'), status=status.HTTP_400_BAD_REQUEST)


# 注册功能实现
# 开发流程 模型-》视图-》序列化器->路由


class UserAPIView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = UserModelSerializer


# from redis import StrictRedis
# class RedisDemoApiView(APIView):
#     """
#     演示python操作的redis
#     """
#
#     def get(self, request, *args, **kwargs):
#         return Response('ok')


class SmsCodeAPIView(APIView):
    def get(self, request, mobile):
        """
        注册时采用短信验证注册
        获取短信验证接口
        """
        # 1 查询数据库是否存在此用户
        try:
            Account.objects.get(mobile=mobile)
            return Response({'message': '手机号已经被注册'}, status=status.HTTP_400_BAD_REQUEST)
        except Account.DoesNotExist:
            # 表示未注册
            pass
        # 2 验证是否在一分钟内发送过验证码，避免频繁发送
        redis_conn = get_redis_connection('sms_code')
        print(redis_conn)
        ret = redis_conn.get("interval_%s" % mobile)
        if ret is not None:
            return Response({'message': '短信发送过于频繁'})
        # 3 生成验证码
        sms_code = '%6d' % random.randint(100, 999999)
        print(sms_code)

        # 4 将验证码和手机号保存到缓存中
        # redis_conn.setex("键","时间","值")
        # redis_conn.setex("键","时间","值")
        # 使用redis提供的事务配合管道[pipeline]操作来保证多条命令要么一起执行，要么一起失败！
        # redis的事务也只能控制数据的修改，设置和删除操作，对于获取数据来说，没必要使用事务！
        pipe = redis_conn.pipeline()  # 创建一个管道
        pipe.multi()  # 开启redis事务
        pipe.setex("sms_%s" % mobile, settings.SMS["sms_expire_time"], sms_code)
        pipe.setex("interval_%s" % mobile, settings.SMS["sms_interval_time"], "_")
        pipe.execute()  # 执行redis事务
        # redis_conn.setex("sms_%s" % mobile, 60, sms_code)
        # redis_conn.setex("interval_%s" % mobile, settings.SMS['sms_interval_time'], "_")  # 保存验证码是否在一份中内发送过
        # 4 发送验证码

        # 5. 发送短信
        # 调用celery执行异步任务
        # 1. 声明一个和celery一模一样的任务函数，但是我们可以导包来解决

        # 2. 调用任务函数，发布任务
        send_sms_code.delay(mobile, sms_code)
        # send_sms_code.delay() 如果调用的任务函数没有参数，则不需要填写任何内容

        return Response({"message": '验证码正在发送中，请等待'})
