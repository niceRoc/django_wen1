# -*- coding: utf-8 -*-

from django.shortcuts import redirect


def check_login(func):
    """
    校验用户是否登录
    :param func: 传递进来的视图
    :return: HttpResponse对象
    """
    def handle(request, *args, **kwargs):

        # 如果存在用户id,则正常登录返回视图，不存在则直接重定向到登录页去重新登陆
        # request.session.get('u_id')
        if request.session.has_key('u_id'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/user/login/')
    return handle
