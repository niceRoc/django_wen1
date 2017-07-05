# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


# 用户模块url配置


urlpatterns = [
    url(r'^login/$', views.login),  # 用户登录页面url
    url(r'^register/$', views.register),  # 用户注册页面
    url(r'^info/$', views.user_center_info),  # 用户中心--个人中心页面
    url(r'^order/$', views.user_center_order),  # 用户中心--全部订单页面
    url(r'^site/$', views.user_center_site),  # 用户中心--收货地址页面
]
