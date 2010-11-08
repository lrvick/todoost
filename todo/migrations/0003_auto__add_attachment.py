# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Attachment'
        db.create_table('todo_attachment', (
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 4, 11, 20, 51, 47, 998122))),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['todo.Task'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('todo', ['Attachment'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Attachment'
        db.delete_table('todo_attachment')
    
    
    models = {
        'todo.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 4, 11, 20, 51, 47, 998122)'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['todo.Task']"})
        },
        'todo.domain': {
            'Meta': {'object_name': 'Domain'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lists': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'lists'", 'null': 'True', 'to': "orm['todo.List']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'people'", 'null': 'True', 'to': "orm['todo.Person']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'todo.list': {
            'Meta': {'object_name': 'List'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_due': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '100'})
        },
        'todo.person': {
            'Meta': {'object_name': 'Person'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tasks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['todo.Task']"})
        },
        'todo.task': {
            'Meta': {'unique_together': "(('name', 'list'),)", 'object_name': 'Task'},
            'completion': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_due': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'tasks'", 'to': "orm['todo.List']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '3', 'max_length': '1', 'blank': 'True'})
        }
    }
    
    complete_apps = ['todo']
