from django.shortcuts import render, get_object_or_404
from .models import Shortener
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import SubmiUrlForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmiUrlForm()
        return render(request, "shortener/home.html", {"form": form})

    def post(self, request, *agrs, **kwargs):
        form = SubmiUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        return render(request, "shortener/home.html", {"form": form})


class ShortenerView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        print(shortcode)
        obj = get_object_or_404(Shortener, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
