# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0005_auto_20141017_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='welcomepage',
            name='undertitle',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'Under Title'),
            preserve_default=True,
        ),
    ]
