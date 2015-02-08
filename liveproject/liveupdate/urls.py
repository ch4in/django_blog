from django.conf.urls import patterns, include, url
from liveupdate.views import UpdateListView

urlpatterns = patterns('',
    url(r'^$', UpdateListView.as_view()),
    url(r'^update-after/(?P<id>\d+)/$', 'liveupdate.views.update_after')
)
