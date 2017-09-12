from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

#function based view

def kirr_redirect_view(request, *args, **kwargs):
    return HttpResponse('hello')

#class based view
class KirrCBView(View):
    def get(self, request, *args, **kwars):
        return HttpResponse("Hello Again")