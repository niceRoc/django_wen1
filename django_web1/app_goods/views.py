# -*- coding: utf-8 -*-

from django.shortcuts import render
from models import GoodsType, GoodsInfo


# Create your views here.


def index(request):
    """网站首页显示加载数据"""

    goods_list = []  # 最后返回的数据列表 [{},{}]

    # 获取所有的商品类型
    t_list = GoodsType.objects.all()
    for t in t_list:
        # 构造最新添加的商品数据  按照id倒序查找最新4条数据
        n_list = t.goodsinfo_set.order_by('-id')[0:4]
        # 构建最火商品数据  按照用户点击最多商品次数倒序4条数据查找
        f_list = t.goodsinfo_set.order_by('-g_click')[0:4]

        goods_list.append({'t_list': t, 'n_list': n_list, 'f_list': f_list})

    context = {'title': '首页', 'goods_list': goods_list}
    return render(request, 'app_goods/index.html', context)


def detail(request, t_id):
    """商品详情页"""

    context = {'title': '商品详情'}
    return render(request, 'app_goods/detail.html', context)


def g_list(request):
    """商品列表页"""

    context = {'list': '商品列表'}
    return render(request, 'app_goods/list.html', context)

