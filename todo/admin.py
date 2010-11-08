from django.contrib import admin
from todo.models import Domain, List, Task, Person

admin.site.register(Domain)
admin.site.register(List)
admin.site.register(Task)
admin.site.register(Person)
