from django.db import models
# Create your models here.

#物资表
class Balance (models.Model):
    """
    """
    bname = models.CharField(max_length=20,verbose_name='物资名称')
    btext = models.CharField(max_length=50,verbose_name='物资描述')
    btime  = models.DateTimeField(auto_now_add=True,verbose_name='购买时间')
    buser = models.ForeignKey('User',verbose_name='购买人',related_name='balance')
    laboratory = models.ForeignKey('laboratory', related_name='Balance',default=1)
    def __str__(self):
        return self.bname

#实验室表
class laboratory(models.Model):
    """
    """
    lname = models.CharField(max_length=20,verbose_name='实验室名称')
    floor = models.IntegerField(verbose_name='楼层')
    room_num = models.CharField(max_length=20,verbose_name='房间号')
    user = models.ForeignKey('User',verbose_name='负责人')
    def __str__(self):
        return  self.lname

class User(models.Model):
    user_name = models.CharField(max_length=20,verbose_name='用户名',unique=True)
    passwd = models.CharField(max_length=20,verbose_name='密码')
    uname  = models.CharField(max_length=6,verbose_name='姓名',)
    phone = models.CharField(max_length=11,verbose_name='手机号',default=0)
    def __str__(self):
        return self.user_name

#用户和实验是一对多的关系
#用户表和物资表是一对多的关系
#实验室表和物资表是一对多的关系