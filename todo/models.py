from django.db import models
from django.contrib.auth.models import User
import datetime

PRIORITY_LEVELS = (
    (1,'Pipe Dream'),
    (2,'Low'),
    (3,'Average'),
    (4,'Medium'),
    (5,'High'),
    (6,'Life/Death'),
)

class List(models.Model):
    name = models.CharField('List Name', max_length=100, default="default")
    date_created = models.DateTimeField(default=datetime.datetime.now)
    date_due = models.DateTimeField(blank=True, null=True)
    class Meta: 
        ordering = ['-date_due', 'name'] 
    def __unicode__(self):
        return self.name

class Task(models.Model):
    name = models.CharField('Task', max_length=250)
    description = models.TextField('Description',blank=True,null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    date_due = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(choices=PRIORITY_LEVELS, max_length=1, default=3,blank=True)
    completion = models.IntegerField(default=0, max_length=3)
    list = models.ForeignKey(List, related_name="tasks", blank=False, default=0)
    class Meta:
        ordering = ['-priority','-date_due', 'name'] 
        unique_together = ('name', 'list')
    def __unicode__(self):
        return self.name

class Person(models.Model):
    name = models.CharField('Name', max_length=250)
    email = models.EmailField(User, blank=True)
    color = models.CharField(max_length=10)
    tasks = models.ManyToManyField(Task)
    class Meta: 
        ordering = ['name'] 
    def __unicode__(self):
        return self.name

class Domain(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)
    lists = models.ManyToManyField(List, related_name="lists", null=True,blank=True)
    people = models.ManyToManyField(Person, related_name="people", null=True,blank=True)
    def __unicode__(self):
        return self.name

class Attachment(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=datetime.datetime.now())
    file = models.FileField(upload_to='attachments') 
    task = models.ForeignKey(Task)
    def __unicode__(self):
        return self.name
