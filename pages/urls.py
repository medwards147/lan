from django.conf.urls import url

import pages.views

urlpatterns = [
    url(r'^$', pages.views.homepage, name='index'),
    url(r'^about/', pages.views.AboutView.as_view(), name='about'),
    url(r'^contact/', pages.views.contact, name='contact'),
]
