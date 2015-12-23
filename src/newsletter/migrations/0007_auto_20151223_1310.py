# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_auto_20151223_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(verbose_name='e-post', max_length=254),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(verbose_name='Fullt navn', null=True, max_length=120, blank=True),
        ),
    ]
