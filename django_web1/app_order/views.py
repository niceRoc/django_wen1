# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from app_order.models import OrderMain, OrderDetail
from app_cart.models import CartInfo
from datetime import datetime
from django.db import transaction

# Create your views here.


@transaction.atomic
def index(request):
    """提交订单"""

    try:
        sid = transaction.savepoint()  # 创建事务保存点
        is_valid = True  # 操作是否有效的判断
        u_id = request.session.get('u_id')  # 用户id
        o_freight = int(request.POST.get('freight'))  # 订单运费
        total = 0  # 统计订单总额

        # 1. 创建订单主表
        order_main = OrderMain()
        current_time = datetime.now().strftime('%Y%m%d%H%M%S')  # 当前时间
        order_main.order_id = '{0}{1}'.format(current_time, u_id)  # 赋值订单号
        order_main.user_id = u_id  # 订单所属用户
        order_main.save()

        # 3. 接收所有的购物车的请求
        cart_ids = request.POST.get('cart_ids').split(',')  # 获取到购物车所有id
        cart_list = CartInfo.objects.filter(pk__in=cart_ids)  # 获取到所有购物车对象
        # 4.循环每个购物车对象，创建该商品的订单详情表
        for cart in cart_list:
            # 4. 判断库存，如果商品数量 < 库存则创建数据，否则不做操作，回滚事务
            if cart.count <= cart.goods.g_stock:
                order_detail = OrderDetail()
                order_detail.order = order_main  # 订单号
                order_detail.goods = cart.goods  # 商品id
                order_detail.count = cart.count  # 商品数量
                order_detail.price = cart.goods.g_price  # 商品价格
                order_detail.save()

                # 5. 统计订单总金额
                total += order_detail.price * order_detail.count  # 商品小计
                order_main.total = total + o_freight  # 订单总金额：商品总价+订单运费
                order_main.save()

                # 6. 改变商品库存
                cart.goods.g_stock -= cart.count
                cart.goods.save()

                # 7. 删除该条购物车记录
                cart.delete()
            else:
                transaction.savepoint_rollback(sid)  # 回滚事务，放弃之前的任何数据操作
                is_valid = False
                break  # 接下来的商品无需循环创建数据提交订单

        # 操作有效,订单创建成功就转向我的订单，否则转向我的购物车
        if is_valid:
            transaction.savepoint_commit(sid)  # 提交事务
    except Exception as e:
        print e
        transaction.savepoint_rollback(sid)  # 回滚事务
        is_valid = False

    if is_valid:
        return redirect('/user/order/')
    else:
        return redirect('/cart/')

