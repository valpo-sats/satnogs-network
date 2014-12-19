# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20141016_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='satellite',
            name='tle',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
    ]
