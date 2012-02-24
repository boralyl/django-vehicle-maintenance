# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'MaintenanceItemVideo'
        db.create_table('vehiclemaintenance_maintenanceitemvideo', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('embed_code', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal('vehiclemaintenance', ['MaintenanceItemVideo'])

        # Adding M2M table for field help_videos on 'MaintenanceItem'
        db.create_table('vehiclemaintenance_maintenanceitem_help_videos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('maintenanceitem', models.ForeignKey(orm['vehiclemaintenance.maintenanceitem'], null=False)),
            ('maintenanceitemvideo', models.ForeignKey(orm['vehiclemaintenance.maintenanceitemvideo'], null=False))
        ))
        db.create_unique('vehiclemaintenance_maintenanceitem_help_videos', ['maintenanceitem_id', 'maintenanceitemvideo_id'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'MaintenanceItemVideo'
        db.delete_table('vehiclemaintenance_maintenanceitemvideo')

        # Removing M2M table for field help_videos on 'MaintenanceItem'
        db.delete_table('vehiclemaintenance_maintenanceitem_help_videos')
    
    
    models = {
        'vehiclemaintenance.maintenanceitem': {
            'Meta': {'object_name': 'MaintenanceItem'},
            'check_occurrence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vehiclemaintenance.Occurrence']"}),
            'help_videos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['vehiclemaintenance.MaintenanceItemVideo']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'procedure': ('django.db.models.fields.TextField', [], {})
        },
        'vehiclemaintenance.maintenanceitemcheck': {
            'Meta': {'object_name': 'MaintenanceItemCheck'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_passable': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'maintenance_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vehiclemaintenance.MaintenanceItem']"}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'vehicle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vehiclemaintenance.Vehicle']"})
        },
        'vehiclemaintenance.maintenanceitemvideo': {
            'Meta': {'object_name': 'MaintenanceItemVideo'},
            'embed_code': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'vehiclemaintenance.occurrence': {
            'Meta': {'object_name': 'Occurrence'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'num_days': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'vehiclemaintenance.vehicle': {
            'Meta': {'object_name': 'Vehicle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }
    
    complete_apps = ['vehiclemaintenance']
