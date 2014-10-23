# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikerocio', '0011_auto_20141018_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conferences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Conference name')),
                ('year', models.IntegerField(verbose_name=b'Year')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact', models.CharField(max_length=100, verbose_name=b'Contact Name')),
                ('description', models.CharField(max_length=200, verbose_name=b'Contact Description', blank=True)),
                ('icon', models.ForeignKey(to='ikerocio.Icon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_presentation', models.TextField(help_text=b'Presentation', verbose_name=b'Presentation')),
                ('about_me', models.TextField(help_text=b'About me', verbose_name=b'About me')),
                ('publish', models.BooleanField(default=False, verbose_name=b'Publish?')),
                ('conferences', models.ManyToManyField(to='cv.Conferences')),
                ('contact', models.ManyToManyField(to='cv.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EducationMilestone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('year', models.IntegerField(verbose_name=b'Year')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExperienceMilestone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('year', models.IntegerField(verbose_name=b'Year')),
                ('work_name', models.CharField(max_length=30, verbose_name=b'Work')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FontIcon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f_icon', models.CharField(help_text=b'Font Awesome Icon. Set content value', max_length=50, verbose_name=b'Font awesome')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hobbie', models.CharField(max_length=50, verbose_name=b'Hobbie')),
                ('font_icon', models.ManyToManyField(to='cv.FontIcon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=50, verbose_name=b'Language')),
                ('percent', models.FloatField(default=0.5, verbose_name=b'Language percent', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Skill Name')),
                ('percent', models.FloatField(help_text=b'Value between 0 and 1', verbose_name=b'Knowledge percent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cv',
            name='education',
            field=models.ManyToManyField(to='cv.EducationMilestone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cv',
            name='experience',
            field=models.ManyToManyField(to='cv.ExperienceMilestone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cv',
            name='hobbies',
            field=models.ManyToManyField(to='cv.Hobbies'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cv',
            name='language',
            field=models.ManyToManyField(to='cv.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cv',
            name='skill',
            field=models.ManyToManyField(to='cv.Skill'),
            preserve_default=True,
        ),
    ]
