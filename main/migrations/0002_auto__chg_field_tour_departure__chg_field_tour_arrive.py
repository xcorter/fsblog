# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tour.departure'
        db.alter_column('main_tour', 'departure', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Tour.arrive'
        db.alter_column('main_tour', 'arrive', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):

        # Changing field 'Tour.departure'
        db.alter_column('main_tour', 'departure', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Tour.arrive'
        db.alter_column('main_tour', 'arrive', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        'main.carousel': {
            'Meta': {'object_name': 'Carousel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.claim': {
            'Meta': {'object_name': 'Claim'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tour': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Tour']"})
        },
        'main.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'main.tour': {
            'Meta': {'object_name': 'Tour'},
            'arrive': ('django.db.models.fields.DateField', [], {}),
            'cost': ('django.db.models.fields.IntegerField', [], {}),
            'departure': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['main']