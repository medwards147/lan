from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Event


class IndexView(generic.ListView):
    template_name = 'lanapp/events.html'
    context_object_name = 'upcoming_event'

    def get_queryset(self):
        """
        return the event with the nearest start date
        """
        return Event.objects.all().order_by('-event_start_date')[:1]

class DetailView(generic.DetailView):
    model = Event
    template_name = 'lanapp/detail.html'
