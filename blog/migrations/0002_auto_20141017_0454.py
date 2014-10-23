# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag_name',
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=b'default', unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
