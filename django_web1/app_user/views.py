# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import JsonResponse
from models import UserInfo
from hashlib import sha1
import datetime
from django.views.decorators.csrf import csrf_exempt
from user_decorate import check_login
from app_goods.models import GoodsInfo


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
    return JsonResponse({'isValid': UserInfo.objects.filter(u_name=u_name).count()})


def login(request):
    """用户登录页面"""

    # 获取当前浏览器存储的用户名cookie值，没有就给一个默认值‘’
    u_name = request.COOKIES.get('u_name', '')
    return render(request, 'app_user/login.html', {'title': '登录', 'u_name': u_name})


def login_handle(request):
    """处理用户登录"""

    post = request.POST  # 拿到post请求对象
    u_name = post.get('u_name')  # 用户填写的用户名
    u_pwd = post.get('u_pwd')  # 用户填写的密码
    is_records = post.get('u_records')  # 判断用户是否需要记住用户名

    s1 = sha1()  # 获得sha1加密对象
    s1.update(u_pwd)  # 将用户填写的密码进行加密
    sha1_pwd = s1.hexdigest()  # 获得加密后的数据

    context = {'title': '登录', 'u_name': u_name, 'u_pwd': u_pwd}  # 构建上下文

    # 根据用户填写的用户名去数据表中查询数据
    user = UserInfo.objects.filter(u_name=u_name)
    if len(user) == 0:  # 用户名错误
        context['user_error'] = '1'
        return render(request, 'app_user/login.html', context)
    else:
        if user[0].u_pwd == sha1_pwd:  # 用户名，密码正确，重定向到用户中心
            # 将当前登录的用户的id记录到session中
            request.session['u_id'] = user[0].id
            request.session['u_name'] = u_name  # 将用户名存到session中

            path = request.session.get('url_path', '/')
            # print path
            response = redirect(path)

            if is_records == 'on':  # 需要记住用户名, 将该用户名存到cookie中，设置过期时间为当前登录时间的7天后
                response.set_cookie('u_name', u_name, expires=datetime.datetime.now() + datetime.timedelta(days=7))
            else:  # 不需要记住，就立即清空cookie值，max_age=-1，表示过去的1秒
                response.set_cookie('u_name', '', max_age=-1)
            return response
        else:
            context['pwd_error'] = '1'
            return render(request, 'app_user/login.html', context)


def logout(request):
    """退出登录"""

    # 删除所有的session会话
    request.session.flush()
    return redirect('/user/login/')


@check_login
def center_info(request):
    """用户中心 -- 个人信息页面"""

    user = UserInfo.objects.get(pk=request.session.get('u_id'))

    # 获取浏览器中的cookie值，没有就设置一个默认值 '', 获取后转换成一个列表[1,2,3,4,5,]
    g_ids = request.COOKIES.get('goods_ids', '').split(',')
    g_ids.pop()  # 删除最后一个，因为之前没有商品时会默认有一个，

    g_list = []  # 存储商品的列表
    # 按照顺序一个个按照保存的id查询所对应的商品对象
    for g_id in g_ids:
        g_list.append(GoodsInfo.objects.get(pk=g_id))

    context = {'title': '用户中心', 'user': user, 'g_list': g_list}
    return render(request, 'app_user/user_center_info.html', context)


@check_login
def center_order(request):
    """用户中心 -- 全部订单页面"""

    return render(request, 'app_user/user_center_order.html', {'title': '用户中心'})


@check_login
def center_site(request):
    """用户中心 -- 收货地址页面"""

    user = UserInfo.objects.get(id=request.session['u_id'])
    return render(request, 'app_user/user_center_site.html', {'title': '用户中心', 'user': user})


@csrf_exempt
def site_handle(request):
    """
    添加用户填写的收货地址
    :param request: HttpRequest对象
    :return: json数据  MIME格式：application/json
    """

    post = request.POST  # 获取post请求对象
    user = UserInfo.objects.get(id=request.session['u_id'])  # 获取当前登录的用户
    user.u_addressee = post.get('u_addressee', '')  # 收件人
    user.u_address = post.get('u_address', '')  # 地址
    user.u_phone = post.get('u_phone', '')  # 手机
    user.save()

    return JsonResponse({'user': [user.u_address, user.u_addressee, user.u_phone]})


def is_login(request):
    """判断用户是否登录"""

    result = 0
    # session中是否保存了id
    if request.session.has_key('u_id'):
        result = 1
    return JsonResponse({'is_login': result})


