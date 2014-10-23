# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogconfiguration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogconfiguration',
            old_name='short_description',
            new_name='quote',
        ),
    ]
