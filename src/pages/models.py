from __future__ import unicode_literals

from django.db import models
from django.db import transaction
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class HomePageManager(models.Manager):
    def create_homepage(self, title):
        homepage = self.create(homepage_name=title, current_homepage=True)
        return homepage

def upload_location(instance, filename):
    """
    defines an upload location for images for the HomePage. 
    Will be served to /media/filename.extension
    """
    HomePageModel = instance.__class__
    qs = HomePageModel.objects.all()
    if not qs.exists():
        new_id = 0
    else:
        new_id = HomePageModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model HomePage. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object,
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)

class TimeStampedModel(models.Model):
    """
    Abstract model for created and updated fields. Most models have a created and updated field to
    track objects over time
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class HomePage(models.Model):
    """
    Main HomePage object. It's useful to build in the HomePage in the back end. Although it does contrict the
    front end designer to specific fields. This would be more useful if requirements for homepage were defined nicely.
    Therefore, you may have to edit html directly. Although, this isn't ideal.
    """
    current_homepage = models.BooleanField(
        help_text="Click here if you want this page to be the current home page",)
    homepage_name = models.CharField(max_length=35)

    banner_image = models.ImageField(upload_to=upload_location,
                    null=True,
                    blank=True,
                    help_text="Banner Image")
    first_image = models.ImageField(upload_to=upload_location,
                null=True,
                blank=True,
                help_text="First Content Heading Image")
    second_image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            help_text="Second Content Heading Image")
    third_image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            help_text="Third Content Heading Image")

    objects = HomePageManager()
    
    class Meta:
        verbose_name = _("Homepage")
        verbose_name_plural = _("Homepages")

    @transaction.atomic
    def save(self, *args, **kwargs):
        """
        Checks to see if any other HomePage objects current_homepage
        is set to True. If one is, it will change the current object to True
        and the other object to False.

        transaction.atomic decorator protects the atomicity of the database
        see django docs for more detail
        """
        if self.current_homepage:
            HomePage.objects.filter(
                current_homepage=True).update(current_homepage=False)
        super(HomePage, self).save(*args, **kwargs)

    def __str__(self):
        return self.homepage_name