# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet', models.CharField(help_text=b'Tweet', max_length=140, verbose_name=b'Tweet')),
                ('send_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TwitterApi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consumer_key', models.CharField(help_text=b'Consumer Key (Api Key)', max_length=300, verbose_name=b'Consumer Key')),
                ('consumer_secret', models.CharField(help_text=b'Consumer Secret (Api Key)', max_length=300, verbose_name=b'Consumer Secret')),
                ('access_token', models.CharField(help_text=b'Access Token', max_length=300, verbose_name=b'Access Token')),
                ('access_token_secret', models.CharField(max_length=300, verbose_name=b'Access Token Secret')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
