# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TestSegmentPluginModel'
        db.delete_table(u'aldryn_segmentation_testsegmentpluginmodel')

        # Adding model 'SwitchSegmentPluginModel'
        db.create_table(u'aldryn_segmentation_switchsegmentpluginmodel', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('on_off', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'aldryn_segmentation', ['SwitchSegmentPluginModel'])


    def backwards(self, orm):
        # Adding model 'TestSegmentPluginModel'
        db.create_table(u'aldryn_segmentation_testsegmentpluginmodel', (
            ('switch', self.gf('django.db.models.fields.BooleanField')(default=True)),
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(default='', max_length=64)),
        ))
        db.send_create_signal(u'aldryn_segmentation', ['TestSegmentPluginModel'])

        # Deleting model 'SwitchSegmentPluginModel'
        db.delete_table(u'aldryn_segmentation_switchsegmentpluginmodel')


    models = {
        u'aldryn_segmentation.cookiesegmentpluginmodel': {
            'Meta': {'object_name': 'CookieSegmentPluginModel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'cookie_key': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '4096'}),
            'cookie_value': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '4096'})
        },
        u'aldryn_segmentation.segmentlimitpluginmodel': {
            'Meta': {'object_name': 'SegmentLimitPluginModel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'max_children': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'aldryn_segmentation.switchsegmentpluginmodel': {
            'Meta': {'object_name': 'SwitchSegmentPluginModel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'on_off': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['aldryn_segmentation']