# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0003_auto_20151221_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='year_to',
            field=models.DateField(null=True, blank=True),
        ),
    ]
