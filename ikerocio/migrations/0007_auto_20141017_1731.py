# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0006_welcomepage_undertitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='fifthsection',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 10, 17), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firstsection',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 10, 17), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fourthsection',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 10, 17), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='secondsection',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 10, 17), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thirdsection',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 10, 17), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='welcomepage',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 10, 17), auto_now_add=True),
            preserve_default=False,
        ),
    ]
