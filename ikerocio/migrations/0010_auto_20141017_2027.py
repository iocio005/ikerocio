# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0009_auto_20141017_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='web_title',
            field=models.CharField(default=b'Iker Ocio - Web Developer', max_length=30, verbose_name=b'Web Title'),
        ),
    ]
