from django.conf.urls import patterns, url
from rango import views, about

# regex . matches any char, * 0-n previous RE, ^ start of expression $ end

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/.*$', about.index, name='index'),)
