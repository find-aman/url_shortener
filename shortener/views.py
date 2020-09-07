from django.shortcuts import render, get_object_or_404
from .models import Shortener
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})

    def post(self, request, *agrs, **kwargs):
        print(request.POST["url"])
        context = request.POST["url"]
        return render(request, "shortener/home.html", {"context": context})


class ShortenerView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        print(shortcode)
        obj = get_object_or_404(Shortener, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
