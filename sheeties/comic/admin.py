__author__ = 'francisco'

from django.contrib import admin
from sheeties.comic.models import Comic

class ComicAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'date_added', )
    #list_filter = ('title',)
    search_fields = ['title']

    '''
    def en_cv_url(self, obj):
        try:
            return u'<a href="%s">File</a>' % (obj.en_cv.file.url)
        except:
            return None
    en_cv_url.short_description = 'EN CV'
    en_cv_url.allow_tags = True
    '''
admin.site.register(Comic, ComicAdmin)
