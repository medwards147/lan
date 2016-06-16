
from django.shortcuts import render

from .models import HomePage
from lanapp.models import Event

def get_image_check(img_obj):
    if img_obj:
        return img_obj
    else:
        return "You need to add an image in the admin"

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

    first_image = get_image_check(homepage.first_image)
    second_image = get_image_check(homepage.second_image)
    third_image = get_image_check(homepage.third_image)

    if Event.objects.all().count() == 0:  
        event = Event.objects.create_event()
    else:
        event = Event.objects.order_by('event_start_date')[0]
    
    context = {
            "homepage": homepage,
            "banner_image": banner_image,
            "first_image": first_image,
            "second_image": second_image,
            "third_image": third_image,
            "event" : event,
    }
    
    return render(request, "pages/index.html", context)