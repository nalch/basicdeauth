from django.conf.urls import url

from views import (
    fetch,
)


urlpatterns = [
    url(r'^(?P<url>[a-z0-9-_]+)/$', fetch, name='fetch'),
]
