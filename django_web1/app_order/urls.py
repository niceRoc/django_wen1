# -*- coding: utf-8 -*-

from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.index),  # 提交订单
]
