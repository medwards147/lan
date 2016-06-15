from django.conf.urls import url

import pages.views

urlpatterns = [
    url(r'^$', pages.views.homepage, name='index'),
]
