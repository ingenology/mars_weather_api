# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Report'
        db.create_table(u'rems_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('terrestrial_date', self.gf('django.db.models.fields.DateField')()),
            ('sol', self.gf('django.db.models.fields.IntegerField')()),
            ('ls', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('min_temp', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('max_temp', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pressure', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pressure_string', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('abs_humidity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('wind_speed', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('wind_direction', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('atmo_opacity', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('season', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sunrise', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sunset', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'rems', ['Report'])


    def backwards(self, orm):
        # Deleting model 'Report'
        db.delete_table(u'rems_report')


    models = {
        u'rems.report': {
            'Meta': {'ordering': "('terrestrial_date',)", 'object_name': 'Report'},
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
            'sol': ('django.db.models.fields.IntegerField', [], {}),
            'sunrise': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sunset': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'terrestrial_date': ('django.db.models.fields.DateField', [], {}),
            'wind_direction': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'wind_speed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rems']