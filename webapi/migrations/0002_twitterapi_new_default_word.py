# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterapi',
            name='new_default_word',
            field=models.CharField(default=datetime.date(2014, 10, 19), max_length=140, verbose_name=b'Default words for new tweet'),
            preserve_default=False,
        ),
    ]
