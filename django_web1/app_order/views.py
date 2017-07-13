# -*- coding: utf-8 -*-

from django.shortcuts import render
from app_user.models import UserInfo
from app_cart.models import CartInfo


# Create your views here.


def index(request):
    """订单首页"""

    # 用户信息
    user = UserInfo.objects.get(pk=request.session.get('u_id'))
    # 购物车
    cart_ids = request.POST.getlist('cart_id')
    cart_list = CartInfo.objects.filter(id__in=cart_ids)
    print cart_list
    context = {'title': '提交订单', 'user': user, 'cart_list': cart_list}

    return render(request, 'app_order/place_order.html', context)
