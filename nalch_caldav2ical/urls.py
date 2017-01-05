from django.conf.urls import url

from views import (
    caldav2ical,
    fetchowncloud,
)


urlpatterns = [
    url(r'^fetch/(?P<calendar>[a-z0-9-_]+)/$', fetchowncloud, name='fetchowncloud'),
    url(r'^(?P<calendar>[a-z0-9-_]+)/$', caldav2ical, name='caldav2ical'),
]
