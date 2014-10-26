# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0019_contactmessage_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='picture',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
