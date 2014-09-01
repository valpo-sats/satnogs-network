# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Transponder'
        db.create_table(u'base_transponder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('alive', self.gf('django.db.models.fields.BooleanField')()),
            ('uplink_low', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('uplink_high', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('downlink_low', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('downlink_high', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('mode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('invert', self.gf('django.db.models.fields.BooleanField')()),
            ('baud', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'base', ['Transponder'])

        # Adding model 'Antenna'
        db.create_table(u'base_antenna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('frequency', self.gf('django.db.models.fields.FloatField')()),
            ('band', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('antenna_type', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'base', ['Antenna'])

        # Adding model 'Station'
        db.create_table(u'base_station', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('alt', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lng', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'base', ['Station'])

        # Adding M2M table for field antenna on 'Station'
        m2m_table_name = db.shorten_name(u'base_station_antenna')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('station', models.ForeignKey(orm[u'base.station'], null=False)),
            ('antenna', models.ForeignKey(orm[u'base.antenna'], null=False))
        ))
        db.create_unique(m2m_table_name, ['station_id', 'antenna_id'])

        # Adding model 'Satellite'
        db.create_table(u'base_satellite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('norad_cat_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'base', ['Satellite'])

        # Adding M2M table for field transponders on 'Satellite'
        m2m_table_name = db.shorten_name(u'base_satellite_transponders')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('satellite', models.ForeignKey(orm[u'base.satellite'], null=False)),
            ('transponder', models.ForeignKey(orm[u'base.transponder'], null=False))
        ))
        db.create_unique(m2m_table_name, ['satellite_id', 'transponder_id'])

        # Adding model 'Observation'
        db.create_table(u'base_observation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('satellite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Satellite'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'base', ['Observation'])

        # Adding model 'Data'
        db.create_table(u'base_data', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('observation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Observation'])),
            ('ground_station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Station'])),
        ))
        db.send_create_signal(u'base', ['Data'])


    def backwards(self, orm):
        # Deleting model 'Transponder'
        db.delete_table(u'base_transponder')

        # Deleting model 'Antenna'
        db.delete_table(u'base_antenna')

        # Deleting model 'Station'
        db.delete_table(u'base_station')

        # Removing M2M table for field antenna on 'Station'
        db.delete_table(db.shorten_name(u'base_station_antenna'))

        # Deleting model 'Satellite'
        db.delete_table(u'base_satellite')

        # Removing M2M table for field transponders on 'Satellite'
        db.delete_table(db.shorten_name(u'base_satellite_transponders'))

        # Deleting model 'Observation'
        db.delete_table(u'base_observation')

        # Deleting model 'Data'
        db.delete_table(u'base_data')


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
            'start': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'base.satellite': {
            'Meta': {'object_name': 'Satellite'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'norad_cat_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'transponders': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.Transponder']", 'symmetrical': 'False'})
        },
        u'base.station': {
            'Meta': {'object_name': 'Station'},
            'alt': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'antenna': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.Antenna']", 'symmetrical': 'False'}),
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
            'bio': ('django.db.models.fields.TextField', [], {}),
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