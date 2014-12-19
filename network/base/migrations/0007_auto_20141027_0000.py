# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20141025_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='payload',
            field=models.FileField(null=True, upload_to=b'data_payloads'),
        ),
    ]
