from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

def upload_location(instance, filename):
    """
    defines an upload location for images for the HomePage. 
    Will be served to /media/filename.extension
    """
    GameModel = instance.__class__
    qs = GameModel.objects.all()
    if not qs.exists(): 
        new_id = 0
    else:
        new_id = GameModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model HomePage. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object,
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)


@python_2_unicode_compatible
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.TextField()
    event_start_date = models.DateTimeField(_('Event Start'))
    event_end_date = models.DateTimeField(_('Event End'))
    venue = models.CharField(max_length=75) 
    logistics_information = models.TextField()
    street_address = models.CharField(max_length=75) 
    city = models.CharField(max_length=75, default="Rome") 
    state = models.CharField(max_length=75, default="New York") 
    zip_code = models.CharField(max_length=75, default="13440") 

    def __str__(self):
        return self.event_name
    
    def full_address(self):
        return "{}, {}, {} {}".format(self.street_address, self.city, self.state, self.zip_code)
    
    def event_coming_soon(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.event_start_date <= now

    @property   
    def event_completed(self):
        now = timezone.now()
        return now >= self.event_end_date

    event_coming_soon.boolean = True
    event_coming_soon.short_description = 'Start within a week?' 

    class Meta:
        ordering = ("-event_start_date", ) 

@python_2_unicode_compatible
class Game(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    genre = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    #gaming_system = models.CharField(max_length=100) # define this as a choice field?
    image = models.ImageField(upload_to=upload_location,
                        null=True,
                        blank=True,
                        help_text="Image field for game")

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_location,
                        null=True,
                        blank=True,
                        help_text="Image field for a sponsor")

    def __str__(self):
        return self.name

class Prize(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_location,
                        null= True,
                        blank=True,
                        help_text="Image field for a prize")

    def __str__(self):
        return self.name

"""
class Tournament(models.Model):
    title = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    time =
"""
