# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0002_auto_20170711_1028'),
        ('app_user', '0002_user_info_modify'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='app_goods.GoodsInfo')),
                ('user', models.ForeignKey(to='app_user.UserInfo')),
            ],
        ),
    ]
