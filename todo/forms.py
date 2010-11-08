from django import forms
from todo.models import Domain, Task, List, Attachment
from django.forms import ModelForm
from django.forms.models import BaseModelFormSet


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('date_created','completion','date_due')
    def __init__(self, domain, default_list_name, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        domain = Domain.objects.get(name=domain) 
        list_id = List.objects.get(name=default_list_name).id
        if domain.lists.count() <= 1:
            self.fields['list'] = forms.ModelChoiceField(queryset=domain.lists.all(), widget=forms.widgets.HiddenInput(attrs={'value': list_id }))
        else:
            self.fields['list'] = forms.ModelChoiceField(queryset=domain.lists.all(), initial=list_id)
        for field in self.fields.keys():
            self.fields[field].widget.attrs['class'] = field
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label

class ListForm(ModelForm):
    class Meta:
        model = List
        exclude = ('date_created')
    def __init__(self, domain, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        domain = Domain.objects.get(name=domain) 
        domain_id = Domain.objects.get(name=domain).id
        #self.fields['domain'] = forms.ModelChoiceField(queryset=domain.all(), widget=forms.widgets.HiddenInput(attrs={'value': domain_id }))
        self.fields['domain'] = forms.CharField(widget=forms.widgets.HiddenInput(attrs={'value': domain_id }))


class TaskBaseFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(TaskBaseFormSet, self).__init__(*args, **kwargs)
        for i in range(0, self.total_form_count()):
            form = self.forms[i]
            for field in form.fields.keys():
                form.fields[field].widget.attrs['class'] = field

class AttachmentForm(ModelForm):
    class Meta:
        model = Attachment
    def __init__(self, id, *args, **kwargs):
        super(AttachmentForm, self).__init__(*args, **kwargs)
        task = Task.objects.get(id=id)
        self.fields['task'] = forms.CharField(widget=forms.widgets.HiddenInput(attrs={'value': id }))
