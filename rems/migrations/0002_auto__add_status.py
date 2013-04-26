# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Status'
        db.create_table(u'rems_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('status_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'rems', ['Status'])


    def backwards(self, orm):
        # Deleting model 'Status'
        db.delete_table(u'rems_status')


    models = {
        u'rems.report': {
            'Meta': {'ordering': "('-sol',)", 'object_name': 'Report'},
            'abs_humidity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'atmo_opacity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ls': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'max_temp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'min_temp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pressure': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pressure_string': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sol': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'sunrise': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sunset': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'terrestrial_date': ('django.db.models.fields.DateField', [], {}),
            'wind_direction': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'wind_speed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rems.status': {
            'Meta': {'object_name': 'Status'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'status_text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['rems']