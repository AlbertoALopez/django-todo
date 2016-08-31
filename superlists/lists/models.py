"""Models for TO DO app."""
from django.db import models


class Item(models.Model):
    """Model class for a TO DO item."""

    text = models.TextField(default='')
    list = models.ForeignKey('List', default=None)


class List(models.Model):
    """Model class for a list of items."""

    pass
