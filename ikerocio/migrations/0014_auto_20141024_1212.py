# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0013_auto_20141024_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fifthsection',
            name='background',
            field=models.ForeignKey(blank=True, to='ikerocio.WebImages', null=True),
        ),
        migrations.AlterField(
            model_name='firstsection',
            name='background',
            field=models.ForeignKey(blank=True, to='ikerocio.WebImages', null=True),
        ),
        migrations.AlterField(
            model_name='fourthsection',
            name='background',
            field=models.ForeignKey(blank=True, to='ikerocio.WebImages', null=True),
        ),
        migrations.AlterField(
            model_name='secondsection',
            name='background',
            field=models.ForeignKey(blank=True, to='ikerocio.WebImages', null=True),
        ),
        migrations.AlterField(
            model_name='thirdsection',
            name='background',
            field=models.ForeignKey(blank=True, to='ikerocio.WebImages', null=True),
        ),
        migrations.AlterField(
            model_name='welcomepage',
            name='background',
            field=models.ForeignKey(blank=True, to='ikerocio.WebImages', null=True),
        ),
    ]
