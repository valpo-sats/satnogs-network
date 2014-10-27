# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20141027_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='payload',
            field=models.FileField(null=True, upload_to=b'data_payloads', blank=True),
            preserve_default=True,
        ),
    ]
