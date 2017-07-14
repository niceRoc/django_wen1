# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.


class UserInfo(models.Model):
    """创建用户信息模型类"""

    # 用户名
    u_name = models.CharField(max_length=20)

    # 密码
    u_pwd = models.CharField(max_length=40)

    # 邮箱
    u_mail = models.CharField(max_length=20)

    # 收件人
    u_addressee = models.CharField(max_length=10, default='')

    # 邮编
    # u_phone = models.CharField(max_length=10, default='')

    # 手机号
    u_phone = models.CharField(max_length=11, default='')

    # 地址
    u_address = models.CharField(max_length=100, default='')

    # 用户浏览的商品

    # 逻辑删除
    isDelete = models.BooleanField(default=False)

