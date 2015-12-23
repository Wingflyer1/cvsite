# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0003_auto_20151222_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='comment',
            field=models.CharField(max_length=120, null=True, default='', blank=True),
        ),
    ]
