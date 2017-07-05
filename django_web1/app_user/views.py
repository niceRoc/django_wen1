# -*- coding: utf-8 -*-

from django.shortcuts import render


# Create your views here.


def login(request):
    """用户登录页面"""

    return render(request, 'app_user/login.html')
