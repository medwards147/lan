from django.conf.urls import url

from . import views

# not needed namespace defined in project urls.py
#app_name = 'lanapp'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='events'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]

