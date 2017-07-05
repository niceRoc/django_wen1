# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import JsonResponse
from models import UserInfo
from hashlib import sha1


# Create your views here.


def register(request):
    """用户注册页面"""

    return render(request, 'app_user/register.html', {'title': '注册'})


def register_handle(request):
    """处理用户提交注册按钮后的操作"""

    # 接收post请求对象
    post = request.POST

    # 实例化一个用户信息对象，并将传递过来的数据保存到数据表中
    user = UserInfo()
    user.u_name = post.get('user_name')

    s1 = sha1()  # 获取sha1对象
    s1.update(post.get('user_pwd'))  # 进行sha1加密
    user.u_pwd = s1.hexdigest()  # 获得加密后的数据，保存到user对象中的u_pwd属性中

    user.u_mail = post.get('user_mail')
    user.save()

    return redirect('/user/login/')


def register_valid(request):
    """查询用户名是否存在，返回一个json数据结果告知客户端是否存在"""

    u_name = request.GET.get('u_name')
    re = UserInfo.objects.filter(u_name=u_name).count()
    print re
    return JsonResponse({'isValid': re})


def login(request):
    """用户登录页面"""

    return render(request, 'app_user/login.html', {'title': '登录'})


def center_info(request):
    """用户中心 -- 个人信息页面"""

    return render(request, 'app_user/user_center_info.html', {'title': '用户中心'})


def center_order(request):
    """用户中心 -- 全部订单页面"""

    return render(request, 'app_user/user_center_order.html', {'title': '用户中心'})


def center_site(request):
    """用户中心 -- 收货地址页面"""

    return render(request, 'app_user/user_center_site.html', {'title': '用户中心'})

