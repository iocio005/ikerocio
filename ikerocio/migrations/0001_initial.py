# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('web_title', models.CharField(default=b'Iker Ocio - Web Developer', max_length=30, verbose_name=b'Web Title')),
                ('welcome_title', models.CharField(default=b'Iker Ocio', max_length=30, verbose_name=b'Welcome Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'Name')),
                ('email', models.EmailField(max_length=30, verbose_name=b'Email')),
                ('body', models.TextField(max_length=30, verbose_name=b'Message')),
                ('has_read', models.BooleanField(default=False, verbose_name=b'Are has read?')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FifthSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Lorem Ipsum', max_length=150)),
                ('body', tinymce.models.HTMLField(default=b'Lorem Ipsum', max_length=500)),
                ('publish', models.BooleanField(default=False, verbose_name=b'Publish?')),
            ],
            options={
                'verbose_name': '6 Contact me',
                'verbose_name_plural': '6 Contact me',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FirstSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Lorem Ipsum', max_length=150)),
                ('body', tinymce.models.HTMLField(default=b'Lorem Ipsum', max_length=500)),
                ('publish', models.BooleanField(default=False, verbose_name=b'Publish?')),
            ],
            options={
                'verbose_name': '2 About Me',
                'verbose_name_plural': '2 About Me',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FourthSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Lorem Ipsum', max_length=150)),
                ('body', tinymce.models.HTMLField(default=b'Lorem Ipsum', max_length=500)),
                ('publish', models.BooleanField(default=False, verbose_name=b'Publish?')),
            ],
            options={
                'verbose_name': '5 Pictures',
                'verbose_name_plural': '5 Pictures',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.CharField(default=b'', max_length=20, verbose_name=b'Fa Icon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SecondSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Lorem Ipsum', max_length=150)),
                ('body', tinymce.models.HTMLField(default=b'Lorem Ipsum', max_length=500)),
                ('publish', models.BooleanField(default=False, verbose_name=b'Publish?')),
            ],
            options={
                'verbose_name': '3 CV',
                'verbose_name_plural': '3 CV',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ThirdSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Lorem Ipsum', max_length=150)),
                ('body', tinymce.models.HTMLField(default=b'Lorem Ipsum', max_length=500)),
                ('publish', models.BooleanField(default=False, verbose_name=b'Publish?')),
            ],
            options={
                'verbose_name': '4 Blog',
                'verbose_name_plural': '4 Blog',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name=b'Title')),
                ('background', models.FileField(default=b'', upload_to=b'static/upload/images/', verbose_name=b'Background')),
                ('color', models.CharField(help_text=b'Hex color', max_length=7, verbose_name=b'Color')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WelcomePage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Lorem Ipsum', max_length=150)),
                ('body', tinymce.models.HTMLField(default=b'Lorem Ipsum', max_length=500)),
                ('publish', models.BooleanField(default=False, verbose_name=b'Publish?')),
                ('background', models.ForeignKey(to='ikerocio.WebImages', blank=True)),
            ],
            options={
                'verbose_name': '1 Welcome Page',
                'verbose_name_plural': '1 Welcome Page',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='thirdsection',
            name='background',
            field=models.ForeignKey(to='ikerocio.WebImages', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='secondsection',
            name='background',
            field=models.ForeignKey(to='ikerocio.WebImages', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fourthsection',
            name='background',
            field=models.ForeignKey(to='ikerocio.WebImages', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='firstsection',
            name='background',
            field=models.ForeignKey(to='ikerocio.WebImages', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fifthsection',
            name='background',
            field=models.ForeignKey(to='ikerocio.WebImages', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configuration',
            name='favicon',
            field=models.ForeignKey(to='ikerocio.WebImages'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configuration',
            name='welcome_icon',
            field=models.ForeignKey(to='ikerocio.Icon'),
            preserve_default=True,
        ),
    ]
