# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tasks'
        db.create_table('todo_tasks', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('task_desc', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('priority', self.gf('django.db.models.fields.CharField')(default='Normal', max_length=10)),
            ('task_state', self.gf('django.db.models.fields.CharField')(default='ToDo', max_length=10)),
            ('created_on', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('todo', ['Tasks'])


    def backwards(self, orm):
        # Deleting model 'Tasks'
        db.delete_table('todo_tasks')


    models = {
        'todo.tasks': {
            'Meta': {'object_name': 'Tasks'},
            'created_on': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'Normal'", 'max_length': '10'}),
            'task_desc': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'task_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'task_state': ('django.db.models.fields.CharField', [], {'default': "'ToDo'", 'max_length': '10'})
        }
    }

    complete_apps = ['todo']