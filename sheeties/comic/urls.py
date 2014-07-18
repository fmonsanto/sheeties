from django.conf.urls import patterns, url

from sheeties.comic import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<comic_id>\d+)/$', views.detail, name='detail'),
)
