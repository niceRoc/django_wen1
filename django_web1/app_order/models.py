# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class OrderMain(models.Model):
    """创建订单主表模型类"""

    order_id = models.CharField(verbose_name=u'订单号', max_length=20, primary_key=True)  # 格式: 201707140000+u_id

    order_date = models.DateTimeField(verbose_name=u'订单日期', auto_now_add=True)  # 以订单创建时的日期做保存

    user = models.ForeignKey('app_user.UserInfo', verbose_name=u'用户')

    total = models.DecimalField(verbose_name=u'商品总价', max_digits=8, decimal_places=2, default=0)  # 共8位数，其中2位小数

    state = models.IntegerField(verbose_name=u'订单状态', default=0)  # 默认值0表示为支付状态


class OrderDetail(models.Model):
    """创建订单详情表模型类"""

    order = models.ForeignKey(OrderMain, verbose_name=u'订单号')
    goods = models.ForeignKey('app_goods.GoodsInfo', verbose_name=u'商品')
    count = models.IntegerField(verbose_name=u'商品数量')
    price = models.DecimalField(verbose_name=u'商品单价', max_digits=5, decimal_places=2)  # 共5位数，小数2位

