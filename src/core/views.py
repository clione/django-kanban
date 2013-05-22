# Copyright 2013 Clione Software
# Licensed under MIT license. See LICENSE for details.

from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):

    """
    Main index page of the platform.
    """
    return render_to_response('site_index.html',
                              context_instance=RequestContext(request))