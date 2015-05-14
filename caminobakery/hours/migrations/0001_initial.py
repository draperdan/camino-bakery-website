# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Schedule'
        db.create_table(u'hours_schedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.IntegerField')()),
            ('open_hour', self.gf('django.db.models.fields.TimeField')()),
            ('close_hour', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'hours', ['Schedule'])


    def backwards(self, orm):
        # Deleting model 'Schedule'
        db.delete_table(u'hours_schedule')


    models = {
        u'hours.schedule': {
            'Meta': {'ordering': "['day']", 'object_name': 'Schedule'},
            'close_hour': ('django.db.models.fields.TimeField', [], {}),
            'day': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'open_hour': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['hours']