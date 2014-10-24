# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='ground_station',
            field=models.ForeignKey(to='base.Station', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='observation',
            field=models.ForeignKey(to='base.Observation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='observation',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='observation',
            name='satellite',
            field=models.ForeignKey(to='base.Satellite', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='observation',
            name='transponder',
            field=models.ForeignKey(to='base.Transponder', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='satellite',
            name='tle',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='satellite',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='station',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transponder',
            name='alive',
            field=models.BooleanField(default=True),
        ),
    ]
