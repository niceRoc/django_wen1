# -*- coding: utf-8 -*-
from django.db.models import Sum
from django.shortcuts import render
from app_user.user_decorate import check_login
from django.http import JsonResponse
from models import CartInfo

# Create your views here.


@check_login
def index(request):
    """展示购物车"""

    u_id = int(request.session.get('u_id'))
    carts = CartInfo.objects.filter(user_id=u_id)
    return render(request, 'app_cart/cart.html', {'title': '购物车', 'carts': carts})


def add(request):
    """加入购物车"""

    try:
        u_id = int(request.session.get('u_id'))  # 用户id
        g_id = int(request.GET.get('g_id'))  # 商品id
        g_num = int(request.GET.get('g_num', '1'))  # 商品数量，没有设置默认值 1

        # 查询是否有购物记录
        carts = CartInfo.objects.filter(user_id=u_id, goods_id=g_id)

        if len(carts) == 1:  # 当前油壶有购买过该商品的记录
            cart_info = carts[0]  # 得到返回的购物车对象
            cart_info.count += g_num  # 数量相加
            cart_info.save()
        else:
            cart_info = CartInfo()  # 购物车对象
            # 当前用户id,因为user在模型类中需要给定用户对象，直接的用户id可以用数据表中user_id字段来存储
            cart_info.user_id = u_id
            cart_info.goods_id = g_id  # 商品id
            cart_info.count = g_num  # 商品数量
            cart_info.save()

        return JsonResponse({'is_add': '1'})
    except Exception as e:
        print e
        return JsonResponse({'is_add': '0'})


def count(request):
    """查询商品数量"""

    try:
        u_id = request.session.get('u_id')  # 获取当前用户id

        # 查询该用户买了多少类商品
        # g_num = CartInfo.objects.filter(user_id=u_id).count()

        # 查询该用户总共买了多少商品
        # 使用aggregate聚合函数查询的结果集，返回的是一个字典{'键':值}，键名为：查询的字段名 + '__' + 具体使用的聚合函数名 --> 如：count_sum
        g_num = CartInfo.objects.filter(user_id=u_id).aggregate(Sum('count')).get('count__sum')
        return JsonResponse({'count': g_num})
    except Exception as e:
        print e
        return JsonResponse({'count': '0'})


def handle(request):
    """处理购物车页面"""

    try:
        u_id = int(request.session.get('u_id'))  # 用户id
        g_id = int(request.GET.get('g_id'))  # 商品id
        g_num = int(request.GET.get('g_num'))  # 商品数量，没有设置默认值 1

        # 查询是否有购物记录
        carts = CartInfo.objects.filter(user_id=u_id, goods_id=g_id)

        if len(carts) == 1:
            cart_info = carts[0]
            cart_info.count = g_num  # 将用户传递过来的商品数量赋值给数据表中进行update
            cart_info.save()

        # 查询该用户想购买的所有商品
        cart_all = CartInfo.objects.filter(user_id=u_id)

        num_list = []  # 商品数量
        price_list = []  # 商品单价

        # 循环所有的购物车对象，将商品数量以及商品单价添加到列表中
        for cart in cart_all:
            num_list.append(cart.count)
            price_list.append(cart.goods.g_price)

        # 让两个列表的元素逐一相乘，构建一个新的列表
        total_list = map(lambda (a, b):a * b, zip(num_list,price_list))
        # print total_list
        total = 0  # 初始化购物车中的商品总价
        for i in total_list:
            total += i
        # print total

        return JsonResponse({'result': '1', 'total': total})
    except Exception as e:
        print e
        return JsonResponse({'result': '0'})


def delete(request):
    """删除购物车"""
    # try:
    cart_id = request.GET.get('cart_id')
    cart = CartInfo.objects.filter(id=cart_id)
    print cart[0].id
    cart.delete()
    return JsonResponse({'is_delete': '1'})
