# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tour'
        db.create_table('main_tour', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('departure', self.gf('django.db.models.fields.DateTimeField')()),
            ('arrive', self.gf('django.db.models.fields.DateTimeField')()),
            ('cost', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['Tour'])

        # Adding model 'Claim'
        db.create_table('main_claim', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('tour', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Tour'])),
        ))
        db.send_create_signal('main', ['Claim'])

        # Adding model 'Image'
        db.create_table('main_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('main', ['Image'])

        # Adding model 'Carousel'
        db.create_table('main_carousel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('main', ['Carousel'])


    def backwards(self, orm):
        # Deleting model 'Tour'
        db.delete_table('main_tour')

        # Deleting model 'Claim'
        db.delete_table('main_claim')

        # Deleting model 'Image'
        db.delete_table('main_image')

        # Deleting model 'Carousel'
        db.delete_table('main_carousel')


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
            'arrive': ('django.db.models.fields.DateTimeField', [], {}),
            'cost': ('django.db.models.fields.IntegerField', [], {}),
            'departure': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['main']