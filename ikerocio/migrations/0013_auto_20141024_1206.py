# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0012_auto_20141024_1159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webimages',
            options={'verbose_name': 'Picture', 'verbose_name_plural': 'Pictures'},
        ),
        migrations.AddField(
            model_name='fifthsection',
            name='background_color',
            field=models.CharField(default=b'#FFFFFF', help_text=b'HEX color', max_length=50, verbose_name=b'Background color'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='firstsection',
            name='background_color',
            field=models.CharField(default=b'#FFFFFF', help_text=b'HEX color', max_length=50, verbose_name=b'Background color'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fourthsection',
            name='background_color',
            field=models.CharField(default=b'#FFFFFF', help_text=b'HEX color', max_length=50, verbose_name=b'Background color'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='secondsection',
            name='background_color',
            field=models.CharField(default=b'#FFFFFF', help_text=b'HEX color', max_length=50, verbose_name=b'Background color'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thirdsection',
            name='background_color',
            field=models.CharField(default=b'#FFFFFF', help_text=b'HEX color', max_length=50, verbose_name=b'Background color'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='welcomepage',
            name='background_color',
            field=models.CharField(default=b'#FFFFFF', help_text=b'HEX color', max_length=50, verbose_name=b'Background color'),
            preserve_default=True,
        ),
    ]
