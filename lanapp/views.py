from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Event, Game, Prize, Sponsor


class IndexView(generic.ListView):
    template_name = 'lanapp/events.html'
    context_object_name = 'events'
    queryset = Event.objects.all().order_by('event_start_date')

class DetailView(generic.DetailView):
    model = Event
    template_name = 'lanapp/detail.html'
