from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import HomePage

def homepage(request):
    """
    Builds view for homepage.
    """
    try:
        homepage = HomePage.objects.get(current_homepage=True)
    except HomePage.DoesNotExist:
        homepage = HomePage.objects.create_homepage("Automatically Created Homepage")

    try:
        banner_image = homepage.banner_image
    except ValueError:
        banner_image = "No banner image"

    first_image = homepage.first_image
    second_image = homepage.second_image
    third_image = homepage.third_image

    context = {
            "homepage": homepage,
            "banner_image": banner_image,
            "first_image": first_image,
            "second_image": second_image,
            "third_image": third_image,

    }
    return render(request, "pages/index.html", context)

def about(request):
    context = {}
    return render(request, "pages/about.html", context)

