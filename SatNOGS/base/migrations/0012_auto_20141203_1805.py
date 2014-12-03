# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_station_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='online',
            field=models.BooleanField(default=False, help_text=b'Is your Ground Station functional?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='station',
            name='alt',
            field=models.PositiveIntegerField(help_text=b'In meters above ground'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='station',
            name='antenna',
            field=models.ManyToManyField(help_text=b'If you want to add a new Antenna contact SatNOGS Team', to='base.Antenna', null=True, blank=True),
            preserve_default=True,
        ),
    ]
