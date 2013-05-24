# Copyright 2013 Clione Software
# Licensed under MIT license. See LICENSE for details.

from django.conf.urls import patterns, include, url

from kanban.views.board import CreateBoard, ViewBoard, EditBoard, DeleteBoard
from kanban.views.tasks import AddTask, ViewTask, EditTask, DeleteTask
from kanban.views.main import home
from kanban import url_names as urln


urlpatterns = patterns('',

    url(r'^$', 'home', name=urln.HOME),

    url(r'^add/$', CreateBoard.as_view(), name=urln.ADD_BOARD),

    url(r'^(?P<board_token>\w+)/$', ViewBoard.as_view(), name=urln.VIEW_BOARD),

    url(r'^(?P<board_token>\w+)/edit', EditBoard.as_view(), name=urln.EDIT_BOARD),

    url(r'^(?P<board_token>\w+)/delete', DeleteBoard.as_view(), name=urln.DELETE_BOARD),

    url(r'^(?P<board_token>\w+)/addtask', AddTask.as_view(), name=urln.ADD_TASK),

    url(r'^(?P<board_token>\w+)/viewtask', ViewTask.as_view(), name=urln.VIEW_TASK)

    url(r'^(?P<board_token>\w+)/edittask', EditTask.as_view(), name=urln.EDIT_TASK),

    url(r'^(?P<board_token>\w+)/deletetask', DeleteTask.as_view(), name=urln.DELETE_TASK),

)