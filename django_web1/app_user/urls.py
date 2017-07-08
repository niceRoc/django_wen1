# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


# 用户模块url配置


urlpatterns = [
    url(r'^register/$', views.register),  # 用户注册页面
    url(r'^register_handle/$', views.register_handle),  # 处理用户注册
    url(r'^register_valid/$', views.register_valid),  # 处理用户名是否存在


    url(r'^login/$', views.login),  # 用户登录页面url
    url(r'^login_handle/$', views.login_handle),  # 处理用户登录
    url(r'^logout/$', views.logout),  # 用户退出

    url(r'^$', views.center_info),  # 用户中心--个人中心页面
    url(r'^order/$', views.center_order),  # 用户中心--全部订单页面
    url(r'^site/$', views.center_site),  # 用户中心--收货地址页面
    url(r'^site_handle/$', views.site_handle),  # 用户中心-新增地址
]
