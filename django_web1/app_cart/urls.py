# -*- coding: utf-8 -*-

from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.index),  # 展示购物车
    url(r'^add/$', views.add),  # 加入购物车
    url(r'^count/$', views.count),  # 查询商品数量
]
