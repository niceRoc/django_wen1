# -*- coding: utf-8 -*-

from django.shortcuts import render
from app_user.user_decorate import check_login


# Create your views here.


@check_login
def cart(request):
    """购物车"""

    return render(request, 'app_cart/cart.html', {'title': '购物车', 'is_cart': '1'})
