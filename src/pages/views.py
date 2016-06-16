
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


    if Event.objects.all().count() == 0:  
        event = Event.objects.create_event()
    else:
        event = Event.objects.order_by('event_start_date')[0]
    
    context = {
            "homepage": homepage,
            "event" : event,
    }
    
    return render(request, "pages/index.html", context)