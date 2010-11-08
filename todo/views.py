from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.forms.formsets import formset_factory
from django.db import IntegrityError
from todo.models import Person, List, Domain, Task
#from todo.forms import PersonForm, ListForm, GroupForm, TaskForm
from todo.forms import AttachmentForm, TaskForm, ListForm, TaskBaseFormSet
from django.forms.models import modelformset_factory

def view_list(request):
    domain, is_created = Domain.objects.get_or_create(name=request.subdomain,slug=request.subdomain)
    default_list_name = request.subdomain + "_default"
    default_list_create, created = List.objects.get_or_create(name=default_list_name)
    domain.lists.add(default_list_create)
    has_tasks = True if [d.tasks.all() for d in domain.lists.all()][0] else False
    return render_to_response('view_list.html', locals(), context_instance=RequestContext(request))

def add_task(request):
    domain, is_created = Domain.objects.get_or_create(name=request.subdomain,slug=request.subdomain)
    default_list_name = request.subdomain + "_default"
    if request.method == 'POST' and 'add_task' in request.POST:
        form = TaskForm(domain, default_list_name, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TaskForm(domain, default_list_name)
        return render_to_response('add_task.html', locals(), context_instance=RequestContext(request))

def add_list(request):
    domain, is_created = Domain.objects.get_or_create(name=request.subdomain,slug=request.subdomain)
    default_list_name = request.subdomain + "_default"
    if request.method == 'POST' and 'add_list' in request.POST:
        form = ListForm(domain, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/') #because thsi one works
    else:
        form = ListForm(domain)
        return render_to_response('add_list.html', locals(), context_instance=RequestContext(request))

def view_task(request, id):
    domain, is_created = Domain.objects.get_or_create(name=request.subdomain,slug=request.subdomain)
    task=Task.objects.get(id=id)
    return render_to_response('view_task.html', locals(), context_instance=RequestContext(request))

def comment_task(request, id):
    domain, is_created = Domain.objects.get_or_create(name=request.subdomain,slug=request.subdomain)
    task=Task.objects.get(id=id)
    return render_to_response('comment_task.html', locals(), context_instance=RequestContext(request))

def edit_task(request, id):
    domain, is_created = Domain.objects.get_or_create(name=request.subdomain,slug=request.subdomain)
    default_list_name = request.subdomain + "_default"
    task=Task.objects.get(id=id)
    if request.method == 'POST' and 'edit_task' in request.POST:
        form = TaskForm(domain, default_list_name, request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:    
        form = TaskForm(domain, default_list_name, instance=task)
        return render_to_response('edit_task.html', locals(), context_instance=RequestContext(request))

def edit_list(request, id):
    domain =get_object_or_404(Domain, slug=request.subdomain) #yea but you probably want to 404 if it doesn't exist
    list=List.objects.get(id=id)
    if request.method == 'POST': # and 'edit_list' in request.POST:
        form = ListForm(domain, request.POST, instance=list)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:    
        form = ListForm(domain, instance=list)
        return render_to_response('edit_list.html', locals(), context_instance=RequestContext(request))


def delete_task(request, id):
    domain, is_created = Domain.objects.get_or_create(name=request.subdomain,slug=request.subdomain)
    task=Task.objects.get(id=id)
    return render_to_response('delete_task.html', locals(), context_instance=RequestContext(request))

def delete_task_confirm(request, id):
    domain, is_created = Domain.objects.get_or_create(name=request.subdomain,slug=request.subdomain)
    task=Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect('/')

def delete_list(request, id):
    domain, is_created = Domain.objects.get_or_create(name=request.subdomain,slug=request.subdomain)
    list=List.objects.get(id=id)
    return render_to_response('delete_list.html', locals(), context_instance=RequestContext(request))

def delete_list_confirm(request, id):
    domain, is_created = Domain.objects.get_or_create(name=request.subdomain,slug=request.subdomain)
    list=List.objects.get(id=id)
    list.delete()
    return HttpResponseRedirect('/')

def check_task(request, id):
    task=Task.objects.get(id=id)
    if task.completion < 100:
        task.completion = 100
        task.save()
    elif task.completion == 100:
        task.completion = 0
        task.save()
    return HttpResponseRedirect('/')

def add_file(request, id):
    user = request.user
    task = get_object_or_404(Task, id=id)
    if request.POST:
        form = AttachmentForm(id, request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            name, file = cd['name'], cd['file']
            new_file = Attachment(
                task = task,
                name = name, 
                file = file,
            )
            new_file.save()
            return HttpResponseRedirect(reverse('view-task', args=[task.id]))
    else:
        form = AttachmentForm(id)
    return render_to_response('add_file.html', locals(), context_instance=RequestContext(request))

