from django.db import models

from luffyapi.utils.models import BaseModel


# Create your models here.

class Banner(models.Model):
    """
    轮播图
    """
    # upload_to 存储子目录，真实存放地址会使用配置中的MADIE_ROOT+upload_to
    image = models.ImageField(upload_to='banner', verbose_name='轮播图', null=True, blank=True)
    name = models.CharField(max_length=150, verbose_name='轮播图名称')
    note = models.CharField(max_length=150, verbose_name='备注信息')
    link = models.CharField(max_length=150, verbose_name='轮播图广告地址')
    orders = models.IntegerField(verbose_name='显示顺序')
    is_show = models.BooleanField(verbose_name="是否上架", default=False)
    is_delete = models.BooleanField(verbose_name="逻辑删除", default=False)

    class Meta:
        db_table = 'ly_banner'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Nav(BaseModel):
    """
    导航栏；分为顶部和底部
    主要字段有 导航名称   导航路径  位置
    """
    Nav_Position = (
        (0, 'top'),
        (1, 'footer')
    )
    name = models.CharField(max_length=50, verbose_name='导航名称')
    link = models.CharField(max_length=250, verbose_name='导航地址')
    # 导航位置显示 顶部表示0，底部表示1
    opt = models.SmallIntegerField(choices=Nav_Position, default=0, verbose_name='导航位置')
    # 0表示不是站外链接，1表示站内链接
    is_http = models.BooleanField(default=0, verbose_name='是否是站外链接')

    class Meta:
        db_table = 'ly_nav'
        verbose_name = '导航'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.get_opt_display() + self.name
