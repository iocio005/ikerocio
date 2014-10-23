# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0008_auto_20141017_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='web_title',
            field=tinymce.models.HTMLField(default=b'Iker Ocio - Web Developer', max_length=30, verbose_name=b'Web Title'),
        ),
        migrations.AlterField(
            model_name='webimages',
            name='background',
            field=models.FileField(default=b'', upload_to=b'/static//upload/images/', verbose_name=b'Background', blank=True),
        ),
        migrations.AlterField(
            model_name='webimages',
            name='color',
            field=models.CharField(help_text=b'Hex color', max_length=30, verbose_name=b'Color', blank=True),
        ),
    ]
