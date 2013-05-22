# Copyright 2013 Clione Software
# Licensed under MIT license. See LICENSE for details.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound, \
                        HttpResponseBadRequest, HttpResponseServerError
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.template import RequestContext

from guardian.shortcuts import assign_perm, get_users_with_perms, remove_perm, \
                               get_perms
from guardian.core import ObjectPermissionChecker