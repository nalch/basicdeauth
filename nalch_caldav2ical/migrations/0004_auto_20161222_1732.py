# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_caldav2ical', '0003_auto_20161222_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarentry',
            name='caldav_url',
            field=models.URLField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='calendarentry',
            name='name',
            field=models.CharField(default='', max_length=255, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calendarentry',
            name='publish',
            field=models.BooleanField(default=False, help_text=b'publish the caldav calendar for users without credentials?'),
            preserve_default=True,
        ),
    ]
