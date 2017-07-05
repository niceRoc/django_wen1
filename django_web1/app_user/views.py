# -*- coding: utf-8 -*-

from django.shortcuts import render


# Create your views here.


def login(request):
    """用户登录页面"""

    return render(request, 'app_user/login.html')


def register(request):
    """用户注册页面"""

    return render(request, 'app_user/register.html')


def user_center_info(request):
    """用户中心 -- 个人信息页面"""

    return render(request, 'app_user/user_center_info.html')


def user_center_order(request):
    """用户中心 -- 全部订单页面"""

    return render(request, 'app_user/user_center_order.html')


def user_center_site(request):
    """用户中心 -- 收货地址页面"""

    return render(request, 'app_user/user_center_site.html')
