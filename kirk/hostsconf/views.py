from django.conf import settings
from django.http import HttpResponseRedirect


DEFAULT_REDIRECT_URL= getattr(settings,"DEFAULT_REDIRECT_URL", "http://www.carlolam.com")
def wildcard_redirect(request,path=None):
    new_url = DEFAULT_REDIRECT_URL
    if path is not None:
        new_url = DEFAULT_REDIRECT_URL + "/" + path
       # new_url = path
    return HttpResponseRedirect(new_url)
