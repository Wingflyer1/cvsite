# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0002_certificates_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='comment',
            field=models.CharField(default=b'', max_length=120, null=True, blank=True),
        ),
    ]
