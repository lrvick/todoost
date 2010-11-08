from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from todo.views import view_list, add_list, add_file, add_task, view_task, edit_task, edit_list, delete_task, delete_task_confirm, delete_list, delete_list_confirm, comment_task, check_task

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('todo.urls')),
    url(r'^add-task/$', add_task, name="add-task"),
    url(r'^add-list/$', add_list, name="add-list"),
    url(r'^add-file/(?P<id>[-\w]+)/$', add_file, name="add-file"),
    url(r'^comment-task/(?P<id>[-\w]+)/$', comment_task, name="comment-task"),
    url(r'^view-task/(?P<id>[-\w]+)/$', view_task, name="view-task"),
    url(r'^edit-task/(?P<id>[-\w]+)/$', edit_task, name="edit-task"),
    url(r'^edit-list/(?P<id>[-\w]+)/$', edit_list, name="edit-list"),
    url(r'^delete-task/(?P<id>[-\w]+)/confirm/$', delete_task_confirm, name="delete-task-confirm"),
    url(r'^delete-task/(?P<id>[-\w]+)/$', delete_task, name="delete-task"),
    url(r'^delete-list/(?P<id>[-\w]+)/confirm/$', delete_list_confirm, name="delete-list-confirm"),
    url(r'^delete-list/(?P<id>[-\w]+)/$', delete_list, name="delete-list"),
    url(r'check-task/(?P<id>[-\w]+)/$', check_task, name="check-task"),
    url(r'^comments/', include('django.contrib.comments.urls')),
)

