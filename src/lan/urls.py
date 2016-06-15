from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    #url(r'^', include('lanapp.urls', namespace='lanapp')),
    #url(r'^$', pages.views.homepage_view, name='homepage'),
    url(r'^', include('pages.urls', namespace='pages')),

    url(r'^front-edit/', include('front.urls')),

    url(r'^adminbrah/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "CNY LAN Administration"
