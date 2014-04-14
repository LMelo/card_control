# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Meal'
        db.create_table(u'sodexo_meal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meal_value', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('meal_date', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'sodexo', ['Meal'])


    def backwards(self, orm):
        # Deleting model 'Meal'
        db.delete_table(u'sodexo_meal')


    models = {
        u'sodexo.meal': {
            'Meta': {'object_name': 'Meal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meal_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'meal_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        }
    }

    complete_apps = ['sodexo']