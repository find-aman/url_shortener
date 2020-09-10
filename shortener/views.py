from django.shortcuts import render, get_object_or_404
from .models import Shortener
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import SubmiUrlForm
from django.contrib import messages


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmiUrlForm()
        context = {"form": form}
        return render(request, "shortener/home.html", context)

    def post(self, request, *agrs, **kwargs):
        form = SubmiUrlForm(request.POST)
        context = {"form": form}
        template = "shortener/home.html"

        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            shortcode = form.cleaned_data.get("shortcode")
            print(form.cleaned_data)
            obj, created = Shortener.objects.get_or_create(
                url=new_url, shortcode=shortcode
            )
            context = {"object": obj, "created": created}

            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already_exists.html"
        else:
            messages.success(request, f"Not a Valid URL ending")
        return render(request, template, context)


class ShortenerView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(Shortener, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
