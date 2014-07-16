from django.conf.urls import patterns, url

from sheeties.comic import views

urlpatterns = patterns('',
    url(r'^$', views.homepage, name='home')
)
