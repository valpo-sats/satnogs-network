# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20150723_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='transmitter',
            name='mode',
        ),
        migrations.AddField(
            model_name='satellite',
            name='image',
            field=models.ImageField(upload_to=b'satellites', blank=True),
        ),
        migrations.AddField(
            model_name='satellite',
            name='names',
            field=models.TextField(blank=True),
        ),
    ]
