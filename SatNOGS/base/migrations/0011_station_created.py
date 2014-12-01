# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_station_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 1, 19, 31, 18, 716421, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
