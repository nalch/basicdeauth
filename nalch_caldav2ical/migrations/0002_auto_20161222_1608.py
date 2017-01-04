# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_caldav2ical', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarentry',
            name='password',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendarentry',
            name='publish',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendarentry',
            name='username',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
