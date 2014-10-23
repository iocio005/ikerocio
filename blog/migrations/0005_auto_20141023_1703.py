# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20141018_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='send_tweet',
            field=models.BooleanField(default=False, help_text=b'Do you want to send tweet about post?', verbose_name=b'Send Post Tweet'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'Title'),
        ),
    ]
