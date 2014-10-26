# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0015_auto_20141024_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(default=datetime.date(2014, 10, 24), verbose_name=b'URL'),
            preserve_default=False,
        ),
    ]
