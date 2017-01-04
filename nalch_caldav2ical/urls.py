from django.conf.urls import url

from views import (
    caldav2ical,
)


urlpatterns = [
    url(r'^(?P<calendar>[a-z]+)/$', caldav2ical, name='caldav2ical'),
]
