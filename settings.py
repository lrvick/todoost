DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'postgresql_psycopg2', 
        'NAME': 'your_db_name',                      
        'USER': 'your_db_user',                     
        'PASSWORD': 'your_pass',          
    }
}

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = '/home/your_username/todoost_folder/media/'

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = 'type_a_bunch_of_random_characters_here'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'todo.middleware.SubdomainMiddleware'
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
		'/home/your_username/todoost_folder/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.comments',
    'django_extensions',
    'south',
    'todo',
)

#Load installation specific settings/passwords from external file with restrictive permissions
from os.path import expanduser
execfile(expanduser('.private-settings'))

# vim: ai ts=4 sts=4 et sw=4
