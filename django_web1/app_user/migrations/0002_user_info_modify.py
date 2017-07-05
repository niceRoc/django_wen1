# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='u_address',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_addressee',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_phone',
            field=models.CharField(default=b'', max_length=11),
        ),
    ]
