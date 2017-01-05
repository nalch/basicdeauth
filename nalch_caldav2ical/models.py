from django.db import models


class CalendarEntry(models.Model):
    name = models.CharField(max_length=255)
    caldav_url = models.URLField()

    username = models.CharField(blank=True, max_length=1024)
    password = models.CharField(blank=True, max_length=1024)

    # this ensures, that the user knows, he's publishing secure pages over an insecure channel
    publish = models.BooleanField(default=False, help_text='publish the caldav calendar for users without credentials?')

    def __unicode__(self):
        return self.name
