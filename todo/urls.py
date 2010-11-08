from django.conf.urls.defaults import *
from todo.views import view_list, add_task

urlpatterns = patterns('', 
   (r'^$', view_list),
   #(r'^(?P<id>[-\w]+)/$', edit_task),
   (r'^add-task/$', add_task),
)

