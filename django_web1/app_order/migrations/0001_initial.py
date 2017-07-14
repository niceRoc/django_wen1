# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0002_user_info_modify'),
        ('app_goods', '0002_auto_20170711_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(verbose_name='\u5546\u54c1\u6570\u91cf')),
                ('price', models.DecimalField(verbose_name='\u5546\u54c1\u5355\u4ef7', max_digits=5, decimal_places=2)),
                ('goods', models.ForeignKey(verbose_name='\u5546\u54c1', to='app_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMain',
            fields=[
                ('order_id', models.CharField(max_length=20, serialize=False, verbose_name='\u8ba2\u5355\u53f7', primary_key=True)),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='\u8ba2\u5355\u65e5\u671f')),
                ('total', models.DecimalField(verbose_name='\u5546\u54c1\u603b\u4ef7', max_digits=8, decimal_places=2)),
                ('state', models.IntegerField(default=0, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to='app_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(verbose_name='\u8ba2\u5355\u53f7', to='app_order.OrderMain'),
        ),
    ]
