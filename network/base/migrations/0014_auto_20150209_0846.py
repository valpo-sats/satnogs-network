# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_remove_station_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='image',
            field=models.ImageField(upload_to=b'ground_stations', blank=True),
            preserve_default=True,
        ),
    ]
