# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0010_auto_20141017_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webimages',
            name='background',
            field=models.FileField(default=b'', upload_to=b'static/upload/images/', verbose_name=b'Background', blank=True),
        ),
    ]
