# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_satellite_tle'),
    ]

    operations = [
        migrations.AddField(
            model_name='satellite',
            name='updated',
            field=models.DateTimeField(default=datetime.date(2014, 10, 24), auto_now_add=True),
            preserve_default=False,
        ),
    ]
