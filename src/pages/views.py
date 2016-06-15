
from django.shortcuts import render

from .models import HomePage
from lanapp.models import Event

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

    if Event.objects.all().count == 0:  
        event = Event.objects.order_by('event_start_date')[0]
    else:
        event = Event.objects.create_event()
    
    context = {
            "homepage": homepage,
            "banner_image": banner_image,
            "first_image": first_image,
            "second_image": second_image,
            "third_image": third_image,
            "event" : event,

    }
    return render(request, "pages/index.html", context)