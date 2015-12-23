# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='comment',
            field=models.CharField(default=b'', max_length=120, null=True, blank=True),
        ),
    ]
