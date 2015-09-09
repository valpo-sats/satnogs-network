# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20151011_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, choices=[(b'Radio', b'Radio'), (b'SDR', b'SDR')])),
                ('rictld_number', models.PositiveIntegerField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='uuid',
            field=models.CharField(db_index=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='station',
            name='rig',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='base.Rig', null=True),
        ),
    ]
