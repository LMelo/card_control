# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant'
        db.create_table(u'sodexo_restaurant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rest_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'sodexo', ['Restaurant'])


    def backwards(self, orm):
        # Deleting model 'Restaurant'
        db.delete_table(u'sodexo_restaurant')


    models = {
        u'sodexo.meal': {
            'Meta': {'object_name': 'Meal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meal_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'meal_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'sodexo.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rest_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['sodexo']