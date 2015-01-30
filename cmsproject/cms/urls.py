#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from cms.models import Story
from cms.views import StoryDetailView, StoryListView

urlpatterns = patterns('cms.views',
    url(r'^category/(?P<slug>[-\w]+)/$', 'category', name = 'cms-category'),
    url(r'^search/', 'search', name = 'cms-search'), #放在DetialView前，防止先匹配执行DetailView
)

urlpatterns += patterns('',
    url(r'^$', StoryListView.as_view(), name = 'cms-home'),
    url(r'^(?P<slug>[-\w]+)/$', StoryDetailView.as_view(), name = 'cms-story'),
)

