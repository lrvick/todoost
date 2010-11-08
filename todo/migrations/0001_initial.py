# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'List'
        db.create_table('todo_list', (
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_due', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='default', max_length=100)),
        ))
        db.send_create_signal('todo', ['List'])

        # Adding model 'Task'
        db.create_table('todo_task', (
            ('completion', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=3)),
            ('date_due', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('list', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tasks', to=orm['todo.List'])),
            ('priority', self.gf('django.db.models.fields.IntegerField')(max_length=1, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('todo', ['Task'])

        # Adding model 'Person'
        db.create_table('todo_person', (
            ('color', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('todo', ['Person'])

        # Adding M2M table for field tasks on 'Person'
        db.create_table('todo_person_tasks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['todo.person'], null=False)),
            ('task', models.ForeignKey(orm['todo.task'], null=False))
        ))
        db.create_unique('todo_person_tasks', ['person_id', 'task_id'])

        # Adding model 'Domain'
        db.create_table('todo_domain', (
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('todo', ['Domain'])

        # Adding M2M table for field lists on 'Domain'
        db.create_table('todo_domain_lists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('domain', models.ForeignKey(orm['todo.domain'], null=False)),
            ('list', models.ForeignKey(orm['todo.list'], null=False))
        ))
        db.create_unique('todo_domain_lists', ['domain_id', 'list_id'])

        # Adding M2M table for field people on 'Domain'
        db.create_table('todo_domain_people', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('domain', models.ForeignKey(orm['todo.domain'], null=False)),
            ('person', models.ForeignKey(orm['todo.person'], null=False))
        ))
        db.create_unique('todo_domain_people', ['domain_id', 'person_id'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'List'
        db.delete_table('todo_list')

        # Deleting model 'Task'
        db.delete_table('todo_task')

        # Deleting model 'Person'
        db.delete_table('todo_person')

        # Removing M2M table for field tasks on 'Person'
        db.delete_table('todo_person_tasks')

        # Deleting model 'Domain'
        db.delete_table('todo_domain')

        # Removing M2M table for field lists on 'Domain'
        db.delete_table('todo_domain_lists')

        # Removing M2M table for field people on 'Domain'
        db.delete_table('todo_domain_people')
    
    
    models = {
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
            'Meta': {'object_name': 'Task'},
            'completion': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_due': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks'", 'to': "orm['todo.List']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'blank': 'True'})
        }
    }
    
    complete_apps = ['todo']
