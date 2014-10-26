# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0020_auto_20141025_1634'),
        ('cv', '0003_conferences_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=70, verbose_name=b'Title')),
                ('url', models.URLField(verbose_name=b'URL')),
                ('description', models.TextField(verbose_name=b'Description about project')),
                ('publish', models.BooleanField(default=False, verbose_name=b'Is Visible?')),
                ('slug', models.SlugField(verbose_name=b'slug')),
                ('picture', models.ForeignKey(to='ikerocio.WebImages')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
