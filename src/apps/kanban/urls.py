# Copyright 2013 Clione Software
# Licensed under MIT license. See LICENSE for details.

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'kanban.views.home', name='home'),

    url(r'^add/$', CreateBoard.as_view()),

    url(r'^(?P<board_token>\w+)/$', ViewBoard.as_view()),

    url(r'^(?P<board_token>\w+)/edit', EditBoard.as_view()),

    url(r'^(?P<board_token>\w+)/delete', DeleteBoard.as_view()),

    url(r'^(?P<board_token>\w+)/addnote', AddNote.as_view()),

    url(r'^(?P<board_token>\w+)/editnote', EditNote.as_view()),

    url(r'^(?P<board_token>\w+)/deletenote', DeleteNote.as_view()),

)