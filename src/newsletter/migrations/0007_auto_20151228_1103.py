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
            field=models.EmailField(max_length=254, verbose_name='e-post'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(null=True, blank=True, max_length=120, verbose_name='Fullt navn'),
        ),
    ]
