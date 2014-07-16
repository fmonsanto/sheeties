# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Comic.date_added'
        db.add_column(u'comic_comic', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 16, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Comic.date_added'
        db.delete_column(u'comic_comic', 'date_added')


    models = {
        u'comic.comic': {
            'Meta': {'object_name': 'Comic'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 16, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['comic']