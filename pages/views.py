

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic

from .forms import ContactForm
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

def about(request):
    context = {}
    return render(request, "pages/about.html", context)

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "pages/contact.html", {'form': form})
