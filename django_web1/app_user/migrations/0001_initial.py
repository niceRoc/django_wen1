# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_name', models.CharField(max_length=20)),
                ('u_pwd', models.CharField(max_length=40)),
                ('u_mail', models.CharField(max_length=20)),
                ('u_addressee', models.CharField(max_length=20)),
                ('u_phone', models.CharField(max_length=20)),
                ('u_address', models.CharField(max_length=200)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
