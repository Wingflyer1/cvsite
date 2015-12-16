# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20151215_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
