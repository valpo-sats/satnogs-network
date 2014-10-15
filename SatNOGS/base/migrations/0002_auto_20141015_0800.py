# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='observation',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='observation',
            name='satellite',
            field=models.ForeignKey(to='base.Satellite'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='observation',
            name='transponder',
            field=models.ForeignKey(to='base.Transponder', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='ground_station',
            field=models.ForeignKey(to='base.Station'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='observation',
            field=models.ForeignKey(to='base.Observation'),
            preserve_default=True,
        ),
    ]
