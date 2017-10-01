from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
# Create your views here.
from analytics.models import ClickEvent
from .models import KirrURL
from .forms import SubmitUrlForm



class HomeView(View):
    #GET Function
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Carlo Lam",
            "form": the_form
        }

        return render(request, "shortener/home.html", context)
    #POST Function
    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Carlo Lam",
            "form": form,
        
        }
        if form.is_valid():
            print(form.cleaned_data)
            new_url = form.cleaned_data.get("url")
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return render(request,template, context)

#class based view
class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = KirrURL.objects.filter(shortcode__iexact = shortcode)
        if qs.count()!=1 and not qs.exists():
            raise Http404
        obj = qs.first()     
        print(ClickEvent.objects.create_event(obj))
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