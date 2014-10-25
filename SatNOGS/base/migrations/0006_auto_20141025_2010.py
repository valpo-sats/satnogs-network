# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_satellite_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='satellite',
            name='tle',
        ),
        migrations.AddField(
            model_name='satellite',
            name='tle0',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='satellite',
            name='tle1',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='satellite',
            name='tle2',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
