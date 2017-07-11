# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),  # 首页
    url(r'^detail/(\d+)/$', views.detail),  # 商品详情页
    url(r'^list/(\d+)/(\d+)/$', views.g_list),  # 商品列表页

    url(r'^search/$', views.MySearchView.as_view(), name='search_view'),
]
