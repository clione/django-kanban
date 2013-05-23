# Copyright 2013 Clione Software
# Licensed under MIT license. See LICENSE for details.

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', include('apps.kanban.urls')),

)

if settings.DEBUG:
    # Serve static files
    urlpatterns += staticfiles_urlpatterns()