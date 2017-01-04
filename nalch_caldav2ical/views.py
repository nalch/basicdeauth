import caldav

from django.http import (
    HttpResponse,
    Http404,
)

from django.shortcuts import (
    get_object_or_404,
    render_to_response
)

from nalch_caldav2ical.models import (
    CalendarEntry,
)


def caldav2ical(request, calendar):
    calentry = CalendarEntry.objects.get(name=calendar)
    try:
        client = caldav.DAVClient(calentry.caldav_url, username=calentry.username, password=calentry.password)
        calendar = caldav.Calendar(client=client, url=calentry.caldav_url)
    except NotFoundError:
        Http404('Calendar not found')
    return HttpResponse(calendar.events())
