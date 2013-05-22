# Copyright 2013 Clione Software
# Licensed under MIT license. See LICENSE for details.

from kanban.settings.defaults import *

# Registration mail settings. Please use a different mail server and account
# during development than in production.
# EMAIL_HOST = ""
# EMAIL_PORT= 25
# EMAIL_HOST_USER= ""
# EMAIL_HOST_PASSWORD= ""
# DEFAULT_FROM_EMAIL = ""
# EMAIL_USE_TLS = True

# Time and zone configuration
TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'

# Cache backend. Default: local memory storage
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}

# Who will we alert?
ADMINS = (
    ('YourAdmin', 'user@host.com'),
)
MANAGERS = ADMINS

# Database configuration. Default: sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'e_cidadania/db/development.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = '21w$*^g1_9how(icw79u8s7jqp^yh0y%dqy6&t^k+&y7p61((-'

FIXTURE_DIRS = (
    (cwd + '/e_cidadania/fixtures/'),
)

# Not needed with debug, but just in case we set it to all.
ALLOWED_HOSTS = ['*']