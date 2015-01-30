from django.conf.urls import patterns, include, url
from blog.views import archive

urlpatterns = patterns('',
    url(r'^$', 'index', name='index'),
    url(r'^archive/$', 'archive'),
    url(r'^archive/(?P<year>d{4})/(?P<month>d{2})/(?P<day>d{2})/$', 'archive', name='archive'),
)
