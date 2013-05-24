# Copyright 2013 Clione Software
# Licensed under MIT license. See LICENSE for details.

import os

__version__ = "0.1"

# Get the current working directory so we can fill automatically other variables.
cwd = os.path.dirname(os.path.realpath(__file__)).strip('settings')
print "Current working dir: %s" % cwd

SITE_ID = 1
######## INTERNAZIONALIZATION ########
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (
    ('es_ES', 'Espanol'),
    ('en_GB', 'English'),
    ('gl_ES', 'Galego'),
)

######## STATIC FILES AND UPLOADS #####
MEDIA_ROOT = cwd + '/uploads/'
MEDIA_URL = '/uploads/'
STATIC_ROOT = cwd + '/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    (cwd + '/static_files/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

######### MIDDLEWARE AND OTHER STUFF ############
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kanban.urls'
WSGI_APPLICATION = 'kanban.wsgi.application'

######## TEMPLATES #############
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    (cwd + '/templates'),
)

######### APPLICATIONS #############
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'apps.kanban',
)

######## LOGGING ###########
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
