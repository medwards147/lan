from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #url(r'^', include('lanapp.urls', namespace='lanapp')),
    #url(r'^$', pages.views.homepage_view, name='homepage'),
    url(r'^$', include('pages.urls', namespace='pages')),
    url(r'^lan/', include('lanapp.urls', namespace='lanapp')),
    url(r'^adminbrah/', include(admin.site.urls)),
]

admin.site.site_header = "CNY LAN Administration"
