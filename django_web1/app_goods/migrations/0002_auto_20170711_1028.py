# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='g_click',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='g_content',
            field=tinymce.models.HTMLField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe4\xbb\x8b\xe7\xbb\x8d'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='g_pic',
            field=models.ImageField(upload_to=b'goods', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='g_price',
            field=models.DecimalField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='g_stock',
            field=models.IntegerField(default=100, verbose_name=b'\xe5\xba\x93\xe5\xad\x98'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='g_subtitle',
            field=models.CharField(max_length=200, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x89\xaf\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='g_title',
            field=models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='g_type',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x88\x86\xe7\xb1\xbb', to='app_goods.GoodsType'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='g_unit',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name=b'\xe9\x80\xbb\xe8\xbe\x91\xe5\x88\xa0\xe9\x99\xa4'),
        ),
    ]
