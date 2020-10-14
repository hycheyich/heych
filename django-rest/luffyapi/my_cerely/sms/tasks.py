# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 19:38
# @Author  : Sunny
# @Site    : 
# @File    : tasks.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密

# celery的任务必须写在tasks.py的文件中，别的文件名称不识别!!!
import logging
from my_cerely.main import app
from django.conf import settings
from luffyapi.libs.yuntongxun.sms import CCP

log = logging.getLogger("django")


@app.task(name='send_sms_code')  # name表示设置任务的名称，如果不填写，则默认使用函数名做为任务名
def send_sms_code(mobile, sms_code):
    try:
        ccp = CCP()
        ccp.send_sms_code(mobile, [sms_code, settings.SMS["sms_expire_time"] // 60], settings.SMS["sms_template_id"])
    except:
        log.error("发送短信失败！用户手机：%s，验证码:%s" % (mobile, sms_code))


@app.task(name="send_sms2")  # name表示设置任务的名称，如果不填写，则默认使用函数名做为任务名
def send_sms2():
    print("发送短信任务2!!!")
