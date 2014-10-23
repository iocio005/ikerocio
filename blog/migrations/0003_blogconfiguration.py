# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141017_0454'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Title of Blog', max_length=10, verbose_name=b'Title')),
                ('short_description', models.CharField(help_text=b'Short quote for Blog', max_length=100, verbose_name=b'Short Quote', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('publish', models.BooleanField(default=False, verbose_name=b'Publish?')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
