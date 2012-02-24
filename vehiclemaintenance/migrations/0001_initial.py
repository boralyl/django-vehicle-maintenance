# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Vehicle'
        db.create_table('vehiclemaintenance_vehicle', (
            ('model', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('vehiclemaintenance', ['Vehicle'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Vehicle'
        db.delete_table('vehiclemaintenance_vehicle')
    
    
    models = {
        'vehiclemaintenance.vehicle': {
            'Meta': {'object_name': 'Vehicle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }
    
    complete_apps = ['vehiclemaintenance']
