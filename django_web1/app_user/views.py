# -*- coding: utf-8 -*-

from django.shortcuts import render


# Create your views here.


def login(request):
    """用户登录页面"""

    return render(request, 'app_user/login.html', {'title': '天天生鲜-登录'})


def register(request):
    """用户注册页面"""

    return render(request, 'app_user/register.html', {'title': '天天生鲜-注册'})


def user_center_info(request):
    """用户中心 -- 个人信息页面"""

    return render(request, 'app_user/user_center_info.html', {'title': '天天生鲜-用户中心'})


def user_center_order(request):
    """用户中心 -- 全部订单页面"""

    return render(request, 'app_user/user_center_order.html', {'title': '天天生鲜-用户中心'})


def user_center_site(request):
    """用户中心 -- 收货地址页面"""

    return render(request, 'app_user/user_center_site.html', {'title': '天天生鲜-用户中心'})

