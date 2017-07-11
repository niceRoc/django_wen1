# -*- coding: utf-8 -*-

from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.cart),  # 购物车
]
