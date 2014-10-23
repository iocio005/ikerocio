# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fonticon',
            name='name',
            field=models.CharField(default=datetime.date(2014, 10, 19), help_text=b'Short description about', max_length=30, verbose_name=b'Icon Name'),
            preserve_default=False,
        ),
    ]
