# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0018_auto_20141024_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 10, 25), auto_now_add=True),
            preserve_default=False,
        ),
    ]
