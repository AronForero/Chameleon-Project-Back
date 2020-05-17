""" Models that are going to be used as mixins by the other models in the project """
from django.db import models


class TimeStampsMixin(models.Model):
    """ This will store the datetime of the created and the updated"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    """ Indicates if a row was deleted or not """
    trashed = models.BooleanField(default=False)
    trashed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
