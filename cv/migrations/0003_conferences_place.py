# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_fonticon_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferences',
            name='place',
            field=models.CharField(default='asdsa', max_length=50, verbose_name=b'Conference place to be', blank=True),
            preserve_default=False,
        ),
    ]
