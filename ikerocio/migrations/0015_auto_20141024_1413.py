# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0014_auto_20141024_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70, verbose_name=b'Title')),
                ('description', models.TextField(verbose_name=b'Description about project')),
                ('publish', models.BooleanField(default=False, verbose_name=b'Is Visible?')),
                ('picture', models.ForeignKey(to='ikerocio.WebImages')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='fifthsection',
            name='body',
            field=tinymce.models.HTMLField(default=b'Lorem Ipsum', max_length=1000),
        ),
        migrations.AlterField(
            model_name='firstsection',
            name='body',
            field=tinymce.models.HTMLField(default=b'Lorem Ipsum', max_length=1000),
        ),
        migrations.AlterField(
            model_name='fourthsection',
            name='body',
            field=tinymce.models.HTMLField(default=b'Lorem Ipsum', max_length=1000),
        ),
        migrations.AlterField(
            model_name='secondsection',
            name='body',
            field=tinymce.models.HTMLField(default=b'Lorem Ipsum', max_length=1000),
        ),
        migrations.AlterField(
            model_name='thirdsection',
            name='body',
            field=tinymce.models.HTMLField(default=b'Lorem Ipsum', max_length=1000),
        ),
        migrations.AlterField(
            model_name='welcomepage',
            name='body',
            field=tinymce.models.HTMLField(default=b'Lorem Ipsum', max_length=1000),
        ),
    ]
