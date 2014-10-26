# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0011_auto_20141018_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webimages',
            name='color',
        ),
        migrations.AddField(
            model_name='webimages',
            name='path',
            field=models.CharField(default=datetime.date(2014, 10, 24), max_length=200, verbose_name=b'Image URL', blank=True),
            preserve_default=False,
        ),
    ]
