# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0003_auto_20141019_1911'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tweet',
        ),
    ]
