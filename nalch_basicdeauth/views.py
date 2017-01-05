import urllib2

from django.http import (
    HttpResponse,
)

from django.shortcuts import (
    get_object_or_404,
)

from nalch_basicdeauth.models import (
    UrlEntry,
)


def fetch(request, url):
    """
    fetch the resource for this UrlEntry using Basic Auth and provide it
    :param request: the HTTP Request
    :type request: HttpRequest
    :param url: The urlentry's name
    :type url: str
    :return: response
    :rtype: HttpResponse
    """
    urlentry = get_object_or_404(UrlEntry, name=url)

    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # this creates a password manager
    passman.add_password(None, urlentry.url, urlentry.username, urlentry.password)
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

    response = urllib2.urlopen(urlentry.url)
    # authentication is now handled automatically for us

    return HttpResponse(response.read())
