# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Special'
        db.create_table(u'specials_special', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('day_offered', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'specials', ['Special'])


    def backwards(self, orm):
        # Deleting model 'Special'
        db.delete_table(u'specials_special')


    models = {
        u'specials.special': {
            'Meta': {'ordering': "['day_offered']", 'object_name': 'Special'},
            'day_offered': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['specials']