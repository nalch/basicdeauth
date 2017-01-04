# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEntry',
            fields=[
                ('caldav_url', models.URLField(serialize=False, primary_key=True)),
                ('name', models.TextField(default=b'', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
