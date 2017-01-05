# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('username', models.CharField(max_length=1024, default='', blank=True)),
                ('password', models.CharField(max_length=1024, default='', blank=True)),
                ('publish', models.BooleanField(default=False, help_text=b'publish the url for users without credentials?')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
