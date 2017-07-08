# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('g_title', models.CharField(max_length=50)),
                ('g_pic', models.ImageField(upload_to=b'goods')),
                ('g_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('g_click', models.IntegerField(default=0)),
                ('g_unit', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
                ('g_subtitle', models.CharField(max_length=200)),
                ('g_stock', models.IntegerField(default=100)),
                ('g_content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('g_title', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='g_type',
            field=models.ForeignKey(to='app_goods.GoodsType'),
        ),
    ]
