from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sheeties.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^comics/', include('sheeties.comic.urls')),
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
