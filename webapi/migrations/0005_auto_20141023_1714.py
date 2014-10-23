# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0004_delete_tweet'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterapi',
            name='default_word_long',
            field=models.CharField(default=datetime.date(2014, 10, 23), help_text=b'*** en http://ikerocio.com/url-del-post', max_length=200, verbose_name=b'Default words for new tweet long'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='twitterapi',
            name='default_word',
            field=models.CharField(help_text=b'***: "Titulo del Post" en http://ikerocio.com', max_length=200, verbose_name=b'Default words for new tweet'),
        ),
    ]
