from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


def get_default_my_date():
  return timezone.now() + datetime.timedelta(days=30)

class EventManager(models.Manager):
    def create_event(self):
        event = self.create(event_start_date=get_default_my_date(), 
                                  event_end_date=get_default_my_date())
        return event


@python_2_unicode_compatible
class Event(models.Model):
    event_name = models.CharField(max_length=100, default="CNY LAN")

    event_start_date = models.DateTimeField(_('Event Start'))
    event_end_date = models.DateTimeField(_('Event End'))
    pay_button_text = models.CharField(max_length=100, default='Pay here with Paypal')
    venue = models.CharField(max_length=75, null=True, blank=True)
    price = models.IntegerField(default=35, null=True, blank=True)
    street_address = models.CharField(max_length=75, null=True, blank=True) 
    city = models.CharField(max_length=75, default="Rome") 
    state = models.CharField(max_length=75, default="New York") 
    zip_code = models.CharField(max_length=75, default="13440")

    def __str__(self):
        return self.event_name
        
    @property
    def full_address(self):
        return "{}, {}, {} {}".format(self.street_address, self.city, self.state, self.zip_code)

    def event_coming_soon(self):
        now = timezone.now()
        if now < self.event_start_date:
            return now + datetime.timedelta(days=30) >= self.event_start_date
        return False

    @property   
    def event_completed(self):
        now = timezone.now()
        return now >= self.event_end_date

    event_coming_soon.boolean = True
    event_coming_soon.short_description = 'Start within a week?' 

    class Meta:
        ordering = ("-event_start_date", )

    objects = EventManager()