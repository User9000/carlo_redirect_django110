from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
# Create your views here.
from .models import KirrURL
#function based view

class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})

#class based view
class KirrCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):

        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)






'''


#function based handles by default GET/POST/DELETE/HEAD
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):

    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)

#function based handles by default GET/POST/DELETE/HEAD
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    #print(request.user)
    #print(request.user.is_authenticated())
    #print(args)
    #print(kwargs)
    #print(shortcode)
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    #obj_url = obj.url
    #try:
     #   obj = KirrURL.objects.get(shortcode=shortcode)
    #except:
     #   obj = KirrURL.objects.all().first()
    #obj_url = None
    #qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    #if qs.exists() and qs.count() == 1:
     #   obj = qs.first()
      #  obj_url = obj.url

    return HttpResponse('hello {sc}'.format(sc=obj.url))
'''