# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0005_auto_20141023_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='EasyMail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.EmailField(max_length=75, verbose_name=b'Mail')),
                ('password', models.CharField(max_length=20, verbose_name=b'Password')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
