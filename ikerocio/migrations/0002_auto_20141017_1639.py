# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='publish',
            field=models.DateTimeField(default=datetime.date(2014, 10, 17), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='webimages',
            name='background',
            field=models.FileField(default=b'', upload_to=b'static/upload/images/', verbose_name=b'Background', blank=True),
        ),
        migrations.AlterField(
            model_name='webimages',
            name='color',
            field=models.CharField(help_text=b'Hex color', max_length=7, verbose_name=b'Color', blank=True),
        ),
    ]
