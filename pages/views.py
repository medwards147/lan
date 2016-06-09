from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic

from .models import HomePage
from lanapp.models import Event, Prize, Sponsor, Game

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

class AboutView(generic.ListView):
    template_name = 'pages/about.html'
    context_object_name = 'prizes'
    queryset = Prize.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['sponsors'] = Sponsor.objects.all()
        context['games'] = Game.objects.all()
        # And so on for more models
        return context

def contact(request):
    context = {}
    return render(request, "pages/contact.html", context)

