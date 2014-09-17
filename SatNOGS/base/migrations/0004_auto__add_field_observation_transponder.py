# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Observation.transponder'
        db.add_column(u'base_observation', 'transponder',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Transponder'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Observation.transponder'
        db.delete_column(u'base_observation', 'transponder_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'base.antenna': {
            'Meta': {'object_name': 'Antenna'},
            'antenna_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'band': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'frequency': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'base.data': {
            'Meta': {'object_name': 'Data'},
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'ground_station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Station']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Observation']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'base.observation': {
            'Meta': {'object_name': 'Observation'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'satellite': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Satellite']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'transponder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Transponder']", 'null': 'True'})
        },
        u'base.satellite': {
            'Meta': {'object_name': 'Satellite'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'norad_cat_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'base.station': {
            'Meta': {'object_name': 'Station'},
            'alt': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'antenna': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.Antenna']", 'symmetrical': 'False'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'base.transponder': {
            'Meta': {'object_name': 'Transponder'},
            'alive': ('django.db.models.fields.BooleanField', [], {}),
            'baud': ('django.db.models.fields.FloatField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'downlink_high': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'downlink_low': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invert': ('django.db.models.fields.BooleanField', [], {}),
            'mode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'satellite': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transponder'", 'null': 'True', 'to': u"orm['base.Satellite']"}),
            'uplink_high': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'uplink_low': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['base']