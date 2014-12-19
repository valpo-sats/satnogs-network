# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
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
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('payload', models.FileField(upload_to=b'data_payloads')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('norad_cat_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('image', models.ImageField(upload_to=b'ground_stations')),
                ('alt', models.PositiveIntegerField()),
                ('lat', models.FloatField(validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('lng', models.FloatField(validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
                ('featured', models.BooleanField(default=False)),
                ('featured_date', models.DateField(null=True, blank=True)),
                ('antenna', models.ManyToManyField(to='base.Antenna')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transponder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('alive', models.BooleanField(default=False)),
                ('uplink_low', models.PositiveIntegerField()),
                ('uplink_high', models.PositiveIntegerField()),
                ('downlink_low', models.PositiveIntegerField()),
                ('downlink_high', models.PositiveIntegerField()),
                ('mode', models.CharField(max_length=10, choices=[(b'FM', b'FM'), (b'AFSK', b'AFSK'), (b'APRS', b'APRS'), (b'SSTV', b'SSTV'), (b'CW', b'CW'), (b'FMN', b'FMN')])),
                ('invert', models.BooleanField(default=False)),
                ('baud', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('satellite', models.ForeignKey(related_name=b'transponder', to='base.Satellite', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
