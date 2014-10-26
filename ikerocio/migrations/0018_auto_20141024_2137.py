# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0017_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(verbose_name=b'slug'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.TextField(max_length=70, verbose_name=b'Title'),
        ),
    ]
