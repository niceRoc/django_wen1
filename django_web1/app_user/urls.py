# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


# 用户模块url配置


urlpatterns = [
    url(r'^login/$', views.login),  # 用户登录页面url
]
