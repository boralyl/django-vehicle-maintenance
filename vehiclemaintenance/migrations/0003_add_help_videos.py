# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'MaintenanceItemVideo'
        db.create_table('vehicle_maintenanceitemvideo', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('embed_code', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal('vehicle', ['MaintenanceItemVideo'])

        # Adding M2M table for field help_videos on 'MaintenanceItem'
        db.create_table('vehicle_maintenanceitem_help_videos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('maintenanceitem', models.ForeignKey(orm['vehicle.maintenanceitem'], null=False)),
            ('maintenanceitemvideo', models.ForeignKey(orm['vehicle.maintenanceitemvideo'], null=False))
        ))
        db.create_unique('vehicle_maintenanceitem_help_videos', ['maintenanceitem_id', 'maintenanceitemvideo_id'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'MaintenanceItemVideo'
        db.delete_table('vehicle_maintenanceitemvideo')

        # Removing M2M table for field help_videos on 'MaintenanceItem'
        db.delete_table('vehicle_maintenanceitem_help_videos')
    
    
    models = {
        'vehicle.maintenanceitem': {
            'Meta': {'object_name': 'MaintenanceItem'},
            'check_occurrence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vehicle.Occurrence']"}),
            'help_videos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['vehicle.MaintenanceItemVideo']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'procedure': ('django.db.models.fields.TextField', [], {})
        },
        'vehicle.maintenanceitemcheck': {
            'Meta': {'object_name': 'MaintenanceItemCheck'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_passable': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'maintenance_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vehicle.MaintenanceItem']"}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'vehicle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vehicle.Vehicle']"})
        },
        'vehicle.maintenanceitemvideo': {
            'Meta': {'object_name': 'MaintenanceItemVideo'},
            'embed_code': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'vehicle.occurrence': {
            'Meta': {'object_name': 'Occurrence'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'num_days': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'vehicle.vehicle': {
            'Meta': {'object_name': 'Vehicle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }
    
    complete_apps = ['vehicle']
