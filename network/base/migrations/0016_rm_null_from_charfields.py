# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_station_qthlocator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satellite',
            name='tle0',
            field=models.CharField(default='', max_length=100, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='satellite',
            name='tle1',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='satellite',
            name='tle2',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='station',
            name='antenna',
            field=models.ManyToManyField(help_text=b'If you want to add a new Antenna contact SatNOGS Team', to='base.Antenna', blank=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='location',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='station',
            name='qthlocator',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=False,
        ),
    ]
