# Copyright 2013 Clione Software
# Licensed under MIT license. See LICENSE for details.

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Board(models.Model):

	"""
	Board data model, the board contains all the rows and the notes of the
	Kanban.
	"""
	name = models.CharField(_('Name'), max_length=200)
	created = models.DateTimeField(_('Date of creation'), auto_now_add=True)

	class Meta:

	def __unicode__(self):
		return self.name


class Column(models.Model):

	"""
	"""
	title = models.CharField(_('Title'), max_length=200)


class Note(models.Model):

	"""
	"""
	pass