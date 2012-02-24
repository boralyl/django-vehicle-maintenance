# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Occurrence'
        db.create_table('vehiclemaintenance_occurrence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num_days', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('vehiclemaintenance', ['Occurrence'])

        # Adding model 'MaintenanceItem'
        db.create_table('vehiclemaintenance_maintenanceitem', (
            ('check_occurrence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vehiclemaintenance.Occurrence'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('procedure', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal('vehiclemaintenance', ['MaintenanceItem'])

        # Adding model 'MaintenanceItemCheck'
        db.create_table('vehiclemaintenance_maintenanceitemcheck', (
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('maintenance_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vehiclemaintenance.MaintenanceItem'])),
            ('vehicle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vehiclemaintenance.vehicle'])),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('is_passable', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('vehiclemaintenance', ['MaintenanceItemCheck'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Occurrence'
        db.delete_table('vehiclemaintenance_occurrence')

        # Deleting model 'MaintenanceItem'
        db.delete_table('vehiclemaintenance_maintenanceitem')

        # Deleting model 'MaintenanceItemCheck'
        db.delete_table('vehiclemaintenance_maintenanceitemcheck')
    
    
    models = {
        'vehiclemaintenance.maintenanceitem': {
            'Meta': {'object_name': 'MaintenanceItem'},
            'check_occurrence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vehiclemaintenance.Occurrence']"}),
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
