from django.db import models


# Create your models here.

class User(models.Model):
    """
    用户表
    """
    user = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')
    roles = models.ManyToManyField('Role', related_name='user', verbose_name='角色')

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user


# 一级菜单
class Munu(models.Model):
    title = models.CharField(max_length=20, verbose_name='')


# 二级菜单
class Permission(models.Model):
    """
    权限表
    """
    url = models.CharField(max_length=100, verbose_name='链接地址')
    title = models.CharField(max_length=20, verbose_name='标题')
    munu = models.ForeignKey('Munu', blank=True)

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色表
    """
    name = models.CharField(max_length=20, verbose_name='角色')
    persisson = models.ManyToManyField('Permission', verbose_name='权限', related_name='role', blank=True)

    class Meta:
        verbose_name = '角色表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
