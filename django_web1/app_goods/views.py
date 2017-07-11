# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from models import GoodsType, GoodsInfo
from django.core.paginator import Paginator
from haystack.generic_views import SearchView


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
        goods.g_click += 1  # 让点击量+1
        goods.save()

        t_all = GoodsType.objects.all()  # 查询所有的商品分类
        t_name = GoodsInfo.objects.filter(g_title=goods.g_title)  # 根据商品的标题查询所属商品分类'

        # t_name[0].g_type_id获得的是当前商品分类的id
        n_list = t_all[t_name[0].g_type_id - 1].goodsinfo_set.order_by('-id')[0:2]  # 查询所属商品分类下最新添加的2条数据, id倒序查询2条

        context = {
            'title': '商品详情', 'cart_show': '1',
            'goods': goods, 't_all': t_all, 't_name': t_name[0], 'n_list': n_list
        }
        response = render(request, 'app_goods/detail.html', context)

        # 保存最近商品浏览id [1,2,3,4,5]<==>'1,2,3,4,5'  ','.join()   .split()
        # 步骤：先读取已经存的-》进行拼接-》输出
        # 获取浏览器中存的之前浏览的商品id，没有就赋值默认值 ''，以，进行分隔每个id转换成列表([1,2,3,4,5])
        g_ids = request.COOKIES.get('goods_ids', '').split(',')
        # 判断当前浏览的商品id是否存在之前存的cookie中 ，如果存在 则删除，然后再加到最前面
        if g_id in g_ids:
            g_id.remove(g_id)
        g_ids.insert(0, g_id)

        # 如果超过5个，则删除最后一个
        # 最后有一个，会在后面转换的时候报错，所以判断6个，在获取的时候删除最后一个就是5个商品id
        if len(g_ids) > 6:
            g_ids.pop()

        # 将当前商品id存到cookie中，以，进行拼接成一个长字符串(1，2，3，4，5，)，过期时间7天后
        response.set_cookie('goods_ids', ','.join(g_ids), max_age=60 * 60 * 24 * 7)

        return response
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

    # try:
    # 根据分类id查询该商品分类对象
    t_list = GoodsType.objects.get(id=t_id)
    t_all = GoodsType.objects.all()  # 所有的商品分类

    # 根据分类对象查询该分类下的所有商品对象，在根据id倒序查询出2条数据
    n_list = t_list.goodsinfo_set.order_by('-id')[0:2]

    order_str = request.GET.get('order', '0')  # 获取浏览器传递来的排序参数
    desc = request.GET.get('desc', '1')  # 获取浏览器传递来的价格是升序，还是倒序的参数

    order_by = '-id'  # 按id倒序排序

    if order_str == '1':
        if desc == '1':
            order_by = '-g_price'  # 按价格倒序排序
        else:
            order_by = 'g_price'  # 按价格升序排序
    elif order_str == '2':
        order_by = '-g_click'  # 按点击量倒序排序

    # 根据分类对象查询该分类下的所有商品对象,在根据指定字段倒序产生数据
    goods_list = t_list.goodsinfo_set.order_by(order_by)

    # 获取分页对象，设置一页显示10条数据
    p = Paginator(goods_list, 15)
    p_index = int(p_index)  # 获取当前页码索引
    if p_index < 1:
        p_index = 1
    elif p_index > p.num_pages:  # 当前页码 > 大于列表总页数
        p_index = p.num_pages
    page = p.page(p_index)  # 获取分页后的当前页面对象

    if page.paginator.num_pages < 5:  # 当前总页码数 < 5
        range_list = page.paginator.page_range  # 直接将页码数赋值到变量中
    elif page.number <= 2:
        range_list = range(1, 6)
    elif page.number >= page.paginator.num_pages - 1:
        range_list = range(page.paginator.num_pages - 5 + 1, page.paginator.num_pages + 1)
    else:
        range_list = range(page.number - 2, page.number + 3)

    context = {
        'title': '商品列表', 'cart_show': '1',
        't_all': t_all, 't_list': t_list, 'n_list': n_list,
        'page': page, 'page_range': range_list,  # 当前页对象， 页码列表
        'order': order_str, 'desc': desc
    }

    return render(request, 'app_goods/list.html', context)

    # except Exception as e:
    #     print e
    #     return redirect('404.html')


class MySearchView(SearchView):
    """My custom search view."""

    def get_context_data(self, *args, **kwargs):
        """自定义向模板页传递数据"""

        # 重写父类中的方法，获取父类中原本获取的context中的数据
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # do something
        context['title'] = '搜索结果'
        context['cart_show'] = '1'  # 自定义的数据，传向模板

        t_all = GoodsType.objects.all()
        context['t_all'] = t_all

        page = context.get('page_obj')  # 获取haystack中的page对象

        if page.paginator.num_pages < 5:  # 当前总页码数 < 5
            range_list = page.paginator.page_range  # 直接将页码数赋值到变量中
        elif page.number <= 2:  # 当前页码数为 1，2时
            range_list = range(1, 6)
        elif page.number >= page.paginator.num_pages - 1:  # 当前页码数为最后2个数时
            range_list = range(page.paginator.num_pages - 5 + 1, page.paginator.num_pages + 1)
        else:
            range_list = range(page.number - 2, page.number + 3)
        context['page_range'] = range_list

        return context



