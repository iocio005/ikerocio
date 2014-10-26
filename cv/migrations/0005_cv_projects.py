# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='projects',
            field=models.ManyToManyField(to='cv.Project'),
            preserve_default=True,
        ),
    ]
