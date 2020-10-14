# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 19:13
# @Author  : Sunny
# @Site    : 
# @File    : sms.py
# @Software: PyCharm
# @WeChat public address : 程序猿与python之间的秘密
# 对云通讯的api接口进行封装
from .CCPRestSDK import REST

# 说明：主账号，登陆云通讯网站后，可在"控制台-应用"中看到开发者主账号ACCOUNT SID
_accountSid = '8aaf07086f0d2ca0016f0dfa873501d6'

# 说明：主账号Token，登陆云通讯网站后，可在控制台-应用中看到开发者主账号AUTH TOKEN
_accountToken = '01e5766a0d4745ada1727ce2bd481912'

# 请使用管理控制台首页的APPID或自己创建应用的APPID
_appId = '8aaf07086f0d2ca0016f0dfa879e01dd'

# 说明：请求地址，生产环境配置成app.cloopen.com
_serverIP = 'sandboxapp.cloopen.com'

# 说明：请求端口 ，生产环境为8883
_serverPort = '8883'

# 说明：REST API版本号保持不变
_softVersion = '2013-12-26'


class CCP(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(CCP, "_instance"):
            cls._instance = super(CCP, cls).__new__(cls, *args, **kwargs)
            cls._instance.rest = REST(_serverIP, _serverPort, _softVersion)
            cls._instance.rest.setAccount(_accountSid, _accountToken)
            cls._instance.rest.setAppId(_appId)
        return cls._instance

    def send_sms_code(self, to, datas, tempId):
        result = self.rest.sendTemplateSMS(to, datas, tempId)
        return result.get("statusCode") == "000000"
