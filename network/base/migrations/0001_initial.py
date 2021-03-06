# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shortuuidfield.fields
import django.db.models.deletion
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Antenna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('frequency', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('band', models.CharField(max_length=5, choices=[(b'HF', b'HF'), (b'VHF', b'VHF'), (b'UHF', b'UHF'), (b'L', b'L'), (b'S', b'S'), (b'C', b'C'), (b'X', b'X'), (b'KU', b'KU')])),
                ('antenna_type', models.CharField(max_length=15, choices=[(b'dipole', b'Dipole'), (b'yagi', b'Yagi'), (b'helical', b'Helical'), (b'parabolic', b'Parabolic')])),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('payload', models.FileField(null=True, upload_to=b'data_payloads', blank=True)),
            ],
            options={
                'ordering': ['-start', '-end'],
            },
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-start', '-end'],
            },
        ),
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('norad_cat_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=45)),
                ('names', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to=b'satellites', blank=True)),
                ('tle0', models.CharField(max_length=100, blank=True)),
                ('tle1', models.CharField(max_length=200, blank=True)),
                ('tle2', models.CharField(max_length=200, blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['norad_cat_id'],
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('image', models.ImageField(upload_to=b'ground_stations', blank=True)),
                ('alt', models.PositiveIntegerField(help_text=b'In meters above ground')),
                ('lat', models.FloatField(validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('lng', models.FloatField(validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
                ('qthlocator', models.CharField(max_length=255, blank=True)),
                ('location', models.CharField(max_length=255, blank=True)),
                ('featured_date', models.DateField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('last_seen', models.DateTimeField(null=True, blank=True)),
                ('antenna', models.ManyToManyField(help_text=b'If you want to add a new Antenna contact SatNOGS Team', to='base.Antenna', blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-active', '-last_seen'],
            },
        ),
        migrations.CreateModel(
            name='Transmitter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(db_index=True, max_length=22, editable=False, blank=True)),
                ('description', models.TextField()),
                ('alive', models.BooleanField(default=True)),
                ('uplink_low', models.PositiveIntegerField(null=True, blank=True)),
                ('uplink_high', models.PositiveIntegerField(null=True, blank=True)),
                ('downlink_low', models.PositiveIntegerField(null=True, blank=True)),
                ('downlink_high', models.PositiveIntegerField(null=True, blank=True)),
                ('invert', models.BooleanField(default=False)),
                ('baud', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('mode', models.ForeignKey(related_name='transmitters', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='base.Mode', null=True)),
                ('satellite', models.ForeignKey(related_name='transmitters', to='base.Satellite', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='observation',
            name='satellite',
            field=models.ForeignKey(to='base.Satellite'),
        ),
        migrations.AddField(
            model_name='observation',
            name='transmitter',
            field=models.ForeignKey(related_name='observations', to='base.Transmitter', null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='ground_station',
            field=models.ForeignKey(to='base.Station'),
        ),
        migrations.AddField(
            model_name='data',
            name='observation',
            field=models.ForeignKey(to='base.Observation'),
        ),
    ]
