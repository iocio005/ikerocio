# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0002_auto_20141017_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 10, 17), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='configuration',
            name='publish',
            field=models.BooleanField(default=False, verbose_name=b'Publish?'),
        ),
    ]
