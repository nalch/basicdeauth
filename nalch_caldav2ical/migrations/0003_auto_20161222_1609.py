# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_caldav2ical', '0002_auto_20161222_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarentry',
            name='name',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='calendarentry',
            name='password',
            field=models.CharField(max_length=1024, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='calendarentry',
            name='username',
            field=models.CharField(max_length=1024, null=True, blank=True),
            preserve_default=True,
        ),
    ]
