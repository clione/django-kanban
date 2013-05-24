# Copyright 2013 Clione Software
# Licensed under MIT license. See LICENSE for details.

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class Board(models.Model):

    """
    Board data model, the board contains all the rows and the notes of the
    Kanban.

    .. versionadded:: 0.1
    """
    name = models.CharField(_('Name'), max_length=255)
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField(_('Created'), auto_now_add=True)

    class Meta:
        permissions = (
            ('view_board', 'Can view the board'),
        )
        ordering = ['name']
        verbose_name = _('Board')
        verbose_name_plural = _('Boards')
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return self.name


class Column(models.Model):

    """
    Column data model. This will contain the tasks, and there can be multiple
    columns on the board.

    .. versionadded:: 0.1
    """
    board = models.ForeignKey(Board)
    title = models.CharField(_('Title'), max_length=255)

    class Meta:
        ordering = ['title']
        verbose_name = _('Column')
        verbose_name_plural = _('Columns')

    def __unicode__(self):
        return self.title


class Task(models.Model):

    """
    Task data model. This will store all the information about the tasks.

    .. versionadded:: 0.1
    """
    column = models.ForeignKey(Column)
    text = models.CharField(_('Name'), max_length=255)
    responsible = models.CharField(User)
    progress = models.PositiveIntegerField(_('Progress'))
    pub_date = models.DateTimeField(_('Created'), auto_now_add=True)

    class Meta:
        ordering = ['pub_date']
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return self.text

    def clean(self):
        if self.progress > 100:
            raise ValidationError(_('A task cannot be completed beyond 100%.'))