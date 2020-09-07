from django.shortcuts import render, get_object_or_404
from .models import Shortener
from django.http import HttpResponse


def shortener_redirect_view(request, shortcode):

    obj = get_object_or_404(Shortener, shortcode=shortcode)
    return HttpResponse(f"Hello {obj.url}")
