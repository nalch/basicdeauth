import caldav
import urllib2

from django.http import (
    HttpResponse,
)

from django.shortcuts import (
    get_object_or_404,
)

from nalch_caldav2ical.models import (
    CalendarEntry,
)


def caldav2ical(request, calendar):
    calentry = get_object_or_404(CalendarEntry, name=calendar)
    client = caldav.DAVClient(calentry.caldav_url, username=calentry.username, password=calentry.password)
    calendar = caldav.Calendar(client=client, url=calentry.caldav_url)
    # todo convert to ical
    return HttpResponse(calendar)


def fetchowncloud(request, calendar):
    """
    fetch the ical representation for this calendar from owncloud using Basic Auth and the export
    :param request: the HTTP Request
    :type request: HttpRequest
    :param calendar: The calendar shortname
    :type calendar: str
    :return: ical representation of this calendar
    :rtype: HttpResponse
    """
    calentry = get_object_or_404(CalendarEntry, name=calendar)
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # this creates a password manager
    passman.add_password(None, calentry.caldav_url, calentry.username, calentry.password)
    # because we have put None at the start it will always
    # use this username/password combination for  urls
    # for which `theurl` is a super-url

    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    # create the AuthHandler

    opener = urllib2.build_opener(authhandler)

    urllib2.install_opener(opener)
    # All calls to urllib2.urlopen will now use our handler
    # Make sure not to include the protocol in with the URL, or
    # HTTPPasswordMgrWithDefaultRealm will be very confused.
    # You must (of course) use it when fetching the page though.

    response = urllib2.urlopen(calentry.caldav_url + '?export')
    # authentication is now handled automatically for us

    return HttpResponse(response.read())
