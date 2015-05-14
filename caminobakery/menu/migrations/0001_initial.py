# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'menu_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='250')),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('one_off_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('item_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.ItemType'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('is_flourless', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_vegan', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vegan_option_available', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('flourless_option_available', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_seasonal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_available', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'menu', ['Item'])

        # Adding model 'Size'
        db.create_table(u'menu_size', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length='100')),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'menu', ['Size'])

        # Adding model 'ItemType'
        db.create_table(u'menu_itemtype', (
            (u'category_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['categories.Category'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'menu', ['ItemType'])

        # Adding M2M table for field size on 'ItemType'
        m2m_table_name = db.shorten_name(u'menu_itemtype_size')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('itemtype', models.ForeignKey(orm[u'menu.itemtype'], null=False)),
            ('size', models.ForeignKey(orm[u'menu.size'], null=False))
        ))
        db.create_unique(m2m_table_name, ['itemtype_id', 'size_id'])

        # Adding model 'ItemTypeGroup'
        db.create_table(u'menu_itemtypegroup', (
            (u'category_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['categories.Category'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'menu', ['ItemTypeGroup'])

        # Adding M2M table for field item_types on 'ItemTypeGroup'
        m2m_table_name = db.shorten_name(u'menu_itemtypegroup_item_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('itemtypegroup', models.ForeignKey(orm[u'menu.itemtypegroup'], null=False)),
            ('itemtype', models.ForeignKey(orm[u'menu.itemtype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['itemtypegroup_id', 'itemtype_id'])

        # Adding model 'BreadSchedule'
        db.create_table(u'menu_breadschedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bread', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.Item'])),
        ))
        db.send_create_signal(u'menu', ['BreadSchedule'])

        # Adding M2M table for field days_available on 'BreadSchedule'
        m2m_table_name = db.shorten_name(u'menu_breadschedule_days_available')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('breadschedule', models.ForeignKey(orm[u'menu.breadschedule'], null=False)),
            ('day', models.ForeignKey(orm[u'menu.day'], null=False))
        ))
        db.create_unique(m2m_table_name, ['breadschedule_id', 'day_id'])

        # Adding model 'Day'
        db.create_table(u'menu_day', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'menu', ['Day'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'menu_item')

        # Deleting model 'Size'
        db.delete_table(u'menu_size')

        # Deleting model 'ItemType'
        db.delete_table(u'menu_itemtype')

        # Removing M2M table for field size on 'ItemType'
        db.delete_table(db.shorten_name(u'menu_itemtype_size'))

        # Deleting model 'ItemTypeGroup'
        db.delete_table(u'menu_itemtypegroup')

        # Removing M2M table for field item_types on 'ItemTypeGroup'
        db.delete_table(db.shorten_name(u'menu_itemtypegroup_item_types'))

        # Deleting model 'BreadSchedule'
        db.delete_table(u'menu_breadschedule')

        # Removing M2M table for field days_available on 'BreadSchedule'
        db.delete_table(db.shorten_name(u'menu_breadschedule_days_available'))

        # Deleting model 'Day'
        db.delete_table(u'menu_day')


    models = {
        u'categories.category': {
            'Meta': {'ordering': "['title']", 'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'lead_image_height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lead_image_width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'menu.breadschedule': {
            'Meta': {'object_name': 'BreadSchedule'},
            'bread': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menu.Item']"}),
            'days_available': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['menu.Day']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'menu.day': {
            'Meta': {'object_name': 'Day'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'menu.item': {
            'Meta': {'ordering': "['name']", 'object_name': 'Item'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'flourless_option_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_flourless': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_seasonal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_vegan': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menu.ItemType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'250'"}),
            'one_off_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'vegan_option_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'menu.itemtype': {
            'Meta': {'ordering': "['title']", 'object_name': 'ItemType', '_ormbases': [u'categories.Category']},
            u'category_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['categories.Category']", 'unique': 'True', 'primary_key': 'True'}),
            'size': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['menu.Size']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'menu.itemtypegroup': {
            'Meta': {'ordering': "['title']", 'object_name': 'ItemTypeGroup', '_ormbases': [u'categories.Category']},
            u'category_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['categories.Category']", 'unique': 'True', 'primary_key': 'True'}),
            'item_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['menu.ItemType']", 'symmetrical': 'False'})
        },
        u'menu.size': {
            'Meta': {'ordering': "['price']", 'object_name': 'Size'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': "'100'"})
        }
    }

    complete_apps = ['menu']