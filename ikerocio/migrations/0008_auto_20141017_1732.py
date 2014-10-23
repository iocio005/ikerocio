# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0007_auto_20141017_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fifthsection',
            name='title',
        ),
        migrations.RemoveField(
            model_name='firstsection',
            name='title',
        ),
        migrations.RemoveField(
            model_name='fourthsection',
            name='title',
        ),
        migrations.RemoveField(
            model_name='secondsection',
            name='title',
        ),
        migrations.RemoveField(
            model_name='thirdsection',
            name='title',
        ),
        migrations.RemoveField(
            model_name='welcomepage',
            name='title',
        ),
    ]
