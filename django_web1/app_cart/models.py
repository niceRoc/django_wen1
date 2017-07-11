# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.


class CartInfo(models.Model):
    """购物车数据模型类"""

    # 用户
    user = models.ForeignKey('app_user.UserInfo')

    # 商品
    goods = models.ForeignKey('app_goods.GoodsInfo')

    # 数量，用来记录买了多少商品
    count = models.IntegerField()
