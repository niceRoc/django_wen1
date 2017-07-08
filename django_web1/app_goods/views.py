# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from models import GoodsType, GoodsInfo
from django.core.paginator import Paginator
from django.http import JsonResponse


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

    context = {'title': '首页', 'goods_list': goods_list, 'cart_show': '1'}
    return render(request, 'app_goods/index.html', context)


def detail(request, g_id):
    """
    商品详情页
    :param request: HttpRequest对象
    :param g_id: 商品id
    :return: HttpResponse对象 模板页
    """
    try:
        goods = GoodsInfo.objects.get(id=g_id)  # 根据商品id查询该商品对象
        t_list = GoodsType.objects.all()  # 查询所有的商品分类
        t_name = GoodsInfo.objects.filter(g_title=goods.g_title)  # 根据商品的标题查询所属商品分类'

        # t_name[0].g_type_id获得的是当前商品分类的id
        n_list = t_list[t_name[0].g_type_id - 1].goodsinfo_set.order_by('-id')[0:2]  # 查询所属商品分类下最新添加的2条数据, id倒序查询2条

        context = {
            'title': '商品详情', 'cart_show': '1',
            'goods': goods, 't_list': t_list, 't_name': t_name[0], 'n_list': n_list
        }
        return render(request, 'app_goods/detail.html', context)
    except Exception as e:
        print e
        redirect('404.html')


def g_list(request, t_id, p_index):
    """
    商品列表页
    :param request: HttpRequest对象
    :param t_id: 商品分类id
    :param p_index: 当前页码索引
    :return: 模板页 HttpResponse对象
    """

    try:
        # 根据分类id查询该商品分类对象
        t_list = GoodsType.objects.get(id=t_id)
        t_all = GoodsType.objects.all()

        # 根据分类对象查询该分类下的所有商品对象，在根据id倒序查询出2条数据
        n_list = t_list.goodsinfo_set.order_by('-id')[0:2]

        # 根据分类对象查询该分类下的所有商品对象,在根据id倒序产生数据
        goods_list = t_list.goodsinfo_set.order_by('-id')

        # 获取分页对象，设置一页显示15条数据
        p = Paginator(goods_list, 5)
        p_index = int(p_index)  # 获取当前页码索引
        if p_index < 1:
            p_index = 1
        elif p_index > p.num_pages:  # 当前页码 > 大于列表总页数
            p_index = p.num_pages
        page = p.page(p_index)  # 获取分页后的当前页面对象

        context = {
            'title': '商品列表', 'cart_show': '1',
            't_all': t_all, 't_list': t_list, 'n_list': n_list,
            'g_list': goods_list, 'page': page
        }

        return render(request, 'app_goods/list.html', context)

    except Exception as e:
        print e
        return redirect('404.html')


def list_handel(request):
    """处理分页数据的操作"""


