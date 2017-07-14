# -*- coding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField


# Create your models here.


class GoodsType(models.Model):
    """构建商品分类的数据模型类"""

    # 商品分类标题
    g_title = models.CharField(max_length=20)

    # 逻辑删除
    isDelete = models.BooleanField(default=False)

    # def __str__(self):
    #     """如果python3可以直接使用str方法不指定utf-8"""
    #     return self.g_title.encode('utf-8')

    def __unicode__(self):
        """使用unicode可以不用指定utf-8的编码格式"""
        return self.g_title


class GoodsInfo(models.Model):
    """构建商品的数据模型类"""

    # 商品标题
    g_title = models.CharField(verbose_name='标题', max_length=50)

    # 商品图片路径
    g_pic = models.ImageField(verbose_name='商品图片', upload_to='goods')

    # 商品价格 最多5位数，小数2位，最大价格：999.99
    g_price = models.DecimalField(verbose_name='价格', max_digits=5, decimal_places=2)

    # 商品点击量
    g_click = models.IntegerField(verbose_name='点击量', default=0)

    # 商品单位
    g_unit = models.CharField(verbose_name='单位', max_length=20)

    # 逻辑删除
    isDelete = models.BooleanField(verbose_name='逻辑删除', default=False)

    # 商品详情页中的商品副标题
    g_subtitle = models.CharField(verbose_name='商品副标题', max_length=200)

    # 商品库存
    g_stock = models.IntegerField(verbose_name='库存', default=100)

    # 商品详情页中的详情信息，通过富文本编辑器添加数据
    g_content = HTMLField(verbose_name='商品介绍')

    # 商品分类，构建外键约束
    g_type = models.ForeignKey('GoodsType', verbose_name='商品分类')



