# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0004_auto_20141017_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='welcome_title',
            field=models.CharField(default=b'Iker Ocio', max_length=40, verbose_name=b'Welcome Name'),
        ),
    ]
