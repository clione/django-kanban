# Copyright 2013 Clione Software
# Licensed under MIT license. See LICENSE for details.

from django.contrib import admin

from guardian.admin import GuardedModelAdmin

from apps.kanban.models import Board, Column, Task


class BoardAdmin(GuardedModelAdmin):

	list_display = ('name', 'pub_date', 'author')
	search = ('name', 'author')

class ColumnAdmin(GuardedModelAdmin):

	list_display = ('title', 'board')
	search = ('title', 'board')

class TaskAdmin(GuardedModelAdmin):

	list_display = ('text', 'responsible', 'progress', 'pub_date')
	search = ('text', 'responsible')

admin.site.register(Board, BoardAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Task, TaskAdmin)